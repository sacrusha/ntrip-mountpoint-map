# Local replacement for the .github/workflows/update-stations.yml + deploy-pages.yml
# pipeline. Designed to be invoked by Windows Task Scheduler.
#
# Expects to run inside a git worktree on the `data-refresh` branch. The dev
# checkout sits on `main` in a sibling worktree sharing the same .git.
#
# Steps:
#   1. Run scripts/fetch_stations.py (refreshes data/stations.json + data/source_health.json).
#   2. Rebase data-refresh onto main so this run sits exactly one commit ahead
#      of main, then commit data/ changes locally. Never pushes (GitHub auth
#      blocked). Dev fast-forward-merges data-refresh into main when wanted:
#         git merge --ff-only data-refresh
#   3. Run scripts/deploy_pages.ps1 to publish to Cloudflare Pages.
#
# Logs every run to .tmp/refresh_and_deploy/<UTC-timestamp>.log.

[CmdletBinding()]
param(
    [switch]$SkipGit,
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

try {
    Write-Output "=== refresh_and_deploy.ps1 run at $stamp UTC ==="

    # --- Step 1: fetch stations ---------------------------------------------
    Write-Output "--- Step 1: fetch_stations.py ---"
    & py -X utf8 scripts/fetch_stations.py
    if ($LASTEXITCODE -ne 0) { throw "fetch_stations.py exited with code $LASTEXITCODE" }

    # --- Step 2: rebase onto main + local commit of data/ -------------------
    # Worktree-aware: this script runs in the data-refresh worktree.
    # Before committing today's data refresh, rebase onto main so we end up
    # exactly one commit ahead of main. Never pushes (GitHub auth blocked).
    if (-not $SkipGit) {
        Write-Output "--- Step 2: rebase data-refresh onto main + commit data/ ---"

        $branch = (git rev-parse --abbrev-ref HEAD).Trim()
        if ($branch -ne 'data-refresh') {
            throw "Expected worktree on 'data-refresh' branch, found '$branch'. Refusing to commit."
        }

        # Any uncommitted fetcher output would block the rebase. Stash if dirty.
        $dirty = git status --porcelain
        $stashed = $false
        if (-not [string]::IsNullOrWhiteSpace($dirty)) {
            git stash push --include-untracked --message "refresh_and_deploy auto-stash $stamp"
            if ($LASTEXITCODE -ne 0) { throw "git stash failed" }
            $stashed = $true
        }

        git rebase main
        if ($LASTEXITCODE -ne 0) {
            git rebase --abort 2>$null
            if ($stashed) { git stash pop }
            throw "git rebase main failed; resolve manually in $repoRoot"
        }

        if ($stashed) {
            git stash pop
            if ($LASTEXITCODE -ne 0) { throw "git stash pop failed (conflict?)" }
        }

        # Now commit any data/ changes (from the fetch step, plus anything
        # that came back via the stash pop).
        $dirty = git status --porcelain data/
        if ([string]::IsNullOrWhiteSpace($dirty)) {
            Write-Output "No changes to data/; nothing to commit."
        } else {
            git add data/
            if ($LASTEXITCODE -ne 0) { throw "git add failed" }

            git diff --cached --quiet -- data/stations.json
            $stationsChanged = ($LASTEXITCODE -ne 0)

            if (-not $stationsChanged) {
                $msg = 'chore(pipeline): heartbeat — refresh source health timestamps'
            } else {
                $counts = & py -c "import json; d=json.load(open('data/stations.json')); print(len(d['sources'].get('rtk2go',{}).get('stations',[])), len(d['sources'].get('centipede',{}).get('stations',[])))"
                $parts = $counts.Trim().Split(' ')
                $rtk = $parts[0]; $cp = $parts[1]
                $msg = "chore(data): refresh NTRIP stations ($rtk rtk2go, $cp centipede)"
            }

            git commit -m $msg
            if ($LASTEXITCODE -ne 0) { throw "git commit failed" }
            Write-Output "Committed on data-refresh: $msg"
        }
    } else {
        Write-Output "--- Step 2: skipped (-SkipGit) ---"
    }

    # --- Step 3: deploy -----------------------------------------------------
    if (-not $SkipDeploy) {
        Write-Output "--- Step 3: deploy_pages.ps1 ---"
        & (Join-Path $PSScriptRoot 'deploy_pages.ps1')
    } else {
        Write-Output "--- Step 3: skipped (-SkipDeploy) ---"
    }

    Write-Output "=== refresh_and_deploy.ps1 succeeded ==="
} catch {
    Write-Output "=== refresh_and_deploy.ps1 FAILED: $($_.Exception.Message) ==="
    Stop-Transcript | Out-Null
    exit 1
}

Stop-Transcript | Out-Null
