# DOCUMENT CONVERSION GUIDE

**Purpose:** Convert Markdown files to Word/PDF format for JAMIA submission  
**Time Required:** 1 hour

---

## FILES TO CONVERT

### Required Conversions:
1. ✅ `manuscript/JAMIA_VERSION.md` → `JAMIA_VERSION.docx`
2. ✅ `manuscript/TITLE_PAGE.md` → `TITLE_PAGE.docx`
3. ✅ `manuscript/COVER_LETTER.md` → `COVER_LETTER.docx`
4. ✅ `manuscript/SUPPLEMENTARY_MATERIALS.md` → `SUPPLEMENTARY_MATERIALS.pdf`

---

## METHOD 1: Using Pandoc (Recommended, Best Formatting)

### Install Pandoc
```powershell
# Option A: Using Chocolatey (Windows package manager)
choco install pandoc

# Option B: Download installer from https://pandoc.org/installing.html
# Install and restart PowerShell
```

### Convert Files
```powershell
cd e:\project\Riset\heart-disease\manuscript

# 1. Main Manuscript (with reference document for better formatting)
pandoc JAMIA_VERSION.md -o JAMIA_VERSION.docx --reference-doc=custom-reference.docx

# If no reference doc, use default:
pandoc JAMIA_VERSION.md -o JAMIA_VERSION.docx

# 2. Title Page
pandoc TITLE_PAGE.md -o TITLE_PAGE.docx

# 3. Cover Letter
pandoc COVER_LETTER.md -o COVER_LETTER.docx

# 4. Supplementary Materials (to PDF)
pandoc SUPPLEMENTARY_MATERIALS.md -o SUPPLEMENTARY_MATERIALS.pdf
```

### Create Reference Document (Optional, for better formatting)
```powershell
# Generate a reference docx first
pandoc JAMIA_VERSION.md -o temp.docx

# Open temp.docx in Word, customize styles:
# - Heading 1: Bold, 14pt
# - Heading 2: Bold, 12pt
# - Normal text: Times New Roman, 12pt
# - Line spacing: Double

# Save as custom-reference.docx
# Then re-run conversion using --reference-doc
```

---

## METHOD 2: Manual Conversion (Simple, No Installation)

### Steps:
1. Open the .md file in VS Code
2. Select All (Ctrl+A)
3. Copy (Ctrl+C)
4. Open Microsoft Word
5. Paste (Ctrl+V)
6. Word will auto-format most Markdown
7. Manual fixes needed:
   - Convert `**text**` to bold if not auto-converted
   - Format tables properly
   - Add page numbers
   - Check references formatting
8. Save as .docx

### For PDF (Supplementary Materials):
1. Follow steps 1-7 above
2. In Word: File → Save As → PDF

---

## METHOD 3: Online Converter (Quick & Easy)

### Recommended Sites:
- https://cloudconvert.com/md-to-docx
- https://convertio.co/md-docx/
- https://products.aspose.app/words/conversion/md-to-docx

### Steps:
1. Go to converter website
2. Upload .md file
3. Select output format (DOCX or PDF)
4. Download converted file
5. Open in Word to verify and make adjustments

---

## POST-CONVERSION CHECKLIST

### For JAMIA_VERSION.docx:
- [ ] Title is formatted correctly
- [ ] Authors and affiliations are properly formatted
- [ ] Abstract is on separate line with heading
- [ ] All 5 tables are properly formatted
- [ ] All figure references are intact (Figure 1, Figure 2, etc.)
- [ ] References are numbered correctly [1-8]
- [ ] Headings are formatted hierarchically
- [ ] Line spacing is double (or as required by JAMIA)
- [ ] Page numbers added (bottom center or as required)
- [ ] Word count is displayed: ~4,900 words
- [ ] No broken formatting or strange characters

### For TITLE_PAGE.docx:
- [ ] Title is prominent
- [ ] All 4 authors listed with full details
- [ ] Corresponding author marked with *
- [ ] Email and phone included
- [ ] ORCID IDs included (if available)
- [ ] Word counts listed
- [ ] Keywords listed
- [ ] Running title included

### For COVER_LETTER.docx:
- [ ] Your contact info at top
- [ ] Date: December 17, 2025
- [ ] Addressed to: Dr. Suzanne Bakken
- [ ] Professional letterhead format
- [ ] Signature line at bottom
- [ ] Co-author names at bottom

### For SUPPLEMENTARY_MATERIALS.pdf:
- [ ] All supplementary tables formatted
- [ ] Figure legends for S1, S2, S3
- [ ] References to main text figures
- [ ] Page numbers
- [ ] Professional formatting

---

## FORMATTING TIPS

### JAMIA Preferred Format:
- **Font:** Times New Roman, 12pt
- **Line Spacing:** Double
- **Margins:** 1 inch (2.54 cm) all sides
- **Page Numbers:** Bottom center
- **Line Numbers:** Add continuous line numbers (Word: Layout → Line Numbers → Continuous)

### To Add Line Numbers in Word:
1. Layout tab → Line Numbers
2. Select "Continuous"
3. Apply to whole document

### To Check Word Count in Word:
1. Review tab → Word Count
2. Verify it matches ~4,900 words

---

## QUALITY CHECK

### Open each converted file and verify:

#### Visual Check:
- [ ] No strange formatting artifacts
- [ ] Tables aligned properly
- [ ] Headings are hierarchical and clear
- [ ] No broken links
- [ ] References formatted consistently

#### Content Check:
- [ ] All sections present
- [ ] No missing paragraphs
- [ ] No missing tables
- [ ] All citations intact [1], [2], etc.
- [ ] Author names spelled correctly

#### Technical Check:
- [ ] File size reasonable (<5MB)
- [ ] File opens without errors
- [ ] Can be printed/exported properly
- [ ] Compatible with Word 2016+

---

## FINAL FILE NAMES

Use these exact names for submission:

```
JAMIA_VERSION.docx          (Main manuscript)
TITLE_PAGE.docx             (Title page)
COVER_LETTER.docx           (Cover letter)
SUPPLEMENTARY_MATERIALS.pdf (Supplementary)
Figure1.png                 (Comprehensive analysis)
Figure2.png                 (Confusion matrices)
Figure3.png                 (Prompt comparison)
FigureS1.png               (ROC curves)
FigureS2.png               (Distributions)
FigureS3.png               (Feature correlations)
```

---

## FIGURE PREPARATION

### Rename Figures for Submission:
```powershell
cd e:\project\Riset\heart-disease\results\evaluation

# Copy figures to a submission folder with clean names
New-Item -ItemType Directory -Force -Path "..\submission_files"

Copy-Item "comprehensive_consistency_analysis.png" "..\submission_files\Figure1.png"
Copy-Item "figure_2_confusion_matrices.png" "..\submission_files\Figure2.png"
Copy-Item "prompt_comparison.png" "..\submission_files\Figure3.png"
Copy-Item "supplementary_fig_s1_roc_curves.png" "..\submission_files\FigureS1.png"
Copy-Item "supplementary_fig_s2_distributions.png" "..\submission_files\FigureS2.png"
Copy-Item "supplementary_fig_s3_feature_correlations.png" "..\submission_files\FigureS3.png"
```

### Verify Figure Quality:
- [ ] Open each figure image
- [ ] Check resolution (should be sharp, not pixelated)
- [ ] Check file size (typically 500KB - 5MB each)
- [ ] Verify colors are vivid and clear
- [ ] Ensure text in figures is readable

---

## CREATING SUBMISSION FOLDER

```powershell
# Create a clean submission folder
cd e:\project\Riset\heart-disease
New-Item -ItemType Directory -Force -Path ".\JAMIA_SUBMISSION"

# After conversion, copy all files here:
# - JAMIA_VERSION.docx
# - TITLE_PAGE.docx
# - COVER_LETTER.docx
# - SUPPLEMENTARY_MATERIALS.pdf
# - Figure1.png
# - Figure2.png
# - Figure3.png
# - FigureS1.png
# - FigureS2.png
# - FigureS3.png

# Create a README in submission folder
@"
JAMIA SUBMISSION PACKAGE
========================

Ready for upload in January 2026

Files included:
- JAMIA_VERSION.docx (main manuscript)
- TITLE_PAGE.docx (title page)
- COVER_LETTER.docx (cover letter)
- SUPPLEMENTARY_MATERIALS.pdf (supplementary)
- Figure1.png to Figure3.png (main figures)
- FigureS1.png to FigureS3.png (supplementary figures)

Upload these files to JAMIA submission portal.
"@ | Out-File -FilePath ".\JAMIA_SUBMISSION\README.txt" -Encoding utf8
```

---

## TROUBLESHOOTING

### Problem: Pandoc not installed
**Solution:** Use Method 2 (manual) or Method 3 (online converter)

### Problem: Tables don't format correctly
**Solution:** 
- In Word, select table → Table Design → choose a style
- Adjust column widths manually
- Ensure all data is visible

### Problem: References lose numbering
**Solution:**
- Find all [1], [2], etc. in text
- Ensure they remain as superscript numbers
- Manually format if needed

### Problem: Figures show as broken links
**Solution:**
- Figures should be referenced as "(Figure 1)" not embedded
- They will be uploaded separately to submission system

---

## ESTIMATED TIME

- **Pandoc conversion:** 10 minutes
- **Manual formatting check:** 20 minutes per document
- **Figure renaming:** 5 minutes
- **Quality verification:** 15 minutes
- **Creating submission folder:** 5 minutes

**Total:** ~1 hour

---

**Next Step:** After conversion, proceed with GitHub setup, then wait until January to submit!
