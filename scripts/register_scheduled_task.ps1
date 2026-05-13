# Registers (or re-registers) the Windows Task Scheduler job that runs
# scripts/refresh_and_deploy.ps1 four times a day. Idempotent: removes any
# existing task of the same name before creating.
#
# Run as the user account that should own the task. Does NOT require admin.
# Defaults to "only when logged in" mode — no password needed.
#
# Usage:
#   .\scripts\register_scheduled_task.ps1
#   .\scripts\register_scheduled_task.ps1 -Times '08:00','14:00','20:00','02:00'
#   .\scripts\register_scheduled_task.ps1 -RepoRoot 'D:\Projects\ntrip-mountpoint-map.scheduler'
#
# The scheduler should point at a dedicated clone of this repo so it can
# commit data/ refreshes without colliding with in-flight dev work.

[CmdletBinding()]
param(
    [string[]]$Times = @('07:00', '13:00', '19:00', '23:00'),
    [string]$TaskName = 'ntrip-mountpoint-map refresh + deploy',
    [string]$RepoRoot,
    [switch]$SkipGit,
    [switch]$SkipDeploy
)

$ErrorActionPreference = 'Stop'
if (-not $RepoRoot) { $RepoRoot = Split-Path -Parent $PSScriptRoot }
$RepoRoot = (Resolve-Path $RepoRoot).Path
$scriptPath = Join-Path $RepoRoot 'scripts/refresh_and_deploy.ps1'
$repoRoot = $RepoRoot

$extraArgs = ''
if ($SkipGit)    { $extraArgs += ' -SkipGit' }
if ($SkipDeploy) { $extraArgs += ' -SkipDeploy' }

if (-not (Test-Path $scriptPath)) { throw "Orchestrator not found at $scriptPath" }

# Sanity check: the target should be the data-refresh worktree, not the dev
# checkout. Refuse to register against any other branch unless -SkipGit is set
# (in which case the orchestrator won't touch git anyway).
if (-not $SkipGit) {
    $branch = (& git -C $RepoRoot rev-parse --abbrev-ref HEAD 2>$null)
    if ($LASTEXITCODE -ne 0) {
        throw "Could not read git branch at $RepoRoot (not a git repo?)."
    }
    $branch = $branch.Trim()
    if ($branch -ne 'data-refresh') {
        throw "Refusing to register: $RepoRoot is on branch '$branch', expected 'data-refresh'. Pass -SkipGit to override."
    }
}

# Remove existing task with the same name (idempotent).
$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Output "Removing existing task '$TaskName'..."
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

$action = New-ScheduledTaskAction `
    -Execute 'powershell.exe' `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`"$extraArgs" `
    -WorkingDirectory $repoRoot

$triggers = foreach ($t in $Times) {
    New-ScheduledTaskTrigger -Daily -At $t
}

# Run only when logged in (current user, interactive).
$principal = New-ScheduledTaskPrincipal `
    -UserId "$env:USERDOMAIN\$env:USERNAME" `
    -LogonType Interactive `
    -RunLevel Limited

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 15) `
    -RestartCount 2 `
    -RestartInterval (New-TimeSpan -Minutes 5)

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $triggers `
    -Principal $principal `
    -Settings $settings `
    -Description "Runs scripts/refresh_and_deploy.ps1 in $repoRoot. Local replacement for former GitHub Actions workflows." | Out-Null

Write-Output "Registered task '$TaskName' with triggers: $($Times -join ', ') (local time)."
Write-Output "Working dir:  $repoRoot"
Write-Output "Orchestrator: $scriptPath$extraArgs"
Write-Output "Logs:         $repoRoot\.tmp\refresh_and_deploy\"
Write-Output ""
Write-Output "To run now:        Start-ScheduledTask -TaskName '$TaskName'"
Write-Output "To view next run:  Get-ScheduledTaskInfo -TaskName '$TaskName'"
Write-Output "To remove:         Unregister-ScheduledTask -TaskName '$TaskName' -Confirm:`$false"
