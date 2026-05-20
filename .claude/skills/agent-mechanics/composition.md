# Composition: what the subagent sees and does

## Prompt composition layers

Order verified via trap-controlled neighbor-quote probes for #1-3 and #5-8; #4 emoji position (?) inferred from sonnet first-300-char dumps, not trap-controlled.

1. Base identity: `You are Claude Code, Anthropic's official CLI for Claude.`
2. Agent-specific role text from the agent file body, verbatim. (Filename does NOT need to match `name` — identity comes from frontmatter.)
3. JSON tool-call inline instruction.
4. Emoji rule (?), baseline phrasing (NOT parent's — independent baseline).
5. Skills catalog: every available skill's frontmatter `name` + `description`, body NOT loaded. Catalog loads unconditionally.
5a. Skills preload: full body of any skill named in the agent's `skills:` frontmatter list. Skipped if `skills:` absent or empty.
6. CLAUDE.md project memory — every level of the memory hierarchy (`~/.claude/CLAUDE.md`, project rules, `CLAUDE.local.md`, managed policy). NOT Explore, NOT Plan.
7. `userEmail` — every subagent including Explore + Plan.
8. `gitStatus` — same set as #6. Absent when cwd isn't a git repo or `includeGitInstructions: false`.
9. Tool schemas, gated by frontmatter `tools:` / `disallowedTools:`; MCP scope by `mcpServers:`.
10. `additionalContext` from `SessionStart` hook if emitted (L per docs) — injected into context before first inference.

## Token cost: fixed baseline vs designer-controlled

Setup tokens for a spawned subagent break into three buckets. Quantities not measured here — see probes.md "Token cost baseline" to nail them down for your environment.

**Fixed baseline (cannot strip)**:

- Base identity (layer #1) — small, fixed.
- JSON tool-call instruction (#3) — small, fixed.
- Emoji rule (#4) — small, fixed.
- Skills catalog (#5) — every available skill's name + description. Scales with how many skills are installed user-wide + project-wide. Often the largest fixed item; can dominate a small body.
- `userEmail` (#7) — single line.

**Designer-controlled (significant deltas)**:

- Agent body (#2) — verbatim. Direct token = direct cost.
- Tool schemas (#9) — gated by `tools:` allowlist. Each schema can be hundreds of tokens; Bash and Edit are large, Read smaller. Narrowing the allowlist is the cheapest knob.
- `skills:` preload (#5a) — full skill body per listed skill. Powerful but expensive.
- CLAUDE.md (#6) — via worktree, can replace project CLAUDE.md with a smaller one. Cost of doing so: worktree creation + no prompt-cache reuse with parent.
- gitStatus (#8) — session-wide `includeGitInstructions: false` strips for everyone.
- `mcpServers:` adding inline servers — each adds schemas for that server's tools.

**Amplifiers (multiply, not add)**:

- Forks (per docs) reuse parent prompt cache on first request; spawning fresh subagent does not. Forks are cheaper for tasks that need the same context.
- Multi-turn subagents: per-turn output tokens are the cost driver after spawn, not setup. Setup cost amortizes over turns.

**Designer rule of thumb**: for minimal setup, pick `name` + `description` only, narrow `tools:` to ≤3 items, empty body, no `skills:` preload, no `mcpServers:`. Accept that the catalog + baseline still load. For absolute minimum-of-minimum, use `Explore` or `Plan` built-in (strips CLAUDE.md + gitStatus too) — at the cost of fixed agent identity.

## What does NOT propagate from main session

Main session persona text, security policy, behavioral rules, tone/style elaboration, session-specific guidance, Environment block (model id, OS, cwd, knowledge cutoff) — all measured absent in probed subagents. Subagents receive a fixed harness baseline regardless of what the main session prompt contains. Section labels track the current main-session prompt and shift across Claude Code releases; the mechanism (subagent ≠ main extension) is stable.

Implication: behavioral rules expected to reach subagents must live in the agent definition body or CLAUDE.md (and CLAUDE.md still misses Explore/Plan).

## Tool propagation

MCP cloud tools (`mcp__claude_ai_*`) propagate (L — observed in several spawns, not trap-controlled). Other single-tool propagation is per-tool and per-subagent-type; probe to verify.

Observed (L, undated): `ShareOnboardingGuide` propagates; `ScheduleWakeup` does not; `AskUserQuestion` does not; deferred tools (`CronCreate`, `TaskCreate`, `Agent`) do not propagate by default.

Note: the Task delegation tool was renamed to Agent in Claude Code 2.1.63. `Task(...)` references still work as aliases. `TaskCreate` above is the task-list management tool, NOT the renamed delegation tool — distinct.

## Read-only / context-isolated agents

Explore + Plan strip both CLAUDE.md and gitStatus (both probed; Plan with trap controls). Per docs (L): hardcoded by agent name; no frontmatter field or per-agent setting exposes this. Custom agents that want stripped-CLAUDE.md must use the worktree-with-custom-CLAUDE.md path — see control.md "Recipe: custom CLAUDE.md per agent".

## Tool surface

- **Schema strip**: frontmatter `tools:` decides which schemas reach subagent at init. Whole-tool exclusion at schema-load. No "permission denied" path in subagents (no UI to prompt).
- **Error strings vary** across agent-definition styles but map to the same schema-strip mechanism. Treat as schema-absent, not as parseable strings.
- **Bash arg-globs in frontmatter** are documentation only. Confirmed empirically (out-of-glob `ls`, `whoami`, `git status`, `py -c` all ran in a subagent declaring `Bash(py scripts/*)` etc.) and per docs. Real arg gate: `settings.json permissions.allow/deny`.
- **Settings allow does NOT re-expose stripped tools**: allow grants permission to existing schemas; strip removes the schema entirely.
- **Tool pool restrict-only**: subagent inherits parent's pool. Frontmatter `tools:` and `disallowedTools:` can RESTRICT; only `mcpServers:` can ADD (MCP-only).
- **Deferred pool per-agent narrower than parent's** (L — observed but not probe-quantified).
- Subagents cannot spawn nested subagents. `Agent` is absent from subagent schemas. (See control.md "Spawn-time controls" for the `tools: Agent(...)` allowlist syntax that DOES matter in `claude --agent` main-session mode.)

### Allowlist recipes

Cheapest-to-load tool sets for common subagent shapes:

- **Read-only investigation**: `tools: Read, Glob, Grep`. No mutations possible. Smallest non-Explore custom shape.
- **Read-only + shell**: `tools: Read, Glob, Grep, Bash`. Add Bash for status/checks/scripts. Bash schema is large — only add if needed.
- **Edit-capable refactor**: `tools: Read, Glob, Grep, Edit`. Read for context, Glob/Grep for find, Edit for surgical changes. Add `Write` only if creating new files.
- **Multi-file write**: `tools: Read, Glob, Grep, Edit, Write`. Both modification tools.
- **Web research**: `tools: Read, Write, WebSearch, WebFetch`. Persist findings via Write.

### Allowlist vs denylist choice

- Use `tools:` allowlist when you want a small explicit surface — token-cheap, intent-clear, fails closed.
- Use `disallowedTools:` denylist when starting from "almost everything" and forbidding one or two — e.g. inheriting parent's MCP pool but blocking `Write`/`Edit`. Token-equivalent to allowlist because schema-strip happens either way.
- If both set, `disallowedTools` applies first, then `tools` resolves against the remaining pool. Tool in both = removed.

## Operator unreliability

**Haiku** is prompt-dependent: fabricates when asked to MAKE tool calls and report results (`tool_uses=0` with invented "results"); introspects own context coherently when told NOT to call tools. Discriminator: ask for an enumeration that requires zero tool calls — if it narrates tool "outputs" anyway, fabrication.

**Sonnet** executes tools reliably but self-enumeration misses items that probe-calls succeed on; self-reports paraphrase past ~few tokens.

Trust rule: read `<usage>`; if `tool_uses=0` and outputs reported, hallucinated.

## Prompting haiku

For haiku prompt-writing patterns (suppress fabrication, structure, structured output, verify silent failure, #10029 mitigation), see the `haiku-prompts` skill. Scope here is limited to how haiku surfaces in agent mechanics — under `Operator unreliability` above.
