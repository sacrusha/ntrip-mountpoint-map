#!/usr/bin/env python3
"""List rtk2go / Centipede / EarthScope (NOTA) stations within a radius.

Usage:  python scripts/stations_by_radius.py <lat> <lon> <radius_km>
Example: python scripts/stations_by_radius.py 48.85 2.35 150
"""
import json, math, sys
from pathlib import Path

STATIONS = Path(__file__).parent.parent / "data" / "stations.json"
SOURCES  = ["rtk2go", "centipede", "earthscope"]

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    return R * 2 * math.asin(math.sqrt(a))

if len(sys.argv) != 4:
    print(__doc__)
    sys.exit(1)

lat, lon, radius = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
data = json.loads(STATIONS.read_text())["sources"]

total = 0
for src in SOURCES:
    hits = []
    for s in data[src]["stations"]:
        d = haversine(lat, lon, s["lat"], s["lon"])
        if d <= radius:
            hits.append((d, s))
    if hits:
        print(f"\n{src} — {len(hits)} station(s) within {radius:.0f} km:")
        for d, s in sorted(hits):
            print(f"  {s['name']:<24} {s['lat']:>9.4f}  {s['lon']:>10.4f}  {d:>6.1f} km  [{s['country']}]")
        total += len(hits)

if not total:
    print(f"No stations within {radius:.0f} km of ({lat}, {lon}).")
