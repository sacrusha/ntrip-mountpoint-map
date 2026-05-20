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

    1. Create branch with modified CLAUDE.md containing a unique marker string.
    2. Check out that branch (so it's HEAD); set `worktree.baseRef: "head"` or stay on default.
    3. Agent(..., isolation: "worktree") with a prompt asking the subagent to quote the marker.
    4. Marker visible = custom CLAUDE.md propagated. Trap-control by also asking it to quote a string known NOT to be in the modified CLAUDE.md — yes on trap = fabrication, not real propagation.

**Token cost baseline**:

    Agent(subagent_type="<minimal>", model="sonnet",
      prompt="Output the literal token '<<DONE>>' and nothing else.")
    # Read <usage> block input_tokens. Minimum-bound for that agent's setup cost.
    # Compare across: empty body vs 1KB body vs +skills preload vs +large mcpServers.

**Skills preload vs catalog**:

    1. Pick a skill with a long, unique body string.
    2. Spawn subagent that does NOT have it in `skills:` frontmatter — ask "quote the string".
       Expected: not visible (only catalog name+description loaded).
    3. Spawn second subagent WITH `skills: [that-skill]` — same prompt.
       Expected: visible (body preloaded).

**Hot-reload check**:

    Write new file under .claude/agents/. Immediately attempt Agent call with that subagent_type.
    "Agent type 'X' not found" = no hot-load, restart required.
    Note: `/agents` panel creates DO take effect immediately — only on-disk edits require restart.

**Hook fire check**:

    Trigger the event (e.g. spawn subagent for SubagentStart). Inspect hook log.
    Absence in log = hook did not fire.

**Permission outcomes (deny + no-rule + allow)**:

    Agent(subagent_type="general-purpose", model="sonnet",
      prompt="Make these literal calls; quote each return verbatim in backticks:
        1. Read on a path covered by settings.json deny rule (e.g. `.git/HEAD`)
        2. Bash with a command not in any allow rule (e.g. `whoami`, `date`)
        3. Bash with a command covered by allow rule (e.g. `curl --version` when Bash(curl:*) is allowed)
      Format: 1. `<text>` 2. `<text>` 3. `<text>` END")

    # Expected: 1 = `[tool_use_error: ... denied by your permission settings.]`,
    # 2 = runs if parent permissive, denies if parent strict, 3 = runs.

## Anti-patterns

- Trusting Haiku subagent narration of tool returns it never made — `tool_uses=0` + reported outputs = fabricated.
- Treating frontmatter `Bash(arg-glob)` as a sandbox — documentation only. Use `settings.json permissions` or PreToolUse hook for real gating.
- Confusing `Agent(isolation: "worktree")` (subagent spawn) with `EnterWorktree` (main session switch).
- Relying on CLAUDE.md to reach all subagents — Explore + Plan strip.
- Writing main-session behavioral rules and expecting subagent inheritance.
- Hot-editing `.claude/agents/` mid-session and expecting pickup.
- Asking subagent for "verbatim" quotes longer than a few tokens — sonnet paraphrases.
- Using `exit 1` in PreToolUse hooks expecting a block (only exit 2 blocks).
- Spawning isolation worktrees while hook scripts are in gitignored paths — `git worktree add` skips untracked, hooks then error and block all tool calls. Canonical fix: `.worktreeinclude` (see control.md "Copying gitignored files"). Workarounds: commit hook scripts, absolute paths in settings, or path-existence guard in the hook command.
- Propagating tool names mentioned in tool returns without verifying own schema enum — Agent return's `SendMessage` hint is SDK-layer leakage.
- Wiring `WorktreeCreate` to a logging-only hook expecting observation semantics — `WorktreeCreate` is REPLACEMENT. The command must return the worktree path; a no-op silently breaks `Agent(isolation: "worktree")` with `WorktreeCreate hook failed: hook succeeded but returned no worktree path`. (`WorktreeRemove` IS observation-only — wiring a logger to it is safe; don't generalize from one to the other.)
- Expecting `settings.json permissions.allow` to re-expose a frontmatter-stripped tool — allow grants permission to existing schemas; strip removes the schema entirely.
- Trying to widen subagent tool pool beyond parent's via frontmatter `tools:` — only `mcpServers:` adds scope (MCP-only).

## Open questions

- Subagent skill auto-trigger reliability — Vercel measured 56% miss in main session; subagent unmeasured.
- Does `Agent(isolation: "worktree")` honor the `worktree.baseRef` setting? Docs treat all worktree entry points uniformly but the setting's section in docs uses CLI examples only — probe by spawning isolation subagent with `baseRef: "head"` vs `"fresh"` and checking the worktree's commit.
- Strict-mode parent (`permissionMode: default`) behavior for subagent tool calls matching neither allow nor deny — likely auto-denies since no UI to prompt, but untested in this session (parent was permissive).
- Worktree path format for subagent isolation — docs document `--worktree <name>` → `.claude/worktrees/<name>/` but don't specify the subagent variant. Probe: spawn isolated subagent, dump cwd.
- Does `skills:` frontmatter inject full skill body? Marker-probe a skill body string in the spawned subagent.
- Are `Stop` hooks declared in frontmatter actually converted to `SubagentStop` when invoked as subagent? Hook-log probe.
- Baseline token count of a minimal agent (only `name` + `description`, empty body, no tools restrictions) — measure via `<usage>` block from a single-message spawn.
- Per-frontmatter-field token cost delta — toggle one field, re-measure, isolate contribution.
