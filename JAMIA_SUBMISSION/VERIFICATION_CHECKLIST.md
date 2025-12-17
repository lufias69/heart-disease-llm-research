# JAMIA Submission Verification Checklist

## ✅ All Changes Applied to manuscript.docx

Berikut adalah **semua perubahan** yang sudah saya terapkan ke JAMIA_VERSION.md dan sudah ter-convert ke manuscript.docx. Anda tidak perlu edit ini lagi:

### 1. ✅ Encoding Symbols - All Fixed
- `>=` (greater than or equal) - fixed di seluruh dokumen
- `×` (multiplication sign) - fixed
- `•` (bullet points) - fixed
- `—` (em dash) - fixed
- `≈` (approximately equal) - fixed
- `é` (accented e in "Liévin") - fixed di References #10

**Lokasi yang sudah diperbaiki:**
- Line 54 Methods: ">=2/4 runs" ✅
- Line 142 Discussion: "patterns—they" ✅
- Line 203 Reference #10: "Liévin V" ✅

### 2. ✅ Horizontal Lines Removed
- Semua garis horizontal standalone (`---`) sudah dihapus
- Table borders (markdown table syntax `|---|`) masih ada (ini normal)

### 3. ✅ Figure Citations Added
**Semua 3 figures sekarang sudah direferensikan dalam text:**

- **Figure 1** - Results section, paragraph 1:
  > "All models demonstrated remarkably high consistency (Table 1, **Figure 1**)."
  
- **Figure 2** - Results section, Model Performance:
  > "Representative confusion matrices (**Figure 2**) showed models predicted..."
  
- **Figure 3** - Results section, Prompt Sensitivity:
  > "Changing from expert to neutral prompt had minimal effect (Table 4, **Figure 3**)."

### 4. ✅ Acknowledgments Section - Complete
Acknowledgments section sudah **tidak ada placeholder lagi**. Sekarang berisi:

- Institutional support: ISTIK Kendari
- API providers: OpenAI (GPT-4o), Google (Gemini-2.0-Flash), Alibaba Cloud (Qwen-Plus)
- Dataset: UCI ML Repository + nama asli collectors (Janosi, Steinbrunn, Pfisterer, Detrano)

### 5. ✅ Manuscript Statistics - Updated
**Di TITLE_PAGE.docx dan COVER_LETTER.docx:**
- Word Count: ~5,000 words ✅
- References: 15 ✅
- Supplementary Figures: 6 ✅
- Supplementary Tables: 4 ✅

### 6. ✅ Metadata Footer Removed
Footer dengan "Word Count: | References: " sudah dihapus dari manuscript

### 7. ✅ AI Disclosure Statements Enhanced
**AUTHOR_CONTRIBUTIONS.docx:**
- Detailed disclosure separating AI as research subjects vs. manuscript tools

**DECLARATIONS.docx:**
- 5-section comprehensive "Generative AI and Technology Disclosure"

---

## 📋 What You Need to Verify in Word

Buka **manuscript.docx** dan cek sections berikut:

### Check 1: Methods Section
- Cari text "Using majority voting"
- Harus tertulis: ">=2/4 runs" atau tampil sebagai "≥2/4 runs"
- **Tidak boleh** ada karakter aneh seperti ‰¥ atau â‰¥

### Check 2: Results Section
- Cari text "Table 1" → harus ada ", Figure 1)" di kalimat yang sama
- Cari text "confusion matrices" → harus ada "(Figure 2)" setelahnya
- Cari text "Table 4" → harus ada ", Figure 3)" di kalimat yang sama

### Check 3: Discussion Section  
- Cari text "reasoning patterns"
- Harus ada em dash (—) sebelum kata "they"
- **Tidak boleh** ada €" atau karakter encoding error

### Check 4: Acknowledgments Section
- Harus ada nama institutions: "Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari"
- Harus ada model names: "GPT-4o, Gemini-2.0-Flash, and Qwen-Plus"
- Harus ada collector names: "Janosi, Steinbrunn, Pfisterer, and Detrano"
- **Tidak boleh** ada placeholder text "[collaborators/institutions]"

### Check 5: References Section
- Total harus 15 references
- Reference #10 harus: "Liévin V" dengan accent aigu di 'e'
- **Tidak boleh** ada "Li©vin" atau karakter encoding error

### Check 6: No Horizontal Lines
- **Tidak boleh** ada garis horizontal standalone di luar table
- Table borders OK (itu markdown table syntax)

### Check 7: End of Document
- **Tidak boleh** ada metadata footer dengan "Word Count:" atau "References:"

---

## ⚠️ Manual Steps Required

Setelah verify checklist di atas, lakukan manual steps ini:

### Step 1: Add Line Numbers
1. Open manuscript.docx
2. Go to **Layout** tab
3. Click **Line Numbers** dropdown
4. Select **Continuous**
5. Save

### Step 2: Add Page Numbers
1. Go to **Insert** tab
2. Click **Page Number**
3. Choose position (Bottom of page, centered is common)
4. Save

### Step 3: Export Supplementary to PDF
1. Open supplementary.docx
2. **File > Save As**
3. Choose **PDF** format
4. Save as **supplementary.pdf**

### Step 4: Final Check All Documents
Review all 7 Word files in `Converted/` folder:
- ✅ manuscript.docx (with line numbers and page numbers)
- ✅ supplementary.docx (also export to PDF)
- ✅ cover_letter.docx
- ✅ title_page.docx
- ✅ author_contributions.docx
- ✅ data_availability.docx
- ✅ declarations.docx

---

## 📊 Document Sizes (Reference)

```
manuscript.docx:           19 KB
supplementary.docx:      1289 KB (large because includes 6 figures)
cover_letter.docx:         12 KB
title_page.docx:           10 KB
author_contributions.docx: 11 KB
data_availability.docx:    12 KB
declarations.docx:         13 KB
```

---

## 🎯 Submission Package Ready

**Folders:**
- `Converted/` - All 7 Word documents + supplementary PDF (after export)
- `Figures/` - Figure1.png, Figure2.png, Figure3.png
- `Supplementary/` - FigureS1.png through FigureS6.png
- `Data/` - 5 CSV files (results and metrics)
- `Documents/` - Original markdown sources

**Next:** Upload ke JAMIA submission portal sesuai SUBMISSION_CHECKLIST.md

---

## ✨ Summary

**Semua encoding errors fixed** ✅  
**Semua figure citations added** ✅  
**Acknowledgments completed** ✅  
**Statistics updated** ✅  
**No horizontal lines** ✅  
**No metadata footer** ✅  
**AI disclosures enhanced** ✅  

**Anda hanya perlu:**
1. Verify 7 checks di atas di manuscript.docx
2. Add line numbers + page numbers (2 menit)
3. Export supplementary.docx to PDF (1 menit)
4. Done! Ready to submit
