# Provenance

Per-pattern source verdicts for `SKILL.md`. Categories:

- **SOURCED** — directly stated in cited Anthropic doc.
- **DERIVED** — composed from sourced principles; not directly stated.
- **WORKAROUND** — author/community-tested mitigation; no Anthropic-published fix.
- **PRACTICE** — general API engineering knowledge; not haiku-specific.

URLs in `sources.md`.

## Triage

- Loop bug exists: SOURCED (anthropics/claude-code#10029, closed "not planned").
- Switch to sonnet: DERIVED. Author recommendation; the issue offers no Anthropic-published fix.

## Suppress fabrication

- Scope-only / external-knowledge restriction: SOURCED. Reduce-hallucinations doc: "Explicitly instruct Claude to only use information from provided documents and not its general knowledge."
- Permit uncertainty: SOURCED. Reduce-hallucinations doc: "Allow Claude to say 'I don't know'... 'state No relevant quotes found'."
- Required-fields nullable: DERIVED from scope-only + permit-uncertainty.
- WebFetch URL echo: DERIVED. Extends Anthropic's "verify with citations" principle to URL-as-detector.
- Cap verbatim quote length: DERIVED. The "force compression rather than pass-through" rationale is author-composed. WebFetch's internal prompt uses a 125-char cap as a copyright guardrail; that is a product detail, not the haiku-craft principle.

## Structure

- Content first, query last: SOURCED. Best-practices doc: "Queries at the end can improve response quality by up to 30% in tests, especially with complex, multi-document inputs." Scope is 20k+ token / multi-document inputs.
- XML doc delimiters with `index="n"`: SOURCED. Best-practices doc shows the structure verbatim.
- Multi-doc anchor: DERIVED. Extends external-knowledge restriction + Anthropic's `index="n"` structure.
- Few-shot examples in `<example>` / `<examples>` tags: SOURCED. Best-practices doc.
- Quote-then-conclude two-step: SOURCED. Best-practices doc provides the template verbatim.
- No second-order inference template: DERIVED. The (1)/(2) split template is author-composed.

## Structured output

All DERIVED. Standard structured-extraction patterns composed from sourced principles, not directly in cited sources:

- Inline schema in prompt: field practice for JSON extraction.
- Output-only directive: extends scope-only to output format.
- Empty-result sentinel: extends permit-uncertainty to structured form.
- Link quotes to fields: extends quote-then-conclude with per-field grounding.

## Call

- `temperature=0` for structured tasks: PRACTICE. Standard API knowledge; not in cited sources.
- `max_tokens` at API level: PRACTICE.

## Verify

- `tool_uses > 0` check: WORKAROUND. Derived from this session's empirical observation that haiku narrates plausible tool returns when no tool was actually called (`tool_uses: 0` in `<usage>` block while output describes tool results).
- `stop_reason == "end_turn"` check: PRACTICE. Standard Anthropic API field.
- WebFetch URL echo verification: pairs with the write-side derived URL-echo pattern. WORKAROUND.

## Tool-call loop mitigation (#10029)

All three bullets: WORKAROUND. Issue #10029 confirms the bug and was closed "not planned" with no Anthropic-side mitigation in the thread. The in-prompt cap, definitive-result framing, and code-side stop_reason check are author-proposed workarounds, not source-recommended.

## Audit history

- 2026-05: opus-tier audit on prior SKILL.md draft. Removed as INVENTED: specific numbers (15-word quote cap, 3-5 steps, 120-180/220 token budget, "3-5" few-shot count). Removed as OVERREACH: "constraints in user turn, not system prompt" (contradicts Anthropic guidance for recent models); "reason/consider not think" applied broadly (the source-quoted note is Opus-4.5-specific). Removed as INVENTED on the basis of #10029 only: `tool_choice` warning, `max_tokens` ignored-by-haiku claim.
- 2026-05: sonnet practical-applicability test added Structured output section closing gaps on JSON schema delivery, output isolation, empty-result sentinel, quote→field linking. Cross-skill review removed duplicated/invalidated haiku patterns from `agent-mechanics/composition.md`.
