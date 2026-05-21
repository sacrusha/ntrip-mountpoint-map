"""Shared helper for the NGS NAD83(2011) bulk coordinate file.

Source: https://geodesy.noaa.gov/corsdata/coord/coord_20/nad83_2011_geo.comp.txt

The file lists every NGS-network CORS in one fixed-format text dump.
Multiple state-DOT networks (ARDOT, CT ACORN, …) re-use these names as
their physical mountpoints; the shared helper parses the file once,
then each per-state scraper filters by state code.

Format (after a 7-line header):
    SITE  EPOCH    DD MM SS.sssss N   DDD MM SS.sssss W   ELLIP_HT  ...  Ctry  STATE  Status
columns are space-separated but variable-width; the unambiguous
landmarks are the `N`/`S` hemisphere letter (lat ends with it) and the
trailing 2-letter state code immediately before the Status word.

The whole file is ~600 kB so we fetch once per scrape, cache the parsed
result inside the calling scraper's `.scraped.json`, and rely on the
7-day cadence to keep the load on NGS negligible.
"""
from __future__ import annotations

import re
import urllib.request

NGS_BULK_URL = (
    "https://geodesy.noaa.gov/corsdata/coord/coord_20/nad83_2011_geo.comp.txt"
)
TIMEOUT = 30
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (scraper ngs_bulk)"

# Capture groups: site (1), lat-deg (2), lat-min (3), lat-sec (4),
# lat-hem (5), lon-deg (6), lon-min (7), lon-sec (8), lon-hem (9),
# state (10). Each numeric run permits flexible whitespace so the
# parser tolerates the file's variable column widths.
_LINE_RE = re.compile(
    r"^(\S{4})\s+"                  # site (4 chars)
    r"\d{4}\.\d{2}\s+"             # epoch
    r"(\d{1,3})\s+(\d{1,2})\s+([\d.]+)\s+([NS])\s+"     # lat DMS + hemi
    r"(\d{1,3})\s+(\d{1,2})\s+([\d.]+)\s+([EW])\s+"     # lon DMS + hemi
    r"-?\d+\.\d+"                   # ellipsoidal height
    r"(?:\s+-?\d+\.\d+){3}\s+"     # 3 velocity columns
    r"\S+\s+([A-Z]{2})\s+\S",       # country code, STATE, status start
)


# In-process memoisation: when two scrapers share the same upstream
# file (e.g. ardot_rtn + ct_acorn), the file fetches once per pipeline
# run instead of once per state. The cache is intentionally tied to
# process lifetime — the per-source `.scraped.json` files on disk are
# the durable cache.
_cached_text: str | None = None


def _fetch_text() -> str:
    global _cached_text
    if _cached_text is not None:
        return _cached_text
    req = urllib.request.Request(NGS_BULK_URL, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        _cached_text = resp.read().decode("utf-8", errors="replace")
    return _cached_text


def _dms(deg: str, minutes: str, seconds: str, hem: str) -> float:
    val = int(deg) + int(minutes) / 60.0 + float(seconds) / 3600.0
    if hem in ("S", "W"):
        val = -val
    return round(val, 6)


def filter_by_state(state_code: str) -> list[dict]:
    """Return all NGS-network stations whose state column matches.

    `state_code` is a 2-letter USPS code (`AR`, `CT`, …). Case-sensitive
    to match the file. Caller is responsible for raising on empty result
    when that would constitute scrape failure.
    """
    text = _fetch_text()
    state_code = state_code.upper()
    out: list[dict] = []
    for line in text.splitlines():
        m = _LINE_RE.match(line)
        if not m or m.group(10) != state_code:
            continue
        name = m.group(1).strip()
        lat = _dms(m.group(2), m.group(3), m.group(4), m.group(5))
        lon = _dms(m.group(6), m.group(7), m.group(8), m.group(9))
        out.append({"name": name, "lat": lat, "lon": lon, "country": "USA"})
    out.sort(key=lambda s: s["name"])
    return out
