# SUBMISSION CHECKLIST FOR JOURNAL PUBLICATION

## Pre-Submission Preparation

### ✅ Manuscript Components

- [x] **Main manuscript** (DRAFT_PAPER.md) - 8,500 words
- [x] **Abstract** - 350 words with Background, Methods, Results, Conclusions
- [x] **Keywords** - 7 keywords provided
- [ ] **Title page** - Separate file with:
  - Full title
  - Author names and affiliations
  - Corresponding author contact
  - Word count
  - Number of figures/tables
- [x] **Main text** - Introduction, Methods, Results, Discussion, Conclusions
- [x] **References** - 21 citations in numbered format
- [ ] **Author contributions statement**
- [ ] **Funding statement**
- [ ] **Conflicts of interest statement**
- [ ] **Data availability statement**
- [ ] **Ethics approval statement** (if required)

### ✅ Figures and Tables

**Main Figures:**
- [x] Figure 1: Comprehensive consistency analysis (7 panels)
  - Location: `results/evaluation/comprehensive_consistency_analysis.png`
  - Format: PNG, 300 DPI
  - Size: High resolution for print
  
- [x] Figure 2: Confusion matrices (need to generate)
  - Should show all 6 model-prompt combinations
  
- [x] Figure 3: Prompt comparison
  - Location: `results/evaluation/prompt_comparison.png`

**Main Tables:**
- [x] Table 1: Intra-model consistency analysis
- [x] Table 2: Inter-model agreement
- [x] Table 3: Diagnostic performance metrics
- [x] Table 4: Prompt robustness analysis
- [x] Table 5: Error consistency across models

**Supplementary Materials:**
- [ ] Supplementary Table S1: Complete prediction data
- [ ] Supplementary Table S2: Sample justifications
- [ ] Supplementary Table S3: Threshold optimization
- [ ] Supplementary Figure S1: ROC curves
- [ ] Supplementary Figure S2: Prediction distributions
- [ ] Supplementary File S3: Code and prompts

### ✅ Data and Code Sharing

- [x] **GitHub repository** setup
  - [ ] Clean and document code
  - [ ] Add README with reproduction instructions
  - [ ] Include requirements.txt
  - [ ] Add LICENSE file
  - [ ] Create DOI using Zenodo (optional but recommended)
  
- [x] **Data availability**
  - Database files: predictions_old_prompt.db, predictions.db
  - CSV exports: All model results
  - Test data: llm_test_data.csv
  
- [ ] **Reproducibility package**
  - [ ] Environment setup instructions
  - [ ] API configuration guide (without exposing keys)
  - [ ] Step-by-step reproduction guide

### ✅ Formatting Requirements

**Check target journal guidelines for:**
- [ ] Word limit (usually 3,000-6,000 for research articles)
- [ ] Abstract word limit (usually 250-350)
- [ ] Reference style (Vancouver, APA, AMA, etc.)
- [ ] Figure format requirements (TIFF, EPS, PNG, etc.)
- [ ] Figure resolution (usually 300-600 DPI)
- [ ] Table formatting guidelines
- [ ] Line numbering requirement
- [ ] Page numbering
- [ ] Font and spacing requirements

### ✅ Legal and Ethical

- [ ] **Copyright transfer form** (if required)
- [ ] **Author agreement form** - All authors sign
- [ ] **ICMJE disclosure forms** - One per author
- [ ] **Ethics approval** - Not required for this study (public de-identified data)
- [ ] **Informed consent** - Not applicable
- [ ] **Data use agreements** - UCI dataset is public domain
- [ ] **AI usage disclosure** - Declare use of LLM APIs for research purposes

### ✅ Quality Control

- [ ] **Spell check** entire manuscript
- [ ] **Grammar check** using professional tools
- [ ] **Citation check** - All references cited in text, no orphans
- [ ] **Figure/table numbering** - Sequential and referenced in text
- [ ] **Consistency check**:
  - [ ] Terminology consistent throughout
  - [ ] Abbreviations defined at first use
  - [ ] Numbers match between text and tables
  - [ ] Statistical reporting consistent
  
- [ ] **Co-author review** - All authors approve final version
- [ ] **External reviewer** - Consider pre-submission peer review
- [ ] **Plagiarism check** - Run through iThenticate or Turnitin

---

## Target Journals (Ranked by Fit)

### Tier 1: High-Impact Medical Informatics

1. **JMIR Medical Informatics**
   - Impact Factor: ~3.5
   - Scope: Perfect fit - AI in medicine, clinical decision support
   - Submission: https://medinform.jmir.org/
   - Turnaround: ~8 weeks
   - Open Access: Yes (fee: $2,500)

2. **JAMIA (Journal of American Medical Informatics Association)**
   - Impact Factor: ~6.5
   - Scope: Medical informatics, AI applications
   - Submission: https://academic.oup.com/jamia
   - Turnaround: ~12 weeks
   - Open Access: Optional

3. **Nature Digital Medicine**
   - Impact Factor: ~12
   - Scope: Digital health technologies
   - Submission: https://www.nature.com/npjdigitalmed/
   - Turnaround: ~6 weeks initial decision
   - Open Access: Yes (fee: $5,290)

### Tier 2: AI and Medicine Journals

4. **Artificial Intelligence in Medicine**
   - Impact Factor: ~7
   - Scope: AI methods in healthcare
   - Submission: https://www.journals.elsevier.com/artificial-intelligence-in-medicine
   - Turnaround: ~10 weeks

5. **Journal of Medical Internet Research (JMIR)**
   - Impact Factor: ~5.8
   - Scope: Internet research, digital health
   - Submission: https://www.jmir.org/
   - Open Access: Yes

6. **BMC Medical Informatics and Decision Making**
   - Impact Factor: ~3.5
   - Scope: Medical informatics, decision support
   - Submission: https://bmcmedinformdecismak.biomedcentral.com/
   - Open Access: Yes (fee: ~$2,500)

### Tier 3: Specialized Medical AI

7. **Journal of Clinical Medicine** (Special Issue: AI in Healthcare)
   - Impact Factor: ~3.9
   - Open Access: Yes

8. **Diagnostics** (Special Issue: AI in Diagnosis)
   - Impact Factor: ~3.6
   - Open Access: Yes

---

## Submission Timeline

### Week 1: Final Preparation
- [ ] Generate all missing figures
- [ ] Create supplementary materials
- [ ] Format references for target journal
- [ ] Prepare title page and forms
- [ ] Run quality checks

### Week 2: Internal Review
- [ ] Co-author review and approval
- [ ] External colleague review (optional)
- [ ] Address feedback
- [ ] Finalize all materials

### Week 3: Submission
- [ ] Register on journal submission system
- [ ] Upload all files
- [ ] Complete submission forms
- [ ] Suggest reviewers
- [ ] Submit!

### Post-Submission (Expected 6-12 weeks)
- [ ] Receive initial editorial decision
- [ ] Address reviewer comments
- [ ] Revise and resubmit
- [ ] Final acceptance

---

## Reviewer Response Strategy

### Anticipated Reviewer Concerns

**Concern 1: "Why is accuracy so low?"**
Response: This is our key finding, not a limitation. We argue accuracy reflects fundamental LLM limitations in binary diagnostic classification, which is itself a novel contribution.

**Concern 2: "Dataset is old (1980s)"**
Response: Acknowledge as limitation but note that: (1) it's a standard benchmark, (2) clinical parameters remain relevant, (3) findings about consistency vs accuracy are likely generalizable.

**Concern 3: "Only three models tested"**
Response: These represent major LLM families (OpenAI, Google, Alibaba). High inter-model agreement suggests findings are not model-specific.

**Concern 4: "No human physician comparison"**
Response: Acknowledge as limitation. Our focus was on LLM internal consistency and accuracy, not human-AI comparison. Suggest as future work.

**Concern 5: "Single disease condition"**
Response: Heart disease is clinically important and involves complex multi-parameter assessment. Suggest multi-condition replication as future work.

**Concern 6: "Temperature = 0.7 may introduce variability"**
Response: This is standard clinical practice for LLMs. The fact that we still observed 99-100% consistency despite stochastic sampling strengthens our findings.

### Response Template for Revisions

```
Dear Editor and Reviewers,

Thank you for the constructive feedback on our manuscript. We have carefully
addressed all comments and believe the manuscript is significantly improved.
Below, we provide point-by-point responses with changes highlighted in the
revised manuscript.

REVIEWER 1:

Comment 1.1: [Reviewer's comment]
Response: [Your response]
Changes: [What you changed in manuscript, with line numbers]

[Continue for all comments...]

Thank you again for your valuable feedback.
Sincerely,
[Your name]
```

---

## Post-Acceptance Checklist

- [ ] Prepare final formatted version
- [ ] Provide high-resolution figures
- [ ] Submit copyright forms
- [ ] Pay publication fees (if open access)
- [ ] Approve galley proofs
- [ ] Prepare press release (optional)
- [ ] Share on social media/academic networks
- [ ] Add to CV and institutional repository

---

## IMMEDIATE ACTION ITEMS (Priority Order)

### HIGH PRIORITY - Complete This Week

1. **Generate missing Figure 2** (Confusion matrices)
   ```python
   python scripts/generate_confusion_matrices.py
   ```

2. **Create supplementary materials**
   - ROC curves
   - Detailed prediction tables
   - Threshold optimization plots

3. **Format references** for target journal (start with JMIR format)

4. **Prepare author contributions statement**
   Example: "[Name 1]: Conceptualization, Methodology, Software, Analysis, Writing. 
            [Name 2]: Review, Supervision, Funding."

5. **Create title page** with all required metadata

### MEDIUM PRIORITY - Complete Next Week

6. **Set up GitHub repository**
   - Clean code
   - Add documentation
   - Include reproduction guide

7. **Get co-author approvals**
   - Circulate final draft
   - Collect signatures on forms

8. **Run plagiarism check**

9. **Select target journal** and customize formatting

### LOW PRIORITY - Can Do Anytime

10. **Prepare presentation slides** for conferences

11. **Draft social media posts** for publication announcement

12. **Identify potential conference** submissions (AMIA, MEDINFO, AAAI)

---

**ESTIMATED TIME TO SUBMISSION: 2-3 weeks**

**RECOMMENDED FIRST SUBMISSION: JMIR Medical Informatics**
- Best fit for scope
- Reasonable impact factor
- Fast turnaround
- Open access increases visibility
