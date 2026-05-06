# country-survey.md — process

Per-file rules for `docs/country-survey.md`. Pipeline context:
`pipeline.md` (same dir).

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

### Deriving volunteer caster counts

rtk2go / Centipede counts come from live `data/stations.json`. Replace `XXX`
with the country code as it appears in the data (3-letter ISO 3166-1 alpha-3
for rtk2go; Centipede uses quirks — `ENG`=GB, `CHZ`=CZ, `SER`=RS, `BIH`=BA,
`NLD`/`BEL` separate, etc.). Run from repo root:

```
jq '[.sources.rtk2go.stations[]    | select(.country=="XXX")] | length' data/stations.json
jq '[.sources.centipede.stations[] | select(.country=="XXX")] | length' data/stations.json
```

For the full per-country table (use to scout codes / spot drift):

```
jq -r '.sources.rtk2go.stations[].country'    data/stations.json | sort | uniq -c | sort -rn
jq -r '.sources.centipede.stations[].country' data/stations.json | sort | uniq -c | sort -rn
```

## Downstream

`networks.md` only when the operator is **substantial** (nationwide,
regional cadastre, recognised commercial operator). Small surveyors stay in
country prose. Markers / fetch follow from `networks.md` changes; never
edit those from a country-survey edit. See `networks.proc.md`.
