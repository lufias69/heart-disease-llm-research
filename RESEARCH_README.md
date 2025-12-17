# 🫀 Evaluating LLM Consistency in Heart Disease Prediction

**Research Project**: Evaluating Consistency and Explainability of Large Language Models (GPT, Gemini, Qwen Plus) in Heart Disease Prediction using Cluster-Based Sampling

**Target**: Q2 International Journal Publication

---

## 📋 Abstract

This research evaluates the consistency and explainability of three state-of-the-art Large Language Models (LLMs) - GPT-4, Gemini Pro, and Qwen Plus - in predicting heart disease. Using a novel cluster-based sampling approach, we test each model multiple times on representative samples to assess prediction consistency. Our methodology combines unsupervised clustering, strategic sampling, and extensive LLM testing to provide insights into the reliability of LLMs for medical diagnosis.

## 🎯 Research Objectives

1. **Clustering Analysis**: Identify natural groupings in heart disease data using unsupervised learning
2. **Representative Sampling**: Extract diverse test cases from each cluster (centroid + edge cases)
3. **Consistency Evaluation**: Test each LLM 10 times per sample to measure prediction consistency
4. **Performance Comparison**: Compare accuracy, precision, recall, F1-score across models
5. **Explainability Analysis**: Qualitatively analyze medical justifications provided by LLMs

## 📊 Methodology

### 1. Data & Clustering
- **Dataset**: Heart Disease Dataset (303 samples, 14 features)
- **Clustering Method**: K-Means (unsupervised)
- **Optimal K Selection**: Elbow Method, Silhouette Score, Davies-Bouldin Index
- **Features**: Age, sex, chest pain, blood pressure, cholesterol, ECG, heart rate, etc.

### 2. Sampling Strategy
- **Samples per Cluster**: 2 (centroid + farthest point)
- **Rationale**: Capture both representative and edge cases for diversity
- **Total Test Samples**: k_clusters × 2

### 3. LLM Testing
- **Models**: GPT-4, Gemini Pro, Qwen Plus
- **Runs per Sample**: 10 (for consistency analysis)
- **Output**: Binary prediction (Disease/No Disease) + Medical justification
- **Metrics**: Consistency score, majority vote, prediction confidence

### 4. Evaluation Metrics
- **Classification**: Accuracy, Precision, Recall, F1-Score
- **Consistency**: Agreement percentage across 10 runs
- **Statistical Tests**: Inter-model comparison
- **Qualitative**: Analysis of medical justifications

---

## 📁 Project Structure

```
heart-disease/
├── data/                           # Dataset
│   └── heart.csv (303 samples, 14 features)
│
├── config/                         # Configuration
│   └── config.yaml
│
├── clustering/                     # Step 1: Clustering
│   └── clustering.py
│
├── sampling/                       # Step 2: Sampling
│   └── sampling.py
│
├── llm_testing/                    # Step 3: LLM Testing
│   └── llm_tester.py
│
├── evaluation/                     # Step 4: Evaluation
│   └── evaluator.py
│
├── results/                        # Output directory
│   ├── clustering/
│   ├── sampling/
│   ├── llm_predictions/
│   ├── evaluation/
│   └── plots/
│
├── experiments/                    # Jupyter notebooks
├── docs/                          # Original analysis
└── run_experiment.py              # Main pipeline
```

---

## 🚀 Getting Started

### Prerequisites

1. **Python 3.8+**
2. **API Keys** for:
   - OpenAI (GPT-4)
   - Google AI (Gemini)
   - DashScope (Qwen Plus)

### Installation

```bash
# Clone repository
cd e:\project\Riset\heart-disease

# Install dependencies
pip install -r requirements.txt
```

### Setup API Keys

Create a `.env` file or set environment variables:

```bash
# Windows PowerShell
$env:OPENAI_API_KEY="your-openai-key"
$env:GOOGLE_API_KEY="your-google-key"
$env:DASHSCOPE_API_KEY="your-dashscope-key"

# Linux/Mac
export OPENAI_API_KEY="your-openai-key"
export GOOGLE_API_KEY="your-google-key"
export DASHSCOPE_API_KEY="your-dashscope-key"
```

---

## 🔬 Running the Experiment

### Option 1: Full Pipeline (Recommended)

```bash
python run_experiment.py
```

This runs all 4 steps automatically:
1. Clustering analysis
2. Sampling strategy
3. LLM testing (10 runs per sample × 3 models)
4. Evaluation and visualization

### Option 2: Step-by-Step

#### Step 1: Clustering

```bash
python clustering/clustering.py
```

**Output**:
- `results/clustering/optimal_k_analysis.png`
- `results/clustering/kmeans_k*_visualization.png`
- `results/clustering/clustered_data.csv`

#### Step 2: Sampling

```bash
python sampling/sampling.py
```

**Output**:
- `results/sampling/test_set.csv`
- `results/sampling/llm_test_data.csv`

#### Step 3: LLM Testing

```bash
python llm_testing/llm_tester.py
```

**Output**:
- `results/llm_predictions/gpt_results.csv`
- `results/llm_predictions/gemini_results.csv`
- `results/llm_predictions/qwen_results.csv`
- `results/llm_predictions/all_results.json`

#### Step 4: Evaluation

```bash
python evaluation/evaluator.py
```

**Output**:
- `results/evaluation/model_comparison.png`
- `results/evaluation/consistency_distributions.png`
- `results/evaluation/model_comparison.csv`
- `results/evaluation/model_comparison_table.tex` (for LaTeX)

---

## 📊 Expected Results

### Clustering
- Optimal number of clusters (determined by metrics)
- Cluster visualization with PCA
- Cluster statistics and characteristics

### Sampling
- Representative samples from each cluster
- Test set with ground truth labels
- Feature descriptions for LLM input

### LLM Testing
- 10 predictions per sample per model
- Binary predictions (0/1)
- Medical justifications
- Raw responses

### Evaluation
- **Performance Metrics**: Accuracy, Precision, Recall, F1-Score
- **Consistency Scores**: Agreement across 10 runs
- **Model Comparison**: Comparative analysis
- **Visualizations**: Charts and plots for paper

---

## 📈 Key Findings (To Be Completed)

After running the experiment, you will obtain:

1. **Consistency Analysis**
   - Which model is most consistent?
   - How does cluster diversity affect consistency?

2. **Performance Comparison**
   - Which model has best F1-score?
   - Precision vs Recall trade-offs

3. **Explainability Insights**
   - Quality of medical justifications
   - Common reasoning patterns
   - Errors and limitations

---

## 📄 For Publication

### Generated Artifacts

1. **Tables**:
   - Model comparison table (CSV + LaTeX)
   - Detailed results per sample
   - Cluster statistics

2. **Figures**:
   - Optimal K analysis
   - Cluster visualizations
   - Model comparison charts
   - Consistency distributions

3. **Data Files**:
   - Raw LLM responses
   - Prediction logs
   - Evaluation metrics

### Suggested Paper Sections

1. **Introduction**: Medical AI, LLM reliability, consistency importance
2. **Related Work**: LLMs in healthcare, consistency evaluation
3. **Methodology**: Clustering, sampling, testing protocol
4. **Experiments**: Dataset, implementation details, parameters
5. **Results**: Performance metrics, consistency analysis
6. **Discussion**: Findings, implications, limitations
7. **Conclusion**: Contributions, future work

---

## 🛠️ Configuration

Edit `config/config.yaml` to customize:

- Clustering parameters (methods, K range, metrics)
- Sampling strategy (samples per cluster)
- LLM settings (models, temperature, runs per sample)
- Output directories

---

## 📚 Dependencies

**Core**:
- pandas, numpy, matplotlib, seaborn, scikit-learn

**LLM APIs**:
- openai (GPT-4)
- google-generativeai (Gemini)
- dashscope (Qwen Plus)

**Utilities**:
- pyyaml, python-dotenv, tqdm, jupyter

See `requirements.txt` for full list.

---

## ⚠️ Important Notes

1. **API Costs**: LLM testing involves many API calls. Estimate costs before running.
   - Example: 20 samples × 10 runs × 3 models = 600 API calls

2. **Rate Limiting**: Built-in delays between API calls to respect rate limits

3. **Error Handling**: Failed API calls are logged but don't stop the experiment

4. **Data Privacy**: Ensure compliance with data usage policies for medical data

---

## 📞 Contact & Support

For questions about this research:
- Check documentation in `docs/`
- Review code comments
- Open an issue on GitHub

---

## 📖 Citation

If you use this code or methodology, please cite:

```bibtex
@article{heart_llm_consistency_2025,
  title={Evaluating Consistency and Explainability of Large Language Models in Heart Disease Prediction: A Cluster-Based Sampling Approach},
  author={[Your Name]},
  journal={[Target Journal]},
  year={2025}
}
```

---

## 📜 License

[Specify your license]

---

## 🎓 Acknowledgments

- Heart Disease Dataset: UCI Machine Learning Repository
- LLM Providers: OpenAI, Google, Alibaba Cloud
- Libraries: scikit-learn, pandas, matplotlib

---

**Status**: 🚧 Research in Progress  
**Target**: Q2 International Journal  
**Date**: December 2025
