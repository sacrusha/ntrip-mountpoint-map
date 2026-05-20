#!/usr/bin/env python3
"""Cross-file contract check: every slot in color_assignments.json must
have a matching entry in the PALETTE const in index.html.

The slot-name enum (global1..global5, community1..community2,
local1..localN) is split across two files: assign_colors.py emits it,
index.html resolves it to hex. If the two drift -- e.g. assign_colors.py
ladders k up to 5 and emits "local5", but index.html's PALETTE still
stops at local4 -- the affected sources silently fall back to
UNKNOWN_SOURCE_COLOR (#888). This check catches that before it ships.

Usage:
    py scripts/palette_check.py    # exit 0 if contract holds, 1 if not.
    py scripts/palette_check.py -h

Not wired into the pipeline (yet); run manually after editing the local
palette in index.html or after a noticeable jump in slot population.

Related tools (in this directory):
    sources_list.py          look up source ids defined in fetch_stations.py
    stations_inspect.py      schema + per-source summary of stations.json
    source_health.py         per-source health from data/source_health.json
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSIGNMENTS = ROOT / "data" / "color_assignments.json"
INDEX_HTML = ROOT / "index.html"


def main() -> int:
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        return 0

    used = set(json.loads(ASSIGNMENTS.read_text(encoding="utf-8"))["assignments"].values())
    html = INDEX_HTML.read_text(encoding="utf-8")
    m = re.search(r"var PALETTE\s*=\s*\{(.*?)\};", html, re.DOTALL)
    if not m:
        print("ERR: PALETTE const not found in index.html", file=sys.stderr)
        return 2
    palette = set(re.findall(r'"([a-z0-9]+)"\s*:', m.group(1)))

    missing = used - palette
    extra = palette - used

    print(f"slots in assignments: {sorted(used)}")
    print(f"slots in PALETTE:     {sorted(palette)}")
    print(f"missing palette for:  {sorted(missing) if missing else 'none'}")
    print(f"unused palette slots: {sorted(extra) if extra else 'none'}")

    if missing:
        print(f"\nFAIL: {len(missing)} slot(s) emitted by assign_colors.py "
              f"with no PALETTE entry. Affected sources render as "
              f"UNKNOWN_SOURCE_COLOR.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
