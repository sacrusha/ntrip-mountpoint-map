# Control: how you steer subagents from outside

## Definition

**Location**: `.claude/agents/<file>.md` (project), `~/.claude/agents/` (user), managed (`.claude/agents/` in [managed settings dir](https://code.claude.com/docs/en/settings#settings-files)), plugin (`<plugin>/agents/`). Identity = frontmatter `name`; filename is cosmetic.

Subfolder behavior is per-scope:
- **Plugin**: subfolder becomes part of the scoped name (`my-plugin/agents/review/security.md` → `my-plugin:review:security`).
- **Project / user**: docs claim recursive scan; Windows probe showed `.claude/agents/sub/q-subfolder.md` did NOT load. Keep project/user agent files at the top level; re-probe on macOS/Linux to scope.

`--add-dir <path>` grants file access for that path only; not scanned for subagents.

**Programmatic (single-session)**: `claude --agents '{"name": {...}}'` accepts JSON with the same frontmatter fields as file-based agents. Use `prompt` for the system prompt (equivalent to the markdown body).

**Scope precedence** when `name` collides: managed > `--agents` flag > project > user > plugin. Collisions WITHIN one scope: Claude Code keeps one and discards the other without warning.

Loaded at session start. Disk edits ignored until restart (`Agent type 'X' not found`). The `/agents` panel applies immediately.

**Frontmatter** (only `name` + `description` required):

| Field             | Req | Effect                                                                                                                                                                                                                  |
| :---------------- | :-- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`            | Yes | Lowercase + hyphens. Used as `agent_type` in Agent calls and `agent_type` in SubagentStart/Stop hook payloads.                                                                                                          |
| `description`     | Yes | Auto-delegation cue. Quality directly affects whether main session picks this agent.                                                                                                                                    |
| `tools`           | No  | Tool-NAME allowlist, comma- or space-separated: `tools: Read, Edit, Grep`.                                                                                                                                              |
| `disallowedTools` | No  | Removes named tools from inherited pool. Same syntax as `tools:`. Tool in both = removed. Cannot widen.                                                                                                                |
| `model`           | No  | `sonnet` \| `opus` \| `haiku` \| full ID (e.g. `claude-opus-4-7`) \| `inherit`. **Default: `inherit`**. Per-call `model` param overrides.                                                                              |
| `isolation`       | No  | `worktree` runs subagent in ephemeral git worktree. Per-call `isolation` param overrides.                                                                                                                              |
| `skills`          | No  | Full body of each named skill preloads into context at startup. Subagent can still invoke unlisted skills via the Skill tool.                                                                                            |
| `mcpServers`      | No  | Adds MCP servers scoped to this subagent. Only field that can widen the inherited pool.                                                                                                                                |
| `memory`          | No  | `user` \| `project` \| `local`. Enables cross-session persistent memory for this agent.                                                                                                                                |
| `hooks`           | No  | Lifecycle hooks scoped to this agent's runs. Frontmatter `Stop` auto-converts to `SubagentStop` when invoked as a subagent.                                                                                             |
| `maxTurns`        | No  | Hard cap on agentic turns. On hit: subagent terminates silently; parent sees `(Subagent completed but returned no output.)`.                                                                                            |
| `background`      | No  | `true` = always run as background task (default `false`). Background subagents run with current session permissions and auto-deny any tool call that would otherwise prompt. Per-call `run_in_background` or Ctrl+B override per spawn. |
| `effort`          | No  | `low`/`medium`/`high`/`xhigh`/`max`. Overrides session effort. Model-dependent availability.                                                                                                                            |
| `permissionMode`  | No  | `default`/`acceptEdits`/`auto`/`dontAsk`/`bypassPermissions`/`plan`. `dontAsk` auto-denies prompts while still honoring explicitly allowed tools. Parent `acceptEdits`/`bypassPermissions`/`auto` propagate to subagent and override this field. |
| `color`           | No  | `red` / `blue` / `green` / `yellow` / `purple` / `orange` / `pink` / `cyan`. Display color in task list / transcript. Cosmetic.                                                                                          |
| `initialPrompt`   | No  | Auto-submitted as first user turn when this agent runs as **main session** (via `claude --agent X`, see "Main-session mode" below). Prepended to any user prompt. Commands + skills processed.                          |

**Plugin agents** lose `hooks`, `mcpServers`, `permissionMode` — those fields are ignored when the agent comes from a plugin. To use them, copy the agent into `.claude/agents/` or `~/.claude/agents/`.

**Body** is appended verbatim as the agent's role text.

## Main-session mode (`claude --agent <name>`)

Same agent file, different invocation. Started via `claude --agent <name>` (or via `agent` setting), the agent IS the main session — not a subagent.

Differences vs subagent mode:

- `initialPrompt` fires as the first user turn (ignored in subagent mode).
- `mcpServers` inline definitions connect at startup, alongside `.mcp.json` and settings-file servers.
- `tools:` Agent semantics for what the main thread can spawn:
  - `Agent` alone in `tools:` → can spawn any subagent type.
  - `Agent(a, b)` → allowlist of subagent types only.
  - `Agent` absent from `tools:` → cannot spawn any subagent.
  - In a subagent definition the syntax is inert: subagents never spawn nested subagents.
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
| `isolation` | `"worktree"` spawns subagent in temporary git worktree. Equivalent to frontmatter `isolation: worktree`, overrides it. |
| `run_in_background` | Detaches subagent; parent notified on completion. Also settable via `background:` frontmatter or Ctrl+B. |

Each Agent call is one-shot by default. With Agent Teams enabled (see "Experimental flags"), the trailing `agentId:` hint in every Agent return becomes a resumption handle via `SendMessage`. Without that flag, the hint dangles.

**Subagents cannot spawn nested subagents.** `Agent` is absent from subagent schemas. The `tools: Agent(...)` allowlist syntax only matters in main-session mode.

## Worktree mechanics

Three entry points that all create worktrees under `.claude/worktrees/`:

| Entry point                              | Scope                                            |
| :--------------------------------------- | :----------------------------------------------- |
| `Agent(..., isolation: "worktree")` or frontmatter `isolation: worktree` | SUBAGENT runs in ephemeral worktree              |
| `claude --worktree <name>` CLI flag      | MAIN session starts in worktree                  |
| `EnterWorktree` / `ExitWorktree` tools   | MAIN session switches into a worktree mid-flight |

All three share the same git logic, settings (`worktree.baseRef`, `worktree.symlinkDirectories`, `worktree.sparsePaths`, `worktree.bgIsolation`, `cleanupPeriodDays`), `.worktreeinclude` copy step, and `WorktreeCreate` / `WorktreeRemove` hook surface. Differences are scope (who's in the worktree) and lifecycle (when it's torn down).

### Base ref

`worktree.baseRef` setting (applies to ALL three entry points):

- `"fresh"` (default) — branch from `origin/<default-branch>` so the worktree starts on a clean tree matching remote. Falls back to local HEAD if no remote or fetch fails.
- `"head"` — branch from local HEAD. Carries unpushed commits + feature-branch state into the worktree. Useful when subagent must operate on in-progress work.

Only `"fresh"` and `"head"`. For arbitrary refs (branch / tag / SHA), use a `WorktreeCreate` hook.

CLI special form: `claude --worktree "#1234"` checks out `pull/1234/head` from origin into `.claude/worktrees/pr-1234`. Subagent isolation has no equivalent shortcut; use a hook.

### Worktree paths

Default path: `.claude/worktrees/<value>/`. Default branch: `worktree-<value>`. `<value>` depends on entry point:

- CLI `--worktree foo` → `<value>` = `foo` (or generated like `bright-running-fox` if omitted).
- CLI `--worktree "#1234"` → `<value>` = `pr-1234`.
- Subagent `isolation: worktree` → `<value>` = `agent-<agentId>` (path `.claude/worktrees/agent-<agentId>/`, branch `worktree-agent-<agentId>`).

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

Applies to all three entry points. A custom `WorktreeCreate` hook bypasses this step; copy files inside the hook instead.

Fallback fixes when `.worktreeinclude` insufficient: commit hook scripts (best long-term), use absolute paths in hook commands, guard hook commands with path-existence checks.

### Cleanup

- No changes, no untracked, no new commits → worktree + branch auto-removed.
- Named session → Claude prompts to keep for later.
- Dirty (uncommitted/untracked/commits) → caller decides keep / remove. Subagent isolation: path + branch returned in the Agent tool result.
- Non-interactive runs (`-p` with `--worktree`): no automatic cleanup; remove with `git worktree remove`.
- Orphan sweep: subagent worktrees orphaned by crash older than `cleanupPeriodDays` setting are swept at startup (only if clean — no uncommitted, no untracked, no unpushed).

### Subagent isolation: when to use

Use `isolation: worktree` when the subagent edits files that could collide (parent / sibling subagents), needs a custom CLAUDE.md (only path to swap per-agent — see recipe), or operates on a different ref (needs `WorktreeCreate` hook). Skip for read-only subagents, cost-sensitive flows (worktree setup + no prompt-cache reuse), or when the parent needs to see edits in-place.

### Recipe: custom CLAUDE.md per agent

Two paths:

- **Branch-based**: commit the alternate CLAUDE.md to a branch, set `worktree.baseRef: "head"` (or use a `WorktreeCreate` hook to check out that branch), spawn with `isolation: worktree`.
- **Hook-based**: a `WorktreeCreate` hook does the default `git worktree add`, overwrites CLAUDE.md in the worktree, prints the path on stdout (replacement contract). `WorktreeCreate` has no matcher — discriminate inside the hook from stdin.

### EnterWorktree / ExitWorktree (main session)

`EnterWorktree(name?, path?)` creates a new worktree or enters an existing one and switches session cwd.

`ExitWorktree(action: keep|remove, discard_changes?)` leaves the worktree session. `remove` refuses dirty worktrees without `discard_changes: true`. Operates only on worktrees entered via `EnterWorktree` this session.

Both honor `worktree.baseRef`. They also fire `WorktreeCreate` / `WorktreeRemove` hooks (L, per docs).

## Hooks

Most relevant for subagent work:

- `PreToolUse` / `PostToolUse` — before / after each tool call. PreToolUse fires INSIDE subagents.
- `SubagentStart` / `SubagentStop` — spawn / return; payload includes agent_id + agent_type.
- `WorktreeCreate` — **REPLACEMENT hook** (not observation). Fires BEFORE the subagent runs. Takes over worktree creation; built-in git logic bypassed. MUST return the worktree path on stdout (or `hookSpecificOutput.worktreePath`). A no-op hook → `WorktreeCreate hook failed: ... returned no worktree path` → creation aborts. Use for: custom base / path / branch, non-git VCS, shared worktrees, out-of-repo isolation. No matchers.
- `WorktreeRemove` (L per docs) — pure **OBSERVATION hook**. Cannot block; exit code + stderr ignored. Fires on subagent finish OR session exit, distinguished by `removal_reason` (`"subagent_finish"` / `"session_exit"`). Receives `worktree_path` + `removal_reason` on stdin. Not symmetric to `WorktreeCreate`.
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
- Call matches neither rule → behavior depends on parent's permission mode AND whether the specific call would prompt:
  - `bypassPermissions` / `acceptEdits` → call runs (K).
  - `auto` → background classifier decides per-call. Classifier-passed calls run; classifier-rejected calls auto-deny with `Permission to use Bash has been denied` (K — observed: `whoami` and `python --version` passed; `py --version` rejected, presumably command-pattern specific).
  - `default` (foreground subagent) → would prompt in main session; subagent has no UI → docs claim auto-deny (?, no default-mode parent in this session).
  - **Background subagent** (per docs + K-confirmed via `py --version`): auto-denies any call that would have prompted/classifier-rejected. Canonical error: `Permission to use Bash has been denied`.

**Worktree subagent caveat**: settings.local.json typically untracked → absent in worktree → its allow/deny rules don't apply for the worktree subagent. Tracked settings.json still applies. Effective permission set is leaner than parent's. If settings.local.json carries critical denies, propagate via `.worktreeinclude` or commit them.

**Settings allow does NOT re-expose stripped tools** — see composition.md "Tool surface".

**Disable a subagent type session-wide**: add `Agent(<name>)` to `permissions.deny` in settings.json, or use `--disallowedTools "Agent(<name>)"` on the CLI. Works for built-in and custom subagents.

## Session-start sequence

1. Settings layers merged (managed > CLI flags > `.local.json` > `.json` > user) — hooks registered, permissions evaluated.
2. `SessionStart` hook fires; its `additionalContext` is appended to Claude's context before the first inference.
3. Static config snapshot (loaded into context before first inference): CLAUDE.md hierarchy, skills catalog (frontmatter only — bodies lazy), agents catalog, MCP servers, tool schemas (gated by `tools:`).
4. `InstructionsLoaded` fires.
5. `UserPromptSubmit` fires per prompt thereafter.

Per-event hooks (`PreToolUse`, `SubagentStart/Stop`, etc.) fire at their moments, not at startup. Subagent variant: same snapshot at the subagent's cwd; Explore/Plan strip CLAUDE.md + gitStatus.

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

**`memory: user|project|local` frontmatter**: enables cross-session persistent memory for this agent. Per-scope directory:

- `user` → `~/.claude/agent-memory/<name>/` (shared across all your projects)
- `project` → `.claude/agent-memory/<name>/` (project-scoped, check in)
- `local` → `.claude/agent-memory-local/<name>/` (project-scoped, gitignored)

When `memory:` is set, Read/Write/Edit are auto-enabled and the first 200 lines (or 25KB) of `MEMORY.md` are injected into the agent's system prompt. Cross-AGENT sharing requires path overlap or going through files / MCP.

**Multi-step orchestration**: simulate continuation by sequential Agent calls from main session. Pattern: Agent #1 writes intermediate state to a file in cwd → Agent #2 starts from that file's content. Main session is the coordinator. `run_in_background: true` parallelizes independent legs; foreground is required when the next leg consumes the previous leg's output.

**Worktree subagent edits**: stay in the ephemeral worktree branch. To bring them into main: read the path + branch from the Agent tool result, then `git merge` / `git cherry-pick` / manual copy. No automatic merge.

**Subagent transcripts**: persisted at `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`, independent of main-conversation compaction. Cleaned up per `cleanupPeriodDays` (default 30 days). Allows resumption via `SendMessage` when Agent Teams is enabled.

**Subagent auto-compaction**: triggers at ~95% context capacity. `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=<n>` lowers the threshold (e.g., `50`). Compaction events are logged in the transcript as `compact_boundary` system entries.

## Hot-reload

- `.claude/agents/*.md` edited on disk: NOT hot-loaded. Restart required for the new definition to be callable.
- `.claude/agents/*.md` created/edited via the `/agents` interactive panel: takes effect immediately, no restart.
- Settings: Claude detects external edit, prompts review via `/hooks`. Not silent.
- CLAUDE.md, skills, MCP servers: snapshotted at session start.

## Settings.json keys (agent-relevant)

- `agent` — default main-session agent name (= `claude --agent <name>`).
- `env` — propagated env vars; use for fork mode / Agent Teams flags (see Experimental flags).
- `permissions.{allow,deny}` — runtime tool/arg gating; `deny: ["Agent(<name>)"]` disables a subagent type session-wide.
- `worktree.{baseRef, symlinkDirectories, sparsePaths, bgIsolation}` — worktree creation behavior; see Worktree mechanics.
- `cleanupPeriodDays` — orphan worktree + transcript sweep (default 30).

## Experimental flags

Both env-var-gated. Set in `settings.json` `"env"` block for persistence.

### `CLAUDE_CODE_FORK_SUBAGENT=1` — fork mode (≥ 2.1.117)

- Every subagent spawn auto-backgrounds regardless of `background:` (K — probed).
- `/fork <directive>` interactive command becomes available; spawns a real fork inheriting full conversation + tools + system prompt + prompt cache (verified path).
- Per docs, organic delegation to `general-purpose` should substitute to a fork. Probe finding: explicit `Agent(subagent_type="general-purpose")` tool calls from main session do NOT fork — token count stays at baseline subagent size, conversation history absent. The substitution likely applies only to Claude's interactive routing, not Agent-tool calls.
- A fork cannot spawn further forks.
- To disable background tasks while fork mode is on: `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`.
- Known issues (2026-05): forced-background path inherits open permission bugs (silent auto-deny, inconsistent prompts, `bypassPermissions` ineffective). See claude-code issues [#34095](https://github.com/anthropics/claude-code/issues/34095), [#21142](https://github.com/anthropics/claude-code/issues/21142), [#32402](https://github.com/anthropics/claude-code/issues/32402).

### `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` — Agent Teams

- Loads deferred tools: `SendMessage`, `TeamCreate`, `TeamDelete`.
- `SendMessage(to=<agentId>, message=...)` resumes a previously-spawned subagent with full prior conversation context (K — verified). If the target has no active task, it's "resumed from transcript in the background" and the reply comes via the standard async-notification path.
- The trailing `agentId: ...` hint in every Agent return becomes the resumption handle.
- Persistence layer: subagent transcripts (see Persistence section above).
- Known issues (2026-05): tooling unstable — tools may fail to load despite flag, SendMessage by *name* silently drops (use agent ID), TeamCreate can spawn 10-150× duplicate teammates, in-process teammates don't survive `/resume`. See claude-code issues [#34750](https://github.com/anthropics/claude-code/issues/34750), [#42999](https://github.com/anthropics/claude-code/issues/42999), [#55586](https://github.com/anthropics/claude-code/issues/55586).
