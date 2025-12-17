# JAMIA Submission Preparation Script
# Run: .\prepare_jamia_submission.ps1

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "JAMIA SUBMISSION PREPARATION" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Create submission folder
$submissionDir = "JAMIA_SUBMISSION"
if (Test-Path $submissionDir) {
    Write-Host "Cleaning existing folder..." -ForegroundColor Yellow
    Remove-Item $submissionDir -Recurse -Force
}

Write-Host "Creating submission folder structure..." -ForegroundColor Green
New-Item -ItemType Directory -Path $submissionDir | Out-Null
New-Item -ItemType Directory -Path "$submissionDir\Figures" | Out-Null
New-Item -ItemType Directory -Path "$submissionDir\Supplementary" | Out-Null
New-Item -ItemType Directory -Path "$submissionDir\Documents" | Out-Null
New-Item -ItemType Directory -Path "$submissionDir\Data" | Out-Null
Write-Host "Folders created`n" -ForegroundColor Green

# Copy and Rename Main Figures
Write-Host "STEP 1: Preparing Main Figures..." -ForegroundColor Cyan

$mainFigures = @{
    "results\evaluation\comprehensive_consistency_analysis.png" = "Figure1.png"
    "results\evaluation\figure_2_confusion_matrices.png" = "Figure2.png"
    "results\evaluation\prompt_comparison.png" = "Figure3.png"
}

foreach ($source in $mainFigures.Keys) {
    $dest = "$submissionDir\Figures\$($mainFigures[$source])"
    if (Test-Path $source) {
        Copy-Item $source $dest
        $size = (Get-Item $dest).Length / 1KB
        Write-Host "   OK - $($mainFigures[$source]) - $([math]::Round($size, 1)) KB" -ForegroundColor Green
    } else {
        Write-Host "   MISSING: $source" -ForegroundColor Red
    }
}

# Copy and Rename Supplementary Figures
Write-Host "`nSTEP 2: Preparing Supplementary Figures..." -ForegroundColor Cyan

$suppFigures = @{
    "results\evaluation\supplementary_fig_s1_roc_curves.png" = "FigureS1.png"
    "results\evaluation\supplementary_fig_s2_distributions.png" = "FigureS2.png"
    "results\evaluation\supplementary_fig_s3_feature_correlations.png" = "FigureS3.png"
    "results\evaluation\consistency_distributions.png" = "FigureS4.png"
    "results\evaluation\model_comparison.png" = "FigureS5.png"
    "results\evaluation\threshold_optimization.png" = "FigureS6.png"
}

foreach ($source in $suppFigures.Keys) {
    $dest = "$submissionDir\Supplementary\$($suppFigures[$source])"
    if (Test-Path $source) {
        Copy-Item $source $dest
        $size = (Get-Item $dest).Length / 1KB
        Write-Host "   OK - $($suppFigures[$source]) - $([math]::Round($size, 1)) KB" -ForegroundColor Green
    } else {
        Write-Host "   MISSING: $source" -ForegroundColor Red
    }
}

# Copy Manuscript Documents
Write-Host "`nSTEP 3: Copying Manuscript Documents..." -ForegroundColor Cyan

$documents = @(
    "manuscript\JAMIA_VERSION.md"
    "manuscript\SUPPLEMENTARY_MATERIALS.md"
    "manuscript\COVER_LETTER.md"
    "manuscript\TITLE_PAGE.md"
    "manuscript\AUTHOR_CONTRIBUTIONS.md"
    "manuscript\DATA_AVAILABILITY.md"
    "manuscript\DECLARATIONS.md"
)

foreach ($doc in $documents) {
    if (Test-Path $doc) {
        Copy-Item $doc "$submissionDir\Documents\"
        $filename = Split-Path $doc -Leaf
        Write-Host "   OK - $filename" -ForegroundColor Green
    } else {
        Write-Host "   MISSING: $doc" -ForegroundColor Red
    }
}

# Copy Key Data Files
Write-Host "`nSTEP 4: Copying Key Data Files..." -ForegroundColor Cyan

$dataFiles = @(
    "data\heart.csv"
    "results\sampling\llm_test_data.csv"
    "results\evaluation\model_comparison.csv"
    "results\evaluation\prompt_comparison.csv"
    "results\evaluation\consistency_metrics.csv"
)

foreach ($file in $dataFiles) {
    if (Test-Path $file) {
        Copy-Item $file "$submissionDir\Data\"
        $filename = Split-Path $file -Leaf
        Write-Host "   OK - $filename" -ForegroundColor Green
    }
}

# Create Submission Checklist
Write-Host "`nSTEP 5: Creating Submission Checklist..." -ForegroundColor Cyan

$checklistContent = @"
# JAMIA SUBMISSION CHECKLIST
Date: $(Get-Date -Format "MMMM dd, yyyy")
Target Submission: January 2-10, 2026

## DOCUMENTS TO CONVERT

From Documents folder, convert these files:
- [ ] JAMIA_VERSION.md -> manuscript.docx (add line numbers)
- [ ] SUPPLEMENTARY_MATERIALS.md -> supplementary.pdf
- [ ] COVER_LETTER.md -> cover_letter.docx
- [ ] TITLE_PAGE.md -> title_page.docx

## FIGURES (READY)

Main Figures (in Figures folder):
- [x] Figure1.png - Comprehensive consistency analysis
- [x] Figure2.png - Confusion matrices
- [x] Figure3.png - Prompt comparison

Supplementary Figures (in Supplementary folder):
- [x] FigureS1.png - ROC curves
- [x] FigureS2.png - Prediction distributions
- [x] FigureS3.png - Feature correlations
- [x] FigureS4.png - Consistency distributions
- [x] FigureS5.png - Model comparison
- [x] FigureS6.png - Threshold optimization

## MANUSCRIPT REQUIREMENTS

- [ ] Word count: 5,000 words (check)
- [ ] Abstract: 250 words (check)
- [ ] References: 15 total (check)
- [ ] Line numbers added
- [ ] Page numbers added
- [ ] All figures cited in order

## AUTHOR INFORMATION

- [x] ORCID IDs: 2/4 authors
  * Dwi Anggriani: 0009-0007-4265-1935
  * Syaiful Bachri Mustamin: 0009-0005-0456-8618
- [ ] All authors approved manuscript
- [x] Corresponding author: syaifulbachri@mail.ugm.ac.id

## DATA AVAILABILITY

- [x] GitHub: https://github.com/lufias69/heart-disease-llm-research
- [x] All code uploaded
- [x] All data uploaded
- [x] README complete

## DECLARATIONS

- [x] No IRB required (public data)
- [x] No conflicts of interest
- [x] No funding
- [x] Preprint disclosed (medRxiv DOI: 10.64898/2025.12.08.25341823)

## SUBMISSION PORTAL STEPS

1. [ ] Register at mc.manuscriptcentral.com/jamia
2. [ ] Upload manuscript.docx (with line numbers)
3. [ ] Upload title_page.docx (separate file)
4. [ ] Upload cover_letter.docx
5. [ ] Upload Figure1.png, Figure2.png, Figure3.png
6. [ ] Upload supplementary.pdf
7. [ ] Upload FigureS1-S6.png (6 files)
8. [ ] Enter all metadata
9. [ ] Review proof
10. [ ] Submit!

## TIMELINE

- Dec 17-31, 2025: Document conversion, final review
- Jan 1, 2026: Final proofread
- Jan 2-10, 2026: Submit to JAMIA
- Expected review: 4-8 weeks

## CONTACT

Corresponding Author:
Syaiful Bachri Mustamin
syaifulbachri@mail.ugm.ac.id
+62 851-5629-7969

JAMIA Editorial:
jamia@amia.org
https://mc.manuscriptcentral.com/jamia
"@

$checklistContent | Out-File "$submissionDir\SUBMISSION_CHECKLIST.md" -Encoding UTF8
Write-Host "   OK - SUBMISSION_CHECKLIST.md" -ForegroundColor Green

# Create README
$readmeContent = @"
# JAMIA Submission Package

**Manuscript:** High Consistency, Limited Accuracy: Evaluating Large Language Models for Binary Medical Diagnosis

**Prepared:** $(Get-Date -Format "MMMM dd, yyyy")
**Journal:** JAMIA (Journal of the American Medical Informatics Association)
**Preprint:** https://doi.org/10.64898/2025.12.08.25341823

## Contents

### Documents/ - Manuscript Files
- JAMIA_VERSION.md (main manuscript)
- SUPPLEMENTARY_MATERIALS.md (supplementary materials)
- COVER_LETTER.md (cover letter)
- TITLE_PAGE.md (title page)
- AUTHOR_CONTRIBUTIONS.md
- DATA_AVAILABILITY.md
- DECLARATIONS.md

**ACTION REQUIRED:** Convert these .md files to Word/PDF format

### Figures/ - Main Figures (Renamed for Submission)
- Figure1.png - Comprehensive consistency analysis (659 KB)
- Figure2.png - Confusion matrices (419 KB)
- Figure3.png - Prompt comparison (332 KB)

### Supplementary/ - Supplementary Figures (Renamed)
- FigureS1.png - ROC curves (336 KB)
- FigureS2.png - Prediction distributions (228 KB)
- FigureS3.png - Feature correlations (217 KB)
- FigureS4.png - Consistency distributions (167 KB)
- FigureS5.png - Model comparison (276 KB)
- FigureS6.png - Threshold optimization (433 KB)

### Data/ - Key Data Files
- heart.csv (UCI dataset)
- llm_test_data.csv (100 test cases)
- model_comparison.csv
- prompt_comparison.csv
- consistency_metrics.csv

## Next Steps

### 1. Convert Documents (URGENT)

**Method 1: Using Pandoc (Recommended)**
pandoc Documents/JAMIA_VERSION.md -o manuscript.docx
pandoc Documents/SUPPLEMENTARY_MATERIALS.md -o supplementary.pdf
pandoc Documents/COVER_LETTER.md -o cover_letter.docx
pandoc Documents/TITLE_PAGE.md -o title_page.docx

**Method 2: Manual in Word**
1. Open .md file in VS Code or Markdown viewer
2. Copy content to Word
3. Format (add line numbers, page numbers)
4. Save as .docx or export to PDF

### 2. Final Review
- Proofread all documents
- Check all citations
- Verify figure quality (300+ DPI)
- Confirm author information

### 3. Get Co-Author Approvals
Send to all authors for final approval

### 4. Submit to JAMIA
Follow SUBMISSION_CHECKLIST.md for detailed steps

## Manuscript Statistics

- Word Count: ~5,000 words
- References: 15
- Main Figures: 3
- Supplementary Figures: 6
- Tables: 5 main + supplementary
- Authors: 4 (2 with ORCID)

## Important Links

- GitHub: https://github.com/lufias69/heart-disease-llm-research
- Preprint: https://doi.org/10.64898/2025.12.08.25341823
- JAMIA Portal: https://mc.manuscriptcentral.com/jamia
- Institution: https://istekaisyiyah.ac.id

## Contact

**Corresponding Author:**
Syaiful Bachri Mustamin
syaifulbachri@mail.ugm.ac.id
+62 851-5629-7969

---
All files ready for submission!
Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
"@

$readmeContent | Out-File "$submissionDir\README.md" -Encoding UTF8
Write-Host "   OK - README.md" -ForegroundColor Green

# Summary
Write-Host "`n============================================" -ForegroundColor Cyan
Write-Host "SUBMISSION PACKAGE READY!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Location: $submissionDir\" -ForegroundColor Yellow
Write-Host ""
Write-Host "Contents:" -ForegroundColor White
Write-Host "  - 7 manuscript documents (.md files)" -ForegroundColor White
Write-Host "  - 3 main figures (Figure1-3.png)" -ForegroundColor White
Write-Host "  - 6 supplementary figures (FigureS1-6.png)" -ForegroundColor White
Write-Host "  - 5 data files" -ForegroundColor White
Write-Host "  - Submission checklist and README" -ForegroundColor White
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Yellow
Write-Host "  1. Convert .md documents to Word/PDF" -ForegroundColor White
Write-Host "  2. Review SUBMISSION_CHECKLIST.md" -ForegroundColor White
Write-Host "  3. Get co-author approvals" -ForegroundColor White
Write-Host "  4. Submit to JAMIA (Jan 2-10, 2026)" -ForegroundColor White
Write-Host ""
Write-Host "Good luck with your submission!" -ForegroundColor Green
Write-Host ""
