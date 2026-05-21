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

import re
import urllib.request

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

# IGS sitelog DMS shape, identical to the SAPOS-BB form. The country
# tag on the sitelog (`X.XX Country` in Section 2) carries through to
# the pin record so cross-border stations are honestly labelled.
_SITE_NAME_RE = re.compile(r"^\s*Site Name\s*:\s*(\S.*?)\s*$", re.MULTILINE)
_FOURCHAR_RE = re.compile(r"Four Character ID\s*:\s*(\S{4})")
_NINECHAR_RE = re.compile(r"Nine Character ID\s*:\s*(\S{9})")
_LAT_RE = re.compile(r"Latitude\s*\(N is \+\)\s*:\s*([+-]\d+\.\d+)")
_LON_RE = re.compile(r"Longitude\s*\(E is \+\)\s*:\s*([+-]\d+\.\d+)")
_COUNTRY_RE = re.compile(r"Country or Region\s*:\s*([A-Za-z][A-Za-z ]+)")


def _http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _dms_decimal(s: str, deg_digits: int) -> float:
    sign = -1 if s.startswith("-") else 1
    body = s.lstrip("+-")
    dd = int(body[:deg_digits])
    mm = int(body[deg_digits:deg_digits + 2])
    ss = float(body[deg_digits + 2:])
    return sign * round(dd + mm / 60.0 + ss / 3600.0, 6)


_COUNTRY_ISO3 = {
    "Belgium": "BEL",
    "Netherlands": "NLD",
    "France": "FRA",
    "Germany": "DEU",
    "Luxembourg": "LUX",
}


def _parse_sitelog(text: str, fallback_id: str) -> tuple[str, float, float, str] | None:
    lat = _LAT_RE.search(text)
    lon = _LON_RE.search(text)
    if not (lat and lon):
        return None
    name_match = (_FOURCHAR_RE.search(text)
                  or _SITE_NAME_RE.search(text)
                  or _NINECHAR_RE.search(text))
    name = name_match.group(1).strip()[:4] if name_match else fallback_id
    country_match = _COUNTRY_RE.search(text)
    country_str = (country_match.group(1).strip()
                   if country_match else "Belgium")
    country = _COUNTRY_ISO3.get(country_str, "BEL")
    return (
        name,
        _dms_decimal(lat.group(1), 2),
        _dms_decimal(lon.group(1), 3),
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
