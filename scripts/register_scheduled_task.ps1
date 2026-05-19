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
#   .\scripts\register_scheduled_task.ps1 -RepoRoot 'D:\Projects\ntrip-mountpoint-map'
#
# The orchestrator creates an ephemeral worktree from main each run, so this
# can point at any worktree of the repo (dev's main checkout is the obvious
# choice). The host worktree's branch does not matter — refresh_and_deploy.ps1
# always builds from main.

[CmdletBinding()]
param(
    [string[]]$Times = @('07:00', '13:00', '19:00', '23:00'),
    [string]$TaskName = 'ntrip-mountpoint-map refresh + deploy',
    [string]$RepoRoot,
    [switch]$SkipDeploy
)

$ErrorActionPreference = 'Stop'
if (-not $RepoRoot) { $RepoRoot = Split-Path -Parent $PSScriptRoot }
$RepoRoot = (Resolve-Path $RepoRoot).Path
$scriptPath = Join-Path $RepoRoot 'scripts/refresh_and_deploy.ps1'

$extraArgs = ''
if ($SkipDeploy) { $extraArgs += ' -SkipDeploy' }

if (-not (Test-Path $scriptPath)) { throw "Orchestrator not found at $scriptPath" }

# Sanity check: the target must be a git worktree (the orchestrator uses
# `git worktree add` from it) and must have a local `main` ref (the
# orchestrator always builds from main).
$inRepo = & git -C $RepoRoot rev-parse --is-inside-work-tree 2>$null
if ($LASTEXITCODE -ne 0 -or $inRepo.Trim() -ne 'true') {
    throw "Not a git worktree: $RepoRoot"
}
& git -C $RepoRoot rev-parse --verify --quiet refs/heads/main *> $null
if ($LASTEXITCODE -ne 0) {
    throw "Local branch 'main' not found at $RepoRoot. The orchestrator builds from main."
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
    -WorkingDirectory $RepoRoot

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
    -Description "Runs scripts/refresh_and_deploy.ps1 in $RepoRoot. Local replacement for former GitHub Actions workflows." | Out-Null

Write-Output "Registered task '$TaskName' with triggers: $($Times -join ', ') (local time)."
Write-Output "Working dir:  $RepoRoot"
Write-Output "Orchestrator: $scriptPath$extraArgs"
Write-Output "Logs:         $RepoRoot\.tmp\refresh_and_deploy\"
Write-Output ""
Write-Output "To run now:        Start-ScheduledTask -TaskName '$TaskName'"
Write-Output "To view next run:  Get-ScheduledTaskInfo -TaskName '$TaskName'"
Write-Output "To remove:         Unregister-ScheduledTask -TaskName '$TaskName' -Confirm:`$false"
