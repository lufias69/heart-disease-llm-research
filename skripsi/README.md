# 📚 FOLDER SKRIPSI - BAB 3 METODOLOGI PENELITIAN

**Judul**: Evaluasi Konsistensi dan Akurasi Large Language Models untuk Diagnosis Biner Penyakit Jantung  
**Tingkat**: S1 - Sarjana Informatika  
**Bahasa**: Indonesia  
**Status**: Draft BAB 3 Selesai ✅

---

## 📂 Struktur Dokumen

### 1. SKRIPSI_PLAN.md
**Deskripsi**: Rencana lengkap pengerjaan skripsi (BAB 3 & BAB 4)  
**Isi**: 
- Timeline 8 minggu
- Target 22,000-27,000 kata
- Outline detail 9 subsections BAB 3
- Outline detail 10 subsections BAB 4
- Checklist deliverables

**Status**: ✅ Selesai, sudah dikoreksi sesuai kode aktual

---

### 2. BAB3_PART1_DESAIN_DAN_DATA.md
**Jumlah Kata**: ~2,400 kata  
**Isi**:
- **3.1 Desain Penelitian**
  - Jenis penelitian (eksperimental kuantitatif)
  - Kerangka konseptual (konsistensi vs akurasi)
  - Alur penelitian (6 tahap)
  - Flowchart lengkap
- **3.2 Data dan Sumber Data**
  - UCI Heart Disease Dataset (303 pasien)
  - Tabel 13 parameter klinis
  - Preprocessing (normalisasi StandardScaler)
  - Validasi kualitas data

**Fitur Kunci**:
- Flowchart ASCII art lengkap
- Tabel karakteristik dataset
- Formula z-score normalisasi
- Contoh hasil normalisasi

---

### 3. BAB3_PART2_CLUSTERING_SAMPLING.md
**Jumlah Kata**: ~2,500 kata  
**Isi**:
- **3.3 Metode Clustering**
  - K-Means algoritma lengkap
  - Formula jarak Euclidean & inertia
  - Evaluasi K=2 hingga K=10 dengan 3 metrik:
    * Elbow Method (hasil lengkap)
    * Silhouette Score (K=2 tertinggi: 0.0798)
    * Davies-Bouldin Index
  - Keputusan pemilihan K=2
  - Distribusi cluster (145 vs 158 pasien)
- **3.4 Metode Sampling Stratified**
  - Strategi "diverse" sampling
  - 5 kuintil berdasarkan jarak ke centroid
  - 10 sampel per kuintil = 50 per cluster
  - Validasi kualitas sampling (KS test)

**Fitur Kunci**:
- Tabel hasil evaluasi K=2-10 lengkap
- Formula semua metrik clustering
- Analisis konsensus 3 metrik
- Validasi statistik sampling

---

### 4. BAB3_PART3_MODEL_PROMPT.md
**Jumlah Kata**: ~2,600 kata  
**Isi**:
- **3.5 Model Large Language Models (LLM)**
  - GPT-4o (OpenAI): Spesifikasi lengkap
  - Gemini-2.0-Flash (Google): Fitur multimodal
  - Qwen-Plus (Alibaba): Bilingual capability
  - Tabel perbandingan 3 model
  - Konfigurasi parameter (temperature=0.7, max_tokens=300)
- **3.6 Desain Prompt**
  - Prompt A: "Expert Cardiologist" (Dr. CardioExpert)
  - Prompt B: "Neutral AI Assistant"
  - Full text kedua prompt
  - Tabel perbandingan Expert vs Neutral
  - Struktur 5 komponen prompt
  - Contoh input-output

**Fitur Kunci**:
- Spesifikasi teknis 3 model detail
- Formula temperature sampling
- Full text prompt (300+ kata each)
- Analisis perbedaan prompt
- Contoh response GPT-4o

---

### 5. BAB3_PART4_PROTOKOL_EKSPERIMEN.md
**Jumlah Kata**: ~2,400 kata  
**Isi**:
- **3.7 Protokol Eksperimen Multi-Run**
  - Konsep multi-run testing
  - Justifikasi 4 runs per kasus
  - Total 2,400 prediksi (100×4×3×2)
  - Workflow eksperimen (pseudocode)
  - Independensi antar runs
- **3.7.2 Sistem Checkpoint SQLite**
  - Arsitektur 3 tabel database
  - SQL schema lengkap
  - Mekanisme checkpoint
  - Resume capability
  - Error handling & retry logic
- **3.8 Implementasi Teknis**
  - Environment setup
  - Struktur kode
  - Main experiment script

**Fitur Kunci**:
- Tabel breakdown 2,400 prediksi
- SQL CREATE TABLE statements
- Python pseudocode workflow
- Estimasi waktu eksperimen (2-3 jam)

---

### 6. BAB3_PART5_METRIK_EVALUASI.md
**Jumlah Kata**: ~2,800 kata  
**Isi**:
- **3.9.1 Intra-Model Consistency** (4 metrik)
  - Consistency score per kasus
  - Average consistency
  - Perfect Consistency Rate (PCR)
  - Consistency distribution
- **3.9.2 Diagnostic Accuracy Metrics** (5 metrik)
  - Majority voting
  - Confusion matrix
  - Accuracy, Sensitivity, Specificity
  - Precision, F1-Score
  - Interpretasi klinis setiap metrik
- **3.9.3 Inter-Model Agreement** (3 metrik)
  - Pairwise agreement
  - Cohen's Kappa (interpretasi Landis & Koch)
  - Three-way agreement
- **3.9.4 Prompt Sensitivity** (2 metrik)
  - Prediction Change Rate
  - Consistency change
- **3.9.5 Consistency-Accuracy Gap**
  - Formula gap
  - Interpretasi "consistently wrong"
- **3.10 Analisis Statistik**
  - McNemar's test
  - Wilcoxon signed-rank test
  - 95% confidence intervals

**Fitur Kunci**:
- 15+ formula matematika lengkap
- Contoh perhitungan setiap metrik
- Interpretasi klinis semua metrik
- Tabel interpretasi Cohen's Kappa

---

## 📊 Statistik Dokumen

| Aspek | Detail |
|-------|--------|
| **Total Kata** | ~12,700 kata |
| **Total Halaman** | ~35-40 halaman (estimasi Word) |
| **Jumlah Formula** | 40+ formula matematika |
| **Jumlah Tabel** | 25+ tabel |
| **Diagram/Flowchart** | 5+ diagram |
| **Referensi Kode** | 100% akurat sesuai implementasi |

---

## ✅ Status Penyelesaian

### BAB 3 METODOLOGI ✅ (100%)
- [x] 3.1 Desain Penelitian
- [x] 3.2 Data dan Sumber Data
- [x] 3.3 Metode Clustering (K-Means K=2-10)
- [x] 3.4 Metode Sampling (Diverse Stratified)
- [x] 3.5 Model LLM (3 model lengkap)
- [x] 3.6 Desain Prompt (Expert vs Neutral)
- [x] 3.7 Protokol Eksperimen (Multi-run + Checkpoint)
- [x] 3.8 Implementasi Teknis
- [x] 3.9 Metrik Evaluasi (15+ metrik)
- [x] 3.10 Analisis Statistik

### BAB 4 HASIL & PEMBAHASAN ⏳ (Belum Dimulai)
- [ ] 4.1 Hasil Clustering
- [ ] 4.2 Hasil Sampling
- [ ] 4.3 Hasil Konsistensi LLM
- [ ] 4.4 Hasil Akurasi Diagnostik
- [ ] 4.5 Inter-Model Agreement
- [ ] 4.6 Prompt Sensitivity
- [ ] 4.7 Analisis Error Patterns
- [ ] 4.8 Consistency-Accuracy Gap
- [ ] 4.9 Pembahasan & Interpretasi
- [ ] 4.10 Implikasi Klinis

---

## 🎯 Next Steps

1. **Review BAB 3**: Baca ulang semua 5 bagian, cek konsistensi
2. **Gabung ke Word**: Convert 5 file MD menjadi 1 dokumen Word
3. **Formatting**: Terapkan style skripsi (heading, spacing, numbering)
4. **Tambah Gambar**: Insert flowchart, diagram, tabel hasil clustering
5. **Mulai BAB 4**: Tulis hasil penelitian dengan data aktual dari `results/`

---

## 📝 Catatan Penting

### Akurasi 100% ✅
Semua informasi dalam BAB 3 berdasarkan kode implementasi aktual:
- Clustering: Baca dari `clustering/clustering.py` dan `results/clustering/clustering_report.txt`
- Sampling: Baca dari `sampling/sampling.py` dan `results/sampling/test_set.csv`
- LLM Testing: Baca dari `llm_testing/llm_tester.py` dan `config/config.yaml`
- Evaluasi: Baca dari `evaluation/evaluator.py`

### Koreksi yang Sudah Dilakukan ✅
1. ✅ Clustering: Ditambahkan detail evaluasi K=2-10 dengan 3 metrik
2. ✅ Sampling: Dikoreksi dari "centroid+farthest" ke "diverse stratified"
3. ✅ Protocol: Dikoreksi dari "10 runs" ke "4 runs per kasus"

### Format Penulisan
- **Bahasa**: Indonesia formal akademik
- **Formula**: LaTeX notation (rendered sebagai $...$ dan $$...$$)
- **Referensi**: Sesuai gaya sitasi skripsi
- **Gambar**: Placeholder, akan diganti dengan actual figures
- **Tabel**: Markdown table (convert ke Word table)

---

## 🔗 File Terkait

### Hasil Penelitian (untuk BAB 4)
- `results/clustering/clustering_report.txt` - Hasil clustering K=2-10
- `results/sampling/test_set.csv` - 100 test cases
- `results/llm_predictions/*.csv` - Prediksi 3 model
- `results/evaluation/*.csv` - Metrik evaluasi
- `results/plots/*.png` - Visualisasi hasil

### Manuscript JAMIA (Referensi)
- `manuscript/JAMIA_VERSION.md` - Paper yang sudah submit
- Manuscript ID: amiajnl-2025-018821
- Status: Under review

---

**Last Updated**: 18 Desember 2025  
**Author**: Syaiful Bachri Mustamin  
**Institution**: Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari
