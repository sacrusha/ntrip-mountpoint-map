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

## Coord overrides (operator-published bad coords)

Some casters publish wrong or placeholder antenna coords (Trimble Pivot
Platform installs are repeat offenders; NPS had 22 sites off by 30–4700
km, ERGNSS ICOL0 rounds 1-decimal sloppily so the truth falls outside
the uncertainty rectangle). Per-station overrides live in
`../data/coord_overrides.json`.

Entry shape:
```json
{ "mountpoint": "NAME", "bad": {"lat": X, "lon": Y},
  "fix": {"lat": X', "lon": Y'[, "latPrec": N, "lonPrec": N]},
  "note": "why + provenance" }
```

`parse_sourcetable` loads the file once at import (`COORD_OVERRIDES`) and
replaces coords (and optionally precision) whenever **all three** —
mountpoint name, parsed lat, parsed lon — match an entry exactly. Float
equality holds because the parser stores the same IEEE-754 value as the
JSON loader for any short decimal the operator publishes; the `bad`
field must match the post-`0..360 -> ±180` normalised lon.

Triple-match guard means a stale override silently stops firing the
moment the operator fixes their sourcetable — no quiet rewrite of good
data. Per-source log gains a `, N corrected` suffix when any entries hit.

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
