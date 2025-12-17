# DATA AVAILABILITY STATEMENT

---

## Data Sharing

All data and code associated with this study are publicly available to ensure reproducibility and transparency.

---

## Source Dataset

**UCI Heart Disease Dataset**  
- **Repository:** UCI Machine Learning Repository  
- **URL:** https://archive.ics.uci.edu/dataset/45/heart+disease  
- **DOI:** 10.24432/C52P4X  
- **License:** CC BY 4.0 (Creative Commons Attribution)  
- **Citation:** Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1988). Heart Disease [Dataset]. UCI Machine Learning Repository.

The original dataset is publicly available and de-identified, containing no personally identifiable information. No additional ethics approval was required for this secondary analysis of public data.

---

## Research Data

**GitHub Repository:** https://github.com/lufias69/heart-disease-llm-research

The repository includes:

### 1. **Raw Prediction Data**

**Original Files (Expert Prompt - for backward compatibility):**
- `llm_predictions/gpt_results.csv` - GPT-4o predictions (400 rows: 100 cases × 4 runs)
- `llm_predictions/gemini_results.csv` - Gemini-2.0-Flash predictions (400 rows)
- `llm_predictions/qwen_results.csv` - Qwen-Plus predictions (400 rows)

**Expert Prompt (OLD):**
- `llm_predictions/gpt_results_old.csv` - GPT-4o predictions (400 rows)
- `llm_predictions/gemini_results_old.csv` - Gemini-2.0-Flash predictions (400 rows)
- `llm_predictions/qwen_results_old.csv` - Qwen-Plus predictions (400 rows)

**Neutral Prompt (NEW):**
- `llm_predictions/gpt_results_new.csv` - GPT-4o predictions (400 rows)
- `llm_predictions/gemini_results_new.csv` - Gemini-2.0-Flash predictions (400 rows)
- `llm_predictions/qwen_results_new.csv` - Qwen-Plus predictions (400 rows)

**Total:** 2,400 predictions (3 models × 2 prompts × 100 cases × 4 runs)

### 2. **Test Set**
- `sampling/llm_test_data.csv` - 100 selected clinical cases with ground truth labels
- Complete feature vectors for reproducibility

### 3. **Analysis Results**
- `evaluation/consistency_metrics.csv` - Intra-model consistency calculations
- `evaluation/model_comparison.csv` - Inter-model agreement statistics  
- `evaluation/prompt_comparison.csv` - Prompt variation analysis (both Expert and Neutral prompts)
- `evaluation/gpt_detailed_results.csv` - GPT-4o consistency per test case (100 cases)
- `evaluation/gemini_detailed_results.csv` - Gemini consistency per test case (100 cases)
- `evaluation/qwen_detailed_results.csv` - Qwen consistency per test case (100 cases)
- `evaluation/threshold_optimization.csv` - Threshold sensitivity analysis

### 4. **Figures and Tables**
- All manuscript figures (PNG, 300+ DPI)
- LaTeX table source files
- Figure generation scripts

### 5. **Source Code**
- `run_experiment.py` - Main experiment execution script
- `llm_testing/llm_tester.py` - LLM API interaction module
- `evaluation/evaluator.py` - Metrics calculation
- `clustering/clustering.py` - K-means clustering for sampling
- `sampling/sampling.py` - Test set selection
- `scripts/` - All analysis and visualization scripts

### 6. **Configuration**
- `config/config.yaml` - Experimental parameters
- `requirements.txt` - Python dependencies
- `README.md` - Reproduction instructions

---

## Reproducibility

### Full Reproduction
Complete reproduction (including new LLM API calls) requires:
1. API keys for OpenAI, Google AI Studio, and Alibaba Cloud
2. Estimated cost: ~$15-20 USD for 1,200 predictions
3. Execution time: ~2-3 hours (depending on API rate limits)

### Partial Reproduction (Analysis Only)
Researchers can reproduce all analyses and figures without API access using our provided prediction data:
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run analysis scripts in `scripts/` directory
4. All figures and tables can be regenerated from saved predictions

### Detailed Instructions
Step-by-step reproduction guide included in repository README.md

---

## API Access

**Note on API Keys:**  
For privacy and security, API keys are not included in the public repository. Researchers wishing to replicate LLM predictions will need to:
1. Obtain API keys from OpenAI, Google, and Alibaba Cloud
2. Configure keys according to instructions in `README.md`
3. API access is generally free (with limits) or low-cost for research purposes

---

## Data Preservation

**Long-term Archival:**  
Upon manuscript acceptance, we will create a permanent archived version of the repository using Zenodo, which will provide:
- Permanent DOI for the code/data package
- Long-term preservation guarantee
- Version control and citability

**Expected Zenodo DOI:** [To be assigned upon archival]

---

## Contact for Data

For questions about data access, code execution, or reproducibility:

**Syaiful Bachri Mustamin**  
Email: syaifulbachri@mail.ugm.ac.id  
Department of Information Technology  
Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari  
Indonesia

We commit to responding to all reasonable requests within 2 weeks and providing assistance for reproduction efforts.

---

## License

**Code:** MIT License (free for any use with attribution)  
**Data:** CC BY 4.0 (as per UCI dataset license)  
**Manuscript:** Copyright retained by authors until publication

---

*Last Updated: December 17, 2025*
