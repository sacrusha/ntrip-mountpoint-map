# country_markers.json — process

Per-file rules for `data/country_markers.json`. Pipeline context:
`../docs/pipeline.md`. Target users: `../docs/target-users.md` — every
`note` is read by a hobbyist on the map, not a developer.

**Refactoring is in scope; consider the entire entry on every edit.** See
`../docs/pipeline.md` §"Edit discipline".

## Role

User-facing translation of `networks.md` — an editorial extract, not a
derived view. `networks.md` answers "what we know"; this file answers
"what the user on a country popup needs to know." A networks.md edit
prompts a marker review; it does not mandate one.

The four top-level keys (`_note_field_convention`, `_yearly_cost_convention`,
`_tiers`, `_vrs_flag`) are the spec. They render straight into popups
— read them first, edit them when conventions evolve, never inline a copy
into prose.

## How a marker renders (mental model for writing notes)

The popup builder in `index.html` auto-fills these lines from the marker's
structured fields:

  1. **header**: `name`
  2. **access banner** (paid/affordable/restricted only): "Paid subscription required" etc. — auto from `tier`/`access`
  3. **yearly_cost** line (if field present)
  4. **region** line: "Covers <b>{region}</b>." — hidden for `tier:weird`
  5. **note** — your free-form prose
  6. **registration** link — auto-rendered as a clickable URL

So the `note` field's job is to add what the structured fields cannot.
Restating price, region, access label, or the registration URL inside
`note` produces a duplicated popup.

`tier:weird` is special: no access banner, no region line. The note
carries the whole explanation — that is the tier's defining trait.

Tier interaction with the pipeline:

- `tier:free` — when the `id` matches a `SOURCES` entry in
  `fetch_stations.py` AND that source is live with ingested stations,
  the renderer hides the country marker glyph and uses the marker's
  fields (`lat`, `lon`, `region`, `stations_declared`, `note`, `vrs`)
  only to enrich the in-pipeline popup. If the source goes stale/dead
  the marker reappears as a grey ring at `lat`/`lon`. If the `id` is
  not in `SOURCES` the marker renders as a grey synthetic ring.
- `tier:paid` / `paid-affordable` / `restricted` / `weird` — always
  render as a $/?/✕ glyph at `lat`/`lon`, regardless of any pipeline
  data sharing the `id`. The marker is the user's only view of the
  network.

Pick `lat`/`lon` with the marker-visible cases in mind (national
centroid, or the operational centre when it tells a clearer story —
Bogotá control centre, Ulaanbaatar). Avoid the caster IP's geo-IP.

## When to add a marker — the only test

The marker exists because, without it, a hobbyist landing on this
country would miss something they need to know to fit their budget,
hardware, or paperwork tolerance. If the marker only confirms absence
("nothing exists"), omit it — empty space beats a dead tag.

### Tier picker

| Tier | Add when | Note convention |
|---|---|---|
| `free` | Free network worth showing at country level even when no pins render (VRS-only, or in-pipeline but currently dead). Pipeline-ingested free entries that render as physical pins → no marker. | Open with `"N stations, free."` when no data is ingested yet. Otherwise often skip note entirely; structured fields suffice. |
| `paid-affordable` | Substantial national paid operator at or below ~$200/yr, hobbyist-eligible (no licence/residency gate). | What makes the cost reachable — cheapest viable tier, monthly fallback, free trial. |
| `paid` | Substantial national paid commercial operator over ~$200/yr. | Why a hobbyist would still care — only option in the country, free trial, volunteer fallback nearby. |
| `restricted` | Substantial network with no hobbyist path at any price (licence gate, sector-only, bundled-hardware). National ID requirement is noteworthy, but doesn't make a network restricted - users should be assumed to often be locals | The specific blocker in plain words, and the next-best free alternative if one exists. |
| `weird` | User-relevant fact that the structured fields cannot carry. The note IS the marker. Past examples (illustrative, not exhaustive): RINEX-only / no real-time NTRIP, announced-but-not-live network, sparse infra (huge baselines), GNSS jamming or spoofing, reseller-only distribution, non-standard NTRIP, named operator with no published endpoint, civil-war disruption, micro-state with no local service. | The note is load-bearing — it has to stand alone. |

`vrs: true` whenever the network delivers any NRTK product, not just
mountpoints literally named "VRS". Orthogonal to tier — free+VRS,
paid+VRS, restricted+VRS are all valid.

## Disqualifiers

- A misplaced marker is worse than no marker — drop it on doubt.
- "No service exists" alone is not enough — omit the marker.

## Note anti-patterns

Restate-from-structured-fields:
- Price in `note` while `yearly_cost` is set.
- Access label ("Paid subscription required") — auto-rendered.
- Region restatement — auto-rendered for non-`weird` tiers.
- Inline registration URL — `registration` renders separately.
- "Contact X at email/phone" — link via `registration` URL instead.

Harassment guard:
- No bare email, phone, named individuals, bank/IBAN, postal address.

Time rot (markers are rarely revisited):
- Anchor in events: "installed 2022", "announced Apr 2024", "free since
  Law 1955/2019". Avoid "as of 2026-05-12", bare "currently", or
  "recently" — they age silently.

Audience drift:
- Developer/internal phrasing ("No explicit restriction found", "PDF
  dated 2024-04-22"). Hobbyist tone: matter-of-fact, ≤2 short sentences,
  ~250 chars.
- Acronyms unexpanded on first use (FKP, iMAX, SBC portal, SPID) — spell
  out or omit.
- UK spelling. "GPS" colloquially; "GNSS" only when hardware/signal
  detail forces it.

## Field reference

| Field | Required | Notes |
|---|---|---|
| `id` | yes | Matches `networks.md` block id when one exists. Stable — used as React-style key downstream. |
| `name` | yes | What appears in the popup header. UI label, not the legal entity. |
| `region` | yes | What appears after "Covers". Country name + clarifier ("Spain", "China (nationwide)", "Belgium (Flanders)"). Hidden for `tier:weird`. |
| `country` | yes | ISO 3166-1 alpha-2. |
| `lat`,`lon` | yes | See "Tier interaction" — drives marker placement and grey-ring fallback. |
| `tier` | yes | One of: `free`, `paid-affordable`, `paid`, `restricted`, `weird`. Drives glyph + colour. |
| `access` | for paid/restricted | Echoes `tier` in current usage; renderer picks the access-banner string from this field. |
| `vrs` | when true | Boolean. Network delivers VRS/NRTK streams. Orthogonal to tier. Drives ring vs pin visuals when the entry is also in-pipeline. |
| `yearly_cost` | recommended on paid* | Single short line — see `_yearly_cost_convention`. If pricing is unpublished, OMIT the field; do not write "not listed" there. |
| `yearly_cost_normalized` | recommended on paid, paid-affordable | Integer, used as color hint for affordability  |
| `stations_declared` | when known | Integer count from `networks.md`; appears in the auto-built copy when no pipeline pins exist. |
| `registration` | when useful | URL — registration portal, ideally; fallback service portal. Auto-rendered as a link. Skip if no useful destination exists. |
| `note` | conditional | Required for `weird`; common on paid/restricted; usually omitted on free with structured fields. |

## Checklist before committing

1. Does `tier` still match `networks.md` `status`? (`free`→`free`, `paid`→`paid`/`paid-affordable`, `restricted`/`weird` all map directly; `candidate` → no marker yet.)
2. Does `note` restate any auto-rendered field? Cut it.
3. Time-rot phrases? Anchor in an event.
4. Email/phone/person/IBAN? Move to `registration` URL.
5. Does the country also already have physical pins rendering from `stations.json`? If yes and `tier:free`, the marker is enrichment only — keep `note` minimal or empty.
6. `lat`/`lon` plausible? National centroid or operational centre, not the caster IP's geo-IP.
7. `stations_declared` consistent with the `networks.md` `stations:` field?
