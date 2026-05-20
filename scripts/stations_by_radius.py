#!/usr/bin/env python3
"""List stations within a radius of a lat/lon across ALL ingested sources.

Usage:    py scripts/stations_by_radius.py <lat> <lon> <radius_km> [full]
Example:  py scripts/stations_by_radius.py 48.85 2.35 150
          py scripts/stations_by_radius.py 48.85 2.35 150 full

Default output: counts per (network, country tag). Caller context stays small.
`full` flag: per-station dump (name, lat, lon, distance, country) per source.

Sources walked: every key in data/stations.json[sources] (84 as of 2026-05),
covering rtk2go, Centipede, EarthScope NOTA, EUREF-IP, IGS-IP and all
national casters in fetch_stations.py SOURCES.

Related tools (in this directory):
    stations_by_country.py   list stations for a country code
    stations_inspect.py      schema + per-source summary of stations.json
    sources_list.py          look up source ids defined in fetch_stations.py
    source_health.py         check status of one or all sources
    network_lookup.py        find every mention of a network/source across the repo
"""
import json, math, sys
from collections import Counter
from pathlib import Path

STATIONS = Path(__file__).parent.parent / "data" / "stations.json"

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    return R * 2 * math.asin(math.sqrt(a))

if len(sys.argv) not in (4, 5) or (len(sys.argv) == 5 and sys.argv[4].lower() != "full"):
    print(__doc__)
    sys.exit(1)

try:
    lat, lon, radius = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
except ValueError:
    print(__doc__)
    sys.exit(1)
full = len(sys.argv) == 5
data = json.loads(STATIONS.read_text())["sources"]
SOURCES = sorted(data.keys())

total = 0
matched_sources = 0
total_skipped = 0
for src in SOURCES:
    hits = []
    skipped = 0
    for s in data[src]["stations"]:
        try:
            d = haversine(lat, lon, s["lat"], s["lon"])
        except (TypeError, KeyError):
            skipped += 1
            continue
        if d <= radius:
            hits.append((d, s))
    total_skipped += skipped
    if hits:
        status = data[src].get("status", "?")
        status_note = f"  [status: {status}]" if status != "ok" else ""
        skip_note = f"  [{skipped} skipped: bad lat/lon]" if skipped else ""
        if full:
            print(f"\n{src} -- {len(hits)} station(s) within {radius:.0f} km:{status_note}{skip_note}")
            for d, s in sorted(hits, key=lambda x: (x[0], x[1]["name"])):
                cc = s.get("country") or "--"
                print(f"  {s['name']:<21} {s['lat']:>9.4f}  {s['lon']:>10.4f}  {d:>6.1f} km  [{cc}]")
        else:
            cc_counts = Counter((s.get("country") or "--") for _, s in hits)
            cc_str = ", ".join(f"{cc}:{n}" for cc, n in sorted(cc_counts.items(), key=lambda x: (-x[1], x[0])))
            print(f"{src:<24} {len(hits):>5}  [{cc_str}]{status_note}{skip_note}")
        total += len(hits)
        matched_sources += 1

if total:
    note = f"  ({total_skipped} skipped: bad lat/lon)" if total_skipped else ""
    print(f"\n# total: {total} station(s) across {matched_sources} source(s){note}")
    if not full:
        print("# add `full` for per-station dump.")
else:
    print(f"No stations within {radius:.0f} km of ({lat}, {lon}).")
