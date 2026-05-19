# Composition: what the subagent sees and does

## TOC

- Prompt composition layers
- Word counts
- What does NOT propagate from main session
- Read-only / context-isolated agents
- Tool surface (schema strip, error strings, Bash arg-globs, deferred pool)
- Operator unreliability inside subagents

## Prompt composition layers

Presence verified (K). Ordering verified (K) for #1-#3 and #5-#8 via probe-E neighbor-quote tests with control traps. Emoji rule position (#4) is K-presence + L-position (relative spot not directly probed but inferred from sonnet's first-300-char dumps).

1. Base identity: `You are Claude Code, Anthropic's official CLI for Claude.` (every subagent) (K)
2. Agent-specific role text from `.claude/agents/<name>.md` body, verbatim (K)
3. JSON tool-call inline instruction (every subagent) (K)
4. Emoji rule, baseline phrasing `Avoid writing emojis to files unless asked` — NOT parent's phrasing, independent baseline (K presence, L position)
5. Skills catalog: names + descriptions, not bodies (every subagent) (K)
6. CLAUDE.md project memory — general-purpose, claude-code-guide, custom agents. NOT Explore (K), NOT Plan (K, verified by probe). Per docs, hardcoded by agent name (L)
7. `userEmail` block, every subagent including Explore + Plan (K)
8. `gitStatus` block: branch, status, recent commits — same set as #6 (K)
9. Tool schemas, gated by frontmatter `tools:` / `disallowedTools:`; MCP scope by `mcpServers:` (K)

### Specific tools propagation (K, observed in general-purpose)

- `mcp__claude_ai_Gmail__*`, `mcp__claude_ai_Google_Calendar__*`, `mcp__claude_ai_Google_Drive__*` (6 total): PROPAGATE
- `ShareOnboardingGuide`: PROPAGATES
- `Skill`: PROPAGATES (gated by frontmatter)
- `ScheduleWakeup`: does NOT propagate
- `AskUserQuestion` (inline in main session): does NOT propagate
- `CronCreate`, `TaskCreate`, `Agent` (deferred in main): do NOT propagate by default

## Word counts (sonnet self-estimate — ordinal K, absolute L)

Sonnet was asked to estimate total word count of its own system context. Numbers are agent-narration self-reports, not measurements. Direction is trustworthy (monotonic reduction); absolute numbers are approximate.

| Agent | Approx words (sonnet estimate) |
|-------|--------------------------------|
| general-purpose | 4,200 |
| ntrip-research (long body) | 3,800 |
| claude-code-guide | 3,200 |
| Explore | 2,100 |
| Plan | not probed for count |
| main session prompt (reference) | ~7-8k |

## Does NOT propagate from main session (K)

Verified absent in all subagents tested:

- Security policy block
- System bullets (auto-compression note, hooks instructions)
- Doing-tasks elaboration (exploratory rule, no-comments rule, refactor discipline)
- Executing-actions-with-care section (reversibility framework)
- Tone/style beyond emoji baseline
- Text-output section (one-sentence-before-tool-call, end-of-turn cap)
- Session-specific guidance (`!` prefix, `/schedule`, `/ultrareview`)
- Environment block (model id, OS, cwd, knowledge cutoff)

Implication: behavioral rules expected to reach subagents must live in agent definition body OR CLAUDE.md (and CLAUDE.md still misses Explore/Plan). Main session prompt rules do not propagate.

## Read-only / context-isolated agents

Explore strips CLAUDE.md AND gitStatus from its context (K — verified by marker probe).
Plan strips CLAUDE.md AND gitStatus (K — verified by trap-controlled marker probe; all 3 trap markers returned `no`, M1-M5 also `no`).
Special-case behavior, not length-driven — ntrip-research has a long body and still receives both. Mechanism per docs: hardcoded by agent name; not exposed in user-writable frontmatter (L).

## Tool surface

**Schema strip** (K): frontmatter `tools:` controls which tool schemas reach the subagent at init. Whole-tool exclusion happens at schema-load level (not at perm-prompt-time). No "permission denied" path in subagents — no UI to display prompt.

**Three error strings** observed when calling a stripped tool, varying by agent-definition style:

- `Tool "X" does not exist.`
- `Tool X is not available in this subagent.`
- `The X tool is not available for use in this session. You are in READ-ONLY mode...`

All three map to the same mechanism. Don't string-match across agent forms.

**Bash arg-globs in frontmatter** (K empirical + L docs): `Bash(py scripts/*), Bash(curl:*), ...` declarations in agent frontmatter `tools:` field are tool-NAME allowlist only. The arg-glob suffix is documentation, never enforces — confirmed empirically (out-of-glob `ls`, `whoami`, `git status`, `py -c` all ran in ntrip-research subagent) and per docs ("Permission rules are enforced by Claude Code, not by the model"). To actually gate Bash args, put rules in `settings.json` `permissions.allow/deny` or use a PreToolUse hook.

**Settings.json allow does NOT re-expose stripped tools** (K — derived): settings.json has `Edit(./**)` allow rule, yet Edit-stripped Explore agent still returns "Edit tool not available" on call attempt. Schema strip wins over settings allow. Allow rules grant permission to existing schemas; they don't add schemas.

**Tool pool — restrict-only by default** (L per docs): subagent inherits parent's tool set. Frontmatter `tools:` and `disallowedTools:` can RESTRICT from inherited pool; cannot ADD a built-in tool the parent lacks. Only documented widening mechanism is `mcpServers:` frontmatter, which attaches additional MCP servers (and their tools) scoped to the subagent.

**Deferred tool pool per-agent** (K): subagent's deferred catalog is narrower than parent's. Example: parent has `TaskCreate` deferred; subagent `ToolSearch "select:TaskCreate"` returns `No matching deferred tools found`. `select:CronCreate` succeeds in same subagent.

Subagents typically cannot spawn nested subagents (K) — `Agent` tool absent from most subagent schemas.

## Operator unreliability inside subagents

**Haiku** (K) — prompt-dependent:
- Fabricates tool returns when asked to MAKE tool calls and report results. `tool_uses: 0` despite confidently returning invented "results" (e.g. fake cron job IDs, knowledge-cutoff prose passed off as WebSearch result).
- Introspects own context coherently when explicitly told NOT to call tools. Counts tools, lists names, quotes context — usually accurate within sonnet-equivalent tolerance.
- Discriminator: ask for an enumeration that requires zero tool calls. If the agent narrates tool "outputs" anyway, that's fabrication.

**Sonnet** (K): executes tools reliably but its self-enumeration of available tools misses items that probe-calls succeed on. Self-reports of "verbatim" content paraphrase past ~few tokens.

Rule: always read `<usage>`; if `tool_uses=0` and outputs reported, hallucinated. Ground truth via probe-call.

## Prompting haiku subagents

Haiku 4.5 (`claude-haiku-4-5-20251001`) is still the current haiku as of 2026-05. WebFetch is haiku-backed; `Agent(..., model="haiku")` explicitly haiku. Patterns to avoid the fabrication mode:

- **Scope boundary** — tell haiku exactly what to ground on. WebFetch's own prompt uses `Provide a concise response based only on the content above` — load-bearing. Without explicit scope, haiku fills gaps from world knowledge.
- **Quote cap** — force paraphrase by capping verbatim quotes (WebFetch: 125-char max). Forces real processing instead of pass-through with appended fabrication.
- **Minimal system prompt; constraints in user turn** — WebFetch's system is one line; all behavioral rules in user turn. Haiku's instruction-following degrades at depth.
- **Labeled sections** — `[Context] [Policy] [Task] [Output]` or XML/markdown delimiters improve compliance vs prose. Helps prompt-injection resistance too.
- **Explicit token budget** — `Target 120-180 tokens; never exceed 220` stops padding.
- **Step-bounded reasoning** — `think in 3-5 steps` prevents runaway chain-of-thought.
- **No multi-hop in a single sentence** — split to numbered steps. Haiku 4.5 drops implicit second-order inference more than Sonnet/Opus.
- **Permitted uncertainty** — `If the answer is not in the content, say 'not found' — do not infer`. Cuts fabrication.
- **Query at end** — long content first, query last. Anthropic docs report up to 30% quality lift; matters most for small models.
- **Force grounding (quote-then-conclude)** — two-step structure (`Find quotes ... place in <quotes> tags. Then based on these ...`) anchors output in retrieved text before reasoning.
- **Anti-loop in agentic uses** — terminate by `stop_reason == "end_turn"`, NOT content-type check. Forcing tool calls when agent is done causes infinite loop.

For Claude Code `Agent(..., model="haiku")` specifically:

- Frame as introspection or constrained text generation, NOT "call X and report result" unless tool calls are explicitly structured in the prompt with literal calls + verbatim return expectations.
- If tool calls ARE required, list them: `Make these 3 literal calls in order. Quote verbatim returns in backticks.` Otherwise haiku narrates fabricated outputs with `tool_uses=0`.

Sources: Piebald-AI/claude-code-system-prompts (current WebFetch dump, 2026-05-15); Liran Yoffe / Mikhail Shilkov reverse-engineering writeups (Oct 2025, structurally still valid in 2026); Anthropic prompt-engineering docs; anthropics/claude-code issue #10029 (anti-loop). No exact-match SKILL.md found in 2025 or 2026 community catalogs.
