param(
    [string]$RepoRoot = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
$RepoRoot = (Resolve-Path -LiteralPath $RepoRoot).Path

function Get-TrackedFiles([string]$Pattern) {
    $files = & git -C $RepoRoot ls-files $Pattern
    if ($LASTEXITCODE -ne 0) { throw "Could not enumerate tracked $Pattern files." }
    return @($files | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
}

function Assert-LocalMarkdownLinks {
    $errors = [System.Collections.Generic.List[string]]::new()
    foreach ($relative in Get-TrackedFiles '*.md') {
        $source = Join-Path $RepoRoot $relative
        $text = Get-Content -Raw -LiteralPath $source
        foreach ($match in [regex]::Matches($text, '!?(?:\[[^\]]*\])\(([^)]+)\)')) {
            $target = $match.Groups[1].Value.Trim()
            if ($target.StartsWith('<') -and $target.EndsWith('>')) {
                $target = $target.Substring(1, $target.Length - 2)
            }
            $target = ($target -split '\s+"', 2)[0]
            if ($target -match '^(?i:https?://|mailto:|#)') { continue }
            $pathPart = ($target -split '#', 2)[0]
            if ([string]::IsNullOrWhiteSpace($pathPart)) { continue }
            $resolved = Join-Path (Split-Path -Parent $source) ([Uri]::UnescapeDataString($pathPart))
            if (-not (Test-Path -LiteralPath $resolved)) { $errors.Add("$relative -> $target") }
        }
    }
    if ($errors.Count -gt 0) { throw "Broken local Markdown links:`n$($errors -join "`n")" }
}

function Assert-JsonParses {
    foreach ($relative in Get-TrackedFiles '*.json') {
        try { Get-Content -Raw -LiteralPath (Join-Path $RepoRoot $relative) | ConvertFrom-Json | Out-Null }
        catch { throw "Invalid JSON: $relative`n$($_.Exception.Message)" }
    }
}

function Assert-ClaimConsistency {
    $matrix = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'EVIDENCE/v2-final/three-service-matrix.json') | ConvertFrom-Json
    $inventory = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'publish-evidence-inventory.json') | ConvertFrom-Json
    foreach ($service in $matrix.services) {
        $published = @($inventory.acceptedClaims | Where-Object { $_.case -eq $service.service }) | Select-Object -First 1
        if ($null -eq $published) { throw "Inventory is missing $($service.service)." }
        foreach ($field in @('runtimePolicy','validRuns','pairedWins','medianPssDeltaKb')) {
            if ($service.$field -ne $published.$field) { throw "Matrix/inventory mismatch: $($service.service).$field" }
        }
    }

    $v21 = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'EVIDENCE/v2.1/petclinic-direct-ram-win.json') | ConvertFrom-Json
    $readme = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'README.md')
    $caseStudy = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'CASE-STUDIES/05-petclinic-v21-direct-ram-win.md')
    if (-not $v21.claimable -or $v21.terminal -ne 'T7R23_R487_SCALE_DIRECT_RAM_WIN') { throw 'The v2.1 portfolio result is not the frozen claimable terminal.' }
    if ($v21.processPssKiB.median -ne -15241.5 -or $v21.processPssKiB.favorableBlocks -ne 12) { throw 'The v2.1 portfolio PSS result drifted.' }
    if ($v21.memoryCurrentBytes.median -ne -17033216) { throw 'The v2.1 portfolio cgroup result drifted.' }
    foreach ($surface in @($readme, $caseStudy)) {
        foreach ($required in @('15,241.5 KiB','17,033,216','14.71','packaging-inclusive')) {
            if (-not $surface.Contains($required)) { throw "A v2.1 release-facing surface is missing $required." }
        }
    }
}

function Assert-NoStaleReleasePresentation {
    $releaseFiles = @(
        'README.md',
        'ASSETS/portfolio-summary.md',
        'DRAFTS/cv-bullet.md',
        'DRAFTS/job-application-paragraph.md',
        'DRAFTS/linkedin-post.md'
    )
    $text = ($releaseFiles | ForEach-Object { Get-Content -Raw -LiteralPath (Join-Path $RepoRoot $_) }) -join "`n"
    foreach ($pattern in @('Portfolio v1','Week 1','reproduction scaffold','~4.2-4.4 MB median','~4.6 MB median PSS')) {
        if ($text -match [regex]::Escape($pattern)) { throw "Stale release-facing wording found: $pattern" }
    }
}

function Assert-PublicationSafety {
    $patterns = @(
        'C:\\Users\\',
        'C:\\Java Developer',
        'BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY',
        '(?i)(password|secret|token|jwt)\s*[=:]\s*[^<\s]'
    )
    foreach ($relative in Get-TrackedFiles '*') {
        if ($relative -eq 'scripts/check-portfolio-quality.ps1') { continue }
        $path = Join-Path $RepoRoot $relative
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { continue }
        if ([IO.Path]::GetExtension($path) -notin @('.md','.json','.mmd','.svg','.ps1','.py','.yml','.yaml','.txt')) { continue }
        $text = Get-Content -Raw -LiteralPath $path
        foreach ($pattern in $patterns) {
            if ($text -match $pattern) { throw "Publication-safety match in $relative for pattern $pattern" }
        }
    }
}

Assert-LocalMarkdownLinks
Assert-JsonParses
Assert-ClaimConsistency
Assert-NoStaleReleasePresentation
Assert-PublicationSafety

foreach ($requiredAsset in @(
    'ASSETS/jmoa-portfolio-hero.png',
    'ASSETS/charts/median-pss-savings.png',
    'ASSETS/charts/petclinic-v21-direct-ram.svg',
    'ASSETS/diagrams/runtime-modes.svg',
    'ASSETS/portfolio-summary.pdf',
    'ASSETS/portfolio-summary-preview.png'
)) {
    if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot $requiredAsset) -PathType Leaf)) {
        throw "Required rendered asset is missing: $requiredAsset"
    }
}

& git -C $RepoRoot diff --check
if ($LASTEXITCODE -ne 0) { throw 'git diff --check failed.' }
Write-Host 'Portfolio quality checks passed.'
