---
name: agent-mechanics
description: How Claude Code agents work end-to-end — definition, spawn-time controls (Agent tool params, worktree isolation, model override), context inheritance, tool gating, subagent lifecycle hooks, worktree mechanics, hot-reload semantics. Use when designing or debugging subagents, composing Agent tool calls, interpreting subagent errors, planning what context a subagent sees, or customizing per-subagent state.
---

# Agent mechanics

Lifecycle-organized knowledge of Claude Code subagents. Three tiers, inline in detail files:

- **K** = Known. Verified by probe; `tool_uses > 0` ground-truthed. Default — items without an inline marker are K.
- **L** = Likely. Docs + community consensus, not probed here. Marked inline.
- **?** = Unknown. Untested or single-source. Marked inline.

## Lifecycle spine

Definition (file) → Spawn (Agent call) → Context inheritance → Execution (tool surface) → Observation (hooks) → Cleanup

## Trust order

`<usage>` block > probe-call return > sonnet self-report > Haiku self-report.
Haiku fabricates with `tool_uses=0`; sonnet paraphrases past ~few tokens.

## Files

- **composition.md** — what subagent SEES + DOES: prompt layers, propagation, tool-surface gating, operator unreliability, haiku-prompt patterns.
- **control.md** — how you CONTROL from outside: agent definition, Agent tool params, worktree mechanics, hooks, load order, hot-reload.
- **probes.md** — verification scaffolds, anti-patterns, open questions.

## Headline facts

- Agent definitions load at session start only — no hot-reload.
- Subagents inherit CLAUDE.md + gitStatus except Explore + Plan (both probed, strip both).
- Frontmatter `tools:` is tool-NAME allowlist; arg-glob suffix is documentation. Real arg gate = `settings.json permissions`.
- `Agent(..., isolation: "worktree")` ≠ `EnterWorktree` tool. First spawns SUBAGENT in worktree, second switches MAIN session.
- Worktrees check out tracked files only — gitignored hook scripts break tool calls in worktree subagents.
- Main session prompt rules + Environment block do NOT propagate.
- Subagent prompt size, ordinal: general-purpose > custom-long-body > narrow-allowlist > read-only (Explore/Plan). All subagents are substantially smaller than main session.
