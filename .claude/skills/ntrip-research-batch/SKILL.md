---
name: ntrip-research-batch
description: >
  [BLOCK: trigger description — should this auto-trigger on batch refresh language, or be manual-only via `/ntrip-research-batch`?
   Draft: "Orchestrate batch refresh of `docs/ntrip_research/` entries. Pre-research → research → 3 reviews (parallel) → reconcile. Use when refreshing multiple country/region files at once."]
---

Orchestrate batch refresh of `docs/ntrip_research/` files.

Pipeline per batch:

```
pre-research (haiku / sonnet) → research (opus) → 3 reviews (sonnet, parallel) → reconcile (opus)
```

## Stages

- **pre-research** — sources sweep, output-only URL list per file, half-sentences describe page genre only ("operator pricing page", "regulatory tariff PDF"), no findings. Keeps research focused.
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

### pre-research

````

Pre-research sources sweep for <N> NTRIP research files. Write to file, no findings in agent reply. Research scope in .claude\agents\ntrip-research.md, WebFetch prompt advice in /haiku-prompt skill

Files:
- docs/ntrip_research/<CC_X>.md
- ...

Scope: find reachable relevant sources for research-task fields. Write URL + half-sentence describing **only the page genre** — what KIND of page it is, not what data it contains. Correct: "operator pricing/registration page", "regulatory tariff PDF", "third-party caster directory", "national survey agency overview". WRONG (content leakage): "23-station deployment profile", "lists 7 cities with stations", "$40/mo + 111 stations".

Write to .tmp/preresearch/<batch_id>.md, format per file:
```
## CC_Name
- <url> — <description, half sentence>
```
Agent reply: file path + per-file URL count only. No URLs, no genres, no findings in the reply.

````

### research

````
Delegate to ntrip-research subagent 

Entries:
- docs/ntrip_research/<CC_X>.md
- ...

URL list: .tmp/preresearch/<batch_id>.md — reachable starting points, not a ceiling.

````

### review A — spec

````
Spec-compliance review of <N> NTRIP research files. Read-only.
Research spec + context: docs/research_task.txt + docs/research_task.primer.txt

Files: [list]

Output per file:
```
## CC_Name
verdict: AGREE | FLAG
issues:
  - <dim>: <one-line>
```
Omit `issues:` if AGREE. ≤500 words.

When done, for each FLAG re-read the rule cited; downgrade if flag is only style preference.
````

### review B — factual

````
Factual probe of <N> NTRIP research files. Verify sources of new/changed claims compared to git. Read-only.

Files: [list]

Research rules and context: .claude\agents\ntrip-research.md + docs/research_task.primer.txt

Output per file:
```
## CC_Name
verdict: AGREE | FLAG
probes:
  - <thing>: <result>
flags:
  - <claim>: <evidence>
```
Omit `flags:` if AGREE. ≤700 words.

When done, for each FLAG assess whether the evidence is clear or ambiguous. If ambiguous look for better sources.
````

### review C — completeness

````
Completeness review of <N> refreshed NTRIP research files. Gaps not visible to spec/factual reviewers — missed link-follow, copy-paste artefacts, oversimplifications, undocumented overlays. Read-only.

Files: [list]

Research rules and context: .claude\agents\ntrip-research.md + docs/research_task.primer.txt

Don't invent specifics. Phrase uncertain flags as questions or pointers, not declaratives.

Output per file:
```
## CC_Name
verdict: AGREE | FLAG
gaps:
  - <what's missing or oversimplified, with evidence>
```
Omit `gaps:` if AGREE. ≤700 words.

When done, assess your own work against task, fix as necessary.
````

### review D — URL verification

[BLOCK: include as standard, or only on caller demand? See top-of-file BLOCK on 4-reviewer promotion.]

````
URL verification of <N> NTRIP research files. Read-only.

Files: [list]

Verify URLs work and pages match what the file claims.

Per .claude\agents\ntrip-research.md + docs/research_task.primer.txt.
````

(Minimal prompt per CLAUDE.md "be as literal as you can be" rule; do not bloat with output format, tool prescriptions, methodology steps, or word caps.)

### reconcile

````
Apply review fixes to <N> NTRIP research files.

Files:
- docs/ntrip_research/<CC_X>.md
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

When done, for each applied edit confirm validation source; for each rejected flag confirm rejection cites a primer rule; confirm escalations are explicit, not silently dropped.
````
