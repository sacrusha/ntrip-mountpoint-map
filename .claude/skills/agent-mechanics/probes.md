# Probes, anti-patterns, open questions

## TOC

- Probes (copy-paste scaffolds)
- Anti-patterns
- Open questions

## Probes

**Schema visibility**:

    Agent(subagent_type="<type>", model="sonnet",
      prompt="List every tool in your function schema, alphabetical, comma-separated.
              For each of [T1, T2, ...] attempt the literal call and quote the exact return in backticks.")

**Context inheritance (marker probe)**:

    Feed list of exact strings from main session. Ask yes/no presence with 60-char window
    around each match. Compare across subagent types to find what propagates.

**Spawn-control merge semantics**:

    Agent(subagent_type="<one with model: opus frontmatter>", model="haiku",
      prompt="Report your operating model name verbatim from system context if visible.")

**Worktree CLAUDE.md customization**:

    1. Create branch with modified CLAUDE.md.
    2. Agent(..., isolation: "worktree") from that branch.
    3. Marker-probe subagent for the modified content.

**Hot-reload check**:

    Write new file under .claude/agents/. Immediately attempt Agent call with that subagent_type.
    "Agent type 'X' not found" = no hot-load, restart required.

**Hook fire check**:

    Trigger the event (e.g. spawn subagent for SubagentStart). Inspect hook script output.
    Absence in log = hook did not fire.

## Anti-patterns

- Trusting Haiku subagent introspection of its own schema or tool returns.
- Treating frontmatter `Bash(arg-glob)` as a sandbox in any parent mode — it's documentation, never enforces. Use settings.json `permissions.allow/deny` or PreToolUse hook for real gating.
- Confusing `Agent(isolation: "worktree")` (subagent spawn) with `EnterWorktree` tool (main session switch) — two distinct mechanisms with different scopes.
- Relying on CLAUDE.md to reach all subagents (Explore/Plan strip — hardcoded by agent name).
- Writing main-session behavioral rules and expecting subagent inheritance.
- Reading subagent error strings to infer mechanism — three strings, one mechanism.
- Hot-editing `.claude/agents/` mid-session and expecting pickup.
- Asking subagent for "verbatim" quotes longer than a few tokens.
- Using `exit 1` in PreToolUse hooks expecting a block (only exit 2 blocks).
- Spawning many isolated subagents without bounding worktree count — disk overhead.
- Forgetting that worktree path + branch in Agent result implies caller must clean up if no longer needed.
- Expecting settings.json `permissions.allow` to re-expose a frontmatter-stripped tool — allow operates on existing schemas; strip removes the schema entirely.
- Trying to widen subagent tool pool beyond parent's via frontmatter `tools:` — only `mcpServers:` field adds scope (MCP-only).
- Spawning isolation-worktree subagents while hook scripts live in untracked paths — `git worktree add` ignores untracked files, every hook fire in the worktree subagent errors and blocks tool calls. Commit hook scripts, use absolute paths in settings, or wrap script invocation in a path-existence check.
- Reporting sonnet's self-estimated word counts as ground-truth measurements — they are ordinal-trustable estimates, not character/token counts.

## Open questions

Resolved (now in composition.md / control.md):

- MCP cloud, ShareOnboardingGuide, ScheduleWakeup, AskUserQuestion propagation — probed.
- Settings allow vs frontmatter strip precedence — derived.
- Plan strips CLAUDE.md + gitStatus — trap-probed.
- 7 hook events stable + wireable; 7 wired here all fire (log inspected).
- Hook firing inside subagents — log shows PreToolUse in ntrip-research subagent.
- model override replaces frontmatter — docs + behavior consistent.
- `CLAUDE_CODE_SUBAGENT_MODEL` is session-scoped, highest precedence.
- Explore/Plan opt-out hardcoded by agent name — docs.
- Per-agent tool pool restrict-only; mcpServers adds MCP scope — docs.
- `disallowedTools` syntax same as `tools`; no wildcards.
- Bash arg-glob in frontmatter never enforces args; settings.json owns regardless of permission mode.
- WorktreeCreate fires on `--worktree` CLI + `Agent(isolation: "worktree")` per docs; replaces default git logic for non-git VCS.
- Skill auto-trigger works in subagents per docs.
- EnterWorktree/ExitWorktree distinct from Agent isolation — schemas loaded.
- Layer order verified via trap-controlled neighbor probe.

Still open:

- **Subagent skill auto-trigger reliability** — no community measurement isolating subagent context (Vercel 56% miss in main session; subagent unmeasured).
- **mcpServers MCP scope persistence** across `SendMessage` continuation of same subagent — untested.
- **Whether `EnterWorktree` tool (user-driven) fires `WorktreeCreate` hook** — docs list `--worktree` CLI + Agent isolation as triggers; EnterWorktree's relation not specified.
- **`permissionMode` frontmatter ignored in `auto` mode parent** — claim from docs research, not directly verified locally.
