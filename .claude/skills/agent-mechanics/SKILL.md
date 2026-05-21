---
name: agent-mechanics
description: How Claude Code agents work end-to-end — definition file + frontmatter, spawn-time controls (Agent tool params, worktree isolation, model override), context inheritance, tool gating, subagent lifecycle hooks, worktree mechanics, persistence, hot-reload semantics. Use when designing or debugging subagents, composing Agent tool calls, interpreting subagent errors, planning what context a subagent sees, or customizing per-subagent state.
---

# Agent mechanics

Lifecycle-organized knowledge of Claude Code subagents. Trust tiers, marked inline (default = K):

- **K** = probed (ground-truth, not "docs claim").
- **L** = likely (docs / community, unprobed).
- **?** = untested or single-source.

## Trust order when interpreting probes

`<usage>` block > probe-call return > sonnet self-report > Haiku self-report. Haiku fabricates at `tool_uses=0`; sonnet paraphrases past ~few tokens.

## Files

- **composition.md** — what subagent SEES + DOES: prompt layers, propagation, token-cost buckets, tool-surface gating, operator unreliability.
- **control.md** — how you CONTROL from outside: definition file, frontmatter table, Agent tool params, main-session `--agent` mode, worktree mechanics, persistence, hooks, session-start order, hot-reload.
- **probes.md** — verification scaffolds, anti-patterns, open questions.

## When designing a new agent

Walk these questions in order. Each links into the relevant section.

1. **Scope** — project (`.claude/agents/`) or user (`~/.claude/agents/`)? Plugin agents lose `hooks`/`mcpServers`/`permissionMode`. See control.md "Location".
2. **Required minimum** — only `name` + `description` required. Description quality drives auto-delegation. See control.md frontmatter table.
3. **Model** — defaults to `inherit`. Set `haiku` for cheap narrow work, `sonnet`/`opus` for reasoning, `inherit` to follow parent.
4. **Tool surface** — `tools:` allowlist OR `disallowedTools:` subtracts from inherited pool. Neither can widen beyond what the parent has. Narrowing is the cheapest token-cost knob. See composition.md "Token cost".
5. **Body** — verbatim into the prompt. Every kB costs every spawn. Default empty.
6. **Isolation** — worktree only if subagent edits or needs custom CLAUDE.md. See control.md "Subagent isolation: decision tree".
7. **Skills preload** — `skills: [name, ...]` injects full skill bodies. Powerful but expensive. See composition.md prompt layers #5 vs #5a.
8. **Persistence** — does state need to survive this call? `memory:` field, file writes, or orchestration via parent. See control.md "Persistence".
9. **Hooks** — frontmatter `hooks:` for agent-scoped lifecycle hooks. `Stop` auto-converts to `SubagentStop` when invoked as subagent.

## Headline facts (most actionable)

- Frontmatter required: `name` + `description`. `model` defaults to `inherit`.
- Subagents inherit CLAUDE.md + gitStatus + userEmail. Explore + Plan strip CLAUDE.md + gitStatus (still get userEmail). Per-agent CLAUDE.md swap requires a worktree (see control.md "Recipe").
- `tools:` / `disallowedTools:` match exact tool names. Arg-glob syntax (`Bash(*)`) has no runtime meaning here; use `settings.json permissions` for arg gating.
- MCP cloud tools propagate; the `Agent` tool does NOT — subagents cannot spawn nested subagents.
- Hook exit codes: **exit 2 blocks, exit 1 only prints stderr**. The most common security-gate footgun.
- `Agent(..., isolation: "worktree")` spawns SUBAGENT in worktree; `EnterWorktree` switches MAIN session. Same hooks and `baseRef` apply to both.
- `.worktreeinclude` (gitignore syntax) copies gitignored files (e.g. hook scripts, `.env`) into new worktrees. A custom `WorktreeCreate` hook bypasses it.
- Agent definitions on-disk: not hot-loaded — restart to pick up. The `/agents` panel applies immediately.
- Main-session prompt rules + Environment block don't propagate. Subagent rules must live in agent body (reaches all agents) or CLAUDE.md (skipped by Explore + Plan).
- Experimental env-flag features (set in `settings.json` `"env":`): `CLAUDE_CODE_FORK_SUBAGENT=1` auto-backgrounds every spawn and enables `/fork`; `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` loads `SendMessage`/`TeamCreate`/`TeamDelete` so subagents can be resumed with full prior context. See control.md "Experimental flags".
