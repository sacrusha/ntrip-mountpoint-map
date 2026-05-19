---
name: haiku-prompts
description: Use when writing a WebFetch prompt or any Claude Haiku prompt — direct API call, Agent(model="haiku"), WebFetch summarization/extraction/classification, or any haiku-class invocation. Patterns to suppress fabrication, force grounding, prevent tool-call loops, structure output, detect silent failure.
---

# Haiku prompts

Goal: write haiku / WebFetch prompts with higher chance of success and lower chance of undetected failure. WebFetch processes fetched content via a haiku-class model.

See `provenance.md` for which patterns are Anthropic-sourced vs author-derived. See `agent-mechanics` skill for how haiku is invoked at the harness level (Agent calls, WebFetch lifecycle).

## Triage

Agentic tool-loop work → switch to sonnet (haiku has a re-call loop bug, #10029).
Haiku for: introspection, summarization, classification, constrained generation, extraction.

## Write the prompt

### Suppress fabrication

- **Scope-only**: `Provide a concise response based only on the content above; do not use general knowledge.`
- **Permit uncertainty**: `If the answer is not in the content, say 'not found' — do not infer.`
- **Required-fields nullable** for extraction: `Any required field not found in source MUST be null; never infer.`
- **WebFetch URL echo**: `Begin response with the URL you summarized in <source-url> tags.`
- **Cap verbatim quote length to force paraphrase**: cap verbatim length in the prompt; outside the cap, no word-for-word reuse.

### Structure

- **Content first, query last** (large quality lift for 20k+ token / multi-document inputs).
- **XML doc delimiters**: `<documents><document index="n">…</document></documents>`.
- **Multi-doc anchor**: `Answer using only document [N]; do not draw on others.`
- **Few-shot examples** in `<example>` / `<examples>` tags.
- **Quote-then-conclude** for document tasks: `Find quotes from <doc>. Place in <quotes>. Then, based on these, <task> in <answer>.`
- **No second-order inference**: `If the answer combines fact A and fact B, state each separately: (1) [A from doc]. (2) [B from doc]. Stop there.`

### Structured output (extraction / classification)

- **Inline schema in prompt**: paste literal schema. `Output JSON array; each element matches: {field: type | null, ...}.`
- **Output-only directive**: `Return only the JSON; no prose wrapper, no explanation.`
- **Empty-result sentinel**: `If <target> not found, return {"error": "not found"}` (or your chosen sentinel).
- **Link quotes to fields** in quote-then-conclude: `<quotes><quote field="X">…</quote></quotes>` — anchors each extracted field to its source span.

## Call

- **`temperature=0`** for extraction / classification / structured output.
- **`max_tokens`** at API level enforces length bound.

## Verify (detect silent failure)

- **`tool_uses > 0`** when tool calls were expected: `if not any(b.type == "tool_use" for b in response.content): treat output as hallucinated.`
- **`stop_reason == "end_turn"`** for clean termination.
- **WebFetch URL echo present** — parse `<source-url>` from response; absent → fetch likely failed silently.

## Tool-call loop mitigation (#10029)

- In-prompt cap: `If a tool returns the same output twice, stop calling it.`
- Definitive-result framing next turn: `Tool returned X — final result, do not retry, proceed.`
- Code-side: terminate by `stop_reason == "end_turn"`, not by content/success-flag check.
