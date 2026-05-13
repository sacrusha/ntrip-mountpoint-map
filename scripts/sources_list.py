#!/usr/bin/env python3
"""List / filter the SOURCES configured in scripts/fetch_stations.py.

Today's session logs show agents writing the same 3-line snippet five times
(`from scripts.fetch_stations import SOURCES; ... if "fvg" in s["id"].lower()`)
and occasionally fighting with multi-line `py -c` quoting on Windows. This
covers that need without quoting gymnastics.

Usage:
    py scripts/sources_list.py                       # one-line summary per source
    py scripts/sources_list.py <substring>           # filter by id substring (case-insensitive)
    py scripts/sources_list.py --country FRA         # filter by source.country
    py scripts/sources_list.py --group europe        # filter by source.group
    py scripts/sources_list.py --field id,url,group  # pick columns
    py scripts/sources_list.py --json                # dump matching entries as JSON

Examples:
    py scripts/sources_list.py fvg
    py scripts/sources_list.py --country ITA
    py scripts/sources_list.py rtk --field id,url,nmea_filter,solution_filter

Related tools: stations_inspect.py, source_health.py, network_lookup.py.
"""
import argparse, json, os, subprocess, sys
from pathlib import Path

# scripts/fetch_stations.py re-execs with `-X utf8` on import when the
# interpreter isn't already in utf8 mode. On Windows that re-exec buffers our
# stdout into the next caller's output (os.execv is emulated via spawn-and-exit).
# Pre-empt: if we're not in utf8 mode, relaunch ourselves via subprocess and
# forward exit code. This keeps stdout/stderr connected.
if not sys.flags.utf8_mode:
    r = subprocess.run([sys.executable, "-X", "utf8", *sys.argv])
    sys.exit(r.returncode)

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def load_sources():
    try:
        from scripts.fetch_stations import SOURCES  # type: ignore
    except Exception as e:
        print(f"failed to import SOURCES from scripts/fetch_stations.py: {e}",
              file=sys.stderr)
        sys.exit(1)
    return SOURCES


def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        return 0

    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("substring", nargs="?", default=None,
                    help="case-insensitive substring match on source id or label")
    ap.add_argument("--country", default=None)
    ap.add_argument("--group", default=None)
    ap.add_argument("--region", default=None)
    ap.add_argument("--field", default=None,
                    help="comma-separated list of fields to print (default: id,country,group,url)")
    ap.add_argument("--json", action="store_true", help="dump matching entries as JSON")
    args = ap.parse_args()

    sources = load_sources()
    needle = (args.substring or "").lower()

    def _as_list(v):
        if v is None: return []
        return v if isinstance(v, (list, tuple)) else [v]

    def match(s):
        if needle and needle not in s.get("id", "").lower() \
                 and needle not in str(s.get("label", "")).lower():
            return False
        if args.country:
            wanted = args.country.upper()
            if not any(str(c).upper() == wanted for c in _as_list(s.get("country"))):
                return False
        if args.group:
            wanted = args.group.lower()
            if not any(str(g).lower() == wanted for g in _as_list(s.get("group"))):
                return False
        if args.region:
            wanted = args.region.lower()
            if not any(str(r).lower() == wanted for r in _as_list(s.get("region"))):
                return False
        return True

    hits = [s for s in sources if match(s)]

    if args.json:
        json.dump(hits, sys.stdout, indent=2, default=str)
        print()
        return 0

    if not hits:
        print(f"no SOURCES match. total defined: {len(sources)}. "
              f"run without args to see all.")
        return 1

    fields = (args.field or "id,country,group,url").split(",")
    widths = {f: max(len(f), max((len(str(s.get(f, ""))) for s in hits), default=0))
              for f in fields}
    print("  ".join(f.ljust(widths[f]) for f in fields))
    print("  ".join("-" * widths[f] for f in fields))
    for s in hits:
        print("  ".join(str(s.get(f, "")).ljust(widths[f]) for f in fields))
    print(f"\n{len(hits)} of {len(sources)} sources shown.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
