# GitHub Repository Setup Guide

**Repository Name:** heart-disease-llm-research  
**Purpose:** Data and code sharing for JAMIA submission  
**Time Required:** 30 minutes

---

## OPTION 1: Quick Setup via GitHub Website (Easiest)

### Step 1: Create Repository on GitHub.com
1. Go to https://github.com
2. Login or create account (free)
3. Click "+" → "New repository"
4. Settings:
   - **Name:** `heart-disease-llm-research`
   - **Description:** "Evaluating Large Language Models for Binary Medical Diagnosis - JAMIA 2025"
   - **Visibility:** ✅ Public (required for open science)
   - **Initialize with README:** ✅ Yes
   - **Add .gitignore:** Python
   - **Choose license:** MIT License
5. Click "Create repository"

### Step 2: Prepare Files Locally
Open PowerShell in your project directory:

```powershell
cd e:\project\Riset\heart-disease

# Create a clean copy for upload (excluding unnecessary files)
New-Item -ItemType Directory -Force -Path ".\github_upload"

# Copy essential files
Copy-Item -Path "*.py" -Destination ".\github_upload" -Recurse
Copy-Item -Path "*.md" -Destination ".\github_upload"
Copy-Item -Path "requirements.txt" -Destination ".\github_upload"
Copy-Item -Path "config" -Destination ".\github_upload" -Recurse -Force
Copy-Item -Path "data\heart.csv" -Destination ".\github_upload\data" -Force
Copy-Item -Path "results" -Destination ".\github_upload" -Recurse -Force
Copy-Item -Path "clustering" -Destination ".\github_upload" -Recurse -Force
Copy-Item -Path "evaluation" -Destination ".\github_upload" -Recurse -Force
Copy-Item -Path "llm_testing" -Destination ".\github_upload" -Recurse -Force
Copy-Item -Path "sampling" -Destination ".\github_upload" -Recurse -Force
Copy-Item -Path "scripts" -Destination ".\github_upload" -Recurse -Force
```

### Step 3: Upload via GitHub Web Interface
1. Go to your new repository page
2. Click "Upload files"
3. Drag and drop everything from `github_upload` folder
4. Commit message: "Initial commit - Complete research code and data"
5. Click "Commit changes"

**DONE!** Your repository is live.

---

## OPTION 2: Setup via Git Command Line (For Git Users)

```powershell
cd e:\project\Riset\heart-disease

# Initialize git if not already done
git init

# Add remote (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/heart-disease-llm-research.git

# Create .gitignore
@"
__pycache__/
*.pyc
*.pyo
*.db
*.db-journal
.env
.venv
venv/
*.log
.DS_Store
.idea/
.vscode/
*.bak
"@ | Out-File -FilePath .gitignore -Encoding utf8

# Add all files
git add .

# Commit
git commit -m "Initial commit - Heart Disease LLM Research"

# Push to GitHub
git push -u origin main
```

---

## OPTION 3: Use GitHub Desktop (User-Friendly GUI)

### Step 1: Install GitHub Desktop
1. Download from: https://desktop.github.com
2. Install and login with GitHub account

### Step 2: Create Repository
1. File → New Repository
2. Name: `heart-disease-llm-research`
3. Local Path: `e:\project\Riset\heart-disease`
4. Initialize with README: Yes
5. Git Ignore: Python
6. License: MIT
7. Click "Create Repository"

### Step 3: Publish to GitHub
1. Click "Publish repository"
2. Description: "Evaluating LLMs for Medical Diagnosis"
3. ✅ Keep this code private: NO (must be public)
4. Click "Publish"

**DONE!**

---

## 📝 REQUIRED FILES TO INCLUDE

### Essential Code Files
- ✅ `run_experiment.py` - Main experiment script
- ✅ `prompts_comparison.py` - Prompt comparison script
- ✅ `requirements.txt` - Python dependencies
- ✅ `config/config.yaml` - Configuration file

### Module Directories
- ✅ `clustering/` - Clustering implementation
- ✅ `evaluation/` - Evaluation metrics
- ✅ `llm_testing/` - LLM API interaction
- ✅ `sampling/` - Test set sampling
- ✅ `scripts/` - Analysis scripts

### Data Files
- ✅ `data/heart.csv` - Original UCI dataset
- ✅ `results/llm_predictions/` - All prediction CSVs
- ✅ `results/evaluation/` - Metrics and figures
- ✅ `results/sampling/` - Test set

### Documentation
- ✅ `README.md` - Main documentation
- ✅ `RESEARCH_README.md` - Research details
- ✅ `IMPLEMENTATION_SUMMARY.md` - Implementation guide

### Manuscript Files (Optional)
- ✅ `manuscript/` folder - All manuscript versions

---

## 📄 CREATE A COMPREHENSIVE README.md

Save this as your repository's main README:

```markdown
# Heart Disease LLM Consistency Study

**Paper:** High Consistency, Limited Accuracy: Evaluating Large Language Models for Binary Medical Diagnosis

**Authors:** Dwi Anggriani, Syaiful Bachri Mustamin*, Muhammad Atnang, Kartini Aprilia Pratiwi Nuzry  
**Institution:** Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari, Indonesia

**Published:** medRxiv Preprint  
**DOI:** [10.64898/2025.12.08.25341823](https://doi.org/10.64898/2025.12.08.25341823)

---

## Abstract

This study evaluates the consistency and diagnostic accuracy of three state-of-the-art Large Language Models (GPT-4o, Gemini-2.0-Flash, Qwen-Plus) on binary heart disease diagnosis. Through 1,200 predictions (100 cases × 4 runs × 3 models), we reveal a critical dissociation: while models achieve 99-100% reproducibility, diagnostic accuracy remains at chance level (~50%). This consistency-accuracy gap has important implications for clinical AI deployment.

---

## Repository Contents

- `run_experiment.py` - Main experiment execution
- `prompts_comparison.py` - Prompt variation analysis
- `clustering/` - K-means clustering for diverse sampling
- `evaluation/` - Metrics calculation and analysis
- `llm_testing/` - LLM API interaction modules
- `sampling/` - Test set selection
- `scripts/` - Additional analysis scripts
- `results/` - All predictions, metrics, and figures
- `data/` - UCI Heart Disease dataset
- `manuscript/` - Paper versions and supplementary materials

---

## Installation

```bash
# Clone repository
git clone https://github.com/[USERNAME]/heart-disease-llm-research.git
cd heart-disease-llm-research

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Option 1: Reproduce Analysis Only (No API Keys Required)

All prediction data is included. You can reproduce all analyses and figures:

```bash
# Generate all figures and metrics
python scripts/comprehensive_consistency_analysis.py
python scripts/compare_prompts.py
python scripts/generate_supplementary_figures.py
```

### Option 2: Full Reproduction (API Keys Required)

To re-run LLM predictions:

1. **Obtain API Keys:**
   - OpenAI: https://platform.openai.com/api-keys
   - Google AI Studio: https://makersuite.google.com/app/apikey
   - Alibaba Cloud: https://www.alibabacloud.com/help/en/dashscope/

2. **Configure Environment:**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=your_key_here" > .env
   echo "GOOGLE_API_KEY=your_key_here" >> .env
   echo "QWEN_API_KEY=your_key_here" >> .env
   ```

3. **Run Experiment:**
   ```bash
   python run_experiment.py
   ```

**Cost:** ~$15-20 for 1,200 API calls  
**Time:** 2-3 hours (rate limits apply)

---

## Dataset

**Source:** UCI Heart Disease Dataset  
**Citation:** Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1988). Heart Disease [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X

**Features:** 13 clinical parameters (age, sex, chest pain, BP, cholesterol, ECG, etc.)  
**Samples:** 303 patients  
**License:** CC BY 4.0

---

## Key Findings

- **Intra-model Consistency:** 99-100% (perfect reproducibility)
- **Diagnostic Accuracy:** ~50% (chance level)
- **Consistency-Accuracy Gap:** ~50 percentage points
- **Inter-model Agreement:** 98-99% (convergent errors)
- **Prompt Sensitivity:** <3% (minimal impact)

---

## Citation

If you use this code or data, please cite:

```bibtex
@article{anggriani2025consistency,
  title={High Consistency, Limited Accuracy: Evaluating Large Language Models for Binary Medical Diagnosis},
  author={Anggriani, Dwi and Mustamin, Syaiful Bachri and Atnang, Muhammad and Nuzry, Kartini Aprilia Pratiwi},
  journal={medRxiv},
  year={2025},
  doi={10.64898/2025.12.08.25341823}
}
```

---

## License

**Code:** MIT License  
**Data:** CC BY 4.0 (as per UCI dataset)

---

## Contact

**Corresponding Author:** Syaiful Bachri Mustamin  
**Email:** syaifulbachri@mail.ugm.ac.id  
**Institution:** Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari

---

## Acknowledgments

We thank OpenAI, Google, and Alibaba Cloud for API access. We acknowledge the UCI Machine Learning Repository for providing the Heart Disease dataset.
```

Save this as `README.md` in your repository root.

---

## ✅ AFTER SETUP: Update Manuscript

Once repository is created, update the GitHub URL in:

**File:** `manuscript/DATA_AVAILABILITY.md`

Replace:
```markdown
**GitHub Repository:** [To be updated with actual repository URL]  
**Expected URL:** https://github.com/[username]/heart-disease-llm-research
```

With:
```markdown
**GitHub Repository:** https://github.com/[YOUR_USERNAME]/heart-disease-llm-research  
**Status:** Public (Open Access)
```

---

## 📊 Verify Your Repository

After setup, check that:
- [ ] Repository is PUBLIC (not private)
- [ ] README.md displays correctly on main page
- [ ] All essential files are uploaded
- [ ] License file is present (MIT)
- [ ] .gitignore excludes sensitive files (.env, API keys)
- [ ] Requirements.txt is present
- [ ] Data files are accessible

---

## 🎯 ESTIMATED TIME

- **GitHub account creation:** 5 minutes (if needed)
- **Repository setup:** 10 minutes
- **File upload:** 10 minutes
- **README writing:** 5 minutes
- **Verification:** 5 minutes

**Total:** ~30-35 minutes

---

**Next Step:** Once repository is live, copy the URL and update `manuscript/DATA_AVAILABILITY.md`
