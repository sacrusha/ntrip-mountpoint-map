# Control: how you steer subagents from outside

## Definition

**Location**: `.claude/agents/<name>.md` (project), `~/.claude/agents/` (user). Loaded at session start only — hot-edit returns `Agent type 'X' not found` until restart.

**Frontmatter**:

- `name` — agent_type used in Agent calls
- `description` — trigger text; auto-delegation cue
- `model` — default model; overridable per call
- `tools` — tool-NAME allowlist (comma- or space-separated). Two forms: allowlist (`tools: Read, Edit`) or "All tools except X, Y" (built-in descriptions). Bash arg-globs are documentation only — see composition.md.
- `disallowedTools` (L) — subtracts from inherited pool. Same syntax as `tools`. No wildcards. If both set, `disallowedTools` applied first.
- `mcpServers` (L) — attaches additional MCP servers scoped to this subagent; only documented widening mechanism.
- `permissionMode` (L) — ignored when parent is `auto`; parent `bypassPermissions`/`acceptEdits` propagate and override subagent.

**Body** appended verbatim.

## Spawn-time controls (Agent tool)

| Param | Effect |
|-------|--------|
| `subagent_type` | picks agent definition; case-sensitive |
| `description` | telemetry; user-visible |
| `prompt` | user-turn-equivalent input; no memory of parent convo |
| `model` (sonnet/opus/haiku) | REPLACES frontmatter `model:`. Resolution: env `CLAUDE_CODE_SUBAGENT_MODEL` (session-scoped) > call-site > frontmatter > main convo |
| `isolation: "worktree"` | spawns subagent in temporary git worktree |
| `run_in_background` (L) | detaches; parent notified on completion |

Each Agent call is one-shot from main session — no built-in continuation. (Trailing `agentId: ... (use SendMessage with to: ...)` hints in Agent output are Claude Agent SDK leakage; `SendMessage` is not a main-session tool.)

Subagents typically cannot spawn nested subagents — `Agent` absent from most subagent schemas.

## Worktree mechanics

Two distinct mechanisms:

| Mechanism | Scope |
|-----------|-------|
| `Agent(..., isolation: "worktree")` | spawns SUBAGENT in ephemeral worktree |
| `EnterWorktree` / `ExitWorktree` tools | switches MAIN session into a worktree |

### Agent isolation worktree

Creates a temporary git worktree from current branch at `.claude/worktrees/agent-<id>/`. Subagent cwd = worktree path. Subagent loads CLAUDE.md from worktree — so a customized CLAUDE.md in the worktree branch yields per-subagent context.

Cleanup per Agent tool docs:

- No changes → worktree auto-removed.
- Changes → worktree path + branch returned; caller decides merge/keep/discard.

**Untracked-files gotcha**: `git worktree add` checks out tracked files only. Hook scripts in gitignored paths are absent from the worktree → every hook fire errors → all tool calls in the worktree subagent block. Fix: commit hook scripts, use absolute paths in settings, or guard the hook command with a path-existence check.

### EnterWorktree / ExitWorktree (main session)

`EnterWorktree(name?, path?)` creates a new worktree in `.claude/worktrees/` (or enters an existing one) and switches session cwd. Use only when explicitly directed.

`worktree.baseRef` setting: `fresh` (default, from `origin/<default-branch>`) or `head` (current local HEAD).

`ExitWorktree(action: keep|remove, discard_changes?)` leaves the worktree session. `remove` refuses dirty worktrees without `discard_changes: true`. Operates only on worktrees entered via `EnterWorktree` this session.

VCS-agnostic outside git: EnterWorktree delegates to `WorktreeCreate` / `WorktreeRemove` hooks per docs.

## Hooks

Most relevant for subagent work:

- `PreToolUse` / `PostToolUse` — before / after each tool call. PreToolUse fires INSIDE subagents.
- `SubagentStart` / `SubagentStop` — spawn / return; payload includes agent_id + agent_type.
- `WorktreeCreate` / `WorktreeRemove` (K) — **REPLACEMENT hooks**, not pure observation. They are effectively the arguments API for `Agent(isolation: "worktree")`, which itself takes no caller knobs (just the binary flag). When wired, the hook command takes over worktree creation/removal entirely; the built-in git logic is bypassed. `WorktreeCreate` fires BEFORE the subagent runs, and its command MUST return the worktree path via stdout (or `hookSpecificOutput.worktreePath` for http/callback variants). A no-op logging hook returns no path → `WorktreeCreate hook failed: hook succeeded but returned no worktree path` → worktree creation aborts. Use cases: custom base ref / path / branch naming, non-git VCS (svn/hg/perforce), shared worktrees across calls, fenced-off untrusted-code isolation outside the repo. Default (no hook wired) = built-in git logic with the project's `worktree.baseRef` setting. No matchers.
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

## Hot-reload

- `.claude/agents/*.md`: NOT hot-loaded. Restart required.
- Settings: Claude detects external edit, prompts review via `/hooks`. Not silent.
- CLAUDE.md, skills, MCP servers: snapshotted at session start.
