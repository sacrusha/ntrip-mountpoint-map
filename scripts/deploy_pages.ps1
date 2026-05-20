# Deploy ntrip-mountpoint-map to Cloudflare Pages from this machine.
# Mirrors .github/workflows/deploy-pages.yml staging + wrangler invocation.
#
# Setup:
#   1. Put CF_API_TOKEN + CF_ACCOUNT_ID in .env/cloudflare.conf (see .env.example).
#   2. Ensure wrangler is on PATH (`npm i -g wrangler`).
#
# Usage (from repo root):
#   powershell.exe -File scripts/deploy_pages.ps1
#   powershell.exe -File scripts/deploy_pages.ps1 -Branch preview   # deploy to a preview branch

[CmdletBinding()]
param(
    [string]$Branch = 'main',
    [string]$ProjectName = 'ntrip-mountpoint-map'
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
# Push-Location + Pop-Location keeps the CWD change scoped to this script so
# the caller (e.g. run_in_worktree.ps1) doesn't end up with a dangling CWD
# inside the worktree after we return.
Push-Location $repoRoot
try {

# --- Load .env/cloudflare.conf -----------------------------------------------
$envFile = Join-Path $repoRoot '.env/cloudflare.conf'
if (-not (Test-Path $envFile)) {
    throw "Secrets file not found at $envFile. See .env.example for format."
}
Get-Content $envFile | ForEach-Object {
    $line = $_.Trim()
    if ($line -eq '' -or $line.StartsWith('#')) { return }
    $eq = $line.IndexOf('=')
    if ($eq -lt 1) { return }
    $name = $line.Substring(0, $eq).Trim()
    $value = $line.Substring($eq + 1).Trim().Trim('"').Trim("'")
    Set-Item -Path "Env:$name" -Value $value
}

if (-not $env:CF_API_TOKEN)   { throw "CF_API_TOKEN missing from .env" }
if (-not $env:CF_ACCOUNT_ID)  { throw "CF_ACCOUNT_ID missing from .env" }

# Wrangler reads CLOUDFLARE_* names.
$env:CLOUDFLARE_API_TOKEN  = $env:CF_API_TOKEN
$env:CLOUDFLARE_ACCOUNT_ID = $env:CF_ACCOUNT_ID

# --- Stage site --------------------------------------------------------------
$siteDir = Join-Path $repoRoot '_site'
if (Test-Path $siteDir) { Remove-Item -Recurse -Force $siteDir }
New-Item -ItemType Directory -Path $siteDir | Out-Null
New-Item -ItemType Directory -Path (Join-Path $siteDir 'data') | Out-Null

$rootFiles = @('index.html', 'guide.html', 'robots.txt', 'sitemap.xml', 'og-preview.png', 'favicon.svg')
foreach ($f in $rootFiles) {
    $src = Join-Path $repoRoot $f
    if (-not (Test-Path $src)) { throw "Missing site file: $f" }
    Copy-Item $src -Destination $siteDir
}

$dataFiles = @('stations.json', 'source_health.json', 'rtk_map.json', 'help_topics.json')
foreach ($f in $dataFiles) {
    $src = Join-Path $repoRoot "data/$f"
    if (-not (Test-Path $src)) { throw "Missing data file: data/$f" }
    Copy-Item $src -Destination (Join-Path $siteDir 'data')
}

Write-Output "Staged site to $siteDir"

# --- Deploy ------------------------------------------------------------------
& wrangler pages deploy $siteDir --project-name=$ProjectName --branch=$Branch
if (-not $? -or $LASTEXITCODE -ne 0) { throw "wrangler failed (exit code: $LASTEXITCODE)" }

Write-Output "Deploy complete."

} finally {
    Pop-Location
}
