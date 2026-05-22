"""ESTPOS (Estonia) — M3G sitelog API scraper.

Source: https://gnss-metadata.eu/v1/sitelog/exportlog?id=<9CHAR>

ESTPOS is operated by the Estonian Land Board (Maa-amet) and its
physical GNSS reference stations are EPN members; the EPN's M3G
metadata service exposes per-station IGS sitelogs by 9-character ID.

The 40 active ESTPOS station 4-char IDs are baked in from the official
ESTPOS quality-plots page (2026-05-22 research):
https://geoportaal.maaamet.ee/est/ruumiandmed/estpos/gnss-tugijaamade-graafikud-p949.html
Appending `00EST` yields the 9-char M3G ID. Hardcoding avoids
predecessor-ID confusion — M3G carries historical installs (renamed
antenna mounts) under different 9-char IDs; querying the project page
directly risks returning retired IDs alongside active ones.
"""
from __future__ import annotations

import urllib.request

from . import _sitelog

API_BASE = "https://gnss-metadata.eu/v1/sitelog/exportlog?id="
TIMEOUT = 20
USER_AGENT = "NTRIP ntrip-mountpoint-map/1.0 (scraper estpos)"

# 40 active station IDs from the ESTPOS quality-plots page (operator-
# published). Sorted alphabetically for stable cache diffs.
STATION_IDS = sorted([
    "AJOE", "ALAK", "NTSL", "AUDR", "AVNR", "EMM1", "HANI", "HRIS",
    "IKLA", "IMAV", "JOGE", "KALL", "KARD", "KIVI", "KLNA", "KOID",
    "KOSI", "KURE", "KUSA", "MEHI", "MOIS", "MRJA", "MUJA", "MUS2",
    "NJO1", "PYRK", "RALL", "RUH1", "SOVE", "SUR4", "TARV", "TOIL",
    "TOR3", "TORV", "TRTU", "UGA2", "UULU", "VAND", "VERG", "VOR2",
])


def _http_get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read().decode("utf-8", errors="replace")


def scrape() -> dict:
    stations: list[dict] = []
    for sid in STATION_IDS:
        url = f"{API_BASE}{sid}00EST"
        try:
            text = _http_get(url)
        except Exception as e:
            print(f"[estpos] {sid}: fetch failed ({e!r}); skipping", flush=True)
            continue
        lat = _sitelog.LAT_RE.search(text)
        lon = _sitelog.LON_RE.search(text)
        if not (lat and lon):
            print(f"[estpos] {sid}: sitelog Section 2 coords missing; skipping", flush=True)
            continue
        stations.append({
            "name": sid,
            "lat": _sitelog.dms_to_decimal(lat.group(1), 2),
            "lon": _sitelog.dms_to_decimal(lon.group(1), 3),
            "country": "EST",
        })

    if not stations:
        raise ValueError("scraped 0 ESTPOS stations from M3G API")

    stations.sort(key=lambda s: s["name"])
    return {
        "source_url": "https://gnss-metadata.eu/v1/sitelog/exportlog?id=...00EST",
        "stations": stations,
    }
