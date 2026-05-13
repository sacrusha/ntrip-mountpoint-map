# RTK survey pipeline

How a finding flows through the RTK survey files.

```
docs/research_task.txt          ← prompt template; research is run externally
        ↓ produces (out-of-band, web-enabled environment)
docs/ntrip_research/CC_*.md     ← per-country primary research, citation-grade
        ↓ distil
docs/networks.md                ← refined operator catalogue, per-network blocks
        ↓ surface (parallel, sibling consumers)
data/country_markers.json       user-facing markers
scripts/fetch_stations.py       ingestion of free endpoints
```

## Research stage (upstream, external)

`docs/ntrip_research/` is the raw research layer. Entries are produced by
running `docs/research_task.txt` in an environment with broad web
access. Treat `ntrip_research/` files as inbound
material to be **distilled**, not authored.

## Direction of work

For pipeline-side edits, new facts enter at the survey first (distilled from
`ntrip_research/` when present). The survey is the file that records what was
investigated and what wasn't found — it carries the negatives.

A `networks.md` block exists only when the operator is **substantial**:
nationwide, regional cadastre, or a recognised commercial operator relevant
to users described in target-users.md. 

A `country_markers.json` marker exists only when the marker tier rules apply
(see `../data/country_markers.proc.md`). Misplaced markers are worse than
missing ones.

A `fetch_stations.py` SOURCES entry exists only when `networks.md` shows a
free / candidate endpoint that lists a host:port and supplies physical
mountpoints. Sweep SOURCES whenever a block's `status:` changes — see
`../scripts/fetch_stations.proc.md` for the status→action table.

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

Each target file has a co-located `.proc.md` sidecar:

- `networks.proc.md` (same dir)
- `../data/country_markers.proc.md`
- `../scripts/fetch_stations.proc.md`

## Edit discipline

**Refactoring is always in scope for pipeline edits.** Pipeline integrity is the
primary goal, and pipeline integrity routinely requires touching
neighbouring fields, moving mis-placed content, and cleaning up convention
drift. Patching the single field you came for and ignoring the rest is a
regression, not restraint.

**Consider the entire entry on every edit.** Look at the whole block,
marker, or country prose — not just the field you arrived to update.  If a price update
reveals a stale station count nearby, fix it. If a closing sentence resolves
an `**investigate**:` tag elsewhere in the entry, remove the tag. If a field
contradicts the prose, settle the contradiction.

**Renames are encouraged when a name is misleading and likely an error
source.** Prefer isolated rename commits.
