---
name: update-country-survey
description: Update or add country/territory entries in docs/country-survey.md and docs/networks.md, then sweep data/country_markers.json. Use this skill whenever the user mentions country entries, the country survey, missing countries, RTK pricing stubs, networks.md back-references, country markers on the map, or asks to audit / improve / fill in entries — even if they don't explicitly say "country survey". Handles per-country research in the country's primary language, tier-appropriate write-ups, the country_markers.json sweep, and a single end-of-session commit.
---

# update-country-survey

Workflow for updating country/territory entries in `docs/country-survey.md`,
the curated network blocks in `docs/networks.md`, and the user-facing
`data/country_markers.json` markers — and committing them together.

## Pipeline context

This skill operates over four files in the RTK survey pipeline. **Per-file
rules and the cross-file flow live in `.claude/process/`** — read the
relevant meta before editing the affected file:

- `.claude/process/pipeline.md` — cross-file flow (LEAD: country-survey → networks → markers + fetch)
- `.claude/process/country-survey.md` — rules for `docs/country-survey.md`
- `.claude/process/networks.md` — rules for `docs/networks.md`
- `.claude/process/country-markers.md` — rules for `data/country_markers.json`
- `.claude/process/fetch-stations.md` — rules for `scripts/fetch_stations.py` SOURCES

This skill is the **workflow runbook** for batch country audits; it does
not duplicate per-file rules.

## Working files

All paths repo-relative (`/home/user/ntrip-mountpoint-map`).

- `docs/country-survey.md` — ~3000 lines, ~40k tokens. **Never read in full.** Grep first.
- `docs/networks.md` — ~3000 lines. Grep + targeted Read.
- `data/country_markers.json` — see `.claude/process/country-markers.md` for tier rules; the file's own `_note_field_convention` / `_yearly_cost_convention` / `_tiers` / `_vrs_flag` keys are the source of truth for copy and format.
- `data/stations.json` — parsed mountpoints; ISO 3166-1 alpha-3.
- `data/*.sourcetable` — raw STR records.
- `docs/requirements.md` — country-marker JSON schema.
- `references/ideal-entry-spec.md` — tier criteria (A/B/C), per-tier checklists, templates, common omissions. **Read first when adding entries.**
- `references/task-brief.md` — the brief each per-country sub-agent reads. Point sub-agents at the path; don't inline.

## Workflow

### 0. Today's date
`date -I` once at session start. Pass as `<TODAY>` to every sub-agent — don't trust memory or session metadata.

### 1. Scope
- Named countries → skip to step 3.
- Open-ended audit → one sonnet sub-agent generates a target list (the precedent audit used top-120 GDP ∪ top-120 population + ~42 administered territories ≈ 232 entities). Save to `/tmp/target-countries.md`.

### 2. Priority bucket (only for >20 countries)
One sonnet sub-agent buckets the list against current `country-survey.md` quality:
- **P0** heading missing.
- **P1** heading present but stub (no networks named, no pricing).
- **P2** content present but missing fields per `ideal-entry-spec` (Gap, host:port, USD, back-ref).
- **P3** adequate; only `date_added` may need adding.

Save to `/tmp/country-priority.md`. Process P0 → P3 (largest quality lift first; P3 is mechanical).

### 3. Plan batches
Group by primary search language so the agent's search routine compounds (Sahel → French; Caucasus → Russian + script; East Asia → respective national languages). **Batch size by research depth:**
- Tier A (war/sanctions/legal context): 1–2 per agent.
- Tier B (one or two named networks): 2–3 per agent.
- Tier C stubs ("likely nothing found"): 4–6 per agent.
- P3 date-only backfill: one sweep agent for the whole bucket.

### 4. Spawn sub-agents sequentially
**Sequential, not parallel.** If main context dies mid-loop, only the in-flight agent's work is lost; everything else is already on disk.

```
Read `.claude/skills/update-country-survey/references/task-brief.md`. Apply sequentially to:

1. **CC — Country Name** — <one-line guidance>
2. ...

Today's date for `**date_added**:` is <TODAY>. Report under <N> words.
```

One-line guidance names the likely tier and what to look for, e.g. `P0 missing; likely Tier B; look for VN-CORS at Cục Đo đạc Bản đồ`. Keep prompts terse — the task brief has the rest.

### 5. Recover from failures
- **Timeout / empty result** → re-run the country alone with explicit "write at least a Tier C stub". Skip only for genuinely uninhabited or closed entities.
- **Malformed edit** → `grep -n "^### CC — " docs/country-survey.md` to confirm placement; re-run alone if missing.
- **Wrong placement** → edit directly; don't respawn a research agent.

### 6. country_markers.json sweep
Required after any `networks.md` change. **Tier rules, vrs flag rules, and
the note-violation checklist all live in `.claude/process/country-markers.md`.**

**Sweep agent prompt:**

```
Update data/country_markers.json.

Read .claude/process/country-markers.md for tier rules, vrs flag rules, and
the note-violation checklist. Also read the self-documenting _note_field_
convention, _yearly_cost_convention, _tiers, and _vrs_flag keys at the top
of country_markers.json itself — those are the source of truth for copy.

Procedure:
1. List existing IDs: jq '.markers[].id' data/country_markers.json.
2. For each networks.md entry not yet represented, pick a tier per
   country-markers.md §"When to add a marker". When in doubt: no marker.
3. Set "vrs": true if the network delivers VRS / network-RTK streams.
4. Skeleton-first JSON edits, ~10 entries per Edit call.
5. After adding, sweep all modified notes against the violations checklist
   in country-markers.md §"Note conventions".

Report: count added per tier and how many got the vrs flag, plus a list of
networks.md IDs deliberately NOT given a marker with a one-word reason
(no-public-service / regional-only / paid-too-small / archive-only / …).
```

### 6b. fetch_stations.py SOURCES sweep
Required when a `networks.md` block flips between `candidate` and ingest-ready,
or to `rejected`. Rules in `.claude/process/fetch-stations.md`.

### 7. Commit and push
Single commit covering all modified files. Message includes: countries added/modified, new `networks.md` blocks, marker count delta, search languages used. `git push -u origin <branch>`. No PR unless asked.

## Conventions

Per-file conventions (date_added, status discipline, yearly_cost format,
type field, tier shape, etc.) live in the corresponding meta:

- `docs/country-survey.md` → `.claude/process/country-survey.md`
- `docs/networks.md` → `.claude/process/networks.md`
- `data/country_markers.json` → `.claude/process/country-markers.md`
- `scripts/fetch_stations.py` → `.claude/process/fetch-stations.md`

Cross-file flow (which file leads, how findings propagate, when to skip a
step) → `.claude/process/pipeline.md`.

## Out of scope

`index.html`, `guide.html`, `data/help_topics.json`,
`scripts/inject_seo_help.py`, the GitHub Actions workflow.
`scripts/fetch_stations.py` SOURCES editing is **in scope** (rules in
`.claude/process/fetch-stations.md`).
