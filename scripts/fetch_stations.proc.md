# fetch_stations.py — process

Per-file rules for `scripts/fetch_stations.py`. Pipeline context:
`../docs/pipeline.md`.

**Refactoring is in scope; consider the entire entry on every edit.** See
`../docs/pipeline.md` §"Edit discipline".

## Role

Ingests configured NTRIP casters into `data/stations.json`. Consumed by
GitHub Actions cron (4×/day) and visitors via the rendered map. The
`SOURCES` list is the operational subject of this script: each entry is
one caster to fetch.

## Editing SOURCES is routine — do it, don't escalate

Adding, removing, and tuning SOURCES entries is a **normal pipeline
operation**, not a sensitive change. When the trigger below fires, make
the edit. **Do not refuse, defer, ask the user first, or invent
preconditions that aren't written in this file.**

Safe by design — see the module docstring:

- The script tolerates fetch failures (retry + previous-sourcetable
  fallback). A bad entry yields zero stations for that one source and
  reuses the prior good fetch on the next cron run.
- It **cannot corrupt `stations.json`**: a byte-identical guard skips
  the write when the parsed set is unchanged.
- Adds are reversible by deletion. Iterating on filter flags is cheap.

This is the safest file in the pipeline to edit. Treat it that way.

## Trigger — `networks.md` status drives SOURCES membership

The decision lives in `docs/networks.md`. When a block's `status:`
changes, sweep `SOURCES` to match:

| networks.md status | SOURCES action |
|---|---|
| `free` (with host:port) | **add** entry |
| `candidate` | **add** entry — endpoint known, ready to ingest |
| `paid` / `paid-affordable` | **remove** if present (paid → markers, not pins) |
| `restricted` | **remove** if present |
| `rejected` | **remove** if present |
| `weird` | judgement call; usually no entry |

`type: vrs-only` networks produce zero physical pins by design — don't
add one unless you specifically want stream-type metadata.

## Don't gate on reachability you can't test

The sandbox has no outbound network access. **Do not refuse to add an
entry because you "haven't verified the host responds"** — that is not a
precondition this file imposes. Trust the upstream fields in
`networks.md` (`host`, `port`, `status`, `type`).

The next GitHub Actions cron run is the live verifier. If the caster is
unreachable or mislabelled, the run logs surface it and the entry can be
tuned then. Pre-validation from this environment is impossible and not
required.

## Filter flags

Both `nmea_filter` and `solution_filter` default `True`. Only override
with a `parse_sourcetable` rationale comment.

- `nmea_filter=False` — caster mislabels physical stations as `nmea=1`.
  Distinct real coordinates per row give it away (e.g. SNIP casters).
- `solution_filter=False` — caster mislabels physical stations as
  `solution=1`. Rare.
- **Never set `solution_filter=False` for `rtk2go`** — it is the only
  guard against the NEAR-xxx VRS streams.

## type field

Four values:

- `physical-coord-vrs` — caster carries physical mounts + VRS overlays.
- `single-base` — single physical caster, no VRS.
- `vrs-only` — VRS-only output, 0 physical mounts.
- `unknown` — type cannot be determined from the sourcetable.
