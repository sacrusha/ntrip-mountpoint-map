# Composition: what the subagent sees and does

## Prompt composition layers

Order verified via trap-controlled neighbor-quote probes for #1-3 and #5-8; #4 emoji position inferred from sonnet first-300-char dumps.

1. Base identity: `You are Claude Code, Anthropic's official CLI for Claude.`
2. Agent-specific role text from `.claude/agents/<name>.md` body, verbatim
3. JSON tool-call inline instruction
4. Emoji rule, baseline phrasing (NOT parent's — independent baseline)
5. Skills catalog (names + descriptions, not bodies)
6. CLAUDE.md project memory — NOT Explore, NOT Plan
7. `userEmail` — every subagent including Explore + Plan
8. `gitStatus` — same set as #6
9. Tool schemas, gated by frontmatter `tools:` / `disallowedTools:`; MCP scope by `mcpServers:`

## What does NOT propagate from main session

Main session persona text, security policy, behavioral rules, tone/style elaboration, session-specific guidance, Environment block (model id, OS, cwd, knowledge cutoff) — all measured absent in probed subagents. Subagents receive a fixed harness baseline regardless of what the main session prompt contains. Section labels track the current main-session prompt and shift across Claude Code releases; the mechanism (subagent ≠ main extension) is stable.

Implication: behavioral rules expected to reach subagents must live in the agent definition body or CLAUDE.md (and CLAUDE.md still misses Explore/Plan).

## Tool propagation

MCP cloud tools (`mcp__claude_ai_*`) propagate. Other single-tool propagation is per-tool and per-subagent-type; probe to verify. Observed: `ShareOnboardingGuide` does propagate; `ScheduleWakeup` does not; `AskUserQuestion` does not; deferred tools (`CronCreate`, `TaskCreate`, `Agent`) do not propagate by default.

## Read-only / context-isolated agents

Explore + Plan strip both CLAUDE.md and gitStatus (both probed; Plan with trap controls). Per docs: hardcoded by agent name; not exposed in user-writable frontmatter.

## Tool surface

- **Schema strip**: frontmatter `tools:` decides which schemas reach subagent at init. Whole-tool exclusion at schema-load. No "permission denied" path in subagents (no UI to prompt).
- **Error strings vary** across agent-definition styles but map to the same schema-strip mechanism. Treat as schema-absent, not as parseable strings.
- **Bash arg-globs in frontmatter** are documentation only. Confirmed empirically (out-of-glob `ls`, `whoami`, `git status`, `py -c` all ran in a subagent declaring `Bash(py scripts/*)` etc.) and per docs. Real arg gate: `settings.json permissions.allow/deny`.
- **Settings allow does NOT re-expose stripped tools**: allow grants permission to existing schemas; strip removes the schema entirely.
- **Tool pool restrict-only**: subagent inherits parent's pool. Frontmatter `tools:` and `disallowedTools:` can RESTRICT; only `mcpServers:` can ADD (MCP-only).
- **Deferred pool per-agent narrower than parent's**.
- Subagents typically cannot spawn nested subagents (`Agent` absent from most subagent schemas).

## Operator unreliability

**Haiku** is prompt-dependent: fabricates when asked to MAKE tool calls and report results (`tool_uses=0` with invented "results"); introspects own context coherently when told NOT to call tools. Discriminator: ask for an enumeration that requires zero tool calls — if it narrates tool "outputs" anyway, fabrication.

**Sonnet** executes tools reliably but self-enumeration misses items that probe-calls succeed on; self-reports paraphrase past ~few tokens.

Trust rule: read `<usage>`; if `tool_uses=0` and outputs reported, hallucinated.

## Prompting haiku

For haiku prompt-writing patterns (suppress fabrication, structure, structured output, verify silent failure, #10029 mitigation), see the `haiku-prompts` skill. Scope here is limited to how haiku surfaces in agent mechanics — under `Operator unreliability` above.
