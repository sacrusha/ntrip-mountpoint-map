---
name: ntrip-research-batch
description: >
  [BLOCK: trigger description — should this auto-trigger on batch refresh language, or be manual-only via `/ntrip-research-batch`?
   Draft: "Orchestrate batch refresh of `docs/ntrip_research/` entries. Pre-research → research → 3 reviews (parallel) → reconcile. Use when refreshing multiple country/region files at once."]
---

Orchestrate batch refresh of `docs/ntrip_research/` files.

Pipeline per batch:

```
pre-research (sonnet) → research (opus) → 3 reviews (sonnet, parallel) → reconcile (opus)
```

[BLOCK: URL-verification reviewer "D" was added ad-hoc in the 2026-05-18 US batch and caught issues A/B/C missed (broken landing/access URLs, hallucinated citations). Promote to standard 4th reviewer? Or invoke conditionally when prior agent runs are suspect?]

[BLOCK: 2026-05-18 user override — reconcile receives **raw review reports** rather than orchestrator pre-distilled fix list. Make raw-reports the default in this skill, or keep pre-distill as default and raw-reports as override?]

## Stages

- **pre-research** — sources sweep, output-only URL list per file, half-sentences describe page genre only ("operator pricing page", "regulatory tariff PDF"), no findings. Keeps research focused.
- **research** — opus researches per the `ntrip-research` subagent (`.claude/agents/ntrip-research.md`).
- **reviews (3 parallel)**:
  - A spec — required-fields, primer rules, no out-of-scope content. Haiku or Sonnet.
  - B factual — spot-verify 1–2 high-value claims per file via direct fetch. Sonnet.
  - C completeness — gaps not visible to A/B. Sonnet.
- **reconcile** — opus validates combined review findings, then fix-or-reject. Can't validate either way → escalate to caller.

Every agent run ends with an agent self-review-and-fix step.

## Batch sizing

Larger batches might work fine. Optimization: batch files by region / culture.

## Scope boundary

Research and reconcile agents edit `docs/ntrip_research/*.md` only. Pipeline edits (`rtk_inventory.md`, `rtk_map.json`, `fetch_stations.py` SOURCES) are a separate task with `.proc.md`-aware agents — they have rules the research agents don't read.

## Output discipline

Output caps on every stage that returns text through context (research, reviews, reconcile) — uncapped output pollutes the orchestrator. Pre-research routes through file (`.tmp/preresearch/<batch>.md`); its return text is acknowledgment only, so its own output is uncapped.

[BLOCK: 2026-05-18 user finding — `≤400 words` reconcile cap was designed for pre-distilled-bullets input and caused triage failure with raw-reports input (5 valid flags silently dropped). Resolve: (a) keep 400-word cap but drop it when raw-reports mode active; (b) bump unconditionally to e.g. 900 words; (c) per-file cap rather than per-batch; (d) leave to caller.]

## CLAUDE.md cross-references

- "Never invent subagent constraints (how to do the task, what tools to use, how to format the output). When creating a task based on caller's request, be as literal as you can be without sabotaging the task." Stage prompts below are the inherited baseline; do not narrow them with added priority hints, tool prescriptions, methodology steps, or invented word caps.
- "Never run an agent if user intent is unknown or ambiguous, always ask for clarification first."

## Stage prompt templates

[BLOCK: keep templates inlined here, or split each to `.claude/skills/ntrip-research-batch/templates/<stage>.md` and load by reference? Inlining keeps single source of truth; splitting allows per-stage iteration without rewriting whole skill.]

### pre-research

````
Pre-research sources sweep for <N> NTRIP research files. Write to file, no findings in agent reply.

Files:
- docs/ntrip_research/<CC_X>.md
- ...

Per docs/research_task.txt + docs/research_task.primer.txt + CLAUDE.md.

Scope: find reachable relevant sources for research-task fields. Write URL + half-sentence describing **only the page genre** — what KIND of page it is, not what data it contains. Correct: "operator pricing/registration page", "regulatory tariff PDF", "third-party caster directory", "national survey agency overview". WRONG (content leakage): "23-station deployment profile", "lists 7 cities with stations", "$40/mo + 111 stations".

Write to .tmp/preresearch/<batch_id>.md, format per file:
```
## CC_Name
- <url> — <genre only>
```

Agent reply: file path + per-file URL count only. No URLs, no genres, no findings in the reply.

When done, re-read your file; if any half-sentence contains numbers, station counts, prices, or other specific findings, rewrite to pure page-genre.
````

### research

[BLOCK: if dispatched as `ntrip-research` subagent invocation, template is mostly irrelevant — orchestrator names entries + URL list, agent handles the rest. Decide: subagent dispatch (preferred per migration), or inline template fallback?]

````
Delegate to ntrip-research subagent per entry.

Entries:
- docs/ntrip_research/<CC_X>.md
- ...

URL list: .tmp/preresearch/<batch_id>.md — reachable starting points, not a ceiling.

When done, self review whether you truly followed research_task, fix when not.
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
Factual probe of <N> NTRIP research files. Spot-verify 1-3 high-value new/modified claims per file via direct fetch. Read-only.
Research spec + context: docs/research_task.txt + docs/research_task.primer.txt

Files: [list]

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

Research rules and context: docs/research_task.txt + docs/research_task.primer.txt

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

Per docs/research_task.txt + docs/research_task.primer.txt.
````

(Minimal prompt per CLAUDE.md "be as literal as you can be" rule; do not bloat with output format, tool prescriptions, methodology steps, or word caps.)

### reconcile

[BLOCK: input mode — pre-distilled fix list vs raw reports. See top-of-file BLOCK.]

````
Apply review fixes to <N> NTRIP research files.

Files:
- docs/ntrip_research/<CC_X>.md
- ...

Per docs/research_task.txt + docs/research_task.primer.txt + CLAUDE.md.

Scope: edits to docs/ntrip_research/*.md only. Do NOT edit rtk_inventory.md, rtk_map.json, fetch_stations.py.

[Either pre-distilled fix list under "### Fixes" headers, OR raw review reports concatenated verbatim, per caller mode.]

For each flag: validate by re-research if not already validated. Validated → apply. Invalidated → reject with one-line reason. Unvalidatable (sources disagree, no authoritative tie-break) → escalate in reply, don't edit.

Output per file:
```
## CC_Name
applied: <what>
rejected: <flag + why> (omit if none)
escalated: <flag + why> (omit if none)
```

[BLOCK: word cap — see top-of-file BLOCK. 400 words is original batch.md value; insufficient for raw-reports input.]

When done, for each applied edit confirm validation source; for each rejected flag confirm rejection cites a primer rule; confirm escalations are explicit, not silently dropped.
````
