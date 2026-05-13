# Local replacement for the .github/workflows/update-stations.yml + deploy-pages.yml
# pipeline. Designed to be invoked by Windows Task Scheduler on the cron that
# used to run in GHA (01:00, 07:00, 13:00, 19:00 UTC).
#
# Steps:
#   1. Run scripts/fetch_stations.py (refreshes data/stations.json + data/source_health.json).
#   2. If data/ changed, commit + push to origin/main with rebase-retry.
#   3. Always run scripts/deploy_pages.ps1 to publish to Cloudflare Pages.
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

    # --- Step 2: local commit of data/ --------------------------------------
    # No push: GitHub has disabled this account's Actions + write access, so
    # the scheduler runs in a dedicated local clone and never pushes upstream.
    # Local commits give us a rollback history if a fetch goes sideways.
    if (-not $SkipGit) {
        Write-Output "--- Step 2: local commit of data/ ---"
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
            Write-Output "Committed locally: $msg"
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
