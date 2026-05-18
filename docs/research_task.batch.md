## Research orchestration (when refreshing ntrip_research/ at scale)

Run as batches, ideal file count not established, works with 50kB per batch; each batch goes through four stages.from draft

```
pre-research (sonnet) → research (opus) → 3 reviews (sonnet, parallel) → reconcile (opus)
```

### Stages

- **pre-research** — sources sweep, output-only URL list per file, half-sentences describe page genre only ("operator pricing page", "regulatory tariff PDF"), no findings. Keeps research focused.
- **research** — opus researches per research_task.txt
- **reviews (3 parallel)**:
  - A spec — required-fields, primer rules, no out-of-scope content. Haiku or Sonnet
  - B factual — spot-verify 1–2 high-value claims per file via direct fetch. Sonnet
  - C completeness — gaps not visible to A/B. Sonnet
- **reconcile** — opus tries to validate combined review findings, then fix-or-reject. Can't validate either way -> escalate to caller. 

Every agent run ends with an agent self-review-and-fix step.

### Batch sizing

Larger batches might work fine. Optimization: batch files by region / culture.

### Scope boundary

Research and reconcile agents edit `docs/ntrip_research/*.md` only. Pipeline edits (`networks.md`, `country_markers.json`, `fetch_stations.py` SOURCES) are a separate task with `.proc.md`-aware agents — they have rules the research agents don't readre.

### Task examples

Output caps on every stage that returns text through context (research, reviews, reconcile) — uncapped output pollutes the orchestrator. Pre-research routes through file (`.tmp/preresearch/<batch>.md`); its return text is acknowledgment only, so its own output is uncapped.

#### pre-research

```
Pre-research sources sweep for <N> NTRIP research files. Write to file, no findings in agent reply.

Files:
- docs/ntrip_research/<CC_X>.md
- ...

Per docs/research_task.txt + docs/research_task.primer.txt + CLAUDE.md.

Scope: find reachable relevant sources for research-task fields. Write URL + half-sentence describing **only the page genre** — what KIND of page it is, not what data it contains. Correct: "operator pricing/registration page", "regulatory tariff PDF", "third-party caster directory", "national survey agency overview". WRONG (content leakage): "23-station deployment profile", "lists 7 cities with stations", "$40/mo + 111 stations".

Write to .tmp/preresearch/<batch_id>.md, format per file:
\`\`\`
## CC_Name
- <url> — <genre only>
\`\`\`

Agent reply: file path + per-file URL count only. No URLs, no genres, no findings in the reply.

When done, re-read your file; if any half-sentence contains numbers, station counts, prices, or other specific findings, rewrite to pure page-genre.
```

#### research

```
Task in research_task.txt
Fix NTRIP research entries per docs/research_task.txt + docs/research_task.primer.txt; Plan your approach immediately *after* reading both files.

Entries:
- docs/ntrip_research/<CC_X>.md
- ...

URL list: .tmp/preresearch/<batch_id>.md - Reachable starting points, not a ceiling.

When done, self review whether you truly followed research_task, fix when not.
```

#### review A — spec

```
Spec-compliance review of <N> NTRIP research files. Read-only.
Research spec + context: docs/research_task.txt + docs/research_task.primer.txt

Files: [list]

Output per file:
\`\`\`
## CC_Name
verdict: AGREE | FLAG
issues:
  - <dim>: <one-line>
\`\`\`
Omit \`issues:\` if AGREE. ≤500 words.

When done, for each FLAG re-read the rule cited; downgrade if flag is only style preference
```

#### review B — factual

```
Factual probe of <N> NTRIP research files. Spot-verify 1-3 high-value new/modified claims per file via direct fetch. Read-only.
Research spec + context: docs/research_task.txt + docs/research_task.primer.txt

Files: [list]

Output per file:
\`\`\`
## CC_Name
verdict: AGREE | FLAG
probes:
  - <thing>: <result>
flags:
  - <claim>: <evidence>
\`\`\`
Omit \`flags:\` if AGREE. ≤700 words.

When done, for each FLAG assess whether the evidence is clear or ambiguous. If ambiguous look for better sources.
```

#### review C — completeness

```
Completeness review of <N> refreshed NTRIP research files. Gaps not visible to spec/factual reviewers — missed link-follow, copy-paste artefacts, oversimplifications, undocumented overlays. Read-only.

Files: [list]

Research rules and context: docs/research_task.txt + docs/research_task.primer.txt

Don't invent specifics. Phrase uncertain flags as questions or pointers, not declaratives.

Output per file:
\`\`\`
## CC_Name
verdict: AGREE | FLAG
gaps:
  - <what's missing or oversimplified, with evidence>
\`\`\`
Omit \`gaps:\` if AGREE. ≤700 words.

When done, assess your own work against task, fix as necessary.
```

#### reconcile

Orchestrator pre-distills the three review reports into a per-file fix list before invoking — reconcile agent gets actionable bullets, not three reports to re-read.

```
Apply review fixes to <N> NTRIP research files (<clean files, if any> untouched).

Files:
- docs/ntrip_research/<CC_X>.md
- ...

Per docs/research_task.txt + docs/research_task.primer.txt + CLAUDE.md.

Scope: edits to docs/ntrip_research/*.md only. Do NOT edit networks.md, country_markers.json, fetch_stations.py.

### Fixes

**CC_X**:
- <validated flag, with specifics + what to write>
- ...

**CC_Y**:
- ...

For each fix: validate by re-research if not already validated by orchestrator. Validated → apply. Invalidated → reject with one-line reason. Unvalidatable (sources disagree, no authoritative tie-break) → escalate in reply, don't edit.

Output per file:
\`\`\`
## CC_Name
applied: <what>
rejected: <flag + why> (omit if none)
escalated: <flag + why> (omit if none)
\`\`\`
≤400 words.

When done, for each applied edit confirm validation source; for each rejected flag confirm rejection cites a primer rule; confirm escalations are explicit, not silently dropped.
```
