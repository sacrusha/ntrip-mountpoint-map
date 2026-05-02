# country_markers.json — process

Per-file rules for `data/country_markers.json`. Pipeline context:
`.claude/process/pipeline.md`.

## Role

The **user-facing translation.** Subset of networks worth a country-level
marker. Renders directly in map popups for end users. Plain English; no
jargon; no "contact X" instructions.

The file's own self-documenting top-level keys (`_note_field_convention`,
`_yearly_cost_convention`, `_tiers`, `_vrs_flag`) are the **source of truth**
for marker copy and format. **Read those keys before editing.**

## When to add a marker

Triggered by a `networks.md` block change. Two orthogonal axes: a `tier`
describing the network's nature, and an optional `vrs: true` flag indicating
VRS / network-RTK streams.

| Tier | Add when |
|---|---|
| `free` | Network costs nothing. Includes ingested + endpoint-unknown free networks. Note must open `"N stations, free."` when no data is ingested yet. |
| `paid` | Substantial national paid commercial operator over ~$200/yr. |
| `paid-affordable` | Substantial national paid operator at or below ~$200/yr. |
| `restricted` | Substantial network with no hobbyist path at any price. |
| `weird` | Unusual constraint overrides access (non-standard NTRIP, jamming, war-disrupted, sparse infrastructure). |
| _none_ | Investigated, nothing meets the bar. **Default when uncertain.** |

`vrs: true` set if and only if the network delivers VRS / network-RTK
streams. Independent of tier. Absent flag means not-VRS or unknown.

## What disqualifies a marker

- A misplaced marker is worse than no marker.
- Pipeline-ingested single-base free entries that already render as physical
  pins → no marker needed (unless `pins:true` to surface coverage).
- `rejected` networks → no marker. (Unless "exists but unobtainable" + the
  operator is substantial → classify as `restricted` instead.)

## Note conventions (enforced by sweep)

- No `"Paid;"` / `"Free;"` opener — tier already encodes this.
- No yearly_cost figure repeated in note.
- No email, phone, named individual, bank/giro details, or "contact X"
  instructions — link to a website via `registration` instead.
- No audit language ("No explicit restriction found", PDF dates, "as per
  Circular Y").
- No hardcoded dates ("as of 2026-04-30") → "currently".
- No unexplained jargon (FKP, iMAX, SBC portal) → spell out.
- `registration` field: full `https://` URL.
- `status: free` upstream but prose says rejected → fix `networks.md` first,
  then re-check the marker.

## Sweep procedure

1. List existing IDs (`jq '.markers[].id' data/country_markers.json`).
2. For each `networks.md` entry not represented, pick a tier per the table
   above. When in doubt: no marker.
3. Set `vrs: true` if applicable; omit otherwise.
4. Skeleton-first JSON edits, ~10 entries per Edit call (env timeout).
5. After adding, scan all modified notes for the violations above.
