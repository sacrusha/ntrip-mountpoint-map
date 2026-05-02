# country-survey.md — process

Per-file rules for `docs/country-survey.md`. Pipeline context:
`.claude/process/pipeline.md`.

## Role

The **completeness picture** — per-country prose: what was investigated, what
was found, what's still gapped. Missing heading = uncovered country. Includes
negatives. Maintainers + hobbyists via GitHub.

UK spelling. Expand acronyms ("CORS" → "permanent GPS reference station").
"GPS" colloquially, "GNSS" structurally.

## File facts

- ~3000 lines, ~40k tokens. **Never read in full.** Grep first.
- Heading format: `### CC — Country Name` (ISO 3166-1 alpha-2).
- `**date_added**:` line directly under each heading.

## Tier shape

Pick the lightest tier that fits — don't pad to the next tier.

- **Tier A** — war / sanctions / legal context materially changes hobbyist
  guidance. Includes a "why" paragraph; otherwise omit the paragraph.
- **Tier B** — one or two named networks. Authority + endpoint, or named gap.
- **Tier C** — likely-nothing-found, or thoroughly-investigated negative. A
  complete "we looked, nothing exists" is a valid Tier C, **not a stub**. The
  axis is presentation, not data volume.

## Conventions

- `**Volunteer**:` canonical form: `**Volunteer**: none. Zero XX stations on
  rtk2go or Centipede.`
- `**missing**:` / `**investigate**:` tags — greppable. When research
  resolves them, remove the tag and replace with a one-sentence closure.
- `**date_added**:` rule: substantive edit → today's date; bulk-only date
  backfill → yesterday's date (so backfills are greppable separately).
- No bare email addresses — link to a website.

## When to update networks.md

Only when the operator is **substantial** (nationwide, regional cadastre,
recognised commercial operator). Small surveyors stay in country prose.
See `.claude/process/networks.md`.

## When to update markers / fetch

Never edit those files from a country-survey edit. Surface the question in
`networks.md`; the marker / fetch sweeps follow from there.
