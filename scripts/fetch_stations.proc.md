# fetch_stations.py — process

Per-file rules for `scripts/fetch_stations.py` source code. Pipeline
context: `../docs/pipeline.md`.

## Role

NTRIP-protocol fetcher and sourcetable parser. Reads operational config
from `../data/rtk_map.json` endpoints; writes `data/stations.json` +
`data/source_health.json` + cached `data/<endpoint_id>.sourcetable`
files. Run by GitHub Actions cron 4×/day.

## When to edit this file

Adding, removing, or retuning a network is **not** a `.py` edit any
more — it is a data edit in `../data/rtk_map.json`. See
`../data/rtk_map.proc.md` for the pipeline-operation rules (status→
endpoints sweep, filter flag overrides, multi-endpoint setup,
port-picking, after-edit checks).

Edit `fetch_stations.py` when the script's own behaviour needs
adjusting:

- NTRIP protocol / sourcetable shape evolves (new fields, new STR
  layout, new transport quirks).
- Parser needs a new carrier class, format mapping, or coordinate
  normalisation.
- Fetch transport needs a new fallback (raw NTRIP/1.0 TCP was added
  when modern HTTP clients started failing on the caster's
  `BadStatusLine`).
- stations.json schema gains an operational field (e.g. per-endpoint
  status detail), or the merge rules across endpoints change.

## stations.json source-record schema

Operational fields only — fetched / runtime state. Editorial fields
(`label`, `region`, `access`, `registration`, `note`, `country`, ...)
live in `../data/rtk_map.json` and are read by `index.html` via
`markersById[sid]` at render time. Do not re-introduce them here; the
dual write was cleaned out to eliminate drift. Current source-record
keys: `url`, `credentials`, `near`, `user`, `pass`, `userNote`,
`status`, `fetched_at`, `last_ok`, `stations`.

## After-edit checks

```sh
# Module-load smoke test:
python -c "from scripts.fetch_stations import NETWORKS, SOURCES; print(len(NETWORKS), len(SOURCES))"

# Local dry-fetch when network is available (fails open in sandbox):
python scripts/fetch_stations.py
# Expected stdout per endpoint: "[sid] fetched N stations (dropped X DGNSS, Y invalid[, Z net-sol])"
```
