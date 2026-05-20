"""Assign one of N descriptive palette slots to every NTRIP source.

Inputs
------
data/stations.json
    Authoritative mountpoint locations per source. A source qualifies for
    a slot iff it has >=1 mountpoint.

data/color_assignments.json (optional)
    Previous run's assignments. Used as a stickiness preference so reruns
    rarely shuffle local buckets.

Output
------
data/color_assignments.json
    {"assignments": {source_id: slot_name, ...}}

    slot_name is one of:
      "global1".."global5"     -- hand-set tier-1 networks (IGS, AUSCORS, MIRAI,
                                   EUREF-IP, EarthScope). Geography-independent
                                   slots; mapping is constant.
      "community1".."community2"  -- hand-set community networks (centipede, rtk2go).
      "local1".."localN"        -- computed locals. N defaults to 4; grows if
                                   the conflict graph demands it.

Algorithm
---------
1. Per source, dedupe coincident coords, then density-aware cluster:
   compute each point's nearest-neighbour distance, take Tukey fence
   tau = Q3 + 1.5*IQR over that NN distribution, union-find on edges
   <= tau. Every connected component is a cluster (singletons included
   -- they are visually-important outliers; their participation in the
   conflict graph forces their source's bucket to differ from
   surrounding foreign sources).

2. Pool all cluster coords across sources; coincident coords across
   sources are merged into one point with multi-cluster ownership.

3. Delaunay-triangulate the pool. For every Delaunay edge between two
   points whose owner clusters span different sources, emit a conflict
   edge between those sources. Same for cross-source pairs at a
   multi-owner coord.

4. Collapse: one supernode per local source (all its clusters share its
   bucket by design). Conflict graph G is at the source level.

5. k-color G. Target k=4; ladder up if infeasible. Among all valid
   k-colorings, pick the one maximising matches with the previous
   cache. On first run (empty cache), substitute a spread pseudo-cache
   so colors distribute evenly across the four buckets.
"""
from __future__ import annotations

import json
import math
import sys
from collections import defaultdict
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
STATIONS_FILE = DATA_DIR / "stations.json"
CACHE_FILE = DATA_DIR / "color_assignments.json"

# Hand-set slot mappings. These IDs key directly into the palette in
# index.html, so the script emits them verbatim. They are excluded from
# local clustering.
GLOBAL_SLOTS = {
    "igs_ip":     "global1",
    "auscors":    "global2",
    "mirai":      "global3",
    "euref_ip":   "global4",
    "nps_cors":   "global4",  # dual slot with EUREF; non-overlapping geography
    "earthscope": "global5",
}
COMMUNITY_SLOTS = {
    "centipede": "community1",
    "rtk2go":    "community2",
}
FIXED_SLOTS = {**GLOBAL_SLOTS, **COMMUNITY_SLOTS}

EARTH_KM = 6371.0
COORD_PRECISION = 4
TARGET_K = 4
MAX_K = 9
# Cap Delaunay edges at this length when deriving cross-source adjacency.
# Sparse global Delaunay produces spurious "neighbour" pairs across oceans
# (e.g., NY <-> NZ); those are not visually-adjacent on the map and would
# bloat the conflict graph. 2000 km keeps real continental adjacencies
# (NL <-> IT, BR <-> AR) and cuts trans-oceanic noise.
MAX_DELAUNAY_EDGE_KM = 2000.0


def haversine_km(a, b):
    la1, lo1 = math.radians(a[0]), math.radians(a[1])
    la2, lo2 = math.radians(b[0]), math.radians(b[1])
    dla, dlo = la2 - la1, lo2 - lo1
    h = math.sin(dla / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin(dlo / 2) ** 2
    return 2 * EARTH_KM * math.asin(math.sqrt(h))


def quantile(xs, q):
    s = sorted(xs)
    idx = q * (len(s) - 1)
    lo = int(idx)
    hi = min(lo + 1, len(s) - 1)
    return s[lo] + (s[hi] - s[lo]) * (idx - lo)


def union_find(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    return list(groups.values())


def cluster_source(stations):
    """Return list of clusters; each cluster = list of (lat, lon) tuples."""
    uniq = set()
    for s in stations:
        if s.get("lat") is None or s.get("lon") is None:
            continue
        uniq.add((round(s["lat"], COORD_PRECISION), round(s["lon"], COORD_PRECISION)))
    pts = list(uniq)
    n = len(pts)
    if n == 0:
        return []
    if n == 1:
        return [pts]
    nn = []
    for i in range(n):
        best = float("inf")
        for j in range(n):
            if i == j:
                continue
            d = haversine_km(pts[i], pts[j])
            if d < best:
                best = d
        nn.append(best)
    if n < 4:
        fence = max(nn)
    else:
        q1 = quantile(nn, 0.25)
        q3 = quantile(nn, 0.75)
        fence = q3 + 1.5 * (q3 - q1)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if haversine_km(pts[i], pts[j]) <= fence:
                edges.append((i, j))
    comps = union_find(n, edges)
    return [[pts[i] for i in c] for c in comps]


def build_clusters(stations_data):
    """Return (clusters, coord_to_owners).

    clusters: list of {id, source, coords}.
    coord_to_owners: dict (lat,lon) -> list of cluster ids touching that coord.
    """
    clusters = []
    coord_to_owners = defaultdict(list)
    for sid in sorted(stations_data["sources"].keys()):
        if sid in FIXED_SLOTS:
            continue
        src = stations_data["sources"][sid]
        comps = cluster_source(src.get("stations", []))
        for idx, coords in enumerate(comps):
            cid = f"{sid}#{idx}"
            clusters.append({"id": cid, "source": sid, "coords": coords})
            for c in coords:
                coord_to_owners[c].append(cid)
    return clusters, dict(coord_to_owners)


def build_conflicts(clusters, coord_to_owners):
    """Return adjacency dict source_id -> set of conflicting source_ids."""
    cluster_by_id = {c["id"]: c for c in clusters}
    conflicts = defaultdict(set)

    def add(s_a, s_b):
        if s_a == s_b:
            return
        conflicts[s_a].add(s_b)
        conflicts[s_b].add(s_a)

    for owners in coord_to_owners.values():
        for i in range(len(owners)):
            for j in range(i + 1, len(owners)):
                add(cluster_by_id[owners[i]]["source"], cluster_by_id[owners[j]]["source"])

    coords = list(coord_to_owners.keys())
    if len(coords) >= 4:
        from scipy.spatial import Delaunay
        import numpy as np

        arr = np.array(coords, dtype=float)
        tri = Delaunay(arr)
        edge_pairs = set()
        for simplex in tri.simplices:
            for i in range(3):
                for j in range(i + 1, 3):
                    a, b = int(simplex[i]), int(simplex[j])
                    if a > b:
                        a, b = b, a
                    edge_pairs.add((a, b))
        for a, b in edge_pairs:
            if haversine_km(coords[a], coords[b]) > MAX_DELAUNAY_EDGE_KM:
                continue
            owners_a = coord_to_owners[coords[a]]
            owners_b = coord_to_owners[coords[b]]
            for cid_a in owners_a:
                s_a = cluster_by_id[cid_a]["source"]
                for cid_b in owners_b:
                    s_b = cluster_by_id[cid_b]["source"]
                    add(s_a, s_b)

    return {s: set(ns) for s, ns in conflicts.items()}


def color_search(sources, conflicts, pref, k):
    """Search for a valid k-coloring maximising pref-match.

    pref maps source -> preferred bucket (used as cache OR first-run spread).
    Returns (assignments, match_count) or None if infeasible.
    """
    order = sorted(sources, key=lambda s: (-len(conflicts.get(s, set())), s))
    n = len(order)
    best = {"match": -1, "assignments": None}
    current = {}

    def recurse(idx, matches):
        if matches + (n - idx) <= best["match"]:
            return
        if idx == n:
            if matches > best["match"]:
                best["match"] = matches
                best["assignments"] = dict(current)
            return
        s = order[idx]
        forbidden = set()
        for neigh in conflicts.get(s, ()):
            if neigh in current:
                forbidden.add(current[neigh])
        preferred = pref.get(s)
        candidates = []
        if preferred is not None and 0 <= preferred < k and preferred not in forbidden:
            candidates.append(preferred)
        for b in range(k):
            if b in forbidden or b == preferred:
                continue
            candidates.append(b)
        for b in candidates:
            current[s] = b
            is_match = preferred is not None and b == preferred
            recurse(idx + 1, matches + (1 if is_match else 0))
            if best["match"] == n:
                return
        current.pop(s, None)

    recurse(0, 0)
    if best["assignments"] is None:
        return None
    return best["assignments"], best["match"]


def load_cache():
    """Read previous slot assignments as {source_id: slot_name}."""
    if not CACHE_FILE.exists():
        return {}
    try:
        prev = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    if not isinstance(prev, dict):
        return {}
    assignments = prev.get("assignments")
    if not isinstance(assignments, dict):
        return {}
    return {s: slot for s, slot in assignments.items() if isinstance(slot, str)}


def assign_locals(stations_data, cache):
    """Cluster locals, build conflict graph, k-color with cache-stickiness."""
    clusters, coord_to_owners = build_clusters(stations_data)
    conflicts = build_conflicts(clusters, coord_to_owners)
    sources = sorted({c["source"] for c in clusters})

    # Parse "localN" cache strings into 0-based bucket ints.
    cached_buckets = {}
    for s, slot in cache.items():
        if isinstance(slot, str) and slot.startswith("local"):
            try:
                cached_buckets[s] = int(slot[5:]) - 1
            except ValueError:
                pass

    if cached_buckets:
        pref = {s: cached_buckets[s] for s in sources if s in cached_buckets}
    else:
        pref = {s: i % TARGET_K for i, s in enumerate(sources)}

    for k in range(TARGET_K, MAX_K + 1):
        res = color_search(sources, conflicts, pref, k)
        if res is not None:
            bucket_of_source, match = res
            return bucket_of_source, k, match, conflicts
    raise RuntimeError(f"could not k-color local graph at k<={MAX_K}; investigate conflict density")


def main(verbose=False, dry_run=False):
    data = json.loads(STATIONS_FILE.read_text(encoding="utf-8"))
    cache = load_cache()
    local_bucket_of, k, match, conflicts = assign_locals(data, cache)

    out_assignments = {}
    for sid, src in data["sources"].items():
        if not src.get("stations"):
            continue
        if sid in FIXED_SLOTS:
            out_assignments[sid] = FIXED_SLOTS[sid]
        elif sid in local_bucket_of:
            out_assignments[sid] = f"local{local_bucket_of[sid] + 1}"
        # else: source had stations but produced no clusters; skip.

    out = {"assignments": dict(sorted(out_assignments.items()))}
    if not dry_run:
        CACHE_FILE.write_text(
            json.dumps(out, indent=2) + "\n",
            encoding="utf-8",
        )
    if verbose:
        slot_count = defaultdict(int)
        for slot in out_assignments.values():
            slot_count[slot] += 1
        changed = sum(
            1 for sid, slot in out_assignments.items()
            if cache.get(sid) and cache[sid] != slot
        )
        cached_present = sum(1 for sid in out_assignments if sid in cache)
        print(f"local_buckets={k}  sources={len(out_assignments)}  "
              f"cache_hits={match}/{cached_present}  changed={changed}")
        print(f"slot population: {dict(sorted(slot_count.items()))}")
        for sid in sorted(out_assignments):
            slot = out_assignments[sid]
            if sid in cache:
                tag = "" if cache[sid] == slot else f" (was {cache[sid]})"
            else:
                tag = " (new)"
            neigh = sorted(conflicts.get(sid, set())) if sid not in FIXED_SLOTS else []
            tail = f"  neighbours={neigh}" if neigh else ""
            print(f"  {sid:22s} {slot}{tag}{tail}")
    return out


if __name__ == "__main__":
    main(
        verbose=("-v" in sys.argv or "--verbose" in sys.argv or "--dry" in sys.argv),
        dry_run=("--dry" in sys.argv),
    )
