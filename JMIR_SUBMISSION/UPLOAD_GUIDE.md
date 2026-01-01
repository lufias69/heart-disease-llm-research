# JMIR MEDICAL INFORMATICS - UPLOAD GUIDE
**Step-by-Step Submission Instructions**

---

## ⚠️ STEP 0: DECLINE JAMIA OPEN (WAJIB DULUAN!)

**SEBELUM submit ke JMIR, decline dulu JAMIA Open untuk menghindari dual submission ethics violation!**

1. **Klik link ini:** https://mc.manuscriptcentral.com/jamia?URL_MASK=95d2e42a6e1c4425b219a8a37578c681
2. Login ke ScholarOne JAMIA
3. Klik **"Decline Transfer"**
4. Reason (optional): "Due to budget constraints related to article processing charges"
5. Submit

**Estimated time:** 2-3 menit

---

## 📤 STEP 1: GO TO JMIR SUBMISSION PORTAL

1. **Open browser:** https://jmir.org/
2. **Click:** "Submit Manuscript" (top menu)
3. **Select Journal:** "JMIR Medical Informatics"
4. **Login/Register:** Gunakan email Anda (jika belum punya account, register dulu)

**Estimated time:** 3-5 menit

---

## 📋 STEP 2: FILL MANUSCRIPT METADATA

### **Article Type:**
- Select: **"Original Paper"**

### **Title:**
```
High Consistency, Limited Accuracy: Evaluating Large Language Models for Binary Medical Diagnosis
```

### **Running Title (Short Title):**
```
LLM Performance in Binary Medical Diagnosis
```

### **Abstract:**
Copy-paste dari `JMIR_SUBMISSION/JMIR_MANUSCRIPT.md` (section Abstract)

**Abstract text (ready to copy):**
```
BACKGROUND: Large language models (LLMs) show promise for clinical decision support, but their performance in medical diagnosis remains incompletely characterized, particularly regarding consistency versus accuracy.

OBJECTIVE: This study aims to evaluate the diagnostic accuracy and reproducibility of three state-of-the-art LLMs (GPT-4o, Gemini-2.0-Flash-Exp, and Qwen-Plus) for binary heart disease classification, and provide practical guidance for clinical implementation.

METHODS: We evaluated three LLMs on 100 heart disease cases from the UCI Heart Disease dataset using two different prompt templates, with 4 repeated runs per configuration to assess consistency. We analyzed accuracy, precision, recall, specificity, and intra-model consistency. Statistical significance was assessed using McNemar's test (α=0.05).

RESULTS: All models achieved near-random accuracy (GPT-4o: 49-51%; Gemini-2.0: 49-51%; Qwen-Plus: 48-51%) with extremely high recall (98-100%) but poor specificity (0-2%), resulting in ~50% false positive rates. However, consistency was remarkably high across all models (GPT-4o: 98.5%; Gemini-2.0: 99.0%; Qwen-Plus: 98.0%). Inter-model agreement reached 98-99% for cases with disease. Prompt engineering showed minimal impact (accuracy differences <3%, p>0.05). Models demonstrated systematic bias toward positive diagnosis regardless of clinical features.

CONCLUSIONS: Current LLMs exhibit a critical dissociation between high consistency and poor accuracy in binary medical diagnosis. While predictions are reproducible, diagnostic performance does not exceed chance levels. These findings suggest LLMs in their current form are unsuitable for standalone diagnostic decision-making but may serve supplementary roles with appropriate human oversight, validation protocols, and bias mitigation strategies. Healthcare systems must prioritize accuracy validation over consistency metrics when evaluating AI diagnostic tools.
```

### **Keywords (6-8 keywords):**
```
artificial intelligence
large language models
clinical decision support
diagnostic accuracy
reproducibility
medical informatics
heart disease
machine learning
```

### **Word Count:**
```
2143
```
(excluding title page, abstract, references, tables, figures)

**Estimated time:** 10-15 menit

---

## 👥 STEP 3: ADD AUTHORS

### **Author 1 - First Author:**
- **First Name:** Nur Arifah Fadhilah
- **Last Name:** Anggriani
- **Email:** nurarifah16@gmail.com
- **Affiliation:** Universitas Hasanuddin, Makassar, Indonesia
- **ORCID:** 0009-0002-5976-7810
- **Role:** Conceptualization, Methodology, Software, Data Curation, Writing - Original Draft

### **Author 2 - Corresponding Author:** ✅
- **First Name:** Andi Besse Firdausiah
- **Last Name:** Mansur
- **Email:** firdamansur@gmail.com
- **Affiliation:** Universitas Hasanuddin, Makassar, Indonesia
- **ORCID:** 0000-0002-1775-0015
- **Role:** Supervision, Methodology, Writing - Review & Editing
- **☑️ Check:** "Corresponding Author"

### **Author 3:**
- **First Name:** Andi Muhamad
- **Last Name:** Atnang
- **Email:** atnang@gmail.com
- **Affiliation:** Universitas Hasanuddin, Makassar, Indonesia
- **ORCID:** (leave blank if none)
- **Role:** Validation, Formal Analysis

### **Author 4:**
- **First Name:** Ahmad Nuzry
- **Last Name:** Ahmad Nuzry
- **Email:** ahmadnuzry@gmail.com
- **Affiliation:** Universitas Hasanuddin, Makassar, Indonesia
- **ORCID:** (leave blank if none)
- **Role:** Resources, Project Administration

**Estimated time:** 8-10 menit

---

## 💰 STEP 4: FINANCIAL DISCLOSURE & FEE WAIVER (CRITICAL!)

### **Funding Statement:**
```
This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.
```

### **Article Processing Charge (APC) Waiver Request:** ✅ **WAJIB!**
- **☑️ Check:** "Request APC waiver or discount"
- **Reason:** Select **"Unfunded research from a developing country"**
- **Additional justification (optional but recommended):**
```
This study was conducted by researchers from Universitas Hasanuddin in Indonesia without external funding. As researchers from a developing country institution, we respectfully request a full fee waiver to enable open access publication of our findings.
```

**Expected outcome:** 100% fee waiver approval (Indonesia is eligible country)

**Estimated time:** 3-5 menit

---

## 📄 STEP 5: UPLOAD MANUSCRIPT FILES

### **File 1: Main Manuscript** (REQUIRED)
- **File Location:** `E:\project\Riset\heart-disease\JMIR_SUBMISSION\JMIR_MANUSCRIPT.docx`
- **File Type:** "Main Document"
- **Label:** "Manuscript"
- **Browse & Upload:** Click "Browse" → Navigate to file → Upload

### **File 2: Figure 1** (Main Figure)
- **File Location:** `E:\project\Riset\heart-disease\JAMIA_SUBMISSION\Figures\Figure1.png`
- **File Type:** "Figure"
- **Label:** "Figure 1"
- **Description:** "Intra-model consistency patterns across repeated runs"

### **File 3: Figure 2** (Main Figure)
- **File Location:** `E:\project\Riset\heart-disease\JAMIA_SUBMISSION\Figures\Figure2.png`
- **File Type:** "Figure"
- **Label:** "Figure 2"
- **Description:** "Confusion matrices for all model-prompt combinations"

### **File 4: Figure 3** (Main Figure)
- **File Location:** `E:\project\Riset\heart-disease\JAMIA_SUBMISSION\Figures\Figure3.png`
- **File Type:** "Figure"
- **Label:** "Figure 3"
- **Description:** "Prompt sensitivity analysis"

### **File 5: Supplementary File** (ALL-IN-ONE!)
- **File Location:** `E:\project\Riset\heart-disease\JMIR_SUBMISSION\MULTIMEDIA_APPENDIX_1_COMPLETE.docx`
- **File Type:** "Supplementary File" atau "Multimedia Appendix"
- **Label:** "Multimedia Appendix 1"
- **Description:** "Supplementary Tables (S1-S5) and Figures (S1-S6)"

**⚠️ IMPORTANT:** Upload MULTIMEDIA_APPENDIX_1_COMPLETE.docx ONLY (jangan upload FigureS1-S6.png terpisah karena sudah embedded!)

**Total files to upload:** 5 files
**Total size:** ~3-4 MB

**Estimated time:** 10-12 menit

---

## 📝 STEP 6: COVER LETTER

Copy-paste dari `E:\project\Riset\heart-disease\JMIR_SUBMISSION\COVER_LETTER.md`

**Quick copy (full text):**

```
December 21, 2025

Dr. Gunther Eysenbach
Editor-in-Chief
JMIR Medical Informatics

Dear Dr. Eysenbach,

We are pleased to submit our original research article entitled "High Consistency, Limited Accuracy: Evaluating Large Language Models for Binary Medical Diagnosis" for consideration for publication in JMIR Medical Informatics.

CONTEXT OF PREVIOUS SUBMISSION

This manuscript was previously submitted to the Journal of the American Medical Informatics Association (JAMIA) under manuscript ID amiajnl-2025-018821. The JAMIA editors indicated that while our work met their quality standards and successfully completed peer review, the scope—evaluating performance of existing LLM models rather than developing novel methodological approaches—was a better fit for JAMIA Open or a journal focused on practical evaluation research. Following this guidance and considering our budget constraints regarding article processing charges, we are now submitting to JMIR Medical Informatics, which we believe is an ideal venue given its emphasis on practical AI applications in healthcare.

MANUSCRIPT OVERVIEW

Our study addresses a critical gap in current AI-for-healthcare research: while much attention focuses on developing novel models, relatively little work systematically evaluates the practical performance characteristics of widely available commercial LLMs in clinical decision support contexts. We evaluated three state-of-the-art large language models (GPT-4o, Gemini-2.0-Flash-Exp, and Qwen-Plus) for binary heart disease diagnosis using 100 cases from the UCI Heart Disease dataset, with repeated runs to assess both accuracy and consistency.

KEY CONTRIBUTIONS

1. Systematic characterization of a critical dissociation between consistency and accuracy in LLM-based medical diagnosis
2. Evidence that current commercial LLMs achieve near-random diagnostic performance (49-51% accuracy) despite high reproducibility (98-99% consistency)
3. Demonstration that prompt engineering provides minimal performance improvement (<3% change)
4. Practical implementation guidelines for healthcare systems considering LLM adoption
5. Cost-benefit analysis framework for evaluating AI diagnostic tools
6. Policy recommendations for regulatory oversight of medical AI applications

SIGNIFICANCE AND PRACTICAL VALUE

This work directly addresses JMIR Medical Informatics' focus on practical evaluation and implementation of health information technology. Our findings have immediate implications for:

- Healthcare administrators evaluating LLM procurement decisions
- Clinical informaticists designing AI-assisted workflows
- Policy makers developing AI governance frameworks
- Researchers planning validation studies for medical AI tools

The manuscript includes comprehensive supplementary materials with detailed performance metrics, prompt templates, and statistical analyses to support reproducibility and practical application.

TARGET AUDIENCE

This manuscript will be of particular interest to:
- Medical informaticians and health IT professionals
- Healthcare administrators and decision-makers
- Clinical practitioners interested in AI decision support
- AI ethics and policy researchers
- Quality improvement and patient safety specialists

PREPRINT AND TRANSPARENCY

A preprint version of this manuscript has been posted to medRxiv (DOI: 10.64898/2025.12.08.25341823) to facilitate rapid dissemination and community feedback. All data, code, and materials are publicly available to support reproducibility and independent validation.

SUGGESTED REVIEWERS

We respectfully suggest the following experts who could provide valuable peer review:

1. Dr. Vince Liévin
   - Technical University of Denmark
   - Email: vili@dtu.dk
   - Expertise: LLM evaluation in medical contexts, consistency analysis
   - Recent work: "Can Large Language Models Reason About Medical Questions?"

2. Dr. Michael Wornow
   - Stanford University
   - Email: wornow@stanford.edu
   - Expertise: Clinical AI deployment, practical performance evaluation
   - Recent work: Clinical LLM benchmarking and evaluation frameworks

3. Dr. Zhengyun Ji
   - Mayo Clinic
   - Email: ji.zhengyun@mayo.edu
   - Expertise: Medical informatics, AI in clinical decision support
   - Recent work: Healthcare AI implementation and validation studies

CONFLICTS OF INTEREST

The authors declare no conflicts of interest.

FUNDING

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

We believe this manuscript represents a timely and important contribution to understanding the practical capabilities and limitations of large language models in medical diagnosis. We look forward to your editorial decision and reviewer feedback.

Thank you for your consideration.

Sincerely,

Andi Besse Firdausiah Mansur (Corresponding Author)
Universitas Hasanuddin
Email: firdamansur@gmail.com
ORCID: 0000-0002-1775-0015
```

**Estimated time:** 2-3 menit (copy-paste)

---

## ✅ STEP 7: REVIEW & SUBMIT

### **Pre-submission Checklist:**
- [ ] All author information complete and accurate
- [ ] ORCID IDs entered (for authors who have them)
- [ ] Corresponding author marked correctly
- [ ] Fee waiver request checked and justified
- [ ] All 5 files uploaded (1 manuscript + 3 figures + 1 supplementary)
- [ ] Cover letter pasted
- [ ] Keywords entered
- [ ] Word count verified
- [ ] Abstract formatted correctly

### **Final Actions:**
1. **Review:** Click "Review Submission" - check all fields
2. **Agree:** Check "I agree to terms and conditions"
3. **Submit:** Click **"Submit Manuscript"**
4. **Confirmation:** Save confirmation email and manuscript ID

**Estimated time:** 5-7 menit

---

## 📧 STEP 8: CONFIRMATION & NEXT STEPS

### **Immediately After Submission:**
1. You'll receive **confirmation email** from JMIR (check spam folder!)
2. Email contains:
   - Manuscript ID (save this!)
   - Login credentials for tracking
   - Estimated timeline

### **Expected Timeline:**
- **Initial screening:** 1-2 weeks (editorial check for fit/quality)
- **Peer review:** 4-8 weeks (typically 2-3 reviewers)
- **First decision:** 6-10 weeks total
- **Revision period:** 2-3 weeks (if revisions requested)
- **Final decision:** 2-4 weeks after revision
- **Publication:** 1-2 weeks after acceptance

**Total timeline:** ~3-4 months from submission to publication

### **Fee Waiver Decision:**
- Expect decision within **1-2 weeks** after submission
- High probability of approval (100%) for Indonesia
- If approved: No APC charges (FREE publication!)
- If questions: Respond promptly with institution/funding details

---

## 🎯 QUICK ACCESS - FILE PATHS

**PowerShell commands untuk quick access:**

```powershell
# Navigate to JMIR submission folder
cd E:\project\Riset\heart-disease\JMIR_SUBMISSION

# Open main manuscript
start JMIR_MANUSCRIPT.docx

# Open supplementary file (all-in-one)
start MULTIMEDIA_APPENDIX_1_COMPLETE.docx

# Navigate to figures folder
cd E:\project\Riset\heart-disease\JAMIA_SUBMISSION\Figures

# List all figure files
ls Figure*.png
```

---

## 📊 SUBMISSION SUMMARY

| Item | Count | Status |
|------|-------|--------|
| Main manuscript | 1 file | ✅ Ready |
| Main figures | 3 files (Figure1-3.png) | ✅ Ready |
| Supplementary | 1 file (all tables + figures) | ✅ Ready |
| **Total files** | **5 files** | ✅ **Ready** |
| Word count | 2,143 words | ✅ Within limit (42.9%) |
| File size | ~3-4 MB | ✅ Within limit |
| Fee waiver | Requested | ✅ Indonesia eligible |

---

## ⚠️ COMMON MISTAKES TO AVOID

1. ❌ **JANGAN** upload FigureS1-S6.png terpisah (sudah embedded!)
2. ❌ **JANGAN** lupa check "Request fee waiver"
3. ❌ **JANGAN** submit sebelum decline JAMIA Open
4. ❌ **JANGAN** lupa mark corresponding author
5. ❌ **JANGAN** paste abstract dengan formatting (plain text only)

---

## 📞 TROUBLESHOOTING

### **Problem: File upload fails**
- **Solution:** Check file size < 10 MB per file, use supported formats (.docx, .png)

### **Problem: Cannot find fee waiver option**
- **Solution:** Look in "Financial Disclosure" or "Author Charges" section

### **Problem: Forgot to decline JAMIA Open first**
- **Solution:** Withdraw JMIR submission immediately, decline JAMIA first, then resubmit

### **Problem: Missing required field**
- **Solution:** ScholarOne will show error message, scroll up to find red-marked fields

---

## 🎉 YOU'RE READY!

**Total estimated time:** 45-60 minutes

**Steps:**
1. ✅ Decline JAMIA Open (2-3 min)
2. ✅ Register/Login to JMIR (3-5 min)
3. ✅ Fill metadata (10-15 min)
4. ✅ Add authors (8-10 min)
5. ✅ Request fee waiver (3-5 min)
6. ✅ Upload files (10-12 min)
7. ✅ Paste cover letter (2-3 min)
8. ✅ Review & submit (5-7 min)

**Good luck! 🚀**
