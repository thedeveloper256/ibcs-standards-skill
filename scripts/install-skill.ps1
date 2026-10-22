#Requires -Version 5.1
[CmdletBinding()]
param(
    [string]$Target = ".opencode/skills/ibcs-standards",
    [switch]$Global,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$repo = "thedeveloper256/ibcs-standards-skill"
$archive = Join-Path $env:TEMP "ibcs-standards-skill.zip"
$tempRoot = Join-Path $env:TEMP ("ibcs-standards-skill-" + [guid]::NewGuid().ToString("N"))

if ($Global) {
    $Target = Join-Path $HOME ".config/opencode/skills/ibcs-standards"
}

try {
    Invoke-WebRequest -Uri "https://github.com/$repo/archive/refs/heads/main.zip" -OutFile $archive
    Expand-Archive -Path $archive -DestinationPath $tempRoot -Force

    $sourceRoot = Get-ChildItem $tempRoot -Directory | Select-Object -First 1
    if (-not $sourceRoot) {
        throw "The downloaded archive is empty."
    }

    $source = Join-Path $sourceRoot.FullName ".opencode/skills/ibcs-standards"
    if (-not (Test-Path $source)) {
        throw "The skill folder was not found in the downloaded archive."
    }

    if (Test-Path $Target) {
        if (-not $Force) {
            throw "Target already exists: $Target. Re-run with -Force to replace it."
        }
        Remove-Item $Target -Recurse -Force
    }

    $parent = Split-Path -Parent $Target
    if ($parent) {
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
    }

    Copy-Item $source $Target -Recurse
    Write-Host "Installed the IBCS skill to $Target"
}
finally {
    if (Test-Path $archive) { Remove-Item $archive -Force }
    if (Test-Path $tempRoot) { Remove-Item $tempRoot -Recurse -Force }
}
