# Simple Document Conversion Script for JAMIA Submission
# Run from JAMIA_SUBMISSION folder: .\convert_documents.ps1

Write-Host "`nConverting documents for JAMIA submission...`n" -ForegroundColor Cyan

# Create output directory
if (-not (Test-Path Converted)) {
    New-Item -ItemType Directory -Path Converted | Out-Null
}

# Convert documents one by one
Write-Host "1. Converting Main Manuscript..." -ForegroundColor Yellow
pandoc Documents\JAMIA_VERSION.md -o Converted\manuscript.docx --standalone
if (Test-Path Converted\manuscript.docx) {
    $size = (Get-Item Converted\manuscript.docx).Length / 1KB
    Write-Host "   SUCCESS - manuscript.docx ($([math]::Round($size, 1)) KB)" -ForegroundColor Green
    Write-Host "   NOTE: Add line numbers in Word (Layout > Line Numbers > Continuous)`n" -ForegroundColor Cyan
}

Write-Host "2. Converting Supplementary Materials..." -ForegroundColor Yellow
pandoc Documents\SUPPLEMENTARY_MATERIALS.md -o Converted\supplementary.docx --standalone
if (Test-Path Converted\supplementary.docx) {
    $size = (Get-Item Converted\supplementary.docx).Length / 1KB
    Write-Host "   SUCCESS - supplementary.docx ($([math]::Round($size, 1)) KB)" -ForegroundColor Green
    Write-Host "   NOTE: Convert to PDF from Word if needed`n" -ForegroundColor Cyan
}

Write-Host "3. Converting Cover Letter..." -ForegroundColor Yellow
pandoc Documents\COVER_LETTER.md -o Converted\cover_letter.docx --standalone
if (Test-Path Converted\cover_letter.docx) {
    $size = (Get-Item Converted\cover_letter.docx).Length / 1KB
    Write-Host "   SUCCESS - cover_letter.docx ($([math]::Round($size, 1)) KB)`n" -ForegroundColor Green
}

Write-Host "4. Converting Title Page..." -ForegroundColor Yellow
pandoc Documents\TITLE_PAGE.md -o Converted\title_page.docx --standalone
if (Test-Path Converted\title_page.docx) {
    $size = (Get-Item Converted\title_page.docx).Length / 1KB
    Write-Host "   SUCCESS - title_page.docx ($([math]::Round($size, 1)) KB)`n" -ForegroundColor Green
}

Write-Host "5. Converting Author Contributions..." -ForegroundColor Yellow
pandoc Documents\AUTHOR_CONTRIBUTIONS.md -o Converted\author_contributions.docx --standalone
if (Test-Path Converted\author_contributions.docx) {
    $size = (Get-Item Converted\author_contributions.docx).Length / 1KB
    Write-Host "   SUCCESS - author_contributions.docx ($([math]::Round($size, 1)) KB)`n" -ForegroundColor Green
}

Write-Host "6. Converting Data Availability..." -ForegroundColor Yellow
pandoc Documents\DATA_AVAILABILITY.md -o Converted\data_availability.docx --standalone
if (Test-Path Converted\data_availability.docx) {
    $size = (Get-Item Converted\data_availability.docx).Length / 1KB
    Write-Host "   SUCCESS - data_availability.docx ($([math]::Round($size, 1)) KB)`n" -ForegroundColor Green
}

Write-Host "7. Converting Declarations..." -ForegroundColor Yellow
pandoc Documents\DECLARATIONS.md -o Converted\declarations.docx --standalone
if (Test-Path Converted\declarations.docx) {
    $size = (Get-Item Converted\declarations.docx).Length / 1KB
    Write-Host "   SUCCESS - declarations.docx ($([math]::Round($size, 1)) KB)`n" -ForegroundColor Green
}

# Summary
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "CONVERSION COMPLETE!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "`nAll documents saved to: Converted\`n" -ForegroundColor Yellow

Write-Host "IMPORTANT NEXT STEPS:" -ForegroundColor Yellow
Write-Host "1. Open manuscript.docx in Word" -ForegroundColor White
Write-Host "2. Add line numbers: Layout > Line Numbers > Continuous" -ForegroundColor White
Write-Host "3. Add page numbers: Insert > Page Number" -ForegroundColor White
Write-Host "4. Check all tables and formatting" -ForegroundColor White
Write-Host "5. Verify figure references" -ForegroundColor White
Write-Host "6. Export supplementary.docx to PDF" -ForegroundColor White
Write-Host "7. Review all documents for accuracy`n" -ForegroundColor White

Write-Host "Files ready for JAMIA submission!" -ForegroundColor Green
Write-Host ""
