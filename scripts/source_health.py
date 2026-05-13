#!/usr/bin/env python3
"""Inspect data/source_health.json without paging through 350+ lines.

Today's session logs show `sed -n '85,95p' data/source_health.json` being used
to fish out a single source's status. This tool does that by name, and also
gives a global view of every source that is not currently `ok`.

Usage:
    py scripts/source_health.py                  # checked_at + counts + non-ok list
    py scripts/source_health.py <source_id> ...  # status for one or more sources
    py scripts/source_health.py --all            # full table, every source

Examples:
    py scripts/source_health.py
    py scripts/source_health.py rtk2go centipede
    py scripts/source_health.py --all

Related tools: stations_inspect.py, sources_list.py.
"""
import json, sys
from pathlib import Path
from collections import Counter

HEALTH = Path(__file__).resolve().parent.parent / "data" / "source_health.json"


def main():
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        return 0
    if not HEALTH.exists():
        print(f"missing: {HEALTH}", file=sys.stderr)
        return 1

    data = json.loads(HEALTH.read_text(encoding="utf-8"))
    checked_at = data.get("checked_at", "?")
    sources = data.get("sources", {})

    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    show_all = "--all" in sys.argv

    if not args and not show_all:
        statuses = Counter(s.get("status", "?") for s in sources.values())
        print(f"checked_at: {checked_at}")
        print(f"sources:    {len(sources)} total")
        for status, n in statuses.most_common():
            print(f"  {status:<10} {n}")
        non_ok = {k: v for k, v in sources.items() if v.get("status") != "ok"}
        if non_ok:
            print(f"\nnon-ok sources ({len(non_ok)}):")
            for sid, v in sorted(non_ok.items()):
                print(f"  {sid:<22} {v.get('status','?'):<10}  last_ok={v.get('last_ok','-')}")
        else:
            print("\nall sources currently ok.")
        return 0

    if show_all:
        targets = sorted(sources)
    else:
        targets = args

    missing = [t for t in targets if t not in sources]
    if missing and not show_all:
        for t in missing:
            candidates = [k for k in sources if t.lower() in k.lower()]
            hint = f" did you mean: {', '.join(candidates)}?" if candidates else ""
            print(f"unknown source '{t}'.{hint}", file=sys.stderr)
        if all(t in missing for t in targets):
            return 2

    print(f"checked_at: {checked_at}\n")
    print(f"{'source':<22} {'status':<10}  last_ok")
    print(f"{'-'*22} {'-'*10}  {'-'*25}")
    for t in targets:
        if t not in sources:
            continue
        v = sources[t]
        print(f"{t:<22} {v.get('status','?'):<10}  {v.get('last_ok','-')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
