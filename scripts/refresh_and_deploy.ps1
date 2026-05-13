# Local replacement for the .github/workflows/update-stations.yml + deploy-pages.yml
# pipeline. Designed to be invoked by Windows Task Scheduler.
#
# Expects to run inside a git worktree on the `data-refresh` branch. The dev
# checkout sits on `main` in a sibling worktree sharing the same .git.
#
# Steps:
#   1. Rebase data-refresh onto main, so this run picks up the latest scripts
#      (including any updates to fetch_stations.py itself) and any tree
#      changes from dev.
#   2. Run scripts/fetch_stations.py (refreshes data/stations.json + sourcetables).
#   3. Commit data/ changes locally. Never pushes (GitHub auth blocked).
#      Result: data-refresh sits exactly one commit ahead of main. Dev brings
#      data in via: git merge --ff-only data-refresh
#   4. Run scripts/deploy_pages.ps1 to publish to Cloudflare Pages.
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

    # --- Step 1: rebase data-refresh onto main ------------------------------
    # Picks up any updates to scripts/ (including fetch_stations.py itself)
    # and any other tree changes from dev before we run the fetcher.
    if (-not $SkipGit) {
        Write-Output "--- Step 1: rebase data-refresh onto main ---"

        $branch = (git rev-parse --abbrev-ref HEAD).Trim()
        if ($branch -ne 'data-refresh') {
            throw "Expected worktree on 'data-refresh' branch, found '$branch'. Refusing to run."
        }

        $dirty = git status --porcelain
        if (-not [string]::IsNullOrWhiteSpace($dirty)) {
            throw "Worktree is dirty at rebase time; aborting. Investigate $repoRoot."
        }

        git rebase main
        if ($LASTEXITCODE -ne 0) {
            git rebase --abort 2>$null
            throw "git rebase main failed; resolve manually in $repoRoot"
        }
    } else {
        Write-Output "--- Step 1: rebase skipped (-SkipGit) ---"
    }

    # --- Step 2: fetch stations ---------------------------------------------
    Write-Output "--- Step 2: fetch_stations.py ---"
    & py -X utf8 scripts/fetch_stations.py
    if ($LASTEXITCODE -ne 0) { throw "fetch_stations.py exited with code $LASTEXITCODE" }

    # --- Step 3: commit data/ ----------------------------------------------
    if (-not $SkipGit) {
        Write-Output "--- Step 3: commit data/ on data-refresh ---"
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
        Write-Output "--- Step 3: commit skipped (-SkipGit) ---"
    }

    # --- Step 4: deploy -----------------------------------------------------
    if (-not $SkipDeploy) {
        Write-Output "--- Step 4: deploy_pages.ps1 ---"
        & (Join-Path $PSScriptRoot 'deploy_pages.ps1')
    } else {
        Write-Output "--- Step 4: skipped (-SkipDeploy) ---"
    }

    Write-Output "=== refresh_and_deploy.ps1 succeeded ==="
} catch {
    Write-Output "=== refresh_and_deploy.ps1 FAILED: $($_.Exception.Message) ==="
    Stop-Transcript | Out-Null
    exit 1
}

Stop-Transcript | Out-Null
