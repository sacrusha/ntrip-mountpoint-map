# Probes, anti-patterns, open questions

## Probes

**Schema visibility**:

    Agent(subagent_type="<type>", model="sonnet",
      prompt="List every tool in your function schema, alphabetical, comma-separated.
              For each of [T1, T2, ...] attempt the literal call and quote the exact return in backticks.")

**Context inheritance (marker probe)**:

    Feed list of exact strings from main session. Ask yes/no presence with 60-char
    window. Add trap markers (strings known absent) — yes on a trap = fabrication.
    Compare across subagent types to find what propagates.

**Spawn-control merge semantics**:

    Agent(subagent_type="<one with model: opus frontmatter>", model="haiku",
      prompt="Diagnostic introspection only — do NOT call tools. List tool count + first 10 alphabetical.")

**Worktree CLAUDE.md customization**:

    1. Create branch with modified CLAUDE.md.
    2. Agent(..., isolation: "worktree") from that branch.
    3. Marker-probe subagent for the modified content.

**Hot-reload check**:

    Write new file under .claude/agents/. Immediately attempt Agent call with that subagent_type.
    "Agent type 'X' not found" = no hot-load, restart required.

**Hook fire check**:

    Trigger the event (e.g. spawn subagent for SubagentStart). Inspect hook log.
    Absence in log = hook did not fire.

## Anti-patterns

- Trusting Haiku subagent narration of tool returns it never made — `tool_uses=0` + reported outputs = fabricated.
- Treating frontmatter `Bash(arg-glob)` as a sandbox — documentation only. Use `settings.json permissions` or PreToolUse hook for real gating.
- Confusing `Agent(isolation: "worktree")` (subagent spawn) with `EnterWorktree` (main session switch).
- Relying on CLAUDE.md to reach all subagents — Explore + Plan strip.
- Writing main-session behavioral rules and expecting subagent inheritance.
- Hot-editing `.claude/agents/` mid-session and expecting pickup.
- Asking subagent for "verbatim" quotes longer than a few tokens — sonnet paraphrases.
- Using `exit 1` in PreToolUse hooks expecting a block (only exit 2 blocks).
- Spawning isolation worktrees while hook scripts are in gitignored paths — `git worktree add` skips untracked, hooks then error and block all tool calls.
- Propagating tool names mentioned in tool returns without verifying own schema enum — Agent return's `SendMessage` hint is SDK-layer leakage.
- Wiring `WorktreeCreate` to a logging-only hook expecting observation semantics — `WorktreeCreate` is REPLACEMENT. The command must return the worktree path; a no-op silently breaks `Agent(isolation: "worktree")` with `WorktreeCreate hook failed: hook succeeded but returned no worktree path`. (`WorktreeRemove` IS observation-only — wiring a logger to it is safe; don't generalize from one to the other.)
- Expecting `settings.json permissions.allow` to re-expose a frontmatter-stripped tool — allow grants permission to existing schemas; strip removes the schema entirely.
- Trying to widen subagent tool pool beyond parent's via frontmatter `tools:` — only `mcpServers:` adds scope (MCP-only).

## Open questions

- Subagent skill auto-trigger reliability — Vercel measured 56% miss in main session; subagent unmeasured.
- `EnterWorktree` tool firing `WorktreeCreate` hook — docs list `--worktree` CLI + Agent isolation; EnterWorktree's relation unstated.
