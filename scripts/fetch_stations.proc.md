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

## Post-process / DGPS filter

`parse_sourcetable` drops two non-RTK stream classes that some Trimble
Pivot casters publish alongside real-time RTK streams:

- **`format == "RAW"`** — raw observation broadcast for RINEX-style
  post-processing. No standard rover consumes RAW in real time.
  Trimble Pivot casters publish `*_RAW` mountpoints next to every
  `*_RTCM3.x` variant (CROPOS does this for all 35 physical stations).
- **`format == "RTCM 2.x"` AND `format-details` contains `PBS`** —
  Trimble Pivot's DGPS-targeted variant. Real RTCM 2.x RTK uses
  messages 18/19/22/23/24/59; the PBS (Position Broadcast Service)
  auxiliary message is RTCM 3 territory and signals the operator
  intends this stream for DGPS rovers, not RTK. CROPOS `*_DPS_23`
  matches. PBS *alongside* `RTCM 3.x` is the normal Trimble Pivot
  RTK config (nps_cors, kycors, sapos_*) — those are kept.

Counted as `dropped_postproc` in per-source log: `, N post-process`.

## Per-station `vrsRequired`

Stations parsed from an endpoint with `"vrs_required": true` in
`../data/rtk_map.json` carry `"vrsRequired": true` in their per-station
record. `index.html` renders them with a smaller pin and a popup that
suppresses the usual Server/Port/Mountpoint copy block (the mountpoint
name is not a valid connect string — the operator only allows VRS),
replacing it with the network's VRS endpoint URL and a "feeds into
VRS" line. Omitted when false to keep diffs small.

The flag rides on the per-endpoint config so a future case where one
network mixes connectable stations on one endpoint with VRS-required
stations on another endpoint Just Works without further plumbing.
Per-station overrides are not implemented yet but the per-station
shape leaves room.

`station_fingerprint` includes `vrsRequired` so toggling the flag on
an existing endpoint triggers a stations.json rewrite (without it the
"unchanged data" short-circuit would keep the old un-flagged record).

## After-edit checks

```sh
# Module-load smoke test:
python -c "from scripts.fetch_stations import NETWORKS, SOURCES; print(len(NETWORKS), len(SOURCES))"

# Local dry-fetch when network is available (fails open in sandbox):
python scripts/fetch_stations.py
# Expected stdout per endpoint: "[sid] fetched N stations (dropped X DGNSS, Y invalid[, Z net-sol])"
```
