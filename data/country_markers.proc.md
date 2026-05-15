# country_markers.json — process

Per-file rules for `data/country_markers.json`. Pipeline context:
`../docs/pipeline.md`. Target users: `../docs/target-users.md` — every
`note` is read by a hobbyist on the map, not a developer.

**Refactoring is in scope; consider the entire entry on every edit.** See
`../docs/pipeline.md` §"Edit discipline".

## Role

editorial user-facing extract of `networks.md` - "what the user on a network marker&popup needs to know." 

## markers Field reference

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Matches `networks.md` block id when one exists. Stable — used as React-style key downstream. |
| `name` | yes | What appears in the popup header. UI label, not the legal entity. |
| `region` | yes | What appears after "Covers". Country name + clarifier ("Spain", "China (nationwide)", "Belgium (Flanders)"). Hidden for `tier:weird`. |
| `country` | yes | ISO 3166-1 alpha-2. |
| `lat`,`lon` | yes | marker map placement |
| `tier` | yes | `free`, `paid`, `restricted`, `weird` |
| `access` | for free | `open`, `registration`, `conditions` |
| `vrs` | when true | boolean, "true" if network delivers VRS/NRTK streams
| `yearly_cost` | recommended on paid* | '$X/yr' / 'X €/yr' / '£X/yr', etc. local currency. if no yearly option, fall back to /mo, /h, /min, one time payment. Only one price, additional relevant pricing options in note field. No known pricing = no yearly_cost field
| `yearly_cost_normalized` | required if yearly_cost present | Integer, used as color hint for affordability  |
| `stations_declared` | when known | Integer
| `registration` | when useful | URL: how to sign up. Ideally registration portal, that explains what the service is and how to register; fallback to service portal if nothing better. Avoid form or login pages without any useful explanation |
| `note` | conditional | If helpful to target user |

## How markers render

markers are displayed at lat/lon, symbol depends on tier & vrs. Color for paid depends on yearly_cost_normalized
popup builder in `index.html` auto-fills from the marker's
structured fields:

  **header**: `name`
  **access banner** : "Paid subscription required" etc. — auto from `tier`/`access`
  **yearly_cost**: yearly_cost
  **region** : "Covers <b>{region}</b>." — hidden for `tier:weird`
  **stations_declared**: "(stations_declared) reference stations"
  **note**: note
  **registration**: auto-rendered as a clickable URL
  
Free networks also display their individual mountpoints on the map
  
## Notes

- Target users are defined in /docs/target-users.md - You must not edit a note without having read this file. Instructions to edit a note are instructions to read this file first. Editing a note without having read target-users.md are a major error.
- **Do not restate what other fields cover.** Do not restate what the map already communicates. Don't mention coverage by other networks, the other networks are on the map.
- **No internal-facing language** The note is for target-users *only*.
- **No filler.** "Useful where no free regional caster exists" is fluff. "Professional focus; no explicit hobbyist ban" is fluff. If a sentence doesn't tell the user something they can act on, cut it.
- **Matter-of-fact, ≤2 short sentences, ~250 chars.** Length is a budget; if you need more, cut earlier.
- **No claims about other networks** unless it adds significant practical value to a user choosing what to use, beyond what is obvious from the map. Avoid both explicit claims ("Centipede station in the north is an alternative") and implicit ones ("The only network in Calabria").
- **No US/Western framing.** Users of a network are physically there. They are locals.
- **Preserve correct names** Don't write "national ID" when you can write "Kazakh ИИН/БИН ID"
- **Harassment guard.** No bare email, phone, named individuals, bank/IBAN, postal address.
- No cryptic acronyms unexpanded on first use (FKP, iMAX, SBC portal, SPID) — spell
  out or omit.
- Anchor in events: "installed 2022", "announced Apr 2024", "free since
  Law 1955/2019". Avoid "as of 2026-05-12", bare "currently", or
  "recently"
- UK spelling. "GPS" colloquially; "GNSS" only when hardware/signal
  detail forces it.


## When to add a marker 

The marker represents a pareto point - coverage, affordability / official-ness. It exists because, without it, a target user would miss something they need to know to fit their need. If the marker only confirms absence ("nothing exists"), omit it unless there's a relevant political explanation why nothing exists for now, that implies when that might change.

### Tier picker

| Tier | Add when | Note convention |
|---|---|---|
| `free` | Free network worth showing at country level even when no pins render (VRS-only, or in-pipeline but currently dead). Pipeline-ingested free entries that render as physical pins → no marker. | Open with `"N stations, free."` when no data is ingested yet. Otherwise often skip note entirely; structured fields suffice. |
| `paid` | Substantial paid commercial operator. Affordability is conveyed via `yearly_cost_normalized`. | Why a hobbyist would still care, free trial |
| `restricted` | Substantial network with no hobbyist path at any price (licence gate, sector-only, bundled-hardware). National ID requirement is noteworthy, but doesn't make a network restricted - users should be assumed to often be locals | The specific blocker in plain words, and the next-best free alternative if one exists. |
| `weird` | User-relevant fact that the structured fields cannot carry. The note IS the marker. Past examples (illustrative, not exhaustive): RINEX-only / no real-time NTRIP, announced-but-not-live network, sparse infra (huge baselines), GNSS jamming or spoofing, reseller-only distribution, non-standard NTRIP, named operator with no published endpoint, civil-war disruption, micro-state with no local service. | The note is load-bearing — it has to stand alone. |
