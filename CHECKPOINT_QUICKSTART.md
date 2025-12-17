# 🚀 Quick Start Guide - Database Checkpoint System

## ⚡ Fitur Utama
- ✅ **Auto-save ke SQLite** setiap prediksi
- ✅ **Resume otomatis** jika terputus
- ✅ **Progress tracking** real-time
- ✅ **No duplicate API calls**

---

## 📋 Commands

### 1. Run Experiment (dengan checkpoint)
```bash
python run_experiment.py
```
- Otomatis skip prediksi yang sudah ada
- Bisa stop kapan saja (Ctrl+C)
- Data aman di database

### 2. Check Progress
```bash
python scripts/check_progress.py
```
Lihat progress setiap model:
```
📊 Overall Statistics:
  Total predictions: 450

🤖 By Model:
  GPT: 180 predictions
    Progress: [████████████░░░░░░] 45.0% (180/400)
    Last completed: Test ID 45, Run 4
```

### 3. Resume Experiment
```bash
python scripts/resume_experiment.py
```
Lanjutkan dari checkpoint terakhir.

### 4. View Errors
```bash
python scripts/view_errors.py
```
Lihat semua error yang terjadi.

### 5. Test Checkpoint (1 sample)
```bash
python scripts/test_checkpoint.py
```
Test sistem dengan 1 sample saja.

---

## 🎯 Workflow

### First Run
```bash
python run_experiment.py
```
Progress: 
- GPT: 0% → 40%
- Gemini: 0% → 35%
- **Internet putus! (Ctrl+C)**

### Check Status
```bash
python scripts/check_progress.py
```
Output:
```
GPT: 160/400 (40.0%)
GEMINI: 140/400 (35.0%)
QWEN: 0/400 (0.0%)
```

### Resume
```bash
python scripts/resume_experiment.py
```
Otomatis lanjut dari Test ID terakhir.

### Complete
```bash
python scripts/check_progress.py
```
Output:
```
GPT: 400/400 (100.0%) ✅
GEMINI: 400/400 (100.0%) ✅
QWEN: 400/400 (100.0%) ✅
```

---

## 📊 Database Structure

### File Location
```
results/llm_predictions/predictions.db
```

### Tables
1. **predictions** - Setiap prediksi individual
   - test_id, run_id, model
   - prediction, justification
   - timestamp, error
   - ground_truth

2. **progress** - Tracking per model
   - completed_predictions
   - total_predictions
   - percentage
   - last_test_id, last_run_id

3. **experiment_metadata** - Info eksperimen

---

## 💡 Benefits

✅ **Hemat biaya API** - Tidak repeat API calls  
✅ **Reliable** - Data tidak hilang jika crash  
✅ **Flexible** - Stop dan resume kapan saja  
✅ **Auditable** - Setiap prediksi tercatat  
✅ **Efficient** - Auto-skip completed tasks  

---

## 🔍 Example Scenario

### Skenario: Internet putus di 40%

**Before:**
```bash
python run_experiment.py
# 480 API calls × $0.01 = $4.80
# Internet putus di 40%
# ❌ Harus ulang dari awal (waste $1.92)
```

**With Checkpoint:**
```bash
python run_experiment.py
# 480 API calls × $0.01 = $4.80
# Internet putus di 40%
# ✅ Database saved: 192 predictions

python scripts/resume_experiment.py
# Continue from 40%
# Only 288 more API calls needed
# Total cost: $4.80 (no waste!)
```

---

## 📁 Output Files

```
results/
├── llm_predictions/
│   ├── predictions.db          # SQLite database (checkpoint)
│   ├── gpt_results.csv         # Exported CSV per model
│   ├── gemini_results.csv
│   └── qwen_results.csv
│
├── clustering/
│   ├── clustered_data.csv
│   └── optimal_k_analysis_report.png
│
├── sampling/
│   ├── test_set.csv
│   └── llm_test_data.csv
│
└── evaluation/
    ├── model_comparison.png
    ├── model_comparison.csv
    └── model_comparison_table.tex
```

---

## 🎓 For Research Paper

### Reproducibility
- Setiap prediksi ada timestamp
- Bisa trace individual predictions
- Export to CSV/LaTeX

### Data Integrity
- UNIQUE constraint on (test_id, run_id, model)
- Automatic deduplication
- Error logging

### Analysis
```python
from llm_testing.database import ResultsDatabase

db = ResultsDatabase('results/llm_predictions/predictions.db')

# Get all predictions
df = db.get_all_predictions()

# Filter by model
gpt_df = db.get_all_predictions('gpt')

# Check consistency for a sample
sample_5 = gpt_df[gpt_df['test_id'] == 5]
consistency = (sample_5['prediction_binary'] == 
               sample_5['prediction_binary'].mode()[0]).mean()

# Export
db.export_to_csv('gpt', 'my_gpt_results.csv')
```

---

## ⚙️ Configuration

### runs_per_sample
Default: 4 (untuk consistency analysis)

### models
Default: ['gpt', 'gemini', 'qwen']

### db_path
Default: 'results/llm_predictions/predictions.db'

---

## 🐛 Troubleshooting

### Database locked?
```bash
# Check if another process is using it
# Close all Python processes
# Try again
```

### Wrong progress shown?
```bash
# Database might be from old run
# Delete and start fresh:
rm results/llm_predictions/predictions.db
python run_experiment.py
```

### Export not working?
```bash
python scripts/check_progress.py
# Check if predictions exist first
```

---

## 📚 More Info

- Full documentation: `docs/DATABASE_CHECKPOINT.md`
- Test checkpoint: `python scripts/test_checkpoint.py`
- View implementation: `llm_testing/database.py`

---

**Ready to run? 🚀**
```bash
python run_experiment.py
```
