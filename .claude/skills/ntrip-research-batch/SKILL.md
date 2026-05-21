---
name: ntrip-research-batch
description: Orchestrate batch refresh of `docs/ntrip_research/` entries. research → 3 reviews (parallel) → reconcile. 
---

Orchestrate batch refresh of `docs/ntrip_research/` files.

Pipeline per batch: research (opus) → 3 reviews (sonnet, parallel) → reconcile (opus)

## Stages

- **research** — opus researches per the `ntrip-research` subagent (`.claude/agents/ntrip-research.md`).
- **reviews (3 parallel)**:
  - A spec — Haiku or Sonnet.
  - B factual — Sonnet.
  - C completeness — Sonnet.
- **reconcile** — opus validates combined review findings, then fix-or-reject. Can't validate either way → escalate to caller.

Every agent run ends with an agent self-review-and-fix step.

## Batch sizing

Larger batches might work fine. Optimization: batch files by region / culture.

## Scope boundary

Research and reconcile agents edit `docs/ntrip_research/*.md` only. Pipeline edits (`rtk_inventory.md`, `rtk_map.json`, `fetch_stations.py` SOURCES) are a separate task with `.proc.md`-aware agents — they have rules the research agents don't read.

## Stage prompt templates

### research

Delegate to ntrip-research subagent 

````
Entries:
- docs/ntrip_research/<CC_X>.md
- ...

````

### review A — spec

Create the file in advance.

````
Spec-compliance review of <N> NTRIP research files. Read-only.
Spec: .claude\agents\ntrip-research.md 

Files: [list]

Write review to .tmp file [filename]:
```
## CC_Name
verdict: AGREE | FLAG
issues:
  - <dim>: <one-line>
```

When done, for each FLAG re-read the rule cited; downgrade if flag is only style preference. Default no output, flag if environment prevented complete execution of task. 
````

### review B — factual

Create the file in advance.
````
Factual probe of <N> NTRIP research files. Verify sources of new/changed claims compared to git. Read-only.

Files: [list]

Research rules and context: .claude\agents\ntrip-research.md + docs/research_task.primer.txt

Write review to .tmp file [filename]:
```
## CC_Name
verdict: AGREE | FLAG
probes:
  - <thing>: <result>
flags:
  - <claim>: <evidence>
```
Omit `flags:` if AGREE.

When done, for each FLAG assess whether the evidence is clear or ambiguous. If ambiguous look for better sources. Default no output, flag if environment prevented faithful execution of task. 
````

### review C — completeness

Create the file in advance.
````
Completeness review of <N> refreshed NTRIP research files. Gaps not visible to spec/factual reviewers — missed link-follow, copy-paste artefacts, oversimplifications, undocumented overlays. Read-only.

Files: [list]

Research rules and context: .claude\agents\ntrip-research.md + docs/research_task.primer.txt

Don't invent specifics. Phrase uncertain flags as questions or pointers, not declaratives.

Write review to .tmp file [filename]:
```
## CC_Name
verdict: AGREE | FLAG
gaps:
  - <what's missing or oversimplified, with evidence>
```
Omit `gaps:` if AGREE.

When done, self review & fix. Default no output, flag if environment prevented faithful execution of task. 
````

### reconcile

````
Apply review fixes to <N> NTRIP research files.

Files:
- docs/ntrip_research/<CC_X>.md
- ...
Reviews: 
- ...

Per .claude\agents\ntrip-research.md + docs/research_task.primer.txt

Scope: edits to docs/ntrip_research/*.md only.

For each flag: validate by re-research if not already validated. Validated → apply. Invalidated → reject with one-line reason. Unvalidatable (sources disagree, no authoritative tie-break) → escalate in reply, don't edit.

Output per file:
```
## CC_Name
applied: <what>
rejected: <flag + why> (omit if none)
escalated: <flag + why> (omit if none)
```

When done, self review & fix. Flag if environment prevented faithful execution of task.
````
