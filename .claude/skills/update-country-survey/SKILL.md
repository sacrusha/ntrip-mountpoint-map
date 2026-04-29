---
name: update-country-survey
description: Update or add country/territory entries in docs/country-survey.md and docs/networks.md, then sweep data/country_markers.json. Use this skill whenever the user mentions country entries, the country survey, missing countries, RTK pricing stubs, networks.md back-references, country markers on the map, or asks to audit / improve / fill in entries — even if they don't explicitly say "country survey". Handles per-country research in the country's primary language, tier-appropriate write-ups, the country_markers.json sweep, and a single end-of-session commit.
---

# update-country-survey

Codifies the methodology used in commit `4942fa6` (which expanded the country survey from ~110 to 188 entries). Future sessions invoking this skill should produce edits of equivalent quality without re-deriving the workflow.

## Repo-relative paths

This skill assumes the working directory is the repo root (typically `/home/user/ntrip-mountpoint-map` but treat all paths as repo-relative).

| Path | Role |
|---|---|
| `docs/country-survey.md` | Country/territory entries (~3000 lines, ~40k tokens — never read in full) |
| `docs/networks.md` | Per-network detail blocks (~3000 lines — grep + targeted Read only) |
| `data/country_markers.json` | Static marker file rendered on the map (three tiers: vrs, deferred, info) |
| `data/stations.json` | Parsed mountpoints; ISO 3166-1 alpha-3 country codes |
| `data/*.sourcetable` | Raw STR records for each in-pipeline caster |
| `docs/requirements.md` | Project spec — has the "Country-level markers" section that defines the JSON schema |

## Reference files in this skill

- `references/ideal-entry-spec.md` (~290 lines) — read first. Sections: tier criteria (A / B / C), per-tier checklists, when the contextual "why" paragraph is required, the `date_added` field convention, three concrete templates, common omissions catalogue.
- `references/task-brief.md` (~70 lines) — the brief each per-country sub-agent reads. Search-language rules, local-data lookup procedure, edit mechanics, reporting format. The orchestrator does **not** need to inline this into sub-agent prompts; just point sub-agents at the file path.

## Workflow

### Step 0 — Get today's date

Run `date -I` once at the start. Use the output (e.g. `2026-04-29`) as `<TODAY>` in every sub-agent prompt. Don't rely on memory or session metadata.

### Step 1 — Scope the work

If the user names specific countries: skip to Step 3.

If the user's request is open-ended ("audit the survey", "make sure we cover the major countries"): generate a target list first. The bulk audit used **top-120 GDP ∪ top-120 population + ~42 administered territories** (≈232 entities). Save the list to `/tmp/target-countries.md` so it's recoverable if the session restarts. Spawn one sonnet sub-agent for this — it's a closed-form task that takes ~2 minutes.

### Step 2 — Priority ranking (required for >20 countries)

For lists longer than ~20 entries, spawn one sonnet sub-agent to bucket them against current `docs/country-survey.md` quality. Buckets:

- **P0** — heading missing entirely.
- **P1** — heading present but stub (1–3 lines, no networks named, no pricing).
- **P2** — heading present with content but missing fields per the ideal-entry-spec (Gap sentence, host:port, USD conversion, back-reference, etc.).
- **P3** — adequate per its tier; only `date_added` may need adding.

Save to `/tmp/country-priority.md`. Process in order P0 → P1 → P2 → P3, since P0 yields the largest quality lift per agent and P3 is mechanical.

For lists ≤20 the orchestrator can skip the dedicated ranking agent and bucket inline.

### Step 3 — Plan batches by language and depth

Group countries into batches sharing a primary search language or region. **Batch size depends on research depth, not a fixed number:**

- **Tier A entries** (war/sanctions/legal-barrier context required): 1–2 per agent. The contextual paragraph takes time to research and write.
- **Tier B entries** (one or two named networks needing pricing/host:port): 2–3 per agent.
- **Tier C stubs** (small market, likely "nothing found"): 4–6 per agent.
- **P3 date-only backfill**: a single sweep agent for the whole bucket, regardless of size.

Group by language so an agent's search routine compounds: Sahel/francophone Africa → French; Caucasus → Russian + local script; Caribbean small states → English; East Asia → respective national languages.

### Step 4 — Spawn sub-agents sequentially

Sequential, not parallel. The reason: if main context dies mid-loop, only the in-flight agent's work is lost. Each completed agent's edits are already on disk.

**Per-agent prompt template:**

```
Read `.claude/skills/update-country-survey/references/task-brief.md`. Apply sequentially to:

1. **CC — Country Name** — <one-line guidance>
2. **CC — Country Name** — <one-line guidance>
3. **CC — Country Name** — <one-line guidance>

Today's date for `**date_added**:` is <TODAY>.

Report under <N> words.
```

The one-line guidance should name the likely tier and the operator/network the agent should look for. Examples:

- P0 missing: `P0 missing entry; likely Tier B; check Vietnam Department of Survey and Mapping (Cục Đo đạc Bản đồ và Thông tin Địa lý) for VN-CORS endpoint`
- P1 stub: `P1 stub; existing entry names CZEPOS but lacks pricing; find CZK/yr at czepos.cuzk.cz and add USD/EUR conversion`
- P2 partial: `P2 missing Gap sentence and back-reference; existing entry references swipos which is in-pipeline as VRS-only`
- Tier A required: `Tier A; ongoing civil war; explain how this changes hobbyist outcome (hardware imports, infrastructure damage)`

Keep prompts terse — the sub-agent reads the task brief and gets full instructions there.

### Step 5 — Recover from failures

If a sub-agent times out, returns "nothing found" without writing anything, or produces a malformed entry:

- **Timeout / empty result**: re-run the country as a single-country batch with an explicit instruction to write at least a Tier C stub. The skip-the-country option is reserved for genuinely uninhabited / closed entities (handle skips inline in the orchestrator's prompt; don't reference an external skip-list file since those are session-temp).
- **Malformed edit**: `grep -n "^### CC — " docs/country-survey.md` to confirm the heading landed; if not, re-run that country alone.
- **Wrong placement**: edit the placement directly rather than respawning a research agent.

### Step 6 — country_markers.json sweep

Required after every session that modifies `docs/networks.md`. Per `CLAUDE.md`'s manual-maintenance rule.

Spawn one sweep agent at the end:

```
Update data/country_markers.json so it covers networks.md entries added or
modified in this session. Read the "Country-level markers" section of
docs/requirements.md for tier definitions and JSON schema.

Procedure:
1. List existing marker IDs (grep '"id":' data/country_markers.json | sort -u).
2. List networks.md IDs that need markers:
   - status=paid, paid-affordable, restricted → info tier (circled-?)
   - status=deferred (free, not in pipeline) → deferred tier (grey circle)
   - status=in-pipeline AND VRS-only → vrs tier (coloured circle)
3. Skip in-pipeline single-base entries — they get physical pins automatically.
4. Skip rejected entries unless the rejection means "exists but unobtainable
   for the target user" (e.g. licensed-surveyors-only).
5. Use country centroid or capital lat/lon for new entries.
6. Use skeleton-first JSON edits (batches of ~10 entries per Edit call) to
   avoid the idle timeout — the bulk audit added 99 markers across 12+ Edit
   calls.

Report: count of new entries added per tier.
```

### Step 7 — Commit and push

Single commit covering all three modified files. Commit message summary:

- Number of country entries added/modified.
- Number of new networks documented in `docs/networks.md`.
- Marker count delta in `data/country_markers.json` (e.g. "122 → 221, +68 deferred, +31 info").
- Search languages used.

Push with `git push -u origin <branch>`. Do not create a PR unless the user asks.

## Date convention (greppable)

- **Substantive edits in this session** → `**date_added**: <TODAY>` under each touched country heading.
- **Bulk-only `date_added` backfills** (only change is adding the field, no content edits) → `**date_added**: <YESTERDAY>`. This makes bulk-pass entries greppable separately from research-driven edits.

The two-date convention only applies within a single bulk-backfill pass at the end of a large audit. In a normal session that processes a handful of countries, every touched entry uses today's date.

In commit `4942fa6` substantive edits were dated `2026-04-29` and the bulk backfill `2026-04-28`.

## Hard rules

- **No bare email addresses** in `docs/networks.md` or `docs/country-survey.md` — link to a website that describes the email-based signup process. (Emails rot; web pages get archived.)
- **`**yearly_cost**:` field is required** in every networks.md block where access is `paid` or `paid-affordable`. Pricing in local currency first, then `(~$USD/yr)` or `(~€EUR/yr)` parenthetical in the prose. Greppable for currency audits.
- **UK spelling** in prose (centimetre, behaviour, organisation). The repo's user-facing copy is UK-spelled; survey prose follows suit.
- **"GPS" colloquially / "GNSS" structurally** — see `CLAUDE.md`. L1 and L2 are not "GPS frequencies" because Galileo E1 and E5b sit on the same bands.
- **Volunteer line canonical phrasing**: `**Volunteer**: none. Zero XX stations on rtk2go or Centipede.` Some past entries deviated; new edits should follow the canonical form for grep-ability.
- **Tier A "why" paragraph** is required only when the access situation is materially different due to a systemic constraint (sanctions, civil war, legal barrier, government collapse). For Tier B/C entries it's clutter — omit.

## Out of scope

`index.html`, `guide.html`, `data/help_topics.json`, `scripts/inject_seo_help.py`, the GitHub Actions workflow, and `scripts/fetch_stations.py` are user-facing copy or pipeline code and are governed by separate workflows. This skill only touches the survey docs and the static marker file.
