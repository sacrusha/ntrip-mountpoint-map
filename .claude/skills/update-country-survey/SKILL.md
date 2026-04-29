---
name: update-country-survey
description: Update or add country/territory entries in docs/country-survey.md and docs/networks.md, then sweep data/country_markers.json. Use this skill whenever the user mentions country entries, the country survey, missing countries, RTK pricing stubs, networks.md back-references, country markers on the map, or asks to audit / improve / fill in entries — even if they don't explicitly say "country survey". Handles per-country research in the country's primary language, tier-appropriate write-ups, the country_markers.json sweep, and a single end-of-session commit.
---

# update-country-survey

Workflow for updating country/territory entries in `docs/country-survey.md`,
the curated network blocks in `docs/networks.md`, and the user-facing
`data/country_markers.json` markers — and committing them together.

## Three files, three roles

The files are **not mirrors of one another**. Each has a distinct purpose;
edits should respect that rather than copy text between them. The flow
narrows at each step: a country may have survey prose with no `networks.md`
block (nothing operator-shaped to catalogue), and a `networks.md` block may
have no marker (regional-only, single-base with pins, etc.). Don't expand or
invent content just to populate the next file.

| File | Role | Register |
|---|---|---|
| `docs/country-survey.md` | **Completeness picture.** Per-country prose: what was investigated, found, gapped. Missing heading = uncovered country. Includes negatives. | Maintainers + hobbyists via GitHub. UK spelling; expand acronyms ("CORS" → "permanent GPS reference station"). |
| `docs/networks.md` | **Refined operator catalogue, for us.** Per-network blocks (status, host:port, yearly_cost, …). | Developer-facing. Acronyms and audit phrasing fine. |
| `data/country_markers.json` | **User-facing translation.** Subset of networks worth a country-level marker; renders directly in map popups. | End users. Plain English; no jargon; no "contact X". Conventions live in the file's own `_note_field_convention` / `_yearly_cost_convention` / `_tiers` keys — that's the source of truth. |

## Working files

All paths repo-relative (`/home/user/ntrip-mountpoint-map`).

- `docs/country-survey.md` — ~3000 lines, ~40k tokens. **Never read in full.** Grep first.
- `docs/networks.md` — ~3000 lines. Grep + targeted Read.
- `data/country_markers.json` — three tiers (`vrs`, `deferred`, `info`); self-documenting top-level keys describe note + yearly_cost format.
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
Required after any `networks.md` change. **A misplaced marker is worse than no marker** — it tells a hobbyist "look here" when there's nothing.

| Tier | Add when | Don't add when |
|---|---|---|
| `vrs` | In-pipeline VRS-only with live data. | Network has physical pins (auto-rendered). |
| `deferred` | **Free** national-scale service confirmed; only the endpoint is the gap. Note must truthfully open with "N stations, free." | Anything not free; post-processing-only; government-internal; defence-controlled; "infrastructure exists but no service confirmed". |
| `info` | **Substantial national-scale** paid or restricted operator (HEPOS, ROMPOS, swipos, KSA-CORS scale). | Small private surveyor with a few cities → country prose only, no marker. |
| _none_ | Investigated, nothing meets the bar above. | (default) |

When unsure between `deferred` and `rejected` upstream in `networks.md`, default to `rejected`. Misclassifying as `deferred` produces a misleading "free option here" marker. When unsure whether to write a `networks.md` block at all, **omit it** and describe inline in the country prose. Empty space in `networks.md` is a feature.

**Sweep agent prompt:**

```
Update data/country_markers.json.

Before writing anything, read the self-documenting `_note_field_convention`,
`_yearly_cost_convention`, and `_tiers` keys at the top of that file —
those are the source of truth for marker copy and format. Also read the
"Country-level markers" section of docs/requirements.md for the JSON schema.

Procedure:
1. List existing IDs: jq '.markers[].id' data/country_markers.json.
2. For each networks.md entry not yet represented, classify per the tier
   table in SKILL.md §6. When in doubt: no marker.
3. Skip in-pipeline single-base entries (they get physical pins).
4. Skip rejected entries unless the rejection is "exists but unobtainable
   for the target user" AND the operator is substantial.
5. Skeleton-first JSON edits, ~10 entries per Edit call.

Report: count added per tier, plus a list of networks.md IDs deliberately
NOT given a marker with a one-word reason (no-public-service / regional-only
/ paid-too-small / archive-only / …).
```

### 7. Commit and push
Single commit covering all modified files. Message includes: countries added/modified, new `networks.md` blocks, marker count delta, search languages used. `git push -u origin <branch>`. No PR unless asked.

## Conventions

### `**date_added**:` (greppable)
- Substantive edit → today's date, on the line directly under `### CC — Country Name`.
- Bulk-only `date_added` backfill (no content change) → yesterday's date, so backfills are greppable separately from research.
- Optional per `## id` block in `networks.md` when a network is revised independently.

### `status:` discipline in `networks.md`
Drives the marker sweep — be strict.

- `in-pipeline` — wired into `fetch_stations.py`.
- `deferred` — **free** service confirmed; only the endpoint is the gap. Nothing else.
- `paid` / `paid-affordable` — accessible to civilians for a fee. Requires `**yearly_cost**:` (local currency first, USD or EUR parenthetical, greppable for audits).
- `restricted` — exists but unobtainable for the target user.
- `rejected` — investigated and ruled out (one-line rationale).

### Tier A "why" paragraph
Required only when a systemic constraint (sanctions, civil war, legal barrier, collapse) materially changes what a hobbyist should do. For Tier B/C it's clutter — omit.

### Curation threshold for paid operators
A `networks.md` block (and any marker) for a paid commercial operator only when the operator is **substantial**: nationwide / near-nationwide / recognised regional or cadastral body. Small surveying companies → describe inline in country prose at most.

### Other
- **No bare email addresses** in either docs file. Link to a website describing the signup.
- **UK spelling** in prose.
- **"GPS" colloquially, "GNSS" structurally** (see `CLAUDE.md`).
- **`**Volunteer**:` canonical form**: `**Volunteer**: none. Zero XX stations on rtk2go or Centipede.` Greppability.
- **`$200/yr` is internal classification only.** In user-visible prose write "expensive" / "modest annual fee" / quote the price.

## Out of scope
`index.html`, `guide.html`, `data/help_topics.json`, `scripts/inject_seo_help.py`, the GitHub Actions workflow, and `scripts/fetch_stations.py`. This skill only touches the survey docs and the marker file.
