---
name: update-country-survey
description: Update or add country/territory entries in docs/country-survey.md and docs/networks.md, then sweep data/country_markers.json. Use this skill whenever the user mentions country entries, the country survey, missing countries, RTK pricing stubs, networks.md back-references, country markers on the map, or asks to audit / improve / fill in entries — even if they don't explicitly say "country survey". Handles per-country research in the country's primary language, tier-appropriate write-ups, the country_markers.json sweep, and a single end-of-session commit.
---

# update-country-survey

Codifies the methodology used in commit `4942fa6` (which expanded the country survey from ~110 to 188 entries). Future sessions invoking this skill should produce edits of equivalent quality without re-deriving the workflow.

## Three files, three roles

The survey, networks doc, and marker JSON are **not mirrors of each other**.
Each has a distinct purpose, audience, and editorial register. Edits should
respect those roles rather than copy text between them.

| File | Role | Audience |
|---|---|---|
| `docs/country-survey.md` | **Completeness picture.** Per-country prose recording what was investigated, what was found, where the gaps are. Missing heading = uncovered country. The flow's input — broad, includes negatives. | Maintainers + hobbyists who follow GitHub links. UK spelling; expand acronyms on first use. |
| `docs/networks.md` | **Refined operator catalogue, for us.** Curates the surveys' findings into per-network blocks (status, host:port, access, yearly_cost, …). Internal working bench between the survey and the markers. | Maintainers (developer register). Acronyms fine; audit phrasing fine. |
| `data/country_markers.json` | **User-facing translation.** Renders directly in map popups for hobbyists. Subset of networks that warrants a country-level marker, written for end users. | End users on the live map. Plain English; no jargon; no "contact X" instructions. |

The flow narrows at each step: a country may have a paragraph in the survey
with no `networks.md` block (nothing operator-shaped to catalogue) and a
`networks.md` block may have no marker (regional-only, not substantial,
single-base with pins, etc.). Don't expand a survey paragraph just to
populate a `networks.md` block, and don't create a marker just to mirror a
`networks.md` block — at every step the question is whether the next file's
role is served.

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

**Critical: tier semantics drive whether to add a marker at all.** Markers render on the world map for hobbyist users. A misplaced marker is worse than no marker because it tells a user "look here for an option" when there isn't one.

| Tier | When to add | When NOT to add |
|---|---|---|
| `vrs` | In-pipeline VRS-only network with live data. | If the network has physical pins (single-base) — those render automatically. |
| `deferred` | A **free** national-scale service is confirmed to exist; the only gap is that the endpoint/host:port isn't yet wired into the pipeline. The note must be able to truthfully start with "**N stations, free.**" | The network is paid, restricted, government-internal, defence-controlled, raw-RINEX-only / post-processing-only, or "infrastructure exists but no public service has been confirmed." None of those is "free, just not connected yet." |
| `info` | A **substantial national-scale** paid or restricted service exists that a hobbyist might investigate. "Substantial" = nationwide or near-nationwide coverage by a recognised operator. | A small private surveying company with a handful of stations in a few cities is NOT national-scale and gets no marker. A 6-station commercial network covering 5 cities does not earn a country-level circle. |
| _no marker_ | The country was investigated and nothing meets the bar above. | (default) |

**Spawn one sweep agent at the end:**

```
Update data/country_markers.json. Read the "Country-level markers" section
of docs/requirements.md for the JSON schema and tier semantics.

Procedure:
1. List existing marker IDs (jq '.markers[].id' data/country_markers.json).
2. For each networks.md entry not already represented by a marker, classify
   strictly per the tier table in the skill's SKILL.md:
   - vrs:      ONLY in-pipeline VRS-only with live data.
   - deferred: ONLY when the underlying network is FREE and the gap is
               purely "endpoint not yet in pipeline." The note MUST be able
               to truthfully open with "N stations, free." If you cannot
               write that, do NOT add a deferred marker.
   - info:     ONLY substantial national-scale paid/restricted operators
               (think HEPOS, ROMPOS, swipos, KSA-CORS — country-spanning
               services from a recognised cadastral or commercial body).
               A regional surveying company with handful of stations does
               NOT earn a marker.
   - no marker: Investigated, nothing operational, post-processing-only,
                government-internal, defence-controlled, "infrastructure
                exists but no public service" — these get NO marker. The
                country-survey.md prose is sufficient documentation.
3. The note field is USER-FACING (renders in map popup tooltips for
   hobbyists). Read the `_note_field_convention` and
   `_yearly_cost_convention` keys at the top of data/country_markers.json,
   and the matching sections in this SKILL.md, before writing any marker.
   In short: do NOT restate the price, access label, or region (the popup
   already renders those); do NOT inline the registration URL (use the
   `registration` field); do NOT write "Contact X" — link to the website
   instead. Plain English; expand acronyms; no internal classifications
   ("$200/yr cutoff") or audit phrasing ("no English pricing page",
   "±2 cm at 95 % confidence"). Skip the note entirely if there is
   nothing useful to add beyond the auto-rendered chrome. Use the
   canonical `yearly_cost` format ($X/yr / €X/yr / X CCY/yr with USD
   parenthetical for non-USD); OMIT yearly_cost when pricing is not
   published rather than writing "not publicly listed" there.
4. Skip in-pipeline single-base entries (they get physical pins).
5. Skip rejected entries unless the rejection means "exists but unobtainable
   for the target user" AND it's substantial.
6. Use skeleton-first JSON edits (batches of ~10 entries per Edit call).

Report: count of new entries added per tier, plus a list of networks.md IDs
deliberately NOT given a marker and the one-word reason
(no-public-service / regional-only / paid-too-small / archive-only / etc.).
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

### Audience: who reads what

- `docs/country-survey.md` — read by humans following GitHub links from the README/map. Hobbyist register. The same audience as `guide.html` and `data/help_topics.json`. Acronyms must be expanded on first use; "CORS" is jargon — prefer "permanent GPS reference station" or "fixed GPS reference network" in prose.
- `docs/networks.md` — internal/developer reference. Acronyms OK. Audit phrasing OK.
- `data/country_markers.json` `note` field — **renders in map popup tooltips for end users.** Plain English. Tells the reader what they need to do next. No acronyms without expansion. No internal classifications (don't say "$200/yr cutoff" — say "expensive" or quote the price). No audit phrasing ("no English pricing page", "±2 cm horizontal accuracy at 95 % confidence" — wrong audience).

### `country_markers.json` `note` field — what to write

The popup chrome (see `index.html:1017-1052`) auto-renders five things from
the marker object: the access label (mapped from `access`), `yearly_cost`,
"Covers `region`.", `note`, and the `registration` URL as a separate link.
The `note` should **add information beyond those**, not restate them.

**Don't:**
- Repeat the price (it's in `yearly_cost`).
- Repeat the access label ("Paid subscription required" / "Access restricted" — already shown).
- Restate the region.
- Include the registration URL inline ("Subscribe at X.gov", "via X.gov", "register at X" — the `registration` field renders separately).
- Instruct the user to "Contact X" or "contact X via …" — link to the website via `registration` instead. The user is on a map looking for an option, not for chores.
- Include internal/audit phrasing ("documented for completeness", "no English pricing page", "±2 cm horizontal accuracy", "$200/yr cutoff", "subordinate body of …").

**Do, when applicable:**
- Station count once, e.g. "78 stations".
- Free hobbyist alternatives where they exist, e.g. "Volunteer rtk2go/Centipede bases provide partial free coverage."
- Terminal access blockers in plain words, e.g. "TxDOT employees and contractors only. No hobbyist registration path."
- Real safety/operational warnings (active spoofing, war disruption, infrastructure collapse).
- Non-obvious access mechanics ("Endpoint disclosed only after account approval", "NOT standard NTRIP — raw TCP streams").

Tone: matter-of-fact, hobbyist-addressed, ≤2 short sentences typical, ~250 chars max. **Skip the field entirely if there's nothing useful to add** — the popup is not weaker without a `note`.

### `country_markers.json` `yearly_cost` field — canonical format

One short line. Choose by currency:

- USD: `$X/yr` (no `~` prefix; no parenthetical needed).
- Symbol currencies: `€X/yr`, `£X/yr`, `¥X/yr`, `₹X/yr`, `₽X/yr`, `S$X/yr`, `₱X/yr`. Append USD parenthetical: `€169/yr (~$183/yr)`.
- ISO-only codes (no symbol): `X CCY/yr`, e.g. `1,500 CHF/yr (~$1,650/yr)`, `9,000 SEK/yr (~$850/yr)`, `8,688 RSD/yr (~€74/yr, ~$80/yr)`.
- Drop the `~` prefix on the local-currency figure unless it's genuinely uncertain — annual fees are estimates by definition.
- Local-currency qualifiers ("private users", "commercial only") belong in `note`, not `yearly_cost`.
- One-time fees: state the form clearly, e.g. `$100 one-time`, `₱1,000 one-time (~$17) plus ongoing subscription`.

**If pricing is not published, OMIT the `yearly_cost` field entirely** so the line disappears from the popup. Do not write `"yearly_cost":"not publicly listed"` or `"contact …"` there. If it's worth surfacing that the operator doesn't publish prices, say so once in `note` (e.g. "Pricing not published online.").

### `status: deferred` in `networks.md` — narrow semantic

`status: deferred` means **a free service exists; only the endpoint isn't yet wired into the pipeline**. This is the only correct use. It directly drives whether `data/country_markers.json` adds a `deferred` (grey-circle, "look here, free option") marker.

Do **not** use `status: deferred` for:
- "Investigated, found infrastructure but no operational public service" — use `status: rejected` with a one-line rationale instead, or document inline in `country-survey.md` prose with no `networks.md` block at all.
- Government-internal / defence-controlled networks not accessible to civilians — `status: rejected`.
- Post-processing / RINEX-archive-only services (no real-time NTRIP) — `status: rejected` (it's not an RTK service).
- "Pricing not publicly listed, may be free or paid" — if access model is unknown, do not pretend it's free; either omit the block or use `status: paid` with a `pricing-unverified` note.

When in doubt, **omit the `networks.md` block** and just describe the finding inline in the `country-survey.md` prose. Empty space in `networks.md` is a feature; cluttering it with "investigations that found nothing" pollutes the marker sweep downstream.

### Curation threshold for paid networks

A `networks.md` block (and any associated marker) for a paid commercial network is appropriate only when the operator is **substantial**: nationwide or near-nationwide coverage, or a recognised regional/cadastral body. A small private surveying company with stations in a few cities does not earn a country-level entry — describe it inline in the country prose if useful, but don't promote it to its own block.

### Other rules

- **No bare email addresses** in `docs/networks.md` or `docs/country-survey.md` — link to a website that describes the email-based signup process. (Emails rot; web pages get archived.)
- **`**yearly_cost**:` field is required** in every networks.md block where access is `paid` or `paid-affordable`. Pricing in local currency first, then `(~$USD/yr)` or `(~€EUR/yr)` parenthetical in the prose. Greppable for currency audits.
- **UK spelling** in prose (centimetre, behaviour, organisation). The repo's user-facing copy is UK-spelled; survey prose follows suit.
- **"GPS" colloquially / "GNSS" structurally** — see `CLAUDE.md`. L1 and L2 are not "GPS frequencies" because Galileo E1 and E5b sit on the same bands.
- **Volunteer line canonical phrasing**: `**Volunteer**: none. Zero XX stations on rtk2go or Centipede.` Some past entries deviated; new edits should follow the canonical form for grep-ability.
- **Tier A "why" paragraph** is required only when the access situation is materially different due to a systemic constraint (sanctions, civil war, legal barrier, government collapse). For Tier B/C entries it's clutter — omit.
- **`$200/yr` is the orchestrator's classification term, not user-visible prose.** Use it to decide tier (paid-affordable vs paid) but write Gap sentences in plain words: "expensive", "modest annual fee", or quote the price directly.

## Out of scope

`index.html`, `guide.html`, `data/help_topics.json`, `scripts/inject_seo_help.py`, the GitHub Actions workflow, and `scripts/fetch_stations.py` are user-facing copy or pipeline code and are governed by separate workflows. This skill only touches the survey docs and the static marker file.
