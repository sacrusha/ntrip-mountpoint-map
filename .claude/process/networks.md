# networks.md — process

Per-file rules for `docs/networks.md`. Pipeline context:
`.claude/process/pipeline.md`.

## Role

The **refined operator catalogue, for us.** Per-network blocks (status,
host:port, yearly_cost, …). Developer-facing; acronyms and audit phrasing
fine.

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

| Status | Meaning |
|---|---|
| `free` | Free NTRIP/RTK service. Includes ingested networks + free-but-endpoint-missing / registration-gated. RINEX-only with no NTRIP → `rejected`, not free. |
| `paid` / `paid-affordable` | Civilian-accessible for a fee. Requires `**yearly_cost**:`. A network with a published private-user tariff is always one of these, never `rejected`. |
| `restricted` | Exists but unobtainable for the target user at any price. |
| `weird` | Unusual constraint overrides access (non-standard NTRIP, jamming, sparse infrastructure, war-disrupted). |
| `candidate` | Free, endpoint known, ready to ingest, not yet wired in fetch. |
| `rejected` | Investigated and ruled out. Keep RINEX-only government networks as PPK alternative — block + survey entry stay. |

## yearly_cost format

Single short line, primary annual tier: `€120/yr (~$130/yr)`. If no annual
plan, lead with the most practical sustained-use plan (`€20/mo`). Multi-tier
tariff tables go in entry prose, not in `yearly_cost`. Field valid only on
`paid` / `paid-affordable`.

## type field

- Leica GNSS Spider / SpiderWeb / SBC → `physical-coord-vrs`
- Trimble VRS Now → `physical-coord-vrs`
- Geo++ GNSMART → `physical-coord-vrs`
- Bare NTRIP caster, no VRS mention → `single-base`
- VRS-only mounts, no physical coordinates → `vrs-only`

## Other

- `registration` field: full `https://` URL, never a bare domain.
- No bare email addresses.
- $200/yr is internal classification only — never written in user-visible
  prose. Use "expensive" / "modest annual fee" / quote the price.

## Downstream

Any block change triggers the marker sweep — see
`.claude/process/country-markers.md`. Wiring a `candidate` into ingestion —
see `.claude/process/fetch-stations.md`.
