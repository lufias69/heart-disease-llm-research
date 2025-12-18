# BAB 3 - METODOLOGI PENELITIAN
## BAGIAN 4: PROTOKOL EKSPERIMEN DAN SISTEM CHECKPOINT

---

## 3.7 Protokol Eksperimen Multi-Run

Protokol eksperimen multi-run merupakan kontribusi metodologis utama penelitian ini. Berbeda dengan penelitian LLM konvensional yang hanya menjalankan satu kali prediksi per kasus, penelitian ini mengimplementasikan **multiple independent runs** untuk mengukur konsistensi (reproducibility) model.

### 3.7.1 Desain Eksperimen Multi-Run

#### Konsep Multi-Run Testing

**Multi-run testing** adalah pendekatan di mana setiap model dijalankan **beberapa kali** untuk kasus yang sama dengan kondisi identik. Tujuannya adalah mengukur **intra-model consistency** - seberapa konsisten model memberikan prediksi yang sama ketika diberikan input identik.

**Analogi Klinis**: Seperti meminta dokter yang sama mendiagnosis pasien yang sama di waktu berbeda tanpa mengingat diagnosis sebelumnya. Jika diagnosis selalu sama = konsisten/reliable. Jika bervariasi = tidak konsisten/unreliable.

#### Parameter Desain

**Jumlah Run per Kasus**: **4 prediksi independen**

**Justifikasi Pemilihan 4 Runs**:

1. **Balance Statistik vs Efisiensi**:
   - 2 runs: Terlalu sedikit untuk analisis konsistensi (hanya binary: sama/beda)
   - 3 runs: Cukup tapi tidak ideal (majority vote bisa tie jika semua berbeda)
   - **4 runs**: Optimal - cukup untuk analisis statistik, tidak terlalu costly
   - 10+ runs: Redundant dan sangat costly (biaya API meningkat 10x)

2. **Granularitas Consistency Score**:
   Dengan 4 runs, consistency score dapat bernilai:
   - 1.00 (4/4 agree) = Perfect consistency
   - 0.75 (3/4 agree) = High consistency
   - 0.50 (2/4 agree) = Low consistency
   - Memberikan granularitas yang cukup untuk analisis

3. **Precedent Penelitian**:
   Penelitian reprodusibilitas LLM sebelumnya (Brown et al., 2020) menggunakan 3-5 runs sebagai standard practice

4. **Biaya Komputasi**:
   Total prediksi = 100 kasus × 4 runs × 3 models × 2 prompts = **2,400 prediksi**
   - Dengan 4 runs: ~$40-50 total biaya API
   - Dengan 10 runs: ~$100-125 (2.5x lebih mahal)
   - Trade-off optimal antara kualitas data dan biaya

#### Total Prediksi

**Perhitungan Total Prediksi**:

$$\text{Total Prediksi} = N_{kasus} \times N_{runs} \times N_{models} \times N_{prompts}$$

$$\text{Total Prediksi} = 100 \times 4 \times 3 \times 2 = 2,400$$

**Breakdown per Komponen**:

| Komponen | Jumlah | Keterangan |
|----------|--------|------------|
| **Kasus Uji** | 100 | Dari stratified sampling |
| **Runs per Kasus** | 4 | Independent predictions |
| **Models** | 3 | GPT-4o, Gemini-2.0-Flash, Qwen-Plus |
| **Prompt Variations** | 2 | Expert vs Neutral |
| **TOTAL** | **2,400** | Total predictions |

**Distribusi Prediksi per Model**:

| Model | Prediksi per Prompt | Total per Model |
|-------|---------------------|-----------------|
| GPT-4o | 100 × 4 = 400 | 400 × 2 = 800 |
| Gemini-2.0-Flash | 100 × 4 = 400 | 400 × 2 = 800 |
| Qwen-Plus | 100 × 4 = 400 | 400 × 2 = 800 |
| **TOTAL** | - | **2,400** |

### 3.7.2 Prosedur Eksperimen

#### Workflow Eksperimen

Eksperimen dilakukan secara sistematis mengikuti workflow berikut:

```
UNTUK setiap model M dalam {GPT-4o, Gemini-2.0-Flash, Qwen-Plus}:
    UNTUK setiap prompt P dalam {Expert, Neutral}:
        UNTUK setiap kasus C dalam test_set (100 kasus):
            UNTUK setiap run R dalam {1, 2, 3, 4}:
                
                1. CHECK: Apakah prediksi (M, P, C, R) sudah ada di database?
                   - Jika YA: SKIP (resume dari checkpoint)
                   - Jika TIDAK: LANJUT
                
                2. PREPARE PROMPT:
                   - Ambil data klinis kasus C
                   - Inject ke template prompt P
                   - Format: "age: X, sex: Y, cp: Z, ..."
                
                3. CALL API:
                   - Kirim prompt ke model M
                   - Parameter: temperature=0.7, max_tokens=300
                   - Timeout: 30 detik
                
                4. PARSE RESPONSE:
                   - Extract PREDICTION (Yes/No)
                   - Extract JUSTIFICATION (reasoning text)
                   - Handle parsing errors
                
                5. SAVE TO DATABASE:
                   - Simpan ke SQLite: (test_id, run_id, model, prompt, prediction, justification)
                   - Timestamp: waktu prediksi
                   - Ground truth: label asli kasus
                
                6. LOG PROGRESS:
                   - Print: "Model M | Prompt P | Case C | Run R | Prediction: X"
                   - Update progress counter
                
                7. RATE LIMITING:
                   - Delay 0.5 detik antar request (avoid API rate limit)
                
ENDFOR
```

#### Independensi Antar Runs

Untuk memastikan setiap run benar-benar **independen**:

✅ **Tidak ada memori antar runs**: Setiap API call adalah request baru, model tidak "mengingat" prediksi sebelumnya

✅ **Prompt identik**: Setiap run menggunakan prompt persis sama, tidak ada variasi input

✅ **Parameter sama**: Temperature, max_tokens, dan parameter lain konsisten di semua runs

✅ **Tidak ada conditioning**: Model tidak diberi informasi tentang prediksi sebelumnya

✅ **Random seed berbeda**: Temperature=0.7 menyebabkan setiap run memiliki sampling random berbeda

### 3.7.3 Sistem Checkpoint SQLite

Mengingat skala eksperimen yang besar (2,400 prediksi) dan risiko error (API failure, network timeout, rate limiting), diimplementasikan **sistem checkpoint berbasis SQLite database** untuk:

1. Mencegah kehilangan data jika terjadi error
2. Memungkinkan resume eksperimen dari titik terakhir
3. Menghindari prediksi duplikat
4. Tracking progress real-time

#### Arsitektur Database

Database SQLite terdiri dari 3 tabel utama:

**Tabel 1: predictions** (Tabel Utama)

| Kolom | Tipe | Deskripsi |
|-------|------|-----------|
| `id` | INTEGER PRIMARY KEY | ID auto-increment |
| `test_id` | INTEGER NOT NULL | ID kasus (0-99) |
| `run_id` | INTEGER NOT NULL | Nomor run (1-4) |
| `model` | TEXT NOT NULL | Nama model (gpt/gemini/qwen) |
| `prompt_type` | TEXT NOT NULL | Tipe prompt (expert/neutral) |
| `prediction` | TEXT | Prediksi (Yes/No) |
| `prediction_binary` | INTEGER | Prediksi binary (1/0) |
| `justification` | TEXT | Clinical reasoning |
| `raw_response` | TEXT | Full response dari LLM |
| `ground_truth` | INTEGER | Label asli (1/0) |
| `timestamp` | TEXT NOT NULL | Waktu prediksi (ISO format) |
| `error` | TEXT | Error message jika ada |

**Unique Constraint**: `UNIQUE(test_id, run_id, model, prompt_type)`
- Mencegah duplikasi prediksi untuk kombinasi yang sama

**Tabel 2: experiment_metadata**

| Kolom | Tipe | Deskripsi |
|-------|------|-----------|
| `id` | INTEGER PRIMARY KEY | ID metadata |
| `total_samples` | INTEGER | Total kasus (100) |
| `runs_per_sample` | INTEGER | Runs per kasus (4) |
| `models` | TEXT | Daftar model (JSON array) |
| `start_time` | TEXT | Waktu mulai eksperimen |
| `last_update` | TEXT | Waktu update terakhir |
| `status` | TEXT | Status (running/completed/paused) |

**Tabel 3: progress**

| Kolom | Tipe | Deskripsi |
|-------|------|-----------|
| `model` | TEXT PRIMARY KEY | Nama model |
| `completed_predictions` | INTEGER | Jumlah prediksi selesai |
| `total_predictions` | INTEGER | Total prediksi target (800) |
| `last_test_id` | INTEGER | ID kasus terakhir |
| `last_run_id` | INTEGER | Run terakhir |
| `last_update` | TEXT | Timestamp update terakhir |

#### SQL Schema

**CREATE TABLE Statement**:

```sql
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_id INTEGER NOT NULL,
    run_id INTEGER NOT NULL,
    model TEXT NOT NULL,
    prompt_type TEXT NOT NULL,
    prediction TEXT,
    prediction_binary INTEGER,
    justification TEXT,
    raw_response TEXT,
    ground_truth INTEGER,
    timestamp TEXT NOT NULL,
    error TEXT,
    UNIQUE(test_id, run_id, model, prompt_type)
);

CREATE TABLE IF NOT EXISTS experiment_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    total_samples INTEGER,
    runs_per_sample INTEGER,
    models TEXT,
    start_time TEXT,
    last_update TEXT,
    status TEXT
);

CREATE TABLE IF NOT EXISTS progress (
    model TEXT PRIMARY KEY,
    completed_predictions INTEGER,
    total_predictions INTEGER,
    last_test_id INTEGER,
    last_run_id INTEGER,
    last_update TEXT
);
```

#### Mekanisme Checkpoint

**1. Sebelum Prediksi**: Check jika prediksi sudah ada

```python
def is_prediction_complete(test_id, run_id, model, prompt_type):
    cursor.execute('''
        SELECT COUNT(*) FROM predictions 
        WHERE test_id = ? AND run_id = ? 
        AND model = ? AND prompt_type = ?
    ''', (test_id, run_id, model, prompt_type))
    
    count = cursor.fetchone()[0]
    return count > 0

# Usage in experiment loop
if is_prediction_complete(case_id, run_num, model_name, prompt_type):
    print(f"⏭️  Skip: Already completed")
    continue
```

**2. Setelah Prediksi**: Simpan immediate ke database

```python
def save_prediction(test_id, run_id, model, prompt_type, result, ground_truth):
    cursor.execute('''
        INSERT OR REPLACE INTO predictions 
        (test_id, run_id, model, prompt_type, prediction, 
         prediction_binary, justification, raw_response, 
         ground_truth, timestamp, error)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        test_id, run_id, model, prompt_type,
        result.get('prediction'),
        1 if result.get('prediction') == 'Yes' else 0,
        result.get('justification'),
        result.get('raw_response'),
        ground_truth,
        datetime.now().isoformat(),
        result.get('error')
    ))
    
    conn.commit()  # COMMIT immediately
```

**3. Error Handling**: Simpan error ke database

```python
try:
    result = call_llm_api(prompt)
except Exception as e:
    result = {
        'prediction': None,
        'justification': None,
        'error': str(e)
    }
    # Still save to database with error info
    save_prediction(..., result, ...)
```

#### Resume Capability

Jika eksperimen terhenti (crash, network error, interrupt), dapat di-resume:

```python
# Count completed predictions
cursor.execute('''
    SELECT COUNT(*) FROM predictions 
    WHERE model = ? AND prompt_type = ?
''', (model_name, prompt_type))

completed = cursor.fetchone()[0]
total = 100 * 4  # 100 cases × 4 runs

print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%)")
print(f"Resume from: test_id={last_test_id}, run_id={last_run_id}")

# Continue from where left off
for case_id in range(last_test_id, 100):
    for run_id in range(last_run_id if case_id == last_test_id else 1, 5):
        # Process prediction
        ...
```

**Keuntungan Checkpoint System**:

✅ **Fault Tolerance**: Tidak kehilangan data jika error
✅ **Resume Seamlessly**: Lanjutkan dari titik terakhir tanpa duplikasi
✅ **Progress Tracking**: Monitoring real-time progress
✅ **Audit Trail**: Semua prediksi tercatat dengan timestamp
✅ **Data Integrity**: UNIQUE constraint mencegah duplikasi

### 3.7.4 Error Handling dan Retry Logic

Untuk menangani API failures yang mungkin terjadi:

**Strategi Error Handling**:

1. **Timeout Protection**: Setiap API call diberi timeout 30 detik
   ```python
   response = call_api(prompt, timeout=30)
   ```

2. **Retry on Failure**: Jika error, retry hingga 3 kali dengan exponential backoff
   ```python
   max_retries = 3
   for attempt in range(max_retries):
       try:
           result = call_api(prompt)
           break  # Success
       except Exception as e:
           if attempt < max_retries - 1:
               wait_time = 2 ** attempt  # 1s, 2s, 4s
               time.sleep(wait_time)
           else:
               # Save error to database
               result = {'error': str(e), 'prediction': None}
   ```

3. **Rate Limiting**: Delay 0.5 detik antar request
   ```python
   time.sleep(0.5)  # Avoid API rate limits
   ```

4. **Error Logging**: Semua error disimpan ke database dengan full traceback
   ```python
   error_info = {
       'error': str(e),
       'traceback': traceback.format_exc(),
       'timestamp': datetime.now().isoformat()
   }
   ```

### 3.7.5 Estimasi Waktu Eksperimen

**Perhitungan Waktu**:

Asumsi:
- Rata-rata response time per API call: 2-5 detik
- Delay antar request: 0.5 detik
- Total time per prediction: ~3 detik (average)

$$\text{Total Waktu} = \text{Total Prediksi} \times \text{Time per Prediction}$$

$$\text{Total Waktu} = 2,400 \times 3 \text{ detik} = 7,200 \text{ detik} \approx 2 \text{ jam}$$

**Estimasi Realistis**:
- Best case (API fast): 1.5-2 jam
- Normal case: 2-3 jam
- Worst case (dengan retries): 3-4 jam

**Strategi Eksekusi**:
- Jalankan per model untuk monitoring lebih mudah
- Total 3 sessions (satu per model)
- Setiap session: ~40-60 menit (800 prediksi)

---

## 3.8 Implementasi Teknis

### 3.8.1 Environment Setup

**Requirement**:
- Python 3.9+
- Libraries: openai, google-generativeai, pandas, numpy, scikit-learn, sqlite3

**Environment Variables**:
```bash
export OPENAI_API_KEY="sk-..."
export GOOGLE_API_KEY="AI..."
export DASHSCOPE_API_KEY="sk-..."
```

### 3.8.2 Struktur Kode

**File Organization**:
```
heart-disease/
├── data/
│   └── heart.csv                   # Dataset
├── clustering/
│   └── clustering.py               # K-Means implementation
├── sampling/
│   └── sampling.py                 # Stratified sampling
├── llm_testing/
│   ├── llm_tester.py              # Main testing module
│   └── database.py                 # SQLite checkpoint system
├── evaluation/
│   └── evaluator.py               # Metrics calculation
├── results/
│   ├── clustering/                # Clustering results
│   ├── sampling/                  # Test set
│   ├── llm_predictions/           # Predictions & database
│   └── evaluation/                # Metrics & analysis
└── run_experiment.py              # Main experiment script
```

### 3.8.3 Main Experiment Script

**Pseudocode**:
```python
# run_experiment.py

# 1. Load test set
test_data = pd.read_csv('results/sampling/test_set.csv')

# 2. Initialize LLM Tester with checkpoint
tester = LLMTester(
    test_data_path='results/sampling/test_set.csv',
    runs_per_sample=4,
    db_path='results/llm_predictions/predictions.db'
)

# 3. Define prompts
prompts = {
    'expert': create_expert_prompt(),
    'neutral': create_neutral_prompt()
}

# 4. Run experiments
for model in ['gpt', 'gemini', 'qwen']:
    for prompt_type in ['expert', 'neutral']:
        print(f"\n{'='*60}")
        print(f"Testing {model.upper()} with {prompt_type} prompt")
        print(f"{'='*60}")
        
        results = tester.test_model(
            model=model,
            prompt_template=prompts[prompt_type],
            prompt_type=prompt_type
        )
        
        print(f"✓ Completed: {len(results)} predictions")

# 5. Export results
tester.export_to_csv('results/llm_predictions/')

print("\n🎉 All experiments completed!")
```

### 3.8.4 Data Export

Setelah semua prediksi selesai, data di-export dari SQLite ke CSV untuk analisis:

**Output Files**:
- `gpt_results.csv`: Semua prediksi GPT-4o
- `gemini_results.csv`: Semua prediksi Gemini-2.0-Flash
- `qwen_results.csv`: Semua prediksi Qwen-Plus

**Format CSV**:
| test_id | run_id | model | prompt_type | prediction | prediction_binary | ground_truth | justification | timestamp |
|---------|--------|-------|-------------|------------|-------------------|--------------|---------------|-----------|
| 0 | 1 | gpt | expert | Yes | 1 | 1 | Multiple risk factors... | 2024-12-01T10:30:00 |

---

**[Lanjut ke BAGIAN 5: Metrik Evaluasi]**
