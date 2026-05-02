# fetch_stations.py — process

Per-file rules for `scripts/fetch_stations.py`. Pipeline context:
`.claude/process/pipeline.md`.

## Role

Ingests configured NTRIP casters into `data/stations.json`. Consumed by
GitHub Actions cron (4×/day) and visitors via the rendered map.

The `SOURCES` list is the operational mirror of the `free` / `candidate`
slice of `docs/networks.md`. Treat it as a derived artefact: every entry
should correspond to a `networks.md` block.

## When to add a SOURCES entry

A `networks.md` block flips from `candidate` → ingest-ready. Required:

- `host:port` resolves and serves a sourcetable.
- Block is `status: free` (ingested networks should not be `paid` /
  `restricted` — those surface to visitors via markers, not pins).
- The caster's STR rows actually carry physical mountpoints (not VRS-only,
  unless you specifically want stream-type metadata).

## When to remove a SOURCES entry

- `networks.md` block flips to `rejected`.
- Caster has been offline long enough that retained sourcetables are stale.

## Filter flags

Both `nmea_filter` and `solution_filter` default `True`. Only override with
a comment explaining the caster-specific rationale.

- `nmea_filter=False` — caster mislabels physical stations as `nmea=1`.
  Distinct real coordinates per row give it away (e.g. SNIP casters).
- `solution_filter=False` — caster mislabels physical stations as
  `solution=1`. Rare.
- **Never set `solution_filter=False` for `rtk2go`** — it is the only guard
  against the NEAR-xxx VRS streams.

## type field

Mirrors the typology in `.claude/process/networks.md`:

- `physical-coord-vrs` — caster carries physical mounts and exposes VRS
  overlays.
- `single-base` — single physical caster, no VRS.
- `vrs-only` — VRS-only output, 0 physical mounts (correct behaviour;
  produces 0 physical pins; included only when stream-type metadata is
  wanted).

## Don't do this

- Don't add a SOURCES entry for a `paid` or `restricted` network — visitors
  see those via markers, not pins.
- Don't add a SOURCES entry for a network missing from `networks.md` —
  settle the upstream record first.
- Don't silently change a filter flag. Add a `parse_sourcetable` rationale
  comment.
