#!/usr/bin/env python3
"""Inspect data/source_health.json without paging through 350+ lines.

Each source record carries: `status`, `last_ok`, `station_count`,
`station_count_prev`, `station_count_declared` (from research, via the
rtk_map.json marker), and optional `flags` set at write time:
  - `regression` : current count < 75% of last successful snapshot.
  - `incomplete` : current count < 50% of research-declared count.

Usage:
    py scripts/source_health.py                  # summary: counts + non-ok + flagged
    py scripts/source_health.py <source_id> ...  # per-source detail
    py scripts/source_health.py --all            # full table, every source
    py scripts/source_health.py --flagged        # one-liner per flagged source

Examples:
    py scripts/source_health.py
    py scripts/source_health.py rtk2go centipede
    py scripts/source_health.py --flagged

Related tools: stations_inspect.py, sources_list.py.
"""
import json, sys
from pathlib import Path
from collections import Counter

HEALTH = Path(__file__).resolve().parent.parent / "data" / "source_health.json"


def _fmt_count(rec: dict) -> str:
    cur = rec.get("station_count")
    prev = rec.get("station_count_prev")
    decl = rec.get("station_count_declared")
    parts = [f"count={cur}" if cur is not None else "count=?"]
    if prev is not None:
        parts.append(f"prev={prev}")
    if decl is not None:
        parts.append(f"declared={decl}")
    return " ".join(parts)


def _fmt_row(sid: str, rec: dict) -> str:
    flags = rec.get("flags") or []
    flag_s = f"[{','.join(flags)}]" if flags else ""
    return (f"{sid:<22} {rec.get('status','?'):<8} "
            f"{_fmt_count(rec):<35} {flag_s:<22} "
            f"last_ok={rec.get('last_ok','-')}")


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
    show_flagged = "--flagged" in sys.argv

    if show_flagged:
        flagged = {k: v for k, v in sources.items() if v.get("flags")}
        if not flagged:
            print("no flagged sources.")
            return 0
        for sid in sorted(flagged):
            print(_fmt_row(sid, sources[sid]))
        return 0

    if not args and not show_all:
        statuses = Counter(s.get("status", "?") for s in sources.values())
        print(f"checked_at: {checked_at}")
        print(f"sources:    {len(sources)} total")
        for status, n in statuses.most_common():
            print(f"  {status:<10} {n}")
        non_ok = {k: v for k, v in sources.items() if v.get("status") != "ok"}
        flagged = {k: v for k, v in sources.items() if v.get("flags")}
        if non_ok:
            print(f"\nnon-ok sources ({len(non_ok)}):")
            for sid, v in sorted(non_ok.items()):
                print(f"  {_fmt_row(sid, v)}")
        if flagged:
            print(f"\nflagged sources ({len(flagged)}):")
            for sid, v in sorted(flagged.items()):
                print(f"  {_fmt_row(sid, v)}")
        if not non_ok and not flagged:
            print("\nall sources currently ok, no count regressions.")
        return 0

    targets = sorted(sources) if show_all else args
    missing = [t for t in targets if t not in sources]
    if missing and not show_all:
        for t in missing:
            candidates = [k for k in sources if t.lower() in k.lower()]
            hint = f" did you mean: {', '.join(candidates)}?" if candidates else ""
            print(f"unknown source '{t}'.{hint}", file=sys.stderr)
        if all(t in missing for t in targets):
            return 2

    print(f"checked_at: {checked_at}\n")
    print(f"{'source':<22} {'status':<8} {'counts':<35} {'flags':<22} last_ok")
    print(f"{'-'*22} {'-'*8} {'-'*35} {'-'*22} {'-'*25}")
    for t in targets:
        if t in sources:
            print(_fmt_row(t, sources[t]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
