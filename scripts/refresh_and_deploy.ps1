# Local replacement for the .github/workflows/update-stations.yml + deploy-pages.yml
# pipeline. Designed to be invoked by Windows Task Scheduler.
#
# Expects to run inside a git worktree on the `data-refresh` branch. The dev
# checkout sits on `main` in a sibling worktree sharing the same .git.
#
# data-refresh is NOT a long-lived branch with merge history. It is a rolling
# pointer that gets reset to main at the start of every run, then advanced by
# exactly one fresh data commit. Previous run's data commit is discarded — main
# is the source of truth for data (dev also commits data/ refreshes directly).
#
# Steps:
#   1. Reset data-refresh hard to main. Picks up any scripts/ updates and any
#      data/ commits dev landed on main since the last run. No rebase, no
#      merge — guarantees a conflict-free start.
#   2. Run scripts/fetch_stations.py (refreshes data/stations.json + sourcetables).
#   3. Commit data/ changes locally. Never pushes (GitHub auth blocked).
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

    # --- Step 1: reset data-refresh hard to main ----------------------------
    # Discards any previous run's data commit. Picks up the latest scripts/
    # (including fetch_stations.py itself) and any data/ commits dev landed
    # on main. No rebase, no merge: data-refresh is a single-commit-ahead
    # rolling pointer, not a branch with its own history.
    if (-not $SkipGit) {
        Write-Output "--- Step 1: reset data-refresh hard to main ---"

        $branch = (git rev-parse --abbrev-ref HEAD).Trim()
        if ($branch -ne 'data-refresh') {
            throw "Expected worktree on 'data-refresh' branch, found '$branch'. Refusing to run."
        }

        # Dirty check guards against silently nuking in-flight work in this
        # worktree. The scheduler is expected to leave a clean tree between
        # runs; anything dirty here means manual intervention left state.
        $dirty = git status --porcelain
        if (-not [string]::IsNullOrWhiteSpace($dirty)) {
            throw "Worktree is dirty at reset time; aborting. Investigate $repoRoot."
        }

        git reset --hard main
        if ($LASTEXITCODE -ne 0) { throw "git reset --hard main failed in $repoRoot" }
    } else {
        Write-Output "--- Step 1: reset skipped (-SkipGit) ---"
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
