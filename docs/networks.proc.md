# networks.md — process

Per-file rules for `docs/networks.md`. Pipeline context:
`pipeline.md` (same dir).

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
| `free` | Free NTRIP/RTK service. |
| `paid` / `paid-affordable` | Civilian-accessible for a fee. Requires `**yearly_cost**:`. |
| `restricted` | Exists but unobtainable for the target user at any price. |
| `weird` | Use when a substantial operator carries user-relevant facts the cost / access fields don't convey on their own — the freeform note is the load-bearing part of the block. The status doesn't enumerate cases; if a hobbyist landing on the country would be helped by knowing this exists or doesn't work the way the other fields suggest, it's `weird`. Past examples (sparse infra, RINEX-only, announced-not-live, reseller-only, non-standard NTRIP, GNSS-spoofed airspace) illustrate, they don't bound. |
| `candidate` | Free, endpoint known, ready to ingest, not yet in fetch. |
| `rejected` | Investigated and **of no value to a target user** — defence-only, abandoned, niche scientific archive, duplicate of another block. The default for an entry that was looked at and produced nothing worth surfacing. If the prose is naming a real RINEX archive, a planned NTRIP service, or a substantial named operator a user might still try to reach, the entry isn't rejected — re-status it. |

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

A block change is a **prompt to revisit** the marker
(`../data/country_markers.proc.md`), not a rule that produces one —
markers are an editorial extract, not a derived view. `candidate` →
ingestion is mechanical (`../scripts/fetch_stations.proc.md`).
