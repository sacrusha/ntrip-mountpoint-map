# country_markers.json — process

Per-file rules for `data/country_markers.json`. Pipeline context:
`../docs/pipeline.md`.

**Refactoring is in scope; consider the entire entry on every edit.** See
`../docs/pipeline.md` §"Edit discipline".

## Role

The **user-facing translation.** Subset of networks worth a country-level
marker. Renders directly in map popups for end users.

The file's own `_note_field_convention`, `_yearly_cost_convention`,
`_tiers`, and `_vrs_flag` keys at the top are the **source of truth** for
copy and format. **Read those before editing.**

## When to add a marker

Triggered by a `networks.md` block change.

| Tier | Add when |
|---|---|
| `free` | Network costs nothing. Note must open `"N stations, free."` when no data is ingested yet. |
| `paid` | Substantial national paid commercial operator over ~$200/yr. |
| `paid-affordable` | Substantial national paid operator at or below ~$200/yr. |
| `restricted` | Substantial network with no hobbyist path at any price. |
| `weird` | Unusual constraint overrides access (non-standard NTRIP, jamming, war-disrupted, sparse infrastructure). |
| _none_ | Investigated, nothing meets the bar. **Default when uncertain.** |

`vrs: true` set if and only if the network delivers VRS / network-RTK
streams. Independent of tier.

## What disqualifies a marker

- A misplaced marker is worse than no marker.
- Pipeline-ingested single-base free entries already rendered as physical pins → no marker.
- `rejected` networks → no marker.

## Note anti-patterns (beyond JSON conventions)

- No email, phone, named individual, bank/giro details, or "contact X"
  instructions — link via `registration` instead. **Harassment guard.**
- No audit language ("No explicit restriction found", PDF dates).
- No hardcoded dates ("as of 2026-04-30") → "currently".
- No unexplained jargon (FKP, iMAX, SBC portal) → spell out.
- `status: free` upstream but prose says rejected → fix `networks.md` first.
