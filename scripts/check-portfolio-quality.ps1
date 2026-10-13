param(
    [string]$RepoRoot = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = 'Stop'
$RepoRoot = (Resolve-Path -LiteralPath $RepoRoot).Path

function Get-TrackedFiles([string]$Pattern) {
    $files = & git -C $RepoRoot ls-files --cached --others --exclude-standard $Pattern
    if ($LASTEXITCODE -ne 0) { throw "Could not enumerate tracked $Pattern files." }
    return @($files | Sort-Object -Unique | Where-Object { -not [string]::IsNullOrWhiteSpace($_) -and (Test-Path -LiteralPath (Join-Path $RepoRoot $_) -PathType Leaf) })
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

function Assert-CurrentPatientScope {
    $record = Get-Content -Raw -LiteralPath (Join-Path $RepoRoot 'EVIDENCE/v2.15/patient-scoped-ram-benchmark.json') | ConvertFrom-Json
    if ($record.medianSavingKiB -ne 8586 -or $record.lowerSavingBoundKiB -ne 8384 -or $record.pairs.Count -ne 12) { throw 'Patient RAM record drifted.' }
    if ($record.performanceBoundsQualified -or $record.fullProductAcceptance -or $record.originalNull.memoryPassed -or -not $record.calibrationException.postObservation) { throw 'Patient provisional qualification drifted.' }
    foreach ($relative in @('README.md','CASE-STUDIES/03-patient-service-confirmation-addendum.md','ASSETS/portfolio-summary.md')) {
        $text = (Get-Content -Raw -LiteralPath (Join-Path $RepoRoot $relative)) -replace '\s+', ' '
        foreach ($required in @('8.38 MiB','8.19 MiB','calibration failed','unqualified or failed','no new Maven binaries')) {
            if ($text -notmatch [regex]::Escape($required)) { throw "Patient scope missing in ${relative}: $required" }
        }
    }
    foreach ($relative in Get-TrackedFiles '*') {
        if ($relative -match '^DRAFTS/' -or $relative -in @('publish-evidence-inventory.json','publish-evidence-inventory.md','publish-readiness-checklist.md','ASSETS/jmoa-portfolio-hero.png','ASSETS/portfolio-summary.pdf','ASSETS/portfolio-summary-preview.png','ASSETS/charts/direct-product-pss.png','ASSETS/charts/median-pss-savings.mmd','ASSETS/charts/median-pss-savings.png','ASSETS/diagrams/jmoa-pipeline.png')) { throw "Removed publication material returned: $relative" }
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
Assert-CurrentPatientScope
Assert-PublicationSafety

foreach ($requiredAsset in @(
    'ASSETS/jmoa-portfolio-hero-v21.svg',
    'ASSETS/charts/petclinic-v21-direct-ram.svg',
    'ASSETS/diagrams/runtime-modes.svg',
    'ASSETS/portfolio-summary.md'
)) {
    if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot $requiredAsset) -PathType Leaf)) {
        throw "Required rendered asset is missing: $requiredAsset"
    }
}

& git -C $RepoRoot diff --check
if ($LASTEXITCODE -ne 0) { throw 'git diff --check failed.' }
Write-Host 'Portfolio quality checks passed.'
