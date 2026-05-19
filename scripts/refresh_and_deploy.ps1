# Local replacement for the .github/workflows/update-stations.yml + deploy-pages.yml
# pipeline. Designed to be invoked by Windows Task Scheduler.
#
# This is the OUTER orchestrator. It creates a throwaway worktree from main,
# copies secrets into it, invokes the inner script (run_in_worktree.ps1) which
# does the actual fetch + deploy, then deletes the worktree. Nothing persists
# between runs except logs.
#
# Why ephemeral: previous design ran in a long-lived `.scheduler` worktree on
# `data-refresh`. Any partial state (mid-rebase, dirty tree, lock files) would
# wedge subsequent runs. With an ephemeral worktree, every run starts from a
# clean checkout of main's tip and leaves nothing behind to corrupt.
#
# Task Scheduler should invoke this script from the dev worktree's repo root
# (the one on branch `main`), NOT from `.scheduler` (which is obsolete and
# should be removed).
#
# Logs every run to .tmp/refresh_and_deploy/<UTC-timestamp>.log in the
# orchestrator's repo root (NOT inside the ephemeral worktree, which would
# disappear with it).

[CmdletBinding()]
param(
    [switch]$SkipDeploy
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

# --- Logging -----------------------------------------------------------------
$logDir = Join-Path $repoRoot '.tmp/refresh_and_deploy'
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }
$stamp = (Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssZ')
$logFile = Join-Path $logDir "$stamp.log"
Start-Transcript -Path $logFile -Append | Out-Null

# Prune logs older than 30 days so .tmp/ doesn't grow unbounded.
Get-ChildItem $logDir -Filter '*.log' | Where-Object { $_.LastWriteTimeUtc -lt (Get-Date).ToUniversalTime().AddDays(-30) } | Remove-Item -Force -ErrorAction SilentlyContinue

$worktreePath = Join-Path $repoRoot ".tmp/scheduler-run-$stamp"

try {
    Write-Output "=== refresh_and_deploy.ps1 run at $stamp UTC ==="

    # --- Stale-worktree cleanup --------------------------------------------
    # If a previous run was killed (Task Scheduler timeout, reboot, etc.) its
    # worktree dir is still on disk. Force-remove any leftover scheduler-run
    # worktrees before creating a new one. `git worktree prune` clears entries
    # whose dir is gone; we then nuke any dirs that survived.
    Write-Output "--- Cleanup: prune stale worktrees ---"
    git worktree prune
    Get-ChildItem (Join-Path $repoRoot '.tmp') -Directory -Filter 'scheduler-run-*' -ErrorAction SilentlyContinue | ForEach-Object {
        $stale = $_.FullName
        Write-Output "Removing stale worktree: $stale"
        git worktree remove --force $stale 2>&1 | Out-Null
        if (Test-Path $stale) { Remove-Item -Recurse -Force $stale -ErrorAction SilentlyContinue }
    }

    # --- Create ephemeral worktree -----------------------------------------
    Write-Output "--- Create ephemeral worktree at $worktreePath ---"
    git worktree add --detach $worktreePath main
    if ($LASTEXITCODE -ne 0) { throw "git worktree add failed" }

    # --- Copy secrets ------------------------------------------------------
    # .env/ is gitignored, so the fresh worktree won't have it. deploy_pages.ps1
    # reads .env/cloudflare.conf. Copy the whole .env/ dir verbatim.
    $envSrc = Join-Path $repoRoot '.env'
    if (Test-Path $envSrc) {
        Copy-Item -Recurse -Force $envSrc (Join-Path $worktreePath '.env')
        Write-Output "Copied .env/ into worktree"
    } else {
        Write-Output "WARNING: no .env/ at $envSrc; deploy step will fail if not -SkipDeploy"
    }

    # --- Invoke inner script -----------------------------------------------
    $innerScript = Join-Path $worktreePath 'scripts/run_in_worktree.ps1'
    if (-not (Test-Path $innerScript)) { throw "Inner script not found at $innerScript" }
    $innerArgs = @{}
    if ($SkipDeploy) { $innerArgs['SkipDeploy'] = $true }
    & $innerScript @innerArgs
    if ($LASTEXITCODE -ne 0) { throw "inner script exited with code $LASTEXITCODE" }

    Write-Output "=== refresh_and_deploy.ps1 succeeded ==="
} catch {
    Write-Output "=== refresh_and_deploy.ps1 FAILED: $($_.Exception.Message) ==="
    Stop-Transcript | Out-Null
    # Best-effort cleanup even on failure. Postmortem state lives in the log
    # plus the inner script's own output; the worktree itself holds nothing
    # we need to inspect.
    git worktree remove --force $worktreePath 2>&1 | Out-Null
    if (Test-Path $worktreePath) { Remove-Item -Recurse -Force $worktreePath -ErrorAction SilentlyContinue }
    exit 1
}

# --- Cleanup ---------------------------------------------------------------
git worktree remove --force $worktreePath 2>&1 | Out-Null
if (Test-Path $worktreePath) { Remove-Item -Recurse -Force $worktreePath -ErrorAction SilentlyContinue }

Stop-Transcript | Out-Null
