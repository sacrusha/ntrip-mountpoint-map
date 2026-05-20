"""Top-level data-refresh orchestrator.

Invoked by scripts/run_in_worktree.ps1. Imports the two Python refresh
steps and runs them in-process so they share working directory + env,
and any failure surfaces as a single Python traceback rather than
masking behind separate subprocess exit codes.

Steps:
  1. fetch_stations.main()  -> data/stations.json, data/source_health.json,
                                data/<sid>.sourcetable
  2. assign_colors.main()   -> data/color_assignments.json

Deploy is the caller's responsibility (deploy_pages.ps1).
"""
from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import fetch_stations
    import assign_colors

    rc = fetch_stations.main()
    if rc != 0:
        return rc
    assign_colors.main()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
