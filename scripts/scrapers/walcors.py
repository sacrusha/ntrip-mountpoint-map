"""WALCORS (Wallonia, Belgium) — M3G sitelog API scraper.

Source: https://gnss-metadata.eu/v1/sitelog/exportlog?id=<9CHAR>

WALCORS is the regional GNSS reference network for Wallonia, operated by
SPW (Service public de Wallonie). The operator portal at
gnss.wallonie.be only ships the station inventory as a static JPG; M3G
carries the per-station IGS sitelogs (all 23 stations are EPN/Belgian
AGN members and registered there).

Station IDs taken from the WALCORS M3G project page
(https://gnss-metadata.eu/MOID/projnet.6059fc54e0e210199a06e792, retrieved
2026-05-22). Append `00BEL` to each 4-char ID to form the 9-char M3G ID.
"""
from __future__ import annotations

import urllib.request

from . import _sitelog

API_BASE = "https://gnss-metadata.eu/v1/sitelog/exportlog?id="
TIMEOUT = 20
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (scraper walcors)"

STATION_IDS = sorted([
    "ARLO", "BATT", "BERL", "CHLR", "FLRV", "FOVA", "GHIS", "KAIN",
    "LEGL", "MABO", "MAFA", "MARI", "MEIX", "MOHA", "NAMR", "NIVL",
    "OLLN", "ONHA", "OSTI", "TELL", "TILM", "VITH", "WERB",
])


def _http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def scrape() -> dict:
    stations: list[dict] = []
    for sid in STATION_IDS:
        url = f"{API_BASE}{sid}00BEL"
        try:
            text = _http_get(url)
        except Exception as e:
            print(f"[walcors] {sid}: fetch failed ({e!r}); skipping", flush=True)
            continue
        lat = _sitelog.LAT_RE.search(text)
        lon = _sitelog.LON_RE.search(text)
        if not (lat and lon):
            print(f"[walcors] {sid}: sitelog Section 2 coords missing; skipping", flush=True)
            continue
        stations.append({
            "name": sid,
            "lat": _sitelog.dms_to_decimal(lat.group(1), 2),
            "lon": _sitelog.dms_to_decimal(lon.group(1), 3),
            "country": "BEL",
        })

    if not stations:
        raise ValueError("scraped 0 WALCORS stations from M3G API")

    stations.sort(key=lambda s: s["name"])
    return {
        "source_url": "https://gnss-metadata.eu/v1/sitelog/exportlog?id=...00BEL",
        "stations": stations,
    }
