#!/usr/bin/env python3
"""List rtk2go / Centipede / EarthScope (NOTA) stations for a country code.

Usage:  py scripts/stations_by_country.py <country_code>
        py scripts/stations_by_country.py          # list all codes

Examples:
        py scripts/stations_by_country.py FRA
        py scripts/stations_by_country.py JAM

Country codes follow each source's own convention.
rtk2go uses ISO 3166-1 alpha-3 (FRA, USA, DEU ...).
Centipede quirks: CHZ=CZ  ENG=GB  SER=RS  BIH=BA  NLD/BEL separate.
EarthScope uses USA for US stations; other territories vary.

Related tools (in this directory):
    stations_by_radius.py    list stations within a radius of a lat/lon
    stations_inspect.py      schema + per-source summary of stations.json
    sources_list.py          look up source ids defined in fetch_stations.py
    source_health.py         check status of one or all sources
    network_lookup.py        find every mention of a network/source across the repo
"""
import json, sys
from pathlib import Path

STATIONS = Path(__file__).parent.parent / "data" / "stations.json"
SOURCES  = ["rtk2go", "centipede", "earthscope"]

data = json.loads(STATIONS.read_text())["sources"]

if len(sys.argv) < 2:
    for src in SOURCES:
        codes = sorted({s["country"] for s in data[src]["stations"] if s["country"]})
        print(f"{src}: {', '.join(codes)}")
    sys.exit(0)

tag = sys.argv[1].upper()
total = 0
for src in SOURCES:
    hits = sorted(
        (s for s in data[src]["stations"] if s["country"].upper() == tag),
        key=lambda s: s["name"],
    )
    if hits:
        print(f"\n{src} — {len(hits)} station(s):")
        for s in hits:
            print(f"  {s['name']:<24} {s['lat']:>9.4f}  {s['lon']:>10.4f}")
        total += len(hits)

if not total:
    print(f"No stations for '{tag}'. Run without arguments to list available codes.")
