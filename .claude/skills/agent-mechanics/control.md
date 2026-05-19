# Control: how you steer subagents from outside

## TOC

- Definition (agent file)
- Spawn-time controls (Agent tool params)
- Worktree mechanics
- Hooks (incl subagent + worktree events)
- Load order at session start
- Hot-reload semantics

## Definition (K)

**Location**: `.claude/agents/<name>.md` (project), `~/.claude/agents/` (user). Loaded at session start only. Hot-edit not picked up — creating a file mid-session returns `Agent type 'X' not found` until restart.

**Frontmatter fields**:

- `name` (K) — agent_type used in Agent calls
- `description` (K) — trigger text; auto-delegation cue
- `model` (K) — default model (sonnet/opus/haiku); overridable per call
- `tools` (K) — tool-NAME allowlist (comma- or space-separated). Two forms:
  - Allowlist: `tools: Read, Edit` → only those loaded
  - "All except" form (in some built-ins' descriptions): `All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit`
  - Bash arg-globs syntax appears (`Bash(py scripts/*)`) but is documentation only — see composition.md
- `disallowedTools` (L) — frontmatter field that subtracts from inherited pool. Same syntax as `tools` (comma- or space-separated bare tool names). No wildcards documented. If both `tools` and `disallowedTools` are set, `disallowedTools` is applied first, then `tools` is resolved against the remaining pool.
- `mcpServers` (L) — attaches additional MCP servers scoped to this subagent; only documented mechanism to ADD tool surface beyond parent's pool
- `permissionMode` (L) — ignored in subagents when parent is in `auto` mode; `bypassPermissions` / `acceptEdits` set in parent propagate and cannot be overridden by subagent frontmatter

**Body** (K) — appended verbatim to subagent system prompt as agent-specific role text. No length limit observed in probe; ntrip-research body ~3kB cited as upper-end without issue.

**Registration timing** (K): start-only. Restart required for any new or edited `.md` to take effect.

## Spawn-time controls (Agent tool params)

| Param | Type | Effect |
|-------|------|--------|
| `subagent_type` | string | picks agent definition; case-sensitive |
| `description` | string (3-5 words) | telemetry; shown to user |
| `prompt` | string | user-turn-equivalent content sent to subagent |
| `model` | enum: sonnet/opus/haiku | REPLACES agent frontmatter `model:` (L per docs + behaviorally consistent). `CLAUDE_CODE_SUBAGENT_MODEL` env var is session-scoped (applies to ALL subagents spawned in that session, overrides both call-site param + frontmatter). Resolution: env > call-site `model` > frontmatter > main convo model. |
| `isolation` | enum: `worktree` | spawns subagent in temporary git worktree of repo. See Worktree mechanics. (K) |
| `run_in_background` | boolean | detaches subagent; parent notified on completion (L) |

Composition: prompt is sent as user-turn to a fresh subagent context. No memory of parent conversation. To continue a previously-spawned agent, use `SendMessage` with the returned `agentId` instead of a new Agent call — preserves subagent's context.

Subagents cannot spawn nested subagents in most configs (K) — Agent tool absent from most subagent schemas. General-purpose may be an exception (?).

## Worktree mechanics

**Two distinct mechanisms** (K — schema-confirmed):

| Mechanism | Scope | Action |
|-----------|-------|--------|
| `Agent(..., isolation: "worktree")` | spawns SUBAGENT in temporary worktree | for isolated subagent work |
| `EnterWorktree` / `ExitWorktree` tools | switches MAIN session into a worktree | for interactive parallel branch work |

Do NOT confuse. The Agent isolation param is per-subagent-spawn; EnterWorktree is a main-session navigation move.

### Agent isolation: "worktree" (subagent spawn)

`Agent(..., isolation: "worktree")` creates a temporary git worktree from current branch, spawns subagent with that as its cwd. Per Agent tool description: "The worktree is automatically cleaned up if the agent makes no changes; otherwise the path and branch are returned in the result."

**Worktree path pattern observed**: `.claude\worktrees\agent-<id>\` (K — surfaced via hook error message when worktree subagent triggered PreToolUse hook).

Implications:

- Subagent cwd = worktree path, not main repo path (K).
- Subagent CLAUDE.md propagates to worktree subagent (K — confirmed via marker probe in worktree subagent: "Scope: NTRIP map" present in context). When the worktree's CLAUDE.md differs from main, the subagent would see the variant — this is the per-subagent CLAUDE.md customization path (L — full path-substitution not directly tested, but CLAUDE.md inheritance verified).
- gitStatus context for subagent reflects worktree, not main (L — not directly verified; was blocked by hook).
- Useful for risky autonomous edits — failures don't dirty main checkout.

**GOTCHA — untracked hook scripts break worktree subagents** (K — observed): `git worktree add` checks out tracked files only. If `settings.json` hooks invoke a script at a path that is untracked in main (e.g. `.claude/hooks/log-event.py` when `.claude/hooks/` is gitignored or just not added), the worktree won't have it. Every hook fire in the worktree subagent then errors, blocking all gated tool calls. Symptoms: tool_uses > 0 but every result is a `PreToolUse:<Tool> hook error: ... can't open file '<worktree-path>\.claude\hooks\<script>.py'`. Fix: commit hook scripts, or use absolute paths in settings, or wrap script invocation in a path-existence check.

Cleanup (K — from tool description):

- No changes → worktree auto-removed, no trace.
- Changes → worktree path + branch name returned in Agent result; caller decides to merge, keep, or discard.

### EnterWorktree / ExitWorktree (main session)

`EnterWorktree(name?, path?)` — creates a new worktree inside `.claude/worktrees/` (or enters an existing one passed via `path`) and switches the session's cwd into it. Use ONLY when user explicitly says "worktree" or CLAUDE.md directs it. (K — schema doc)

`worktree.baseRef` setting (K): controls base ref for new worktrees. `fresh` (default) branches from `origin/<default-branch>`; `head` branches from current local HEAD.

`ExitWorktree(action: keep|remove, discard_changes?)` (K): leaves the worktree session.

- `keep` — worktree directory and branch stay on disk.
- `remove` — deletes worktree directory and branch. Refuses if uncommitted files or unmerged commits unless `discard_changes: true`.

Scope: only operates on worktrees this session entered via EnterWorktree. No-op otherwise. Will NOT touch manually-created or previous-session worktrees.

VCS-agnostic outside git: EnterWorktree delegates to `WorktreeCreate`/`WorktreeRemove` hooks per its docs — confirming those hooks exist (K via tool-doc reference).

## Hooks

**Hook firing in subagents** (K — confirmed via `.tmp/hook_log.tsv` inspection):
- SessionStart, InstructionsLoaded, UserPromptSubmit, PreToolUse, SubagentStart, SubagentStop, SessionEnd all fire in this session.
- SubagentStart/Stop log captures `agent_id` + `agent_type` fields.
- PreToolUse fires INSIDE subagent execution: log row shows ntrip-research subagent (`agent_id=adc3f7de879ee6f58`) generating PreToolUse for Bash.
- For SPARSE events (SessionStart, InstructionsLoaded, SessionEnd, SubagentStart, SubagentStop) the local `log-event.py` also emits `hookSpecificOutput.additionalContext` with `[hook-marker <ts>] <event> ...` — visible in Claude's own context. That's why SessionStart's hook-marker appeared in the conversation.

**Hook events** (L per docs, all listed stable; K for the 7 wired in this repo):

| Event | Notes |
|-------|-------|
| `SessionStart` / `SessionEnd` | top-level session lifecycle |
| `UserPromptSubmit` | user submits a prompt |
| `PreToolUse` / `PostToolUse` | before / after each tool call |
| `Stop` | Claude finishes response |
| `Notification` | UI notification path |
| `PreCompact` | before context auto-compaction |
| `PermissionRequest` | permission dialog appears |
| `InstructionsLoaded` | CLAUDE.md / rules loaded |
| `SubagentStart` / `SubagentStop` | subagent spawn / return |
| `WorktreeCreate` | fires on `--worktree` CLI flag OR `Agent(isolation: "worktree")` subagent spawn (L per docs). For non-git VCS, replaces default git worktree logic. No matchers. |
| `WorktreeRemove` | fires on session exit if worktree retained, or when isolation subagent finishes (L). No matchers. |

**Hook load vs fire timing** (L):

- Hook *definitions* load with settings (early; before CLAUDE.md), so `SessionStart` and `InstructionsLoaded` can fire correctly.
- Hook *runs* on the lifecycle event it subscribes to. Snapshotted at session start; mid-session edits to settings prompt review via `/hooks`, not silent apply.

**Hook semantics** (L):

- Exit code 2 blocks + routes stderr to Claude. Exit code 1 prints stderr but does NOT block. Most common security-gate footgun.
- PostToolUse cannot undo — tool already ran. Use PreToolUse to prevent.
- Matchers case-sensitive PascalCase (`Bash`, not `bash`).
- Multiple matching hooks run in parallel; deny beats allow.
- PreToolUse `permissionDecision: "deny"` overrides `--dangerously-skip-permissions`.
- Shell-profile (`.zshrc`, `.bashrc`) echo statements prepend garbage to JSON stdin → silent breakage.
- Performance: Node/Python spawn per event can reach ~20s/turn. Target <1-2s.

**Repo wiring** (K — `.claude/settings.local.json` of this repo): SessionStart, UserPromptSubmit, InstructionsLoaded, PreToolUse, SubagentStart, SubagentStop, SessionEnd all wired to `py .claude/hooks/log-event.py`. PostToolUse, Stop, Notification, PreCompact, PermissionRequest, WorktreeCreate, WorktreeRemove not wired.

## Load order at session start

1. System prompt (internal)
2. Settings (precedence: managed > CLI flags > `.local.json` > `.json` > user `~/.claude/`) — includes hook definitions
3. CLAUDE.md (concatenation across project + user + enterprise; conflicts resolved arbitrarily)
4. Skills catalog (frontmatter at start; body lazy on invocation)
5. Agents catalog (`.claude/agents/` + parents + user)
6. MCP servers
7. Hook activation (definitions from #2 wired to lifecycle events; events begin firing)
8. Tool schemas

Subagent variant: same sequence in worktree's cwd; layers #3 + #8 stripped for Explore/Plan; agent-body composes onto #1.

## Hot-reload

- `.claude/agents/*.md` files: NOT hot-loaded. Restart required (K).
- Settings files: Claude detects external edit and prompts review via `/hooks`. Not silent (L).
- CLAUDE.md, skills, MCP servers: snapshotted at session start (L).
