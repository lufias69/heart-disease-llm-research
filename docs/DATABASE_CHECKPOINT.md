# Database Checkpoint System

## 🎯 Fitur Utama

**Setiap prediksi LLM langsung disimpan ke SQLite database** dengan informasi:
- Test ID (nomor sample)
- Run ID (urutan ke berapa: 1-4)
- Model (gpt/gemini/qwen)
- Prediction (Yes/No)
- Justification (alasan medis lengkap)
- Timestamp
- Ground truth
- Error (jika ada)

## 🔄 Resume Otomatis

Jika eksperimen berhenti di tengah jalan (error, internet putus, dll), **otomatis melanjutkan** dari checkpoint terakhir tanpa mengulang prediksi yang sudah selesai.

## 📊 Struktur Database

### Tabel: `predictions`
Menyimpan setiap prediksi individual:
- PRIMARY KEY: (test_id, run_id, model)
- Kolom: id, test_id, run_id, model, prediction, prediction_binary, justification, raw_response, ground_truth, timestamp, error

### Tabel: `progress`
Tracking progress per model:
- Completed predictions
- Total predictions
- Last test_id
- Last run_id
- Percentage

### Tabel: `experiment_metadata`
Metadata eksperimen

## 🚀 Cara Menggunakan

### 1. Run Experiment (Otomatis dengan Checkpoint)
```bash
python run_experiment.py
```
- Otomatis skip prediksi yang sudah ada
- Langsung simpan ke database setiap kali prediksi selesai
- Bisa dihentikan kapan saja (Ctrl+C)

### 2. Check Progress
```bash
python scripts/check_progress.py
```
Output:
```
📊 Overall Statistics:
  Total predictions: 450

🤖 By Model:
  GPT: 180 predictions
    Progress: [████████████░░░░░░] 45.0% (180/400)
    Last completed: Test ID 45, Run 4
  
  GEMINI: 150 predictions
    Progress: [██████████░░░░░░░░] 37.5% (150/400)
    Last completed: Test ID 38, Run 2
```

### 3. Resume (Jika Terputus)
```bash
python scripts/resume_experiment.py
```
- Otomatis cek progress
- Lanjutkan dari posisi terakhir
- Skip prediksi yang sudah selesai

### 4. View Errors
```bash
python scripts/view_errors.py
```
- Lihat semua error yang terjadi
- Detail: test_id, run_id, model, error message

### 5. Export ke CSV
Otomatis export saat experiment selesai:
```
results/llm_predictions/
├── predictions.db          # Database SQLite
├── gpt_results.csv         # Export CSV per model
├── gemini_results.csv
└── qwen_results.csv
```

## 💡 Keuntungan

✅ **Tidak perlu ulang dari awal** jika berhenti
✅ **Real-time progress tracking**
✅ **Data aman tersimpan** di database
✅ **Resume otomatis** dari checkpoint
✅ **Error logging** lengkap
✅ **Export fleksibel** ke CSV

## 🔧 Technical Details

### Database Path
```
results/llm_predictions/predictions.db
```

### Auto-Skip Logic
```python
if db.is_prediction_complete(test_id, run_id, model):
    # Skip, sudah ada
    continue
else:
    # Run prediction
    result = test_single_sample(...)
    db.save_prediction(...)  # Langsung simpan
```

### Progress Tracking
```python
progress = db.get_progress('gpt')
# Returns: {
#   'completed': 180,
#   'total': 400,
#   'percentage': 45.0,
#   'last_test_id': 45,
#   'last_run_id': 4
# }
```

## 📈 Example Flow

### First Run (Berhenti di 40%)
```bash
python run_experiment.py
# Progress: GPT 40%, Gemini 35%, Qwen 30%
# Ctrl+C (stop)
```

### Check Progress
```bash
python scripts/check_progress.py
# GPT: 160/400 (40%)
# Gemini: 140/400 (35%)
# Qwen: 120/400 (30%)
```

### Resume
```bash
python scripts/resume_experiment.py
# Otomatis lanjut dari:
# - GPT: Test 41
# - Gemini: Test 36
# - Qwen: Test 31
```

## 🎓 Research Benefits

Untuk riset Q2 paper:
1. **Reproducible**: Setiap prediksi tercatat dengan timestamp
2. **Auditable**: Bisa trace setiap prediksi individual
3. **Efficient**: Tidak waste API calls
4. **Reliable**: Data tidak hilang jika crash
5. **Flexible**: Export ke format apapun dari database

## 🔍 Query Examples

### Get all predictions for a sample
```python
db.get_all_predictions()
df[df['test_id'] == 5]
```

### Check consistency for a sample
```python
df = db.get_all_predictions('gpt')
test_5 = df[df['test_id'] == 5]
consistency = (test_5['prediction_binary'] == test_5['prediction_binary'].mode()[0]).mean()
```

### Export specific model
```python
db.export_to_csv('gpt', 'my_gpt_results.csv')
```
