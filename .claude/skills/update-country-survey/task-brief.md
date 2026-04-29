# Per-country task: research and update RTK survey entry

## Goal
Apply the ideal-entry spec to a specific country (or small batch of related countries) in the ntrip-mountpoint-map repo.

## Files to read (in order)
1. `.claude/skills/update-country-survey/ideal-entry-spec.md` — tier definitions, templates, `date_added` field rule. Read in full (small).
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

## What to write

### `docs/country-survey.md`
- Find the right alphabetical/regional position. The file is grouped by region (Western Europe, Mediterranean, Nordics, etc.). If a regional section is unclear, place near similar-region entries.
- Use the appropriate Tier A / B / C template from `.claude/skills/update-country-survey/ideal-entry-spec.md`.
- Add `**date_added**: <today's date in YYYY-MM-DD>` on the line immediately under the `### CC — Country Name` heading. The orchestrator will pass today's date to you in the assignment prompt — use that exact value.
- If updating an existing entry, bump `date_added` to today's date only if you made substantive changes (more than typo/link fixes).

### `docs/networks.md`
For each newly-documented network, add a `## id` block following the existing style (status, country, type, host:port, access, registration, yearly_cost, stations, notes). Optional: add `**date_added**:` per network if precision is useful.

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
