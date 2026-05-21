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
    # 2 = depends on parent mode (auto classifier / bypassPermissions / default) — see control.md Permissions,
    # 3 = runs.

## Anti-patterns

- Trusting Haiku subagent narration of tool returns it never made — `tool_uses=0` + reported outputs = fabricated.
- Treating frontmatter `Bash(arg-glob)` as an arg gate — it isn't. Use `settings.json permissions` or a PreToolUse hook.
- Confusing `Agent(isolation: "worktree")` (subagent spawn) with `EnterWorktree` (main session switch).
- Relying on CLAUDE.md to reach all subagents — Explore + Plan strip.
- Writing main-session behavioral rules and expecting subagent inheritance.
- Hot-editing `.claude/agents/` mid-session and expecting pickup.
- Asking subagent for "verbatim" quotes longer than a few tokens — sonnet paraphrases.
- Using `exit 1` in PreToolUse hooks expecting a block (only exit 2 blocks).
- Spawning isolation worktrees with hook scripts in gitignored paths — `git worktree add` skips untracked → hook script missing → exit 2 blocks every tool call. Fix: `.worktreeinclude`, commit the scripts, or use absolute paths.
- Treating the trailing `agentId: ... (use SendMessage ...)` hint as SDK leakage — it's real, but only callable when `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. Without that flag, the hint dangles.
- Wiring `WorktreeCreate` to a logging-only hook — it's a REPLACEMENT hook (mechanism in control.md). `WorktreeRemove` IS observation-only; don't generalize.
- Expecting `settings.json permissions.allow` to re-expose a frontmatter-stripped tool — allow grants permission to existing schemas; strip removes the schema entirely.
- Trying to widen subagent tool pool beyond parent's via frontmatter `tools:` — only `mcpServers:` adds scope (MCP-only).
- Placing project agent files in subfolders expecting they'll load — probed Windows, did not load. Keep agent files at the top level of `.claude/agents/`.
- Expecting `Agent(subagent_type="general-purpose")` to become a fork when `CLAUDE_CODE_FORK_SUBAGENT=1` is set — it doesn't (token count stays at subagent baseline, history not inherited). Auto-background still fires. For an explicit fork, use the `/fork` interactive command.
- Inferring auto-deny is broken from one ran call — probe multiple; only classifier-rejected commands hit auto-deny. See control.md Permissions for the per-mode breakdown.

## Open questions

- Subagent skill auto-trigger reliability — public reports of high miss rate in main session; subagent unmeasured.
- Strict-mode parent (`permissionMode: default`) behavior for subagent tool calls matching neither allow nor deny — likely auto-denies since no UI to prompt, but untested in this session (parent was permissive).
- Baseline token count of a minimal agent (only `name` + `description`, empty body, no tools restrictions) — measure via `<usage>` block from a single-message spawn.
- Per-frontmatter-field token cost delta — toggle one field, re-measure, isolate contribution.
- Recursive subfolder scan for project agents — docs claim it works; Windows probe failed (`.claude/agents/sub/q-subfolder.md` did not load). Re-probe on macOS / Linux to scope the discrepancy.
- Background subagent auto-deny under `default`-mode parent — untested (K only under `auto` parent so far). Expected: same auto-deny path since no UI to prompt.
- `/fork` interactive command behavior — Agent-tool `general-purpose` doesn't fork even with `CLAUDE_CODE_FORK_SUBAGENT=1`. Verify `/fork <directive>` produces a real fork (high cached_read on first request, full conversation history visible to fork).
- `Agent(isolation: "worktree")` second baseRef value — first run confirmed `"fresh"` default (HEAD = origin/HEAD). Re-run with `"worktree": {"baseRef": "head"}` set; expected HEAD = local HEAD, not origin/HEAD.
- `settings.local.json` absence in worktree subagent — claimed but unprobed. Add a benign deny rule there, spawn isolated subagent attempting the denied call.
