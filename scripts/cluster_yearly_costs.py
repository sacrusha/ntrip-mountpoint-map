#!/usr/bin/env python3
"""Quick-and-dirty: extract yearly_cost_normalized from country_markers.json
and look for natural cluster boundaries a few different ways.

Usage: python3 scripts/cluster_yearly_costs.py
"""
import json, math, statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "data" / "country_markers.json").read_text())

rows = []
for m in data.get("markers", []):
    if not isinstance(m, dict): continue
    n = m.get("yearly_cost_normalized")
    if n is None: continue
    rows.append((n, m.get("tier"), m.get("id")))

rows.sort()
vals = [r[0] for r in rows]
n = len(vals)

print(f"=== {n} entries with yearly_cost_normalized ===")
print(f"min={min(vals)} max={max(vals)} mean={statistics.mean(vals):.0f} "
      f"median={statistics.median(vals):.0f}")
qs = statistics.quantiles(vals, n=10)
print("deciles: " + ", ".join(f"{q:.0f}" for q in qs))

# --- 1. Sorted dump with current tier label
print("\n=== sorted (norm | tier | id) ===")
for v, t, i in rows:
    flag = " <-- AFFORDABLE" if t == "paid-affordable" else ""
    print(f"{v:6d}  {t or '':18s}  {i}{flag}")

# --- 2. Largest gaps between consecutive values (natural breaks)
print("\n=== top 10 gaps between consecutive values ===")
gaps = []
for i in range(1, n):
    g = vals[i] - vals[i-1]
    gaps.append((g, vals[i-1], vals[i]))
gaps.sort(reverse=True)
for g, lo, hi in gaps[:10]:
    print(f"gap={g:5d}  between {lo} and {hi}")

# --- 3. Histogram (log-ish buckets)
print("\n=== bucket histogram ===")
buckets = [(0,100),(100,150),(150,200),(200,250),(250,300),(300,400),
           (400,500),(500,750),(750,1000),(1000,1500),(1500,2500),(2500,10000)]
for lo, hi in buckets:
    c = sum(1 for v in vals if lo <= v < hi)
    aff = sum(1 for v,t,_ in rows if lo <= v < hi and t=='paid-affordable')
    bar = "#" * c
    print(f"  [{lo:5d},{hi:5d})  n={c:3d}  affordable={aff:2d}  {bar}")

# --- 4. 1-D k-means for k=2 and k=3 (Jenks-ish via simple iteration)
def kmeans1d(xs, k, iters=100):
    xs = sorted(xs)
    # init: evenly-spaced quantiles
    centers = [xs[int((i+0.5)*len(xs)/k)] for i in range(k)]
    for _ in range(iters):
        groups = [[] for _ in range(k)]
        for x in xs:
            j = min(range(k), key=lambda j: abs(x - centers[j]))
            groups[j].append(x)
        new_centers = [statistics.mean(g) if g else centers[j]
                       for j,g in enumerate(groups)]
        if new_centers == centers: break
        centers = new_centers
    # boundaries: midpoints
    centers.sort()
    bounds = [(centers[i]+centers[i+1])/2 for i in range(k-1)]
    return centers, bounds, [len([x for x in xs if (i==0 or x>=bounds[i-1])
                                  and (i==k-1 or x<bounds[i])])
                             for i in range(k)]

for k in (2, 3, 4):
    c, b, sizes = kmeans1d(vals, k)
    print(f"\n=== k-means k={k} ===")
    print(f"  centers: {[round(x) for x in c]}")
    print(f"  boundaries: {[round(x) for x in b]}")
    print(f"  sizes: {sizes}")

# --- 5. Where does current 'paid-affordable' tag actually sit?
aff_vals = [v for v,t,_ in rows if t=='paid-affordable']
paid_vals = [v for v,t,_ in rows if t=='paid']
if aff_vals:
    print(f"\n=== current 'paid-affordable' (n={len(aff_vals)}) ===")
    print(f"  values: {sorted(aff_vals)}")
    print(f"  max affordable = {max(aff_vals)}")
if paid_vals:
    print(f"=== current 'paid' (n={len(paid_vals)}) ===")
    print(f"  min paid = {min(paid_vals)}")
    overlap_lo = min(paid_vals)
    overlap_hi = max(aff_vals) if aff_vals else 0
    if overlap_hi >= overlap_lo:
        print(f"  OVERLAP: paid range starts at {overlap_lo}, "
              f"affordable extends to {overlap_hi}")
        in_overlap = [(v,t,i) for v,t,i in rows
                      if overlap_lo <= v <= overlap_hi]
        for v,t,i in sorted(in_overlap):
            print(f"    {v:5d}  {t:18s}  {i}")
