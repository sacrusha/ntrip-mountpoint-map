"""ASG-EUPOS (Poland) — HTML reference-station coordinates scraper.

Source: https://www.asgeupos.pl/language/en/services-2/coordinates-of-reference-stations/

The page tabulates Polish CORS stations with their geocentric (ECEF
XYZ) coordinates in PL-ETRF2000 epoch 2011.0. Each data row carries:

    <4-char ID>  <Polish locality name>  <X[m]>  <Y[m]>  <Z[m]>

XYZ is converted to geodetic (lat, lon) on the GRS80 / WGS84 ellipsoid
via Bowring's closed-form approximation, which is exact to better than
1 mm at the surface of the Earth — orders of magnitude tighter than
the 6-decimal precision we round to. PL-ETRF2000 and WGS84 differ by
<10 cm in Europe; for a pin on a map the offset is invisible.

Several rows publish zero coordinates (offline / placeholder); those
are dropped without erroring.
"""
from __future__ import annotations

import math
import re
import urllib.request

SOURCE_URL = (
    "https://www.asgeupos.pl/language/en/"
    "services-2/coordinates-of-reference-stations/"
)
TIMEOUT = 20
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (scraper asg_eupos)"

# GRS80 ellipsoid (also matches WGS84 to 11 decimal places in `a` and `f`)
_A = 6378137.0
_F = 1.0 / 298.257222101
_E2 = _F * (2.0 - _F)
_EP2 = _E2 / (1.0 - _E2)
_B = _A * (1.0 - _F)

# Row regex anchored on a 4-char alphanumeric ID followed by a locality
# name then three signed decimals. The locality column carries Polish
# diacritics which we don't otherwise need; non-greedy match swallows
# everything between ID and the first XYZ float.
_ROW_RE = re.compile(
    r"\b([A-Z0-9]{4})\s+[^\n\r]*?\s+"
    r"(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)"
)

# HTML tag stripper for the row scan — keep it conservative (only
# replace block-level breaks with newlines so rows stay on separate
# lines, then strip remaining tags).
_BLOCK_RE = re.compile(r"</(tr|td|th|p|div|li|table|tbody|thead)>", re.IGNORECASE)
_TAG_RE = re.compile(r"<[^>]+>")
_HTML_ENTITY = re.compile(r"&(?:nbsp|amp|lt|gt|#\d+);", re.IGNORECASE)


def _http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _strip_html(html: str) -> str:
    text = _BLOCK_RE.sub("\n", html)
    text = _TAG_RE.sub(" ", text)
    text = _HTML_ENTITY.sub(" ", text)
    return text


def _ecef_to_geodetic(x: float, y: float, z: float) -> tuple[float, float]:
    """Closed-form ECEF→geodetic on the GRS80 ellipsoid (Bowring 1976).

    Returns (lat, lon) in decimal degrees. Height is discarded — we
    only pin the surface footprint.
    """
    lon = math.atan2(y, x)
    p = math.hypot(x, y)
    theta = math.atan2(z * _A, p * _B)
    sin_t = math.sin(theta)
    cos_t = math.cos(theta)
    lat = math.atan2(
        z + _EP2 * _B * sin_t ** 3,
        p - _E2 * _A * cos_t ** 3,
    )
    return math.degrees(lat), math.degrees(lon)


def scrape() -> dict:
    html = _http_get(SOURCE_URL)
    text = _strip_html(html)

    seen: set[str] = set()
    stations: list[dict] = []
    for sid, sx, sy, sz in _ROW_RE.findall(text):
        if sid in seen:
            continue
        x, y, z = float(sx), float(sy), float(sz)
        # Offline / placeholder rows ship as 0,0,0 — operator-known and
        # safe to drop.
        if x == 0 and y == 0 and z == 0:
            seen.add(sid)
            continue
        # Sanity: a real ECEF triple has |X|,|Y| <~ 6.4e6 and |Z| similar.
        # The Polish bbox lies at radii ~6.36e6; anything off by an
        # order of magnitude is a parser misfire.
        if max(abs(x), abs(y), abs(z)) < 1e6:
            continue
        lat, lon = _ecef_to_geodetic(x, y, z)
        # Sanity gate: Poland sits roughly 49–55 lat, 14–24 lon. Allow
        # a generous border halo so cross-border EPN partners aren't
        # accidentally dropped, but skip wildly wrong values.
        if not (45.0 <= lat <= 60.0 and 10.0 <= lon <= 30.0):
            continue
        seen.add(sid)
        stations.append({
            "name": sid,
            "lat": round(lat, 6),
            "lon": round(lon, 6),
            "country": "POL",
        })

    if not stations:
        raise ValueError("scraped 0 stations from ASG-EUPOS coords page")

    stations.sort(key=lambda s: s["name"])
    return {"source_url": SOURCE_URL, "stations": stations}
