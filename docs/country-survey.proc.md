# country-survey.md — process

Per-file rules for `docs/country-survey.md`. Pipeline context:
`.claude/process/pipeline.md`.

**Refactoring is in scope; consider the entire entry on every edit.** See
`pipeline.md` §"Edit discipline".

## Role

The **completeness picture** — per-country prose: what was investigated,
what was found, what's still gapped. Missing heading = uncovered country.
Includes negatives. Maintainers + hobbyists via GitHub.

## File facts

- ~3000 lines, ~40k tokens. **Never read in full.** Grep first.
- Heading format: `### CC — Country Name` (ISO 3166-1 alpha-2).
- `**date_added**:` line directly under each heading.

## Tier shape

Pick the lightest tier that fits.

- **Tier A** — sanctions / war / legal context that materially changes
  hobbyist guidance; includes a "why" paragraph.
- **Tier B** — one or two named networks; authority + endpoint, or named gap.
- **Tier C** — thoroughly-investigated negative. "We looked, nothing exists"
  is a valid Tier C. The axis is presentation, not data volume.

## Conventions

- `**date_added**:` rule — substantive edit → today; bulk-only date backfill
  → yesterday (greppable separately).
- Mention zero rtk2go / Centipede coverage somewhere in negatives.
- No bare email addresses — link to a website. **Harassment guard.**

## Downstream

`networks.md` only when the operator is **substantial** (nationwide,
regional cadastre, recognised commercial operator). Small surveyors stay in
country prose. Markers / fetch follow from `networks.md` changes; never
edit those from a country-survey edit.
