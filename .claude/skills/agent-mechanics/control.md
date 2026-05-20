# Control: how you steer subagents from outside

## Definition

**Location**: `.claude/agents/<file>.md` (project), `~/.claude/agents/` (user), plus managed (`.claude/agents/` in [managed settings dir](https://code.claude.com/docs/en/settings#settings-files)) and plugin (`<plugin>/agents/`). Filename does NOT need to match `name`; identity comes from the frontmatter `name` field. Subfolders allowed (recursive scan).

**Scope precedence** when `name` collides: managed > project > user > plugin. Collisions WITHIN one scope: Claude Code keeps one and discards the other without warning.

Loaded at session start only — hot-edit on disk returns `Agent type 'X' not found` until restart. Exception: `/agents` interactive panel creates/edits take effect immediately.

**Frontmatter** (only `name` + `description` required):

| Field             | Req | Effect                                                                                                                                                                                                                  |
| :---------------- | :-- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`            | Yes | Lowercase + hyphens. Used as `agent_type` in Agent calls and `agent_type` in SubagentStart/Stop hook payloads.                                                                                                          |
| `description`     | Yes | Auto-delegation cue. Quality directly affects whether main session picks this agent.                                                                                                                                    |
| `tools`           | No  | Tool-NAME allowlist (comma- or space-separated). Two forms: explicit (`tools: Read, Edit`) or "All tools except X, Y". Bash arg-globs are documentation only — real arg gate is `settings.json permissions`.            |
| `disallowedTools` | No  | Subtracts from inherited pool. Same syntax. Applied before `tools` resolves; tool in both = removed.                                                                                                                    |
| `model`           | No  | `sonnet` \| `opus` \| `haiku` \| full ID (e.g. `claude-opus-4-7`) \| `inherit`. **Default: `inherit`**. Per-call `model` param overrides.                                                                              |
| `isolation`       | No  | `worktree` runs subagent in ephemeral git worktree. Same mechanism as `Agent(..., isolation: "worktree")` per-call param — frontmatter makes it the default for that agent.                                             |
| `skills`          | No  | List of skill names whose **full body** preloads into context at startup (NOT just description — the body). Subagent can still invoke unlisted skills via the Skill tool.                                                |
| `mcpServers`      | No  | Adds MCP servers scoped to this subagent. **Only documented widening mechanism** — `tools:` and `disallowedTools:` can only restrict the inherited pool.                                                                |
| `memory`          | No  | `user` \| `project` \| `local`. Enables cross-session persistent memory for this agent.                                                                                                                                |
| `hooks`           | No  | Lifecycle hooks scoped to this agent's runs. Frontmatter `Stop` auto-converts to `SubagentStop` when invoked as a subagent.                                                                                             |
| `maxTurns`        | No  | Hard cap on agentic turns. Safety + cost knob.                                                                                                                                                                          |
| `background`      | No  | `true` = always run as background task. Default `false`. Foreground/background can also be toggled per-call (Agent `run_in_background`) or interactively (Ctrl+B).                                                     |
| `effort`          | No  | `low`/`medium`/`high`/`xhigh`/`max`. Overrides session effort. Model-dependent availability.                                                                                                                            |
| `permissionMode`  | No  | `default`/`acceptEdits`/`auto`/`dontAsk`/`bypassPermissions`/`plan`. **Overridden whenever parent uses `acceptEdits`, `bypassPermissions`, or `auto`** — those propagate with the same force and ignore this field.    |
| `color`           | No  | `red` / `blue` / `green` / `yellow` / `purple` / `orange` / `pink` / `cyan`. Display color in task list / transcript. Cosmetic.                                                                                          |
| `initialPrompt`   | No  | Auto-submitted as first user turn when this agent runs as **main session** (via `claude --agent X`, see "Main-session mode" below). Prepended to any user prompt. Commands + skills processed.                          |

**Plugin agents** lose `hooks`, `mcpServers`, `permissionMode` — those fields are ignored when the agent comes from a plugin. To use them, copy the agent into `.claude/agents/` or `~/.claude/agents/`.

**Body** appended verbatim as the agent-specific role text (layer #2 in composition.md).

## Main-session mode (`claude --agent <name>`)

Same agent file, different invocation. Started via `claude --agent <name>` (or via `agent` setting), the agent IS the main session — not a subagent.

Differences vs subagent mode:

- `initialPrompt` fires as the first user turn (ignored in subagent mode).
- `mcpServers` inline definitions connect at startup, alongside `.mcp.json` and settings-file servers.
- `tools: Agent(worker, researcher)` syntax actually gates which subagent_types the main thread can spawn. In subagent mode, `Agent(...)` allowlist has no effect since subagents cannot spawn nested subagents anyway.
- Frontmatter `Stop` hooks fire as `Stop` (in subagent mode they convert to `SubagentStop`).
- The system prompt is the agent body, replacing the default Claude Code prompt (same as `--system-prompt`). CLAUDE.md and memory still load through the normal flow.

The agent name appears as `@<name>` in the startup header so you can confirm the active agent.

## Spawn-time controls (Agent tool)

| Param | Effect |
|-------|--------|
| `subagent_type` | picks agent definition; case-sensitive |
| `description` | telemetry; user-visible |
| `prompt` | user-turn-equivalent input; no memory of parent convo |
| `model` | REPLACES frontmatter `model:`. Resolution order: env `CLAUDE_CODE_SUBAGENT_MODEL` (session-scoped) > call-site param > frontmatter > main convo |
| `isolation` | `"worktree"` spawns subagent in temporary git worktree. Same effect as frontmatter `isolation: worktree` — per-call is the override path. |
| `run_in_background` | Detaches subagent; parent notified on completion. Foreground/background also settable via `background:` frontmatter (always) or Ctrl+B (interactively). |

Each Agent call is one-shot — no built-in continuation. (Trailing `agentId: ... (use SendMessage with to: ...)` hints in Agent output are Claude Agent SDK leakage; `SendMessage` is not a main-session tool.)

**Subagents cannot spawn nested subagents.** `Agent` is absent from subagent schemas. `tools: Agent(worker, researcher)` syntax in a frontmatter only matters for `claude --agent` main-session mode (see above) — in subagent mode it's a no-op.

## Worktree mechanics

Three entry points that all create worktrees under `.claude/worktrees/`:

| Entry point                              | Scope                                            |
| :--------------------------------------- | :----------------------------------------------- |
| `Agent(..., isolation: "worktree")` or frontmatter `isolation: worktree` | SUBAGENT runs in ephemeral worktree              |
| `claude --worktree <name>` CLI flag      | MAIN session starts in worktree                  |
| `EnterWorktree` / `ExitWorktree` tools   | MAIN session switches into a worktree mid-flight |

All three share the same git logic, settings (`worktree.baseRef`, `cleanupPeriodDays`), `.worktreeinclude` copy step, and `WorktreeCreate` / `WorktreeRemove` hook surface. Differences are scope (who's in the worktree) and lifecycle (when it's torn down).

### Base ref

`worktree.baseRef` setting (applies to ALL three entry points):

- `"fresh"` (default) — branch from `origin/<default-branch>` so the worktree starts on a clean tree matching remote. Falls back to local HEAD if no remote or fetch fails.
- `"head"` — branch from local HEAD. Carries unpushed commits + feature-branch state into the worktree. Useful when subagent must operate on in-progress work.

Only `"fresh"` or `"head"` — no arbitrary refs via this setting. For arbitrary base (specific branch, tag, SHA), use the `WorktreeCreate` hook (see Hooks below).

CLI special form: `claude --worktree "#1234"` checks out `pull/1234/head` from origin into `.claude/worktrees/pr-1234`. Subagent isolation has no equivalent shortcut — use the hook.

### Worktree paths

Default path: `.claude/worktrees/<value>/`. `<value>` depends on entry point:

- CLI `--worktree foo` → `<value>` = `foo` (or generated like `bright-running-fox` if omitted).
- CLI `--worktree "#1234"` → `<value>` = `pr-1234`.
- Subagent `isolation: worktree` → `<value>` per implementation; not specified in docs. Treat as opaque, read from `WorktreeCreate` stdin or `SubagentStart` hook payload if you need it.

### Copying gitignored files: `.worktreeinclude`

`git worktree add` checks out tracked files only. Gitignored files (`.env`, hook scripts in ignored paths, local config) are absent. This was the source of the "all tool calls in subagent block" failure pattern — gitignored hook scripts → hook fires → script not found → exit 2 blocks every tool call.

**Canonical fix**: add `.worktreeinclude` to repo root. Same syntax as `.gitignore`. Patterns matched against gitignored files; matching files are copied into each new worktree. Tracked files are never duplicated.

Example:
```
.env
.env.local
config/secrets.json
.claude/hooks/
```

Applies to all three entry points. NOT processed when a `WorktreeCreate` hook replaces the default git logic — the hook must copy files itself.

Fallback fixes when `.worktreeinclude` insufficient: commit hook scripts (best long-term), use absolute paths in hook commands, guard hook commands with path-existence checks.

### Cleanup

- No changes, no untracked, no new commits → worktree + branch auto-removed.
- Named session → Claude prompts to keep for later.
- Dirty (uncommitted/untracked/commits) → caller decides keep / remove. Subagent isolation: path + branch returned in the Agent tool result.
- Non-interactive runs (`-p` with `--worktree`): no automatic cleanup; remove with `git worktree remove`.
- Orphan sweep: subagent worktrees orphaned by crash older than `cleanupPeriodDays` setting are swept at startup (only if clean — no uncommitted, no untracked, no unpushed).

### Subagent isolation: decision tree

Opt into `isolation: worktree` when:

- Subagent edits files AND its edits could collide with the parent session (or with sibling subagents running in parallel).
- Subagent needs a CLAUDE.md that differs from the project's (only way to swap CLAUDE.md per-agent — see "Custom CLAUDE.md per agent" recipe below).
- Subagent must operate on a different ref (PR branch, feature branch, etc.) — needs `WorktreeCreate` hook.

Skip isolation when:

- Subagent is read-only (Read, Grep, Glob, no Edit/Write/Bash mutations).
- Cost-sensitive: worktree creation adds setup time and re-reads CLAUDE.md from disk (no prompt-cache reuse with parent's CLAUDE.md).
- Parent session needs to see subagent's file changes in-place (worktree changes stay in the worktree branch until merged).

### Recipe: custom CLAUDE.md per agent

Goal: subagent sees a different CLAUDE.md than the project's, without polluting main checkout.

Approach A — separate branch:
1. Create a branch (e.g. `agent-context/minimal`) with the desired CLAUDE.md committed.
2. Set `worktree.baseRef: "head"` and check out that branch before spawning, OR use a `WorktreeCreate` hook that checks out the agent-context branch.
3. Spawn agent with `isolation: worktree`.

Approach B — `WorktreeCreate` hook overwrites CLAUDE.md after creation:
1. Hook receives agent_type on stdin.
2. Hook runs `git worktree add` (default behavior) into the target path.
3. Hook copies/writes a custom CLAUDE.md into the worktree path.
4. Hook prints the worktree path on stdout (replacement-hook contract).

Caveat: `WorktreeCreate` has no matcher — the hook fires for every worktree creation path. Discriminate inside the hook by reading stdin for agent context.

### EnterWorktree / ExitWorktree (main session)

`EnterWorktree(name?, path?)` creates a new worktree or enters an existing one and switches session cwd.

`ExitWorktree(action: keep|remove, discard_changes?)` leaves the worktree session. `remove` refuses dirty worktrees without `discard_changes: true`. Operates only on worktrees entered via `EnterWorktree` this session.

Both honor `worktree.baseRef` and (L per docs) `WorktreeCreate` / `WorktreeRemove` hooks.

## Hooks

Most relevant for subagent work:

- `PreToolUse` / `PostToolUse` — before / after each tool call. PreToolUse fires INSIDE subagents.
- `SubagentStart` / `SubagentStop` — spawn / return; payload includes agent_id + agent_type.
- `WorktreeCreate` (K) — **REPLACEMENT hook**, not observation. Effectively the arguments API for `Agent(isolation: "worktree")`, which itself takes no caller knobs (just the binary flag). When wired, the hook takes over worktree creation; built-in git logic is bypassed. Fires BEFORE the subagent runs. Hook MUST return the worktree path via stdout (or `hookSpecificOutput.worktreePath` for http/callback variants). A no-op logging hook returns no path → `WorktreeCreate hook failed: hook succeeded but returned no worktree path` → worktree creation aborts. Use cases: custom base ref / path / branch naming, non-git VCS (svn/hg/perforce), shared worktrees across calls, fenced-off out-of-repo isolation. Default (no hook) = built-in git logic with `worktree.baseRef` setting. No matchers.
- `WorktreeRemove` (L per docs) — pure **OBSERVATION hook**. Cannot block removal; exit code + stderr ignored. Fires on subagent finish OR session exit, distinguished by `removal_reason` field (`"subagent_finish"` / `"session_exit"`). Receives `worktree_path` + `removal_reason` on stdin. Default (no hook) = built-in git removal. Pairing with `WorktreeCreate` advisory, not required. NOT symmetric to WorktreeCreate.
- `InstructionsLoaded` — CLAUDE.md / rules loaded.
- `UserPromptSubmit` — user submits a prompt.

Other lifecycle events: `SessionStart`, `SessionEnd`, `Stop`, `Notification`, `PreCompact`, `PermissionRequest`.

**Load vs fire**: hook definitions load with settings (step 2 of load order, below); events fire on lifecycle triggers. Snapshotted at session start; mid-session settings edits prompt review via `/hooks`, not silent apply.

**Semantics**:

- Exit 2 blocks + routes stderr to Claude. Exit 1 prints stderr but does NOT block — most common security-gate footgun.
- PostToolUse cannot undo; use PreToolUse to prevent.
- Matchers PascalCase, case-sensitive.
- Multiple matching hooks run in parallel; deny beats allow.
- PreToolUse `permissionDecision: "deny"` overrides `--dangerously-skip-permissions`.
- Shell-profile (`.zshrc`, `.bashrc`) echo prepends garbage to JSON stdin → silent breakage.
- Performance: Node/Python spawn per event can reach ~20s/turn. Target <1-2s.

A hook can also emit `hookSpecificOutput.additionalContext` — that string is injected into Claude's own context. Useful for surfacing lifecycle markers visible to the model.

## Permissions (runtime)

Two distinct gating layers; permissions is the second one — runtime, not context-level.

- **Schema-load** (frontmatter `tools:` / `disallowedTools:`): whole-tool include/exclude — changes what's IN subagent context. Errors are schema-strip class (see composition.md).
- **Runtime** (`settings.json permissions.allow/deny`): tool name + argument-pattern matching at call time. Rules NOT surfaced in subagent context — subagent only sees call outcomes.

**Per-arg deny error** (K, observed): a tool call hitting a `deny` rule returns:
`[tool_use_error: File is in a directory that is denied by your permission settings.]`
Distinct from the three schema-strip error strings — different code path. Path-pattern denial fires this; whole-tool denial via frontmatter fires schema-strip class.

**No prompt UI in subagent** — outcomes by case:
- Call matches `allow` rule → silently runs (K).
- Call hits `deny` rule → `tool_use_error` as above (K).
- Call matches neither rule → behavior follows parent's permission mode. Permissive parent (`bypassPermissions` / `acceptEdits` / `auto`) → silently allows (K — observed for `Bash(date /T)`, `Bash(whoami)`, none in allow). Strict parent (`default`) → likely auto-denies since no prompt path exists (L, not tested).

**Worktree subagent caveat**: settings.local.json typically untracked → absent in worktree → its allow/deny rules don't apply for the worktree subagent. Tracked settings.json still applies. Effective permission set is leaner than parent's. If settings.local.json carries critical denies, propagate via `.worktreeinclude` or commit them.

**Settings allow does NOT re-expose stripped tools** (K, see composition.md "Tool surface"). Allow rules grant permission to existing schemas; they don't add schemas.

## Session-start sequence

Hook lifecycle interleaves with static config loading. Approximate observed order:

1. Settings layers merged (managed > CLI flags > `.local.json` > `.json` > user `~/.claude/`) — hook definitions registered, permissions evaluated.
2. `SessionStart` hook fires (observed before CLAUDE.md per hook log); its `additionalContext` if emitted is appended to Claude's context.
3. Static config snapshot — all loaded into Claude's context before first inference:
   - CLAUDE.md concatenation (project + user + enterprise)
   - Skills catalog (frontmatter only; body lazy on invocation)
   - Agents catalog (`.claude/agents/` + parents + user)
   - MCP servers
   - Tool schemas (gated by frontmatter `tools:`)
4. `InstructionsLoaded` hook fires once CLAUDE.md / rules are loaded.
5. `UserPromptSubmit` fires per prompt thereafter.

Per-event hooks (`PreToolUse`, `PostToolUse`, `SubagentStart` / `Stop`, etc.) fire at their respective lifecycle moments — not as part of startup.

Subagent variant: same snapshot at the subagent's cwd; CLAUDE.md + gitStatus stripped for Explore/Plan; agent body composes onto the base identity layer.

## Persistence: what survives subagent exit

Each Agent call is one-shot — no built-in continuation, no shared state with the next call. Persistence is achieved by writing somewhere durable BEFORE the subagent returns.

**Channels available**:

| Channel                     | Lives where                        | Read back by                                         |
| :-------------------------- | :--------------------------------- | :--------------------------------------------------- |
| Tool result text            | Agent tool result in parent context | Parent reads automatically when call returns         |
| Files written to cwd        | Parent's working tree              | Parent reads via Read tool                           |
| Files written in worktree   | Ephemeral worktree path + branch   | Parent merges / cherry-picks branch; or reads at returned path |
| `memory:` scope             | User / project / local memory file | Same agent (or whole session) on later runs          |
| External (DB, MCP-stored)   | Wherever MCP writes                | Whoever has MCP access                               |

**`memory: user|project|local` frontmatter**: enables cross-session persistent memory for this agent. `user` = `~/.claude/`, `project` = `.claude/`, `local` = `.claude/` but git-ignored path. Pattern: agent writes findings to memory file; next run of the SAME agent reads them. Cross-AGENT sharing requires same memory scope + path overlap, or going through files / MCP.

**Multi-step orchestration**: simulate continuation by sequential Agent calls from main session. Pattern: Agent #1 writes intermediate state to a file in cwd → Agent #2 starts from that file's content. Main session is the coordinator. `run_in_background: true` parallelizes independent legs; foreground is required when the next leg consumes the previous leg's output.

**Worktree subagent edits**: stay in the ephemeral worktree branch. To bring them into main: read the path + branch from the Agent tool result, then `git merge` / `git cherry-pick` / manual copy. No automatic merge.

## Hot-reload

- `.claude/agents/*.md` edited on disk: NOT hot-loaded. Restart required for the new definition to be callable.
- `.claude/agents/*.md` created/edited via the `/agents` interactive panel: takes effect immediately, no restart (per docs).
- Settings: Claude detects external edit, prompts review via `/hooks`. Not silent.
- CLAUDE.md, skills, MCP servers: snapshotted at session start.
