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
| `weird` | Anything interesting to a target user that doesn't fit the other tiers: non-standard NTRIP, jamming, war-disrupted, sparse infrastructure, free RINEX-only with no real-time NTRIP, network announced/under construction but not yet operational, government CORS distributed only via licensed commercial resellers, micro-state with no local service. The note carries the explanation. |
| _none_ | Investigated, nothing of interest to a target user. **Default when uncertain.** |

`vrs: true` set if and only if the network delivers VRS / network-RTK
streams. Independent of tier.

## What disqualifies a marker

- A misplaced marker is worse than no marker.
- Pipeline-ingested single-base free entries already rendered as physical pins → no marker.
- `rejected` networks with no signal value to a target user (defence-only, abandoned, niche scientific) → no marker. RINEX-only PPK alternatives, announced-but-not-operational networks, and similar "rejected from pipeline but interesting to a user" cases get a `weird` marker instead — see the table above.

## Note anti-patterns (beyond JSON conventions)

- No email, phone, named individual, bank/giro details, or "contact X"
  instructions — link via `registration` instead. **Harassment guard.**
- No audit language ("No explicit restriction found", PDF dates).
- Anchor time claims in historical events ("installed 2022", "announced 2025"). Avoid "as of <date>" snapshots and bare "currently" — both rot silently.
- No unexplained jargon (FKP, iMAX, SBC portal) → spell out.
- `status: free` upstream but prose says rejected → fix `networks.md` first.
