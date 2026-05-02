# RTK survey pipeline

How a finding flows through the four files of the RTK survey.

```
docs/country-survey.md      ← LEAD: per-country prose, completeness picture
        ↓ distil (substantial operators only)
docs/networks.md            ← refined operator catalogue, per-network blocks
        ↓ surface (parallel, sibling consumers)
data/country_markers.json   user-facing markers
scripts/fetch_stations.py   ingestion of free endpoints
```

## Direction of work

New facts enter at the survey first. The survey is the only file that records
what was investigated and what wasn't found — it carries the negatives.

A `networks.md` block exists only when the operator is **substantial**:
nationwide, regional cadastre, or recognised commercial operator. Small
private surveyors stay in country prose.

A `country_markers.json` marker exists only when the marker tier rules apply
(see `country-markers.md`). Misplaced markers are worse than missing ones.

A `fetch_stations.py` SOURCES entry exists only when `networks.md` shows a
free / candidate endpoint that resolves and supplies physical mountpoints.

## The flow narrows

A country may have survey prose with no networks block. A block may have no
marker. A block may have no SOURCES entry. **Don't invent content just to
populate the next file** — empty space downstream is a feature, not a gap.

## Direction of repair

Fix from upstream. A status mismatch in `networks.md` invalidates the marker
downstream; a mislabelled access in country prose creates a wrong marker
tier. Settle the question at the highest source in the chain, then sweep
downstream. **Don't patch a leaf without fixing the source.**

## Per-file rules

- `.claude/process/country-survey.md`
- `.claude/process/networks.md`
- `.claude/process/country-markers.md`
- `.claude/process/fetch-stations.md`
