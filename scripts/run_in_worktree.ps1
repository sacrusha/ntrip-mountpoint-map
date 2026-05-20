# Inner script for the refresh + deploy pipeline. Invoked by
# refresh_and_deploy.ps1 from inside an ephemeral worktree. Runs the actual
# work: fetch fresh NTRIP data, then deploy to Cloudflare Pages.
#
# Lives in scripts/ on main so every ephemeral worktree carries a fresh copy.
# No git operations: no commit, no push. The outer orchestrator destroys this
# worktree after this script returns.
#
# CWD discipline: Push-Location + Pop-Location keep the working dir change
# scoped to this script. The outer orchestrator can `Remove-Item` the worktree
# immediately after this returns without the process holding a handle inside it.

[CmdletBinding()]
param(
    [switch]$SkipDeploy
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot

Push-Location $repoRoot
try {
    Write-Output "--- run_in_worktree.ps1 in $repoRoot ---"

    # --- Refresh data ------------------------------------------------------
    # Python orchestrator: imports fetch_stations + assign_colors and runs
    # both in one process. Cache stickiness for color_assignments.json comes
    # from main's last-committed copy that the worktree carries; ephemeral
    # updates here are discarded with the worktree but published to CF Pages
    # by the deploy step below.
    Write-Output "--- Step 1: refresh_data.py (fetch_stations + assign_colors) ---"
    & py -X utf8 scripts/refresh_data.py
    # Belt-and-braces: `& py` with py-launcher missing raises CommandNotFound
    # under EAP=Stop, but if EAP changes elsewhere, a `$null` $LASTEXITCODE
    # would slip past a bare `-ne 0` check. Test both.
    if (-not $? -or $LASTEXITCODE -ne 0) { throw "refresh_data.py failed (exit code: $LASTEXITCODE)" }

    # --- Deploy ------------------------------------------------------------
    if (-not $SkipDeploy) {
        Write-Output "--- Step 2: deploy_pages.ps1 ---"
        & (Join-Path $PSScriptRoot 'deploy_pages.ps1')
        if (-not $? -or $LASTEXITCODE -ne 0) { throw "deploy_pages.ps1 failed (exit code: $LASTEXITCODE)" }
    } else {
        Write-Output "--- Step 2: deploy skipped (-SkipDeploy) ---"
    }
} finally {
    Pop-Location
}
