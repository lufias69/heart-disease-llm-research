Dear Editor-in-Chief,
JMIR Medical Informatics

Re: Submission of Original Research Article

We are pleased to submit our original research article titled "High Consistency, Limited Accuracy: Evaluating Large Language Models for Binary Medical Diagnosis" for consideration for publication in JMIR Medical Informatics.

## Study Significance and Fit with JMIR Medical Informatics

As healthcare systems increasingly consider deploying Large Language Models (LLMs) for clinical decision support, understanding their reliability and accuracy is critical for patient safety. Our study addresses a critical gap in the literature by systematically evaluating the relationship between consistency and accuracy in LLM medical diagnosis—a dimension rarely examined but essential for clinical implementation.

This manuscript aligns with JMIR Medical Informatics' focus on evaluation of health information technologies and their clinical applications. Our findings provide evidence-based guidance for healthcare informaticians, clinical decision-makers, and AI developers regarding appropriate use cases, implementation safeguards, and technical limitations of current LLM systems.

## Key Contributions

Our study makes several novel contributions to medical informatics:

1. **Systematic Reproducibility Assessment**: First comprehensive evaluation of intra-model consistency across multiple independent diagnostic runs, revealing 99-100% reproducibility despite 50% accuracy

2. **Consistency-Accuracy Dissociation**: Documentation of a fundamental paradox where exceptional reproducibility coexists with chance-level diagnostic performance, challenging assumptions about AI reliability

3. **Prompt Engineering Limitations**: Demonstration that diagnostic behavior is deeply encoded in model weights (GPT-4o: 0% sensitivity, others: 1-2%), with important implications for prompt-based optimization strategies

4. **Systematic Error Patterns**: Evidence that errors are not random but shared across models (98-99% agreement), suggesting fundamental limitations in LLM medical reasoning

5. **Practical Implementation Guidance**: Evidence-based recommendations for healthcare systems, including appropriate use cases, validation protocols, and cost-benefit considerations

## Clinical and Implementation Relevance

Our findings have immediate practical implications:

- **Patient Safety**: Identifies risks of LLM over-diagnosis (49-51 false positives per 100 cases) that could lead to unnecessary testing and patient anxiety
- **Resource Allocation**: Quantifies downstream costs of false positives for healthcare budget planning
- **Deployment Guidelines**: Provides specific recommendations for restricting LLM use to supplementary roles with mandatory human oversight
- **Validation Protocols**: Establishes need for rigorous local validation before clinical deployment

## Methodological Rigor

Our study employs:
- Multiple state-of-the-art models (GPT-4o, Gemini-2.0-Flash, Qwen-Plus)
- Repeated independent assessments (4 runs × 100 cases × 3 models = 1,200 predictions)
- Multiple prompt variations to assess sensitivity
- Diverse clinical cases through stratified sampling
- Comprehensive statistical analysis with multiple performance metrics
- Qualitative analysis of reasoning patterns

## Target Audience

This work is directly relevant to JMIR Medical Informatics' readership:
- Health informaticians designing clinical decision support systems
- Healthcare administrators evaluating AI adoption
- Clinical AI developers optimizing diagnostic models
- Medical professionals considering LLM integration
- Regulatory bodies establishing AI deployment guidelines
- Researchers studying reproducibility in medical AI

## Prior Presentation

This work was previously submitted to JAMIA but was redirected as being more suitable for journals focused on AI evaluation rather than methodological innovation. We believe JMIR Medical Informatics is an ideal venue given its emphasis on rigorous evaluation of health information technologies and practical implementation guidance.

A preprint version is available on medRxiv (DOI: 10.64898/2025.12.08.25341823), ensuring transparency and enabling early access to our findings.

## Author Contributions and Conflicts

All authors have made substantial contributions to conception, design, analysis, and manuscript preparation. We have no conflicts of interest to declare. This research was conducted without external funding, ensuring complete independence of findings.

## Manuscript Specifications

- Word count: ~3,800 words (excluding abstract, references, tables, figures)
- Tables: 4 main text + 5 supplementary
- Figures: 3 main text + 6 supplementary  
- References: 15
- Supplementary materials: Comprehensive appendix with detailed statistical analyses, sample predictions, and additional visualizations

We confirm that:
- This manuscript is original and not under consideration elsewhere
- All authors have approved the final version
- Data and code will be made publicly available upon acceptance
- We will comply with JMIR's open access policies

## Data and Code Availability

The UCI Heart Disease dataset used in this study is publicly available. All analysis code, experiment results, and supplementary materials will be deposited in a public repository upon acceptance, ensuring reproducibility and enabling further research.

We believe this manuscript will be of significant interest to JMIR Medical Informatics' readership and contributes important evidence for responsible LLM deployment in clinical settings. We appreciate your consideration and look forward to your response.

Yours sincerely,

**Syaiful Bachri Mustamin, M.Cs.**
Corresponding Author
Department of Information Technology
Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari
Kendari, Southeast Sulawesi, Indonesia
Email: syaifulbachri@mail.ugm.ac.id
Phone: +62 851-5629-7969
ORCID: https://orcid.org/0009-0005-0456-8618

**On behalf of all authors:**
- Dwi Anggriani, S.Kom. (First Author)
- Muhammad Atnang, S.Kom., M.Kom. (Co-author)
- Kartini Aprilia Pratiwi Nuzry, S.Kom., M.MT. (Co-author)

---

## ARTICLE PROCESSING CHARGE (APC) WAIVER REQUEST

We respectfully request a full APC waiver for this submission.

**Justification:**
1. Authors are from Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari, Indonesia (developing country)
2. This research received no funding from any source (public, commercial, or not-for-profit sectors)
3. Our institution has no budget allocated for article processing charges
4. This study provides important practical insights for responsible AI deployment in healthcare

We believe our manuscript meets the quality standards and scope of JMIR Medical Informatics and would contribute valuable evidence-based guidance to the field.

Thank you for considering our waiver request.
- Kartini Aprilia Pratiwi Nuzry, S.Kom., M.MT.

---

**Suggested Reviewers:**

1. **Dr. Vince Liévin**
   - Technical University of Denmark
   - Expert in LLM medical reasoning and evaluation
   - Recent publication: "Can large language models reason about medical questions?" (Patterns, 2024)
   - Email: vlor@dtu.dk

2. **Dr. Michael Wornow**
   - Stanford University
   - Expert in health AI reproducibility and evaluation
   - Recent work on clinical LLM validation
   - Email: wornow@stanford.edu

3. **Dr. Zhengyun Ji**
   - Expert in AI hallucination and consistency
   - Recent publication: "Survey of hallucination in natural language generation" (ACM Computing Surveys, 2023)
   - Email: zhengyun.ji@gmail.com

**Note:** We have no personal or professional relationships with the suggested reviewers that would constitute a conflict of interest.
