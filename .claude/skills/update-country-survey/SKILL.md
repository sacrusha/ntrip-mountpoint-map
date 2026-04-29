---
name: update-country-survey
description: Update or add country/territory entries in docs/country-survey.md and docs/networks.md to a consistent quality bar. Use when the user asks to update one or more country entries, add missing countries, fill in pricing/host:port for stub entries, or audit the country survey. Handles per-country research (in the country's primary language), tier-appropriate write-ups, networks.md back-references, and the country_markers.json sweep at the end.
---

# update-country-survey

This skill orchestrates the per-country research and edit workflow used to bring `docs/country-survey.md` and `docs/networks.md` up to a consistent quality bar. It mirrors the methodology used in the bulk audit (commit `4942fa6`) that took the survey from ~110 entries to 188.

## When to invoke

- "Update the survey entry for X" / "Add country X to the survey"
- "Fill in pricing for the Balkan stubs"
- "These entries are weak — fix them"
- A list of country codes with no further direction

## Reference files in this skill

- `ideal-entry-spec.md` — tier scheme (A / B / C), per-tier checklists, when the contextual "why" paragraph is required, the `date_added` field convention, three concrete templates, and a catalogue of common omissions. **Read this first.**
- `task-brief.md` — the brief that each per-country sub-agent reads. Contains search-language rules, local-data lookup procedure, edit mechanics, and reporting format.

## Workflow

### 1. Read reference files

Read `ideal-entry-spec.md` and `task-brief.md` to internalise the tier scheme and editing rules. Read once at the start; sub-agents will read them again on their own.

### 2. Plan batches

Group the requested countries into batches of **~3 countries per sub-agent**, choosing groupings that share a primary search language or region:

- Sahel/francophone West Africa → French
- Latin America → Spanish (Brazil → Portuguese)
- Caucasus → Russian + local script
- Caribbean small states → English (Tier C stubs, can batch larger)
- East Asia → respective national language

This lets one sub-agent reuse the same language-search routine across countries. If a single Tier-A country needs a long contextual paragraph (e.g. wartime sanctions), give it its own batch.

### 3. Spawn sub-agents sequentially

For each batch, spawn one sonnet agent (`subagent_type: general-purpose`, `model: sonnet`). Per-agent prompt template:

```
Read `.claude/skills/update-country-survey/task-brief.md`. Apply sequentially to:

1. **CC — Country Name** — <one-line guidance, e.g. "P0 missing entry; check XYZ
   national authority for CORS network">
2. **CC — Country Name** — <guidance>
3. **CC — Country Name** — <guidance>

Today's date for `**date_added**:` is <YYYY-MM-DD>.

Report under 100 words.
```

**Sequential, not parallel.** The user's preference: if main context dies, only the in-flight agent loses work. Wait for each agent to complete before launching the next.

**Per-agent prompts should be terse.** The sub-agent reads the task brief; you don't need to repeat its rules. Just name the countries, give a one-line research hint per country (operator name, what's already known), and pass today's date.

### 4. Edit-mechanics gotchas to enforce

These are documented in `CLAUDE.md` but worth repeating to sub-agents when relevant:

- **Skeleton-first writing for large outputs** — if a sub-agent will produce a long entry, instruct it to Write a skeleton first then Edit-fill each section. Single large Writes can hit the ~300 s idle timeout and produce nothing.
- **Targeted Reads, never full-file** — `docs/country-survey.md` is >40k tokens; `docs/networks.md` is comparable. Sub-agents should grep + Read only the relevant sections. The task brief already instructs this.
- **Use local data, not web search, for station counts** — `data/stations.json` (alpha-3 country codes), `data/rtk2go.sourcetable`, `data/centipede.sourcetable`, `data/earthscope.sourcetable`. Web search is for finding networks, not counting them.

### 5. Date convention

- **Substantive edits in the current session** → `**date_added**: <today>` under the country heading.
- **Bulk-only backfills** (when the only change to an entry is adding the date_added field for greppability, no other content edited) → `**date_added**: <yesterday>`. The two-date convention makes the bulk-pass entries greppable separately.
- This convention was used for commit `4942fa6` (substantive edits dated 2026-04-29; bulk backfill dated 2026-04-28).

### 6. Optional priority ranking

If the user gives a long list (>20 countries) without prioritisation, spawn a single ranking sub-agent first to bucket the list against current `docs/country-survey.md` quality:

- **P0** — heading missing entirely.
- **P1** — heading present but stub (1–3 lines, no networks named, no pricing).
- **P2** — heading present with content but missing one or more required fields per `ideal-entry-spec.md` (e.g. pricing, Gap sentence, back-reference, USD/EUR conversion).
- **P3** — adequate per its tier; only `date_added` may need adding.

Process P0 first (yields biggest improvement), then P1, then P2, then a single bulk agent for any P3 `date_added` backfills.

### 7. country_markers.json sweep (required when networks.md changes)

Per `CLAUDE.md`'s manual-maintenance rule: every time a network is added or removed in `docs/networks.md`, `data/country_markers.json` must move with it. After all per-country agents complete, spawn one sweep agent:

```
Update data/country_markers.json so it covers networks.md entries added or
modified in this session. Read the "Country-level markers" section of
docs/requirements.md for tier definitions (vrs / deferred / info) and schema.

Procedure:
1. List existing marker IDs.
2. List networks.md IDs that are status=paid/paid-affordable/restricted (→
   info tier) or status=deferred (→ deferred tier) or status=in-pipeline
   AND VRS-only (→ vrs tier).
3. Add missing markers using country centroid or capital lat/lon.
4. Skip in-pipeline single-base entries (they get physical pins).
5. Skip rejected entries that don't represent an obtainable service.

Report: count of new entries added per tier.
```

The sweep is sizeable (the bulk audit added 99 markers) but mechanical. Use skeleton-first for the JSON edits (batches of ~10 entries per Edit call).

### 8. Commit

Single commit covering all three modified files (`docs/country-survey.md`, `docs/networks.md`, `data/country_markers.json`). The commit message should summarise:

- Number of country entries added/modified.
- Number of new networks documented in `networks.md`.
- Marker count delta in `country_markers.json` (e.g. "122 → 221, +68 deferred, +31 info").
- Search languages used.

Push with `git push -u origin <branch>`. Do not create a PR unless the user asks.

## Hard rules

These are inherited from the project conventions (CLAUDE.md, requirements.md):

- **No bare email addresses** in `docs/networks.md` or `docs/country-survey.md` — link to a website that describes the email-based signup process instead.
- **UK spelling** in prose (centimetre, behaviour, organisation).
- **"GPS" colloquially / "GNSS" structurally** — see CLAUDE.md.
- **Pricing format**: local currency first, then `(~$USD/yr)` or `(~€EUR/yr)` parenthetical.
- **Volunteer line canonical phrasing**: `**Volunteer**: none. Zero XX stations on rtk2go or Centipede.` (Some past entries deviated; new edits should follow the canonical form.)
- **Tier A "why" paragraph** is required only when the access situation is materially different due to a systemic constraint (sanctions, civil war, legal barrier, government collapse). Do not add a "why" paragraph to Tier B/C entries — it's clutter.

## Out of scope

- Updating `index.html`, `guide.html`, `data/help_topics.json` (different concern; these are user-facing copy).
- Running `scripts/inject_seo_help.py` (only relevant when `data/help_topics.json` changes).
- Modifying `scripts/fetch_stations.py` or adding new in-pipeline sources (separate workflow; requires testing the pipeline).
