# Ideal country-survey entry spec

## 1. Three tiers — criteria and examples

Entries in `docs/country-survey.md` vary in depth. Three tiers reflect how much
context a reader actually needs to act, not editorial ambition.

---

### Tier A — Full context entry

**Criteria (two or more of the following must hold):**
- One or more named networks exist (free, deferred, or paid-affordable) whose
  access model has a non-obvious constraint: a legal barrier, sanctions,
  national-ID gating, credentials that limit qualifying users, or a time-limited
  free window.
- The country has significant hobbyist demand (large population / economy) and
  the constraint is a transferable lesson for similar countries.
- A "why this situation exists" answer meaningfully changes what a reader should do.
- Multiple networks exist with mixed pipeline status that would confuse a reader
  without a structured summary.

**Examples:** RU (sanctions), CN (测量法 legal barrier), MM (military coup),
IT (12+ regional networks with mixed pipeline status), NE (Saharan geography).

---

### Tier B — Standard entry

**Criteria:**
- Outcome is clear: free government network exists, or paid only, or volunteer
  only.
- One or two constraints worth naming (VRS-only, registration step, non-standard
  port, session cap, CI timeout, EarthScope overlap).
- No exotic legal/political explanation needed — the situation is typical for
  the region.
- Country is large enough that the entry carries independent value.

**Examples:** AT (eAMA credential constraint), DE (per-state registration),
AU (AUSCORS free, state VRS paid), BR (5-station limit), UY (Spanish portal),
MT (single volunteer base, no government NTRIP), LU (two lines — correct).

---

### Tier C — Stub entry

**Criteria:**
- No confirmed free public NTRIP exists (government or volunteer).
- No named paid alternative worth surfacing (over cutoff or completely unknown).
- No special political/legal/geographic explanation needed beyond "no public
  endpoint found" or "station spacing too wide for RTK."
- Entry exists to record that the country was investigated and ruled out.

**Examples (adequate Tier C):**
- **AL, XK, MD** — "none confirmed / negligible / no free RTK." Three lines.
- **MK** — No confirmed network name, no endpoint, no volunteer. Three lines.
- **BA** — BiHPOS paid, negligible volunteer, networks.md ref. Two lines.

**Current weakness in Tier C Balkan entries (AL, BA, ME, MK, RS, XK):**
Entries that name a paid network (RS: AGROS, ME: MONTEPOS, BA: BiHPOS) lack
pricing — a reader cannot determine if it is affordable or out of scope. These
are structurally Tier C but are missing one required field (see §2).

## 2. Per-tier content checklist

Legend: **R** = required, *N* = nice-to-have, — = not applicable / skip.

| Field | Tier A | Tier B | Tier C |
|---|---|---|---|
| `### CC — Name` heading | **R** | **R** | **R** |
| `**Free government RTK**:` bullet (or explicit "none confirmed") | **R** | **R** | **R** |
| Network name + operator | **R** | **R** | **R** if named |
| `host:port` (if known) | **R** | **R** | *N* |
| Station count (approx.) | **R** | **R** | — |
| Access model: free / registration / conditions / paid | **R** | **R** | *N* |
| Pricing in local currency + USD or EUR equivalent | **R** | **R** | **R** if paid |
| Registration URL or portal name | **R** | *N* | — |
| `→ networks.md: \`id\`` back-reference | **R** | **R** | **R** if entry exists |
| VRS / single-base / physical-coord-vrs note | **R** | **R** | — |
| `**Volunteer**:` bullet (even if "none. Zero XX stations...") | **R** | **R** | **R** |
| "Why" contextual paragraph | **R** | — | — |
| `**Gap**:` summary sentence | **R** | **R** | *N* |
| Paid fallback mention when under $200/yr cutoff | **R** | *N* | — |
| Pipeline status note (deferred / timing-out / candidate) | **R** | **R** | — |
| EarthScope/overlap warning (US entries only) | **R** | **R** | — |

**Notes:** Pricing = local currency first, then USD/EUR in parentheses (most
common gap). Volunteer bullet = always explicit even when zero. Gap sentence =
Tier C may omit unless a practical workaround exists (e.g., MO: SatRef HK).

## 3. When the "why" paragraph is required vs. overkill

A "why" paragraph explains the systemic reason the access model is what it is,
beyond "the agency decided so." It is required when at least one of the
following is true:

1. **Changes what a hobbyist should do.** RU post-2022: sanctions suspended
   Western services; the paragraph redirects hobbyists to deploying a local
   base rather than subscribing to RTKNet (~$333/yr but unreliable internationally).

2. **Transfers across borders.** CN's 测量法 closes all government CORS to
   unlicensed individuals — knowing this explains why HK (SatRef) is unaffected
   while mainland commercial services are the only viable path.

3. **Predicts near-term change (or its absence).** MM's coup context signals
   no public endpoint is coming soon under military governance — do not wait.

4. **The absence is structural, not a policy gap.** NE: Saharan geography +
   infrastructure constraints make a physical RTK network structurally hard;
   it is not a bureaucratic delay.

**When to omit:** routine absence (AL, MK, KE, TR); standard paid pricing with
no political overlay (GR, NO, SI); small country fully described in one bullet
(LU, CY, MT).

**Rule of thumb:** if you cannot complete "a hobbyist reads this and therefore
_does X differently_", the paragraph is overkill. Cut it.

## 4. `date_added` field — format, location, granularity

### Proposed format

```
**date_added**: 2026-04-29
```

This follows the exact bold-key pattern used by `**yearly_cost**:` in
`docs/networks.md` — greppable with `grep "date_added"` and parseable
without a schema change. ISO 8601 date (YYYY-MM-DD), no time component.

### Where it lives

**Required: `docs/country-survey.md`**, one `**date_added**:` per country
heading (`### CC — Country Name`), placed on the line immediately under the
heading, before any prose.

**Optional/additional: `docs/networks.md`**, one `**date_added**:` per `## id`
block, placed after `**status**:`. Use this when an individual network entry
is added or substantially revised on a different date than the country entry
itself. When the country and its sole network are added in the same pass,
the country-level date is sufficient.

### Granularity

- Country-level (required): per `### CC — Country Name` heading. Records when
  the country survey entry was added or last substantively rewritten. A small
  fix (typo, link refresh) does not warrant bumping the date.
- Network-level (optional): per `## id` block in networks.md, when network-level
  precision is useful (e.g. country has multiple networks added at different
  times, or a network is revised independently of the country prose).
- Retroactive backfill: use `pre-2026-04-01` only when git log confirms the
  approximate date; otherwise leave existing entries undated until they are
  next substantively edited.

Both `**yearly_cost**:` and `**date_added**:` are query-time reference fields
in the same bold-key style. A country `date_added` > 18 months old with
`status: deferred` or `candidate` networks is a natural re-verification trigger.

## 5. Templates — one per tier

---

### Tier A template

```markdown
### CC — Country Name

**date_added**: 2026-04-29

- **Context**: [one sentence: the systemic reason the access model is what it is —
  legal framework / sanctions / political event / geography.]

- **Free government RTK**: [Name] ([Operator], `host:port`, N stations,
  single-base | VRS | physical-coord-vrs) — [access terms]. [Optional: access
  deadline, language barrier, credential type.] → networks.md: `id`

  [Additional named networks with same structure, one bullet each.]

- **Commercial** (paid, over $200/yr cutoff / paid-affordable, under cutoff):
  - **Name** (`host:port`): N stations; local_price/period (~$USD/yr | ~€EUR/yr);
    [trial, registration path]. → networks.md: `id`

- **Volunteer**: rtk2go ~N CC bases, Centipede ~N CC nodes. [One sentence on
  distribution / significance.]

- **Gap**: [One sentence: what a hobbyist actually gets and what they must do
  instead or additionally.]
```

---

### Tier B template

```markdown
### CC — Country Name

**date_added**: 2026-04-29

- **Free government RTK**: [Name] ([Operator], `host:port`, N stations,
  VRS | single-base) — [access terms, e.g., free, web registration].
  → networks.md: `id`
- **Volunteer**: rtk2go ~N CC bases, Centipede ~N CC nodes.
- **Gap**: [one sentence on the main friction or practical limitation].
```

For paid-only:

```markdown
### CC — Country Name

**date_added**: 2026-04-29

- **Free government RTK**: none. [Name] ([Operator]) local_price/period
  (~$USD/yr) — [over / under] $200/yr cutoff. → networks.md: `id`
- **Volunteer**: rtk2go ~N CC bases, Centipede ~N CC nodes. [One line.]
- **Paid only**: [restate the option and price for skimmability.]
```

---

### Tier C template

```markdown
### CC — Country Name

**date_added**: 2026-04-29

- **Free government RTK**: none confirmed. [One sentence: what agency was
  checked, what was found. Omit if truly nothing found.]
- **Volunteer**: none. Zero CC stations on rtk2go or Centipede.
```

If a named paid network exists at any price:

```markdown
### CC — Country Name

**date_added**: 2026-04-29

- **Free government RTK**: [Name] — paid; local_price/period (~$USD/yr).
  → networks.md: `id`
- **Volunteer**: negligible.
```

Omit Gap sentence unless a practical workaround exists.

## 6. Common omissions

These are gaps found by auditing the current `docs/country-survey.md` entries:

**1. Pricing absent for named paid networks (most prevalent gap).**
Affected entries: RS (AGROS), ME (MONTEPOS), BA (BiHPOS), TR (TUSAGA-Aktif),
CZ (CZEPOS commercial tier), SK (SKPOS commercial tier), TW (e-GNSS pay-per-use).
Fix: add local currency price + USD/EUR equivalent, or write "not publicly
listed (contact [agency])" — but do not silently omit. The `**yearly_cost**:`
field in networks.md is the authoritative source; copy it into the survey entry.

**2. `host:port` missing for in-pipeline or known-endpoint networks.**
Even when `→ networks.md: \`id\`` is present, the host:port in the survey entry
lets a reader understand the network without switching files. Required for Tier A
and Tier B.

**3. Volunteer bullet omitted entirely (ambiguous with "not checked").**
Several Middle East and Central Africa entries omit the Volunteer bullet.
The zero-confirmation form is required: "**Volunteer**: none. Zero XX stations
on rtk2go or Centipede."

**4. USD/EUR equivalent missing or stale.**
GR (HEPOS €160/3 months) should state the annualised cost and USD equivalent.
Exchange rates drift; note the implicit rate in a comment when precision matters.

**5. networks.md back-reference missing for deferred entries.**
LitPOS (LT), ZAKPOS (UA), Thailand DOL (TH) have no `→ networks.md: \`id\``
reference, breaking the audit grep `grep "networks.md:" docs/country-survey.md`.

**6. Registration URL omitted when it is the primary action.**
REGNA-ROU (UY) correctly includes `rtk.igm.gub.uy/SBC/Account/Register`.
ASG-EUPOS (PL) and AUSCORS (AU) omit a direct signup URL. Tier A requires it;
Tier B should include it when the URL is the hobbyist's immediate next step.

**7. Pipeline status not surfaced for deferred/timing-out entries.**
FLEPOS, WALCORS, ESTPOS, LatPos, KSA-CORS time out in CI — survey entries
should note this so the grey VRS circle is not mistaken for a data gap.

**8. VRS / single-base type omitted.**
State counts without type leave a reader unable to predict whether map pins
or a VRS circle appear. Add "(VRS)" or "(single-base)" after station count.
