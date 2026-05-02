# networks.md — process

Per-file rules for `docs/networks.md`. Pipeline context:
`.claude/process/pipeline.md`.

**Refactoring is in scope; consider the entire entry on every edit.** See
`pipeline.md` §"Edit discipline".

## Role

The **refined operator catalogue, for us.** Per-network blocks (status,
host:port, yearly_cost, …). Developer-facing.

## File facts

- ~3000 lines. Grep + targeted Read.
- One block per network with `## id`, fields, free-form notes.
- Optional `**date_added**:` per block when revised independently.

## Curation threshold

A block exists only for **substantial** operators (nationwide, regional
cadastre, recognised commercial operator). Small surveying companies →
country prose only. **Empty space here is a feature.**

## Status discipline

The `status:` field drives the marker sweep — be strict.

**Section placement follows status.** networks.md is organised into
status-named sections (`## Free —`, `## Paid — affordable`,
`## Paid — over cutoff …`, `## Rejected …`, …). On any `status:` change,
move the block to the matching section — don't update in place.
Mis-sectioning is a recurring failure mode.

| Status | Meaning |
|---|---|
| `free` | Free NTRIP/RTK service. RINEX-only no NTRIP → `rejected`. |
| `paid` / `paid-affordable` | Civilian-accessible for a fee. Requires `**yearly_cost**:`. |
| `restricted` | Exists but unobtainable for the target user at any price. |
| `weird` | Non-standard NTRIP, jamming, sparse infrastructure, war-disrupted. |
| `candidate` | Free, endpoint known, ready to ingest, not yet in fetch. |
| `rejected` | Investigated, ruled out. Keep RINEX-only government networks as PPK reference. |

## yearly_cost format

Single short line, primary annual tier: `€120/yr (~$130/yr)`. If no annual
plan, lead with the most practical sustained-use plan (`€20/mo`). Multi-tier
tables go in entry prose. Field valid only on `paid` / `paid-affordable`.

## type field

Four values: `physical-coord-vrs` (caster has both physical mounts and VRS
overlays — Leica GNSS Spider / Trimble VRS Now / Geo++ GNSMART backends),
`single-base` (bare NTRIP, no VRS), `vrs-only` (VRS-only, no physical
mounts), `unknown`.

## Other

- No bare email addresses. **Harassment guard.**

## Downstream

Block change → marker sweep (`.claude/process/country-markers.md`). Wiring
a `candidate` into ingestion (`.claude/process/fetch-stations.md`).
