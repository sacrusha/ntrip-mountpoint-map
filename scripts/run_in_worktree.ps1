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

    # --- Fetch stations ----------------------------------------------------
    Write-Output "--- Step 1: fetch_stations.py ---"
    & py -X utf8 scripts/fetch_stations.py
    # Belt-and-braces: `& py` with py-launcher missing raises CommandNotFound
    # under EAP=Stop, but if EAP changes elsewhere, a `$null` $LASTEXITCODE
    # would slip past a bare `-ne 0` check. Test both.
    if (-not $? -or $LASTEXITCODE -ne 0) { throw "fetch_stations.py failed (exit code: $LASTEXITCODE)" }

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
