"""SAPOS Nordrhein-Westfalen refmap scraper.

Source: https://gppspro.saposnrw.de/refmap.php

The index page lists `<a href="refmap.php?detail=XXXX">NAME</a>` entries
for each physical reference station. The per-station detail page embeds
IGS-style DMS strings from the operator's sitelog:

    Latitude (N is +)      : +DDMMSS.ss
    Longitude (E is +)     : +DDDMMSS.ss
    Four Character ID      : XXXX

Both index and detail pages are static HTML — no JS rendering needed.
"""
from __future__ import annotations

import re
import urllib.request
from urllib.parse import urljoin

from . import _sitelog

INDEX_URL = "https://gppspro.saposnrw.de/refmap.php"
TIMEOUT = 15
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (scraper sapos_nw)"

# Detail-page link shape: ?detail=2576 / ?detail=DUS2 / ?detail=0580. Allow
# any 4-char alphanumeric to absorb future renames (NRW migrated several
# stations to 4-letter IDs in 2025).
_DETAIL_RE = re.compile(r'detail=([0-9A-Z]{4})\b')

def _http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _parse_detail(text: str, fallback_name: str) -> tuple[str, float, float]:
    """Return (site_name, lat, lon) from a station detail page.

    Prefers Site Name from the embedded sitelog; falls back to the
    `detail=XXXX` parameter when the page only embeds the 4-char ID."""
    lat_match = _sitelog.LAT_RE.search(text)
    lon_match = _sitelog.LON_RE.search(text)
    if not (lat_match and lon_match):
        raise ValueError("detail page missing DMS coordinates")
    name_match = _sitelog.SITE_NAME_RE.search(text) or _sitelog.FOURCHAR_RE.search(text)
    name = name_match.group(1).strip() if name_match else fallback_name
    lat = _sitelog.dms_to_decimal(lat_match.group(1), 2)
    lon = _sitelog.dms_to_decimal(lon_match.group(1), 3)
    return name, lat, lon


def scrape() -> dict:
    index_html = _http_get(INDEX_URL)
    detail_ids = sorted(set(_DETAIL_RE.findall(index_html)))
    if not detail_ids:
        raise ValueError(f"no detail= links matched at {INDEX_URL}")

    stations = []
    for did in detail_ids:
        url = urljoin(INDEX_URL, f"refmap.php?detail={did}")
        text = _http_get(url)
        try:
            name, lat, lon = _parse_detail(text, fallback_name=did)
        except ValueError as e:
            print(f"[sapos_nw] skipping detail={did}: {e}", flush=True)
            continue
        stations.append({"name": name, "lat": lat, "lon": lon, "country": "DEU"})

    if not stations:
        raise ValueError("scraped 0 stations from sapos-nw refmap")

    stations.sort(key=lambda s: s["name"])
    return {"source_url": INDEX_URL, "stations": stations}
