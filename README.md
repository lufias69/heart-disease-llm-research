# High Consistency, Limited Accuracy: Evaluating LLMs for Binary Medical Diagnosis

[![DOI](https://img.shields.io/badge/medRxiv-10.64898%2F2025.12.08.25341823-blue)](https://doi.org/10.64898/2025.12.08.25341823)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This repository contains the complete code and data for our study evaluating the consistency and accuracy of Large Language Models (GPT-4o, Gemini-2.0-Flash, Qwen-Plus) in binary medical diagnosis using heart disease data.

## 📄 Publication

**Preprint:** [medRxiv DOI: 10.64898/2025.12.08.25341823](https://doi.org/10.64898/2025.12.08.25341823)

**Authors:** Dwi Anggriani, Syaiful Bachri Mustamin, Muhammad Atnang, Kartini Aprilia Pratiwi Nuzry

**Affiliation:** Department of Information Technology, Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari, Indonesia

## 🔬 Key Findings

- **Exceptional Consistency:** All LLMs achieved 99-100% intra-model consistency across repeated runs
- **Limited Accuracy:** Diagnostic accuracy remained at ~50%, equivalent to random guessing
- **Systematic Bias:** Strong bias toward positive diagnosis (49-51 false positives vs 0-1 false negatives per 100 cases)
- **Prompt Insensitivity:** Minimal impact from prompt variation (<3% change)
- **High Inter-Model Agreement:** 98-99% agreement across different LLM architectures

## 🗂️ Repository Structure

```
heart-disease/
├── data/
│   └── heart.csv                          # UCI Heart Disease dataset (303 patients)
├── config/
│   └── config.yaml                        # Configuration file (API keys, models, prompts)
├── clustering/
│   └── clustering.py                      # K-means clustering for diverse sampling
├── sampling/
│   └── sampling.py                        # Stratified sampling (100 test cases)
├── llm_testing/
│   ├── llm_tester.py                      # Main LLM evaluation engine
│   └── database.py                        # SQLite checkpoint system
├── evaluation/
│   └── evaluator.py                       # Consistency and accuracy metrics
├── scripts/
│   ├── analyze.py                         # Comprehensive analysis
│   ├── compare_prompts.py                 # Prompt sensitivity analysis
│   └── [other analysis scripts]           # Additional analysis tools
├── results/
│   ├── llm_predictions/                   # Raw predictions from each model
│   ├── evaluation/                        # Consistency and accuracy metrics
│   └── plots/                             # Visualization outputs
├── manuscript/
│   ├── JAMIA_VERSION.md                   # Manuscript for JAMIA submission
│   └── SUPPLEMENTARY_MATERIALS.md         # Supplementary materials
├── requirements.txt                       # Python dependencies
└── README.md                              # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for OpenAI GPT-4o, Google Gemini, and Alibaba Qwen
- ~2GB disk space for results

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/heart-disease-llm-research.git
cd heart-disease-llm-research

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. Create `config/config.yaml` with your API keys:

```yaml
api_keys:
  openai: "your-openai-api-key"
  google: "your-google-api-key"
  qwen: "your-qwen-api-key"

models:
  gpt: "gpt-4o"
  gemini: "gemini-2.0-flash-exp"
  qwen: "qwen-plus"

temperature: 0.7
```

**⚠️ Important:** Never commit `config.yaml` with real API keys!

### Running the Experiment

**Option 1: Complete pipeline**

```bash
python run_experiment.py
```

This executes:
1. K-means clustering (k=2) on UCI dataset
2. Stratified sampling (50 cases per cluster = 100 total)
3. LLM evaluation (3 models × 2 prompts × 4 runs × 100 cases = 2,400 predictions)
4. Comprehensive analysis and visualization

**Option 2: Resume interrupted experiment**

```bash
python scripts/resume_experiment.py
```

The SQLite checkpoint system automatically saves progress.

**Option 3: Run specific analysis**

```bash
# Prompt comparison
python scripts/compare_prompts.py

# Threshold optimization
python scripts/optimize_threshold.py

# View prediction errors
python scripts/view_errors.py

# Check experiment progress
python scripts/check_progress.py
│   ├── resume_experiment.py       # Resume from checkpoint
│   ├── view_errors.py             # View errors
│   ├── test_checkpoint.py         # Test checkpoint system
│   ├── reset_database.py          # Reset database
│   ├── export_predictions.py      # Export to various formats
│   ├── test_api.py                # Test API connections
│   └── generate_clustering_report.py
│
├── results/                        # Output files
│   ├── clustering/                # Clustering results
│   │   ├── clustered_data.csv
│   │   └── optimal_k_analysis_report.png
│   ├── sampling/                  # Test samples
│   │   ├── test_set.csv
│   │   └── llm_test_data.csv
```

## 📊 Expected Outputs

After running the experiment, results will be saved in `results/`:

### LLM Predictions
- `llm_predictions/gpt_results_old.csv` - GPT-4o predictions (Expert prompt, 400 rows)
- `llm_predictions/gpt_results_new.csv` - GPT-4o predictions (Neutral prompt, 400 rows)
- `llm_predictions/gemini_results_old.csv` - Gemini predictions (Expert prompt, 400 rows)
- `llm_predictions/gemini_results_new.csv` - Gemini predictions (Neutral prompt, 400 rows)
- `llm_predictions/qwen_results_old.csv` - Qwen predictions (Expert prompt, 400 rows)
- `llm_predictions/qwen_results_new.csv` - Qwen predictions (Neutral prompt, 400 rows)
- Original files (`*_results.csv` without suffix) available for backward compatibility

### Evaluation Metrics
- `evaluation/model_comparison.csv` - Accuracy, precision, recall, F1 for all models
- `evaluation/consistency_metrics.csv` - Intra-model consistency analysis
- `evaluation/prompt_comparison.csv` - Prompt sensitivity results

### Visualizations
- `plots/comprehensive_consistency_analysis.png` - Figure 1 (consistency metrics)
- `plots/figure_2_confusion_matrices.png` - Figure 2 (confusion matrices)
- `plots/prompt_comparison.png` - Figure 3 (prompt impact)

## 🔧 Key Features

### 1. SQLite Checkpoint System
- **Automatic saving** after each prediction
- **Duplicate prevention** - skips already-completed cases
- **Crash recovery** - resume from last checkpoint
- **Query interface** - inspect progress anytime

```python
# Check experiment progress
python scripts/check_progress.py
```

### 2. Robust API Handling
- Exponential backoff for rate limits
- Automatic retry on transient errors
- Timeout protection
- Cost tracking per model

### 3. Comprehensive Evaluation
- **Intra-model consistency:** Agreement across 4 runs
- **Inter-model agreement:** Cohen's kappa, pairwise agreement
- **Diagnostic accuracy:** Accuracy, precision, recall, F1, confusion matrices
- **Prompt sensitivity:** Prediction changes across prompts
- **Error pattern analysis:** All-correct, all-wrong, mixed outcomes

## 📦 Dataset

We use the **UCI Heart Disease Dataset** (Janosi et al., 1988):
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease)
- **Cases:** 303 patients from Cleveland Clinic
- **Features:** 13 clinical parameters (age, sex, chest pain, BP, cholesterol, ECG, etc.)
- **Outcome:** Binary (presence/absence of significant coronary stenosis)
- **DOI:** 10.24432/C52P4X

**Sampling Strategy:**
- K-means clustering (k=2) for diversity
- 50 cases per cluster (100 total)
- Balanced prevalence: 51% positive, 49% negative

## 🔑 Reproducibility

All experiments are fully reproducible:

1. **Fixed random seeds** in clustering and sampling
2. **Temperature=0.7** for all LLM calls (controlled stochasticity)
3. **Checkpoint system** logs exact timestamps and parameters
4. **Versioned dependencies** in `requirements.txt`
5. **Complete code** with detailed comments

### 4. Database
`results/llm_predictions/predictions.db`
Full audit trail with timestamps

---

## 💡 Usage Examples

### Example 1: Full Run
```bash
python run_experiment.py
# Runs complete pipeline with checkpoint
```

### Example 2: Test First
```bash
python scripts/test_checkpoint.py
# Test with 1 sample only
```

### Example 3: Monitor While Running
```bash
# Terminal 1
python run_experiment.py

# Terminal 2
watch -n 5 python scripts/check_progress.py
```

## 📈 Results Summary

| Model | Consistency | Accuracy | Precision | Recall | F1 |
|-------|------------|----------|-----------|--------|-----|
| **GPT-4o (Expert)** | 99.25% | 51.0% | 51.0% | 100% | 67.6% |
| **GPT-4o (Neutral)** | 99.00% | 49.0% | 49.0% | 100% | 65.8% |
| **Gemini (Expert)** | 99.50% | 51.0% | 51.0% | 98% | 67.1% |
| **Gemini (Neutral)** | 99.25% | 49.0% | 49.0% | 100% | 65.8% |
| **Qwen (Expert)** | **100.00%** | 51.0% | 51.0% | 100% | 67.6% |
| **Qwen (Neutral)** | 99.75% | 48.0% | 48.5% | 98% | 64.9% |

**Key Finding:** 50-percentage-point gap between consistency (99-100%) and accuracy (~50%)

## 💡 Clinical Implications

Our findings suggest:

✅ **Suitable for:**
- Second opinion systems (high reproducibility builds confidence)
- Triage/screening tools (high sensitivity for rule-out)
- Medical education (consistent explanations)
- Research hypothesis generation

❌ **Not suitable for:**
- Primary diagnostic decision-making
- Binary classification without human oversight
- Low-resource settings requiring high specificity

## 🛠️ Requirements

See `requirements.txt` for full list. Key dependencies:

```
openai>=1.0.0           # GPT-4o API
google-generativeai     # Gemini API
dashscope              # Qwen API
pandas>=2.0.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
pyyaml>=6.0
scipy>=1.10.0
```

## 📝 Citation

If you use this code or data, please cite our preprint:

```bibtex
@article{anggriani2025consistency,
  title={High Consistency, Limited Accuracy: Evaluating Large Language Models for Binary Medical Diagnosis},
  author={Anggriani, Dwi and Mustamin, Syaiful Bachri and Atnang, Muhammad and Nuzry, Kartini Aprilia Pratiwi},
  journal={medRxiv},
  year={2025},
  doi={10.64898/2025.12.08.25341823}
}
```

## 📧 Contact

**Corresponding Author:** Syaiful Bachri Mustamin  
**Email:** syaifulbachri@mail.ugm.ac.id  
**Affiliation:** Department of Information Technology, Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari, Indonesia

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the Heart Disease dataset
- OpenAI, Google, and Alibaba for API access
- Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari for institutional support

## 🔗 Links

- **Preprint:** https://doi.org/10.64898/2025.12.08.25341823
- **Dataset:** https://archive.ics.uci.edu/dataset/45/heart+disease
- **Institution:** https://istekaisyiyah.ac.id

---

**Last Updated:** December 2025
- Model performance comparison (accuracy, F1)
- Consistency patterns across models
- Quality of medical justifications
- Practical implications for clinical AI

---

## 👥 Authors & Citation

**Research Team**: [Your Name/Institution]  
**Target Journal**: Q2 Medical/AI Journal  
**Dataset**: UCI Heart Disease Dataset

```bibtex
@article{heartdisease_llm_2025,
  title={Evaluating Consistency and Explainability of Large Language Models in Heart Disease Prediction},


