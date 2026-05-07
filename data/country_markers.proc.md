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

Markers are an **editorial extract** of `networks.md`, not a derived view.
`networks.md` is "what we know"; `country_markers.json` is "what we want
the user to know." A `networks.md` edit is the prompt to revisit the
marker, not a rule that mandates one.

| Tier | Add when |
|---|---|
| `free` | Network costs nothing. Note must open `"N stations, free."` when no data is ingested yet. |
| `paid` | Substantial national paid commercial operator over ~$200/yr. |
| `paid-affordable` | Substantial national paid operator at or below ~$200/yr. |
| `restricted` | Substantial network with no hobbyist path at any price. |
| `weird` | Use when there is user-relevant info the structural fields (tier, yearly_cost, access, registration, stations_declared) cannot carry. The note is the marker's whole point — it states what the shape of the other fields cannot. Past examples (sparse infra, GNSS spoofing in the airspace, free RINEX with no NTRIP, announced-but-not-live networks, reseller-only distribution, non-standard NTRIP, named operator with no published endpoint) illustrate the principle but don't enumerate it. If the situation doesn't match a past example but a hobbyist landing here would still be helped by the explanation, that's a weird marker. |
| _none_ | Investigated, nothing of interest to a target user. **Default when uncertain.** |

`vrs: true` set if and only if the network delivers VRS / network-RTK
streams. Independent of tier.

## What disqualifies a marker

- A misplaced marker is worse than no marker.
- Pipeline-ingested single-base free entries already rendered as physical pins → no marker.
- **Nothing-here guard.** If the only thing to say is "no service exists"
  AND a hobbyist has an accessible alternative within practical reach
  (cross-border network 5–50 km away, neighbouring marker already
  visible), omit the marker. Empty space beats a tag that just confirms
  absence — Liechtenstein with swipos 5 km across the Swiss border is
  the canonical case, and the marker only earns its place by naming the
  alternative. Small island states with no fallback are different: their
  marker carries that fact.
- `status: free` upstream but prose says rejected → fix `networks.md` first.

## Note anti-patterns (beyond JSON conventions)

- No email, phone, named individual, bank/giro details, or "contact X"
  instructions — link via `registration` instead. **Harassment guard.**
- No audit language ("No explicit restriction found", PDF dates).
- Anchor time claims in historical events ("installed 2022", "announced 2025"). Avoid "as of <date>" snapshots and bare "currently" — both rot silently.
- No unexplained jargon (FKP, iMAX, SBC portal) → spell out.
