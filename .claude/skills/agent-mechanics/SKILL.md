---
name: agent-mechanics
description: How Claude Code agents work end-to-end — definition file + frontmatter, spawn-time controls (Agent tool params, worktree isolation, model override), context inheritance, tool gating, subagent lifecycle hooks, worktree mechanics, persistence, hot-reload semantics. Use when designing or debugging subagents, composing Agent tool calls, interpreting subagent errors, planning what context a subagent sees, or customizing per-subagent state.
---

# Agent mechanics

Lifecycle-organized knowledge of Claude Code subagents. Three trust tiers, marked inline:

- **K** = Known. Verified by probe; `tool_uses > 0` ground-truthed. Default — items without an inline marker are K. NOT a synonym for "stated in docs" — probe required.
- **L** = Likely. Docs + community consensus, not probed here. Marked inline.
- **?** = Unknown. Untested or single-source. Marked inline.

## Lifecycle spine

Definition (file) → Spawn (Agent call) → Context inheritance → Execution (tool surface) → Observation (hooks) → Persistence → Cleanup

## Trust order

`<usage>` block > probe-call return > sonnet self-report > Haiku self-report.
Haiku fabricates with `tool_uses=0`; sonnet paraphrases past ~few tokens.

## Files

- **composition.md** — what subagent SEES + DOES: prompt layers, propagation, token-cost buckets, tool-surface gating, operator unreliability.
- **control.md** — how you CONTROL from outside: definition file, frontmatter table, Agent tool params, main-session `--agent` mode, worktree mechanics, persistence, hooks, session-start order, hot-reload.
- **probes.md** — verification scaffolds, anti-patterns, open questions.

## When designing a new agent

Walk these questions in order. Each links into the relevant section.

1. **Scope** — project (`.claude/agents/`) or user (`~/.claude/agents/`)? Plugin agents lose `hooks`/`mcpServers`/`permissionMode`. See control.md "Location".
2. **Required minimum** — only `name` + `description` required. Description quality drives auto-delegation. See control.md frontmatter table.
3. **Model** — defaults to `inherit`. Set `haiku` for cheap narrow work, `sonnet`/`opus` for reasoning, `inherit` to follow parent.
4. **Tool surface** — `tools:` allowlist or `disallowedTools:` denylist. Narrowing the allowlist is the cheapest token-cost knob. See composition.md "Token cost".
5. **Body** — verbatim into the prompt. Every kB costs every spawn. Default empty.
6. **Isolation** — worktree only if subagent edits or needs custom CLAUDE.md. See control.md "Subagent isolation: decision tree".
7. **Skills preload** — `skills: [name, ...]` injects full skill bodies. Powerful but expensive. See composition.md prompt layers #5 vs #5a.
8. **Persistence** — does state need to survive this call? `memory:` field, file writes, or orchestration via parent. See control.md "Persistence".
9. **Hooks** — frontmatter `hooks:` for agent-scoped lifecycle hooks. `Stop` auto-converts to `SubagentStop` when invoked as subagent.

## Headline facts (most actionable)

- Frontmatter required fields: only `name` + `description`. Everything else has documented defaults. `model` defaults to `inherit`.
- Subagents inherit CLAUDE.md + gitStatus except Explore + Plan (both probed, strip both). No frontmatter field overrides this — only the worktree-with-custom-CLAUDE.md path swaps CLAUDE.md per agent (see control.md "Recipe").
- `tools:` is a tool-NAME allowlist. Bash arg-globs are documentation only — real arg gate is `settings.json permissions`.
- MCP cloud tools propagate; the `Agent` tool does NOT — subagents cannot spawn nested subagents.
- Hook exit codes: **exit 2 blocks, exit 1 only prints stderr**. The most common security-gate footgun.
- `Agent(..., isolation: "worktree")` ≠ `EnterWorktree` tool. First spawns SUBAGENT in worktree, second switches MAIN session. Same hooks and `worktree.baseRef` apply to both.
- `.worktreeinclude` (gitignore syntax) copies gitignored files (e.g. local hook scripts, `.env`) into new worktrees. NOT processed when `WorktreeCreate` hook replaces the default git logic.
- Agent definitions on-disk are NOT hot-loaded — restart required. Exception: `/agents` interactive panel takes effect immediately.
- Main session prompt rules + Environment block do NOT propagate to subagents. Rules expected to reach subagents must live in agent body or CLAUDE.md (and CLAUDE.md still misses Explore/Plan).
