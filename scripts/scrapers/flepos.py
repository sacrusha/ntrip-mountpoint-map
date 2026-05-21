"""FLEPOS (Flanders, Belgium) — M3G sitelog API scraper.

Source: https://gnss-metadata.eu/v1/sitelog/exportlog?id=<4CHAR>00BEL

FLEPOS is operated by Agentschap Digitaal Vlaanderen and its physical
GNSS reference stations are EPN members; the EPN's M3G metadata
service exposes per-station IGS sitelogs by 9-character ID.

The 48 FLEPOS station 4-char IDs are baked into this module from the
EPOS GNSS Quality Portal `network=FLEPOS` listing (2026-05-21
research). The list includes a small number of cross-border partner
stations (LEEU/MAAS/MAME/HOUT in the Netherlands) that contribute to
the FLEPOS solution — we keep them because the operator does, and
the country tag follows what the M3G sitelog actually carries.
"""
from __future__ import annotations

import urllib.request

from . import _sitelog

API_BASE = "https://gnss-metadata.eu/v1/sitelog/exportlog?id="
TIMEOUT = 20
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (scraper flepos)"

# 48 station IDs from the FLEPOS network listing (operator-published
# via EPOS GNSS Quality Portal). Sorted alphabetically so the cache
# diff is stable across runs.
STATION_IDS = sorted([
    "AARS", "ANTW", "ATWR", "BERT", "BEZA", "BGGN", "BLIG", "BRCT",
    "BRGG", "BUGG", "DIES", "DIKS", "EEKL", "ERPE", "GBGN", "GENT",
    "GILL", "HERE", "HOEG", "HOUT", "IEPE", "KALL", "LEEU", "MAAS",
    "MAME", "MECH", "MENE", "MOL1", "NEER", "NIK1", "NIKL", "OOST",
    "OSTE", "OSTN", "OUDE", "OUDN", "PITM", "PTTM", "RUIS", "TGRN",
    "TIEN", "TRUI", "TURN", "VEUR", "VOER", "ZEEB", "ZEL1", "ZELZ",
    "ZWEV",
])

def _http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


_COUNTRY_ISO3 = {
    "Belgium": "BEL",
    "Netherlands": "NLD",
    "France": "FRA",
    "Germany": "DEU",
    "Luxembourg": "LUX",
}


def _parse_sitelog(text: str, fallback_id: str) -> tuple[str, float, float, str] | None:
    lat = _sitelog.LAT_RE.search(text)
    lon = _sitelog.LON_RE.search(text)
    if not (lat and lon):
        return None
    name_match = (_sitelog.FOURCHAR_RE.search(text)
                  or _sitelog.SITE_NAME_RE.search(text)
                  or _sitelog.NINECHAR_RE.search(text))
    name = name_match.group(1).strip()[:4] if name_match else fallback_id
    country_match = _sitelog.COUNTRY_RE.search(text)
    country_str = (country_match.group(1).strip()
                   if country_match else "Belgium")
    country = _COUNTRY_ISO3.get(country_str, "BEL")
    return (
        name,
        _sitelog.dms_to_decimal(lat.group(1), 2),
        _sitelog.dms_to_decimal(lon.group(1), 3),
        country,
    )


def scrape() -> dict:
    stations: list[dict] = []
    for sid in STATION_IDS:
        url = f"{API_BASE}{sid}00BEL"
        try:
            text = _http_get(url)
        except Exception as e:
            print(f"[flepos] {sid}: fetch failed ({e!r}); skipping", flush=True)
            continue
        parsed = _parse_sitelog(text, fallback_id=sid)
        if parsed is None:
            print(f"[flepos] {sid}: sitelog unparseable; skipping", flush=True)
            continue
        name, lat, lon, country = parsed
        stations.append({"name": name, "lat": lat, "lon": lon, "country": country})

    if not stations:
        raise ValueError("scraped 0 FLEPOS stations from M3G API")

    stations.sort(key=lambda s: s["name"])
    return {
        "source_url": "https://gnss-metadata.eu/v1/sitelog/exportlog?id=...00BEL",
        "stations": stations,
    }
