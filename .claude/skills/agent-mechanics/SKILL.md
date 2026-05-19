---
name: agent-mechanics
description: How Claude Code agents work end-to-end — definition, spawn-time controls (Agent tool params, worktree isolation, model override), context inheritance, tool gating, subagent lifecycle hooks, worktree mechanics, hot-reload semantics. Use when designing or debugging subagents, composing Agent tool calls, interpreting subagent errors, planning what context a subagent sees, or customizing per-subagent state.
---

# Agent mechanics

Lifecycle-organized knowledge of Claude Code subagents. Three tiers, marked inline in detail files:

- **K** = Known. Verified by probe in this codebase. `tool_uses` > 0 ground-truthed.
- **L** = Likely. Official docs + community consensus, not directly tested.
- **?** = Unknown. Untested, conflicting, or single-source.

## Lifecycle spine

Definition (file) → Spawn (Agent call) → Context inheritance → Execution (tool surface) → Observation (hooks) → Cleanup

Each phase has its own knobs. Agent file is one control point; the Agent tool call itself carries spawn-time knobs that override file defaults.

## Trust order

`<usage>` block > probe-call return > sonnet self-report > Haiku self-report.
Haiku in subagents fabricates with `tool_uses=0`; sonnet paraphrases past ~few tokens.

## Where to look

- **composition.md** — what the subagent SEES + DOES: prompt composition layers, what propagates from main session, word counts, tool schema gating, Bash-glob non-enforcement, deferred tool pool, read-only agent context strip, operator unreliability inside subagents.
- **control.md** — how you CONTROL from outside: agent definition fields, spawn-time Agent tool params (incl `isolation: "worktree"`, `model` override), worktree mechanics (per-subagent CLAUDE.md path, cleanup semantics), hook events (incl WorktreeCreate/Remove), load order at session start, hot-reload semantics.
- **probes.md** — verify any claim: schema visibility, marker probe, ground-truth rule, worktree CLAUDE.md customization probe, hot-reload check, hook fire check, plus anti-patterns and open questions.

## Quick facts

- Agent files: start-only registration, no hot-reload (K)
- Subagents inherit CLAUDE.md + gitStatus EXCEPT Explore + Plan strip both (K — both verified via trap-controlled marker probes); hardcoded by agent name per docs, no user-configurable opt-out (L)
- Frontmatter `tools:` is tool-NAME allowlist only; `Bash(arg-glob)` in frontmatter is documentation, never enforces — arg gating lives in settings.json `permissions.allow/deny` engine (K + L)
- `Agent(..., isolation: "worktree")` spawns subagent in ephemeral repo copy at `.claude/worktrees/agent-<id>/` (K — path observed); CLAUDE.md propagates (K); hooks fire (K). ≠ `EnterWorktree` tool (switches MAIN session into a worktree). Two distinct mechanisms.
- **Worktree gotcha** (K): `git worktree add` checks out tracked files only — hook scripts in gitignored/untracked locations break every tool call in worktree subagents.
- Hook events: ~12 total. PostToolUse/Stop/Notification/PreCompact/PermissionRequest/WorktreeCreate/WorktreeRemove all wireable per docs (L). 7 wired here (SessionStart, InstructionsLoaded, UserPromptSubmit, PreToolUse, SubagentStart, SubagentStop, SessionEnd) — all confirmed firing in `.tmp/hook_log.tsv`. PreToolUse fires inside subagents too. (K)
- `model` on Agent call REPLACES frontmatter `model:` (L per docs + behaviorally consistent). Precedence: env `CLAUDE_CODE_SUBAGENT_MODEL` (session-scoped, highest) > call-site `model` > frontmatter `model:` > main convo model. Haiku subagent behavior is prompt-dependent: it fabricates when asked to invent tool returns, but introspects own context coherently when told NOT to call tools.
- Subagent tool pool: inherited from parent, frontmatter `tools`/`disallowedTools` restrict-only; only `mcpServers` frontmatter can ADD scope (MCP-only) (L)
- MCP cloud tools (`mcp__claude_ai_*`) propagate (K); `ShareOnboardingGuide` propagates (K); `ScheduleWakeup` does NOT (K); `AskUserQuestion` does NOT (K)
- Settings.json `permissions.allow` does NOT re-expose frontmatter-stripped tools (K — derived)
- Main session behavioral rules do NOT propagate to subagents (K)
