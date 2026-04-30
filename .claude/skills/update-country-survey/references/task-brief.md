# Per-country task: research and update RTK survey entry

## Goal
Apply the ideal-entry spec to a specific country (or small batch of related countries) in the ntrip-mountpoint-map repo.

## Files to read (in order)
1. `.claude/skills/update-country-survey/references/ideal-entry-spec.md` — tier definitions, templates, `date_added` field rule. Read in full (small).
2. `docs/country-survey.md` — **DO NOT read in full** (>40k tokens).
   Instead: `grep -n "^### " docs/country-survey.md` to find headings; for each assigned country, `grep -n "^### CC — " docs/country-survey.md` to find its line if it exists, then `Read` only that section (~30 lines around the match) and a few neighbouring entries to establish placement context. If your assigned country is missing, use `grep -n "^### " | grep -B1 -A1 <neighbouring CC>` to find the right insertion point alphabetically/regionally.
3. `docs/networks.md` — **DO NOT read in full**. Grep for related network IDs (`grep -n "^## <id>" docs/networks.md`) and read targeted blocks only. To find the end of the file for appends, use `wc -l docs/networks.md` and Read the last 30 lines.

## Search rules
1. Use the **dominant administrative language** of the country/region for primary searches. If unclear, use the top 2 official languages. If you can't read either, fall back to the next-best regional business language you can handle (English for most former British colonies; French for francophone Africa; Spanish for Latin America; Portuguese for Lusophone Africa & Brazil; Arabic for MENA; Russian for CIS; etc.). State which language(s) you used in your final report.
2. **Use WebSearch only.** WebFetch is broken in this environment — do not call it.
3. For countries with regional networks (Canada, Brazil, Australia, India, China, Russia, US states, German Länder, Italian regions, Spanish autonomous communities, Argentine provinces, etc.), do **per-region searches** in the region's language (e.g. Quebec searches in French; Catalonia in Catalan/Spanish).

## Authoritative local data (use these, don't guess)
- `data/stations.json` — every parsed mountpoint with `country` field. To count stations in a country: `grep -o "\"country\": \"<CC>\"" data/stations.json | wc -l`. Per source, filter the relevant `"<source_id>"` block first.
- `data/rtk2go.sourcetable` and `data/centipede.sourcetable` — raw STR records. To find country mountpoints, `grep -i "<country fragment>" data/rtk2go.sourcetable` (NET field often contains country name) or filter by approximate latitude/longitude.
- `data/earthscope.sourcetable` — NOTA / COCONet stations across the Americas; for Caribbean and US territories, this is often the authoritative source for "what's already covered".
- Country code mapping: `data/stations.json` uses ISO 3166-1 alpha-3 (`USA`, `BRA`, `IND`, `RWA`, `BTN`, etc.). Convert the alpha-2 country code in your assignment to alpha-3 before grepping.

When reporting station counts for rtk2go / Centipede / EarthScope, **use these files, not web searches** — the local files are the authoritative current count.

## What to find
For each network you discover (free OR paid):
- **Name** of the network (Latin script + native script if relevant).
- **Operator** (government agency, university, commercial company).
- **Registration URL** or process description URL.
- **Host:port** of the NTRIP caster, if discoverable.
- **Access model**: free / free-with-registration / paid-affordable (<$200/yr) / paid (≥$200/yr) / restricted.
- **Pricing**: local currency + USD or EUR equivalent at current rates (`~$X/yr`).
- **Stations**: approximate count and physical-vs-VRS mix.
- **Why** context: only when the country meets Tier A criteria per the spec (legal barrier, sanctions, civil war, complex regional patchwork). Do NOT add a "why" paragraph to Tier B/C entries.

## Audience and writing register

`docs/country-survey.md` is read by hobbyists following GitHub links from the README/map — same audience as `guide.html` and `data/help_topics.json`. Write in their register:

- **Expand acronyms on first use** in each entry. "CORS" is jargon; prefer "permanent GPS reference station" or "fixed reference network". Acronyms are fine in `docs/networks.md` (developer-facing) but not in country-survey prose.
- **Don't leak internal classifications.** `$200/yr cutoff` is the orchestrator's term for choosing tier. In user-visible Gap sentences, write the reality: "modest annual fee", "expensive — over USD 200/yr", or quote the price directly.
- **Don't write audit-document phrasing** in user-visible places. "No English pricing page", "±2 cm horizontal accuracy", "subordinate body of Defence Ministry" are wrong audience. Tell the user what to do or what to expect.
- **Negative findings**: when there is no service, say so plainly and stop. Don't pad with pseudo-detail ("a 6-station national backbone was planned but…") — that reads as if something exists.

## What to write

### `docs/country-survey.md`
- Find the right alphabetical/regional position. The file is grouped by region (Western Europe, Mediterranean, Nordics, etc.). If a regional section is unclear, place near similar-region entries.
- Use the appropriate Tier A / B / C template from `.claude/skills/update-country-survey/references/ideal-entry-spec.md`.
- Add `**date_added**: <today's date in YYYY-MM-DD>` on the line immediately under the `### CC — Country Name` heading. The orchestrator will pass today's date to you in the assignment prompt — use that exact value.
- If updating an existing entry, bump `date_added` to today's date only if you made substantive changes (more than typo/link fixes).

### `docs/networks.md`
For each network you find that is **operational and accessible to a hobbyist** (free, free-with-registration, paid-affordable, or substantial paid), add a `## id` block following the existing style (status, country, type, host:port, access, registration, yearly_cost, stations, notes). Optional: add `**date_added**:` per network if precision is useful.

**`yearly_cost` format:** one short line, primary annual tier only — `€120/yr (~$130/yr)`. If no annual plan exists, lead with the most practical sustained-use plan (`€20/mo`). Multi-tier tariff tables and per-day/per-hour variants go in the entry prose, not in `yearly_cost`. `yearly_cost` is only valid for `paid` and `paid-affordable` entries — omit it for `free`, `restricted`, `weird`, and `rejected`.

**`type` field — backend software implies stream type:** Leica GNSS Spider / SpiderWeb / SBC deployments → `physical-coord-vrs`; Trimble VRS Now → `physical-coord-vrs`; Geo++ GNSMART → `physical-coord-vrs`; bare Ntrip Caster with no VRS mention → `single-base` unless confirmed otherwise.

**Before writing a new block**, grep for any `**missing**:` or `**investigate**:` tags on this country in the existing entry (`grep -n "missing\|investigate" docs/networks.md | grep -A2 "^## .*<CC>"`) and resolve them as part of this edit — either with a definitive finding or a closing sentence explaining the gap. Replace any "Deferred pending …" language with a concrete statement.

**Same-institution check:** before creating a new block, verify the operator isn't a reorganised form of an existing entry. Common pattern: a national IGN absorbed into a cadastre or land-registry ministry; the old IGN brand persists on a secondary website but maps to the same CORS network.

**Do NOT create a `networks.md` block for**:
- "Investigated, infrastructure exists but no operational public service" — record the finding inline in the country-survey prose only.
- Government-internal / defence-controlled / closed-cadastral-only networks the public can't reach.
- Post-processing / RINEX-archive-only services (these are not RTK).
- A small private surveying company with stations in a few cities (regional, not national-scale).

**`status` field discipline** — these values mean specific things and drive
the marker sweep downstream. Status describes the **network's nature**, not
whether it's wired into the pipeline; ingestion is derivable from
`data/stations.json`.

- `status: free` — a free NTRIP/RTK service. Use both for networks already
  wired into `scripts/fetch_stations.py` and for free networks where the
  only gap is that the host:port isn't yet known or is registration-gated.
  **RINEX-download-only with no NTRIP/RTK service → `rejected`, not `free`.**
  RINEX archive ≠ real-time corrections; the two are not interchangeable.
- `status: paid` / `paid-affordable` — accessible to civilians for a fee.
  Requires `**yearly_cost**:` field. A network with a published hobbyist
  tariff is always `paid` or `paid-affordable` (based on amount), never
  `rejected`. `restricted` means no hobbyist path at any price.
- `status: restricted` — exists but unobtainable for the target user
  (licensed-surveyors only, government-only, defence-only).
- `status: weird` — something unusual overrides the access question:
  non-standard NTRIP, active jamming/spoofing, infrastructure too sparse to
  work, war-disrupted with unknown status. The entry's notes carry the
  warning.
- `status: candidate` — meta-status: free, endpoint known, ready to ingest
  but not yet wired in.
- `status: rejected` — meta-status: investigated and ruled out (one-line
  rationale required).

If you're not sure between `free` and `rejected`, default to `rejected` with
a rationale. Misclassifying as `free` produces a misleading "free option
here" marker on the map.

### Do NOT touch
- `data/country_markers.json` — handled in a final sweep.
- `data/stations.json` — pipeline-managed.
- `index.html` — frontend handles markers automatically once JSON is updated.
- `data/help_topics.json` or `guide.html` — out of scope.

## Editing technique
- Use Edit (not Write) for both files. country-survey.md is 1081 lines; networks.md is ~2000 lines.
- For a brand-new country heading, find the right neighbour heading and Edit-insert above/below it.
- For a new network entry in networks.md, append at the end of the relevant region section, or near the country's other networks.

## Reporting
After the edits, report under 100 words:
- Which countries processed.
- What was found per country (1 line each: network name, access, pricing if any).
- Search language(s) used.
- Any unresolved ambiguity (e.g. "registration URL not discoverable; documented from secondary source").

## Hard rules
- Do not invent host:port or pricing. If not discoverable, write "host:port not publicly listed" or "pricing not on public website".
- Do not add bare email addresses (per CLAUDE.md rule). Link to a website that describes the email-based signup process.
- UK spelling in prose (centimetre, behaviour). "GPS" colloquially / "GNSS" structurally.
- If the country has no plausible RTK presence (e.g. a tiny island with population <50k and no government CORS programme), write a 2-line Tier C stub confirming nothing was found, rather than skip the entry.
- `registration` field must be a full `https://` URL, never a bare domain.
- **Note field rules** (the `note` renders directly in map popups for hobbyists):
  - No email addresses, phone numbers, named individuals, or bank account/giro details.
  - No "contact X" or "email X to subscribe" instructions — link to a website.
  - No internal classifications: never open with "Paid;" or "Free;" (the tier already shows this); never repeat the `yearly_cost` figure verbatim.
  - No audit-document phrasing: "No explicit eligibility restriction stated", "as per Circular Y", PDF edition dates, source provenance.
  - No hardcoded dates ("as of 2026-04-30") — use "currently" if recency matters.
  - No local-script abbreviations opaque to English speakers (e.g. Cyrillic ID-type codes) — spell them out in English.
  - Do not expand or unexplained acronyms: "SBC portal" → "online portal".
