# fetch_stations.py — process

Per-file rules for `scripts/fetch_stations.py`. Pipeline context:
`../docs/pipeline.md`.

**Refactoring is in scope; consider the entire entry on every edit.** See
`../docs/pipeline.md` §"Edit discipline".

## Role

Ingests configured NTRIP casters into `data/stations.json`. Consumed by
GitHub Actions cron (4×/day) and visitors via the rendered map. The
`SOURCES` list is the operational subject of this script: each entry is one
caster to fetch.

## When to add a SOURCES entry

A caster is ingest-ready when:

- `host:port` resolves and serves a sourcetable.
- The caster's STR rows actually carry physical mountpoints (not VRS-only,
  unless you specifically want stream-type metadata).
- The network is free for visitors (paid / restricted networks should not
  appear in pins — those surface via markers).

## When to remove a SOURCES entry

- Caster has been offline long enough that retained sourcetables are stale.
- Network is no longer a free-for-visitor service.

## Filter flags

Both `nmea_filter` and `solution_filter` default `True`. Only override with
a `parse_sourcetable` rationale comment.

- `nmea_filter=False` — caster mislabels physical stations as `nmea=1`.
  Distinct real coordinates per row give it away (e.g. SNIP casters).
- `solution_filter=False` — caster mislabels physical stations as
  `solution=1`. Rare.
- **Never set `solution_filter=False` for `rtk2go`** — it is the only guard
  against the NEAR-xxx VRS streams.

## type field

Four values:

- `physical-coord-vrs` — caster carries physical mounts + VRS overlays.
- `single-base` — single physical caster, no VRS.
- `vrs-only` — VRS-only output, 0 physical mounts.
- `unknown` — type cannot be determined from the sourcetable.
