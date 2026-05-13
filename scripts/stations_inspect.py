#!/usr/bin/env python3
"""Summarise the shape and contents of data/stations.json.

Today's session logs show agents repeatedly writing 4–10-line `py -c` snippets
to rediscover this file's structure (top keys, sources list, per-source station
keys). This prints all of that in one go, no quoting required.

Usage:
    py scripts/stations_inspect.py                # global summary
    py scripts/stations_inspect.py <source_id>    # detail for one source
    py scripts/stations_inspect.py --sample 3     # show 3 sample stations per source

Examples:
    py scripts/stations_inspect.py
    py scripts/stations_inspect.py rtk2go
    py scripts/stations_inspect.py centipede --sample 5

Related tools (in this directory):
    sources_list.py          look up source ids defined in fetch_stations.py
    source_health.py         check status of one or all sources
    stations_by_country.py   list stations for a country code
    stations_by_radius.py    list stations within a radius of a lat/lon
    network_lookup.py        find every mention of a network/source across the repo
"""
import argparse, json, os, subprocess, sys
from pathlib import Path

# repo data contains non-cp1252 characters (en-dash, arrows in some labels).
# Re-launch in utf8 mode if needed so prints don't crash on Windows.
if not sys.flags.utf8_mode:
    r = subprocess.run([sys.executable, "-X", "utf8", *sys.argv])
    sys.exit(r.returncode)

STATIONS = Path(__file__).resolve().parent.parent / "data" / "stations.json"


def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        return 0

    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("source", nargs="?", default=None)
    ap.add_argument("--sample", type=int, default=1,
                    help="how many sample stations to print per source (default 1)")
    args = ap.parse_args()

    if not STATIONS.exists():
        print(f"missing: {STATIONS}", file=sys.stderr)
        return 1

    data = json.loads(STATIONS.read_text(encoding="utf-8"))
    sources = data["sources"]

    if args.source is None:
        print(f"file:     {STATIONS}")
        print(f"updated:  {data.get('updated')}")
        print(f"scope:    {data.get('scope')}")
        print(f"top keys: {list(data.keys())}")
        print(f"source-record keys: {list(next(iter(sources.values())).keys())}")
        first_with_stations = next((v for v in sources.values() if v.get('stations')), None)
        if first_with_stations:
            print(f"station-record keys: {list(first_with_stations['stations'][0].keys())}")
        total = sum(len(v["stations"]) for v in sources.values())
        print(f"\nsources: {len(sources)} total, {total} stations across them")
        # one line per source, sorted by station count desc
        rows = sorted(((sid, len(s["stations"]), s.get("status", "?"))
                       for sid, s in sources.items()),
                      key=lambda r: -r[1])
        print(f"\n{'source':<22} {'stations':>9}  status")
        print(f"{'-'*22} {'-'*9}  {'-'*6}")
        for sid, n, status in rows:
            print(f"{sid:<22} {n:>9}  {status}")
        print("\nRe-run with a source id (e.g. `py scripts/stations_inspect.py rtk2go`) "
              "to see its caster URL, credentials note, and sample stations.")
        return 0

    sid = args.source
    if sid not in sources:
        candidates = [k for k in sources if sid.lower() in k.lower()]
        msg = f"unknown source '{sid}'."
        if candidates:
            msg += f" did you mean: {', '.join(candidates)}?"
        print(msg, file=sys.stderr)
        return 2

    s = sources[sid]
    print(f"source:      {sid}")
    for key in ("label", "url", "type", "country", "region", "group",
                "credentials", "registration", "access", "user", "pass",
                "status", "fetched_at", "last_ok", "openNote", "userNote", "near"):
        if key in s and s[key] not in (None, "", []):
            val = s[key]
            if isinstance(val, str) and len(val) > 140:
                val = val[:137] + "..."
            print(f"  {key:<13} {val}")
    stations = s.get("stations", [])
    print(f"\nstations:    {len(stations)}")
    if stations:
        # country breakdown
        from collections import Counter
        cc = Counter(st.get("country", "") for st in stations)
        common = cc.most_common(10)
        print(f"countries:   {len(cc)} distinct; top: " +
              ", ".join(f"{c}={n}" for c, n in common))
        print(f"\nsample (first {min(args.sample, len(stations))}):")
        for st in stations[: args.sample]:
            print(f"  {st}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
