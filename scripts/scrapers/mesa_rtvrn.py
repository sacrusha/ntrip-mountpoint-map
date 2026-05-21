"""Mesa County RTVRN — per-station HTML scraper.

Source: https://www.mesacounty.us/departments-and-services/public-works/
        gps-survey/gnss-cors-index/

The index page links to one HTML page per CORS station; each page
displays Latitude / Longitude as DMS strings. Operator publishes 27
active sites + 1 decommissioned (MC10). We pin only the active ones —
the decommissioned page is detected by the slug suffix.

Slug shape: `<4char>-<descriptor>` (e.g. `mc01-grand-junction-fire-station-2`,
`coal-alamosa`). The 4-char head is the operator's mountpoint-aligned
station code; that's what we use as the pin name.

DMS shape on detail pages varies slightly between stations (some use
`°`/`'`/`"` glyphs, some use plain space + ASCII apostrophe). The
regex below tolerates either; we don't try to parse the long
descriptor name because the operator already encodes the code in the
URL slug.
"""
from __future__ import annotations

import re
import urllib.request
from urllib.parse import urljoin

INDEX_URL = (
    "https://www.mesacounty.us/departments-and-services/"
    "public-works/gps-survey/gnss-cors-index/"
)
TIMEOUT = 15
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (scraper mesa_rtvrn)"

# Slug capture: 4 alphanumerics + hyphen. Decommissioned pages end in
# `-decommissioned` and are filtered out.
_LINK_RE = re.compile(r'href="([^"]*?/gnss-cors-index/([a-z0-9]{4})-[a-z0-9-]+)"')

# DMS pattern, tolerant of:
#   - presence/absence of ° ' " glyphs (some pages strip them in CMS render)
#   - extra spaces between tokens
#   - hemisphere letter case
_LAT_RE = re.compile(
    r"latitude\s*:?\s*(\d{1,3})[^\d]+(\d{1,2})[^\d]+([\d.]+)\D*([NS])",
    re.IGNORECASE,
)
_LON_RE = re.compile(
    r"longitude\s*:?\s*(\d{1,3})[^\d]+(\d{1,2})[^\d]+([\d.]+)\D*([EW])",
    re.IGNORECASE,
)


def _http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _dms_decimal(deg: str, minutes: str, seconds: str, hem: str) -> float:
    val = int(deg) + int(minutes) / 60.0 + float(seconds) / 3600.0
    if hem.upper() in ("S", "W"):
        val = -val
    return round(val, 6)


def _parse_detail(html: str) -> tuple[float, float] | None:
    lat = _LAT_RE.search(html)
    lon = _LON_RE.search(html)
    if not (lat and lon):
        return None
    return (
        _dms_decimal(lat.group(1), lat.group(2), lat.group(3), lat.group(4)),
        _dms_decimal(lon.group(1), lon.group(2), lon.group(3), lon.group(4)),
    )


def scrape() -> dict:
    index_html = _http_get(INDEX_URL)
    # de-duplicate while keeping discovery order; decommissioned suffix
    # is dropped before the regex matches (slug `mc10-montrose-decommissioned`
    # is captured as code=mc10 still, so we filter on URL substring).
    seen_codes: set[str] = set()
    pairs: list[tuple[str, str]] = []  # (full_url, code_upper)
    for href, code in _LINK_RE.findall(index_html):
        if "decommissioned" in href:
            continue
        code_u = code.upper()
        if code_u in seen_codes:
            continue
        seen_codes.add(code_u)
        full = urljoin(INDEX_URL, href)
        pairs.append((full, code_u))

    if not pairs:
        raise ValueError(f"no station detail links matched at {INDEX_URL}")

    stations: list[dict] = []
    for url, code in pairs:
        html = _http_get(url)
        parsed = _parse_detail(html)
        if parsed is None:
            print(f"[mesa_rtvrn] skipping {code} ({url}): coords not parseable", flush=True)
            continue
        lat, lon = parsed
        stations.append({"name": code, "lat": lat, "lon": lon, "country": "USA"})

    if not stations:
        raise ValueError("scraped 0 stations from mesa county index")

    stations.sort(key=lambda s: s["name"])
    return {"source_url": INDEX_URL, "stations": stations}
