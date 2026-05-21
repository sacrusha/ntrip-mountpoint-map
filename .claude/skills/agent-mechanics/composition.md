# Composition: what the subagent sees and does

## Prompt composition layers

Order trap-probed for #1-3, #5-8; #4 emoji position (?) inferred from sonnet dumps, untrapped.

1. Base identity: `You are Claude Code, Anthropic's official CLI for Claude.`
2. Agent-specific role text from the agent file body, verbatim.
3. JSON tool-call inline instruction.
4. Emoji rule (?), baseline phrasing (NOT parent's — independent baseline).
5. Skills catalog: every available skill's frontmatter `name` + `description`, body NOT loaded. Catalog loads unconditionally.
5a. Skills preload: full body of every skill named in the agent's `skills:` frontmatter list.
6. CLAUDE.md project memory — every level of the memory hierarchy (`~/.claude/CLAUDE.md`, project rules, `CLAUDE.local.md`, managed policy). NOT Explore, NOT Plan.
7. `userEmail` — every subagent including Explore + Plan.
8. `gitStatus` — same set as #6. Absent when cwd isn't a git repo or `includeGitInstructions: false`.
9. Tool schemas, gated by frontmatter `tools:` / `disallowedTools:`; MCP scope by `mcpServers:`.
10. `additionalContext` from `SessionStart` hook if emitted — injected into Claude's context before the first prompt. 10,000-char cap; overflow saved to file with preview.

## Token cost

**Fixed baseline (cannot strip)**: base identity, JSON tool-call instruction, emoji rule, skills catalog (name + description per skill — scales with installed skills, often dominates), `userEmail`.

**Designer-controlled**: agent body (#2, verbatim), tool schemas (#9 — Bash/Edit large, Read small; narrowing `tools:` is the cheapest knob), `skills:` preload (full body per listed skill), CLAUDE.md (swappable only via worktree, at cost of no prompt-cache reuse), gitStatus (`includeGitInstructions: false` strips session-wide), inline `mcpServers:`.

**Amplifiers**:
- Forks reuse parent's prompt cache; fresh subagents don't. Fork mode (`CLAUDE_CODE_FORK_SUBAGENT=1`, ≥2.1.117): every spawn auto-backgrounds. Explicit `Agent(subagent_type="general-purpose")` tool calls do NOT fork (K — token count at subagent baseline, history absent). Per docs, organic `general-purpose` delegation should substitute to a fork (unconfirmed via this path). `/fork <directive>` is the verified user-driven path.
- Multi-turn subagents: output tokens drive cost after spawn; setup amortizes.

**Minimum custom agent**: empty body, ≤ 3 tools, no `skills:` / `mcpServers:`. Catalog + baseline still load. Absolute minimum: `Explore` / `Plan` (also strip CLAUDE.md + gitStatus, fixed identity).

## What does NOT propagate from main session

Main-session persona, security policy, behavioral rules, tone, session guidance, Environment block — all absent in probed subagents. Subagents get a fixed harness baseline. Rules that must reach subagents go in the agent body (reaches all) or CLAUDE.md (skipped by Explore + Plan).

## Tool propagation

MCP cloud tools (`mcp__claude_ai_*`) propagate. Other tool propagation is per-tool, per-subagent-type — probe to verify. Observed L: `ShareOnboardingGuide` propagates; `ScheduleWakeup`/`AskUserQuestion`/deferred tools (`CronCreate`, `TaskCreate`, `Agent`) do not.

Naming: the delegation tool was renamed `Task` → `Agent` in 2.1.63. `Task(...)` references still alias. `TaskCreate` is the unrelated task-list tool.

## Read-only / context-isolated agents

Explore + Plan strip CLAUDE.md and gitStatus (hardcoded by name; no frontmatter exposes this). For a custom stripped-CLAUDE.md agent, use the worktree recipe (control.md).

## Tool surface

- **Schema strip**: frontmatter `tools:` decides which schemas reach subagent at init. Whole-tool exclusion at schema-load. No "permission denied" path in subagents (no UI to prompt).
- **Error strings vary** across agent-definition styles but map to the same schema-strip mechanism. Treat as schema-absent, not as parseable strings.
- **Match is exact and case-sensitive**: `Bash` ≠ `bash`. Unknown names = no-op. Comma list and YAML inline-list (`[Bash, Edit]`) both parse.
- **Arg-globs (`Bash(*)`) don't gate arg patterns**: ignored in `tools:`; strip the whole base tool in `disallowedTools:`. For arg gating use `settings.json permissions.allow/deny`.
- **Settings allow does NOT re-expose stripped tools**: allow grants permission to existing schemas; strip removes the schema entirely.
- **Tool pool restrict-only**: subagent inherits parent's pool. Frontmatter `tools:` and `disallowedTools:` can RESTRICT; only `mcpServers:` can ADD (MCP-only).
- **Deferred pool per-agent narrower than parent's** (L — observed but not probe-quantified).
- `Agent` tool is absent from subagent schemas → no nested subagents. (`tools: Agent(...)` only matters in `claude --agent` main-session mode; see control.md.)

### Allowlist recipes

- **Read-only investigation**: `Read, Glob, Grep`. Smallest non-Explore shape.
- **Read-only + shell**: `Read, Glob, Grep, Bash`. Bash schema is large; add only if needed.
- **Edit refactor**: `Read, Glob, Grep, Edit`. Add `Write` only if creating new files.
- **Multi-file write**: `Read, Glob, Grep, Edit, Write`.
- **Web research**: `Read, Write, WebSearch, WebFetch`.

### Choosing `tools:` vs `disallowedTools:`

- `tools:` — explicit small surface, fails closed. Use when you want a tight, named set.
- `disallowedTools:` — subtracts named tools from whatever was inherited. Use when you want "parent's pool minus a few." Cannot widen the pool.
- If both set, tool in both = removed.

## Operator unreliability

**Haiku** is prompt-dependent. Fabricates when asked to call tools and report results (`tool_uses=0` + invented output). Introspects own context coherently when told NOT to call tools. Discriminator: ask for an enumeration that requires zero tool calls — fabrication if it narrates tool "outputs" anyway.

**Sonnet** executes tools reliably. Self-enumeration is incomplete (probe-call success doesn't guarantee a tool appears in the listing). Self-reports paraphrase past ~few tokens.

Trust rule: read `<usage>`; if `tool_uses=0` and outputs reported, hallucinated.

## Prompting haiku

For haiku prompt-writing patterns (suppress fabrication, structure, structured output, verify silent failure, #10029 mitigation), see the `haiku-prompts` skill. Scope here is limited to how haiku surfaces in agent mechanics — under `Operator unreliability` above.
