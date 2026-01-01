# PETA KONSEP BAB 4 - HASIL DAN PEMBAHASAN

**Dokumen**: Analisis Struktur dan Mapping Konten BAB 4  
**Total**: ~2,626 baris (~53 halaman)  
**Struktur**: 4 BAGIAN UTAMA, 14 Seksi, 58 Sub-seksi, 64 Sub-sub-seksi

---

## STATISTIK RINGKASAN

| Metrik | Nilai |
|--------|-------|
| **Total Baris** | 2,626 baris |
| **Estimasi Halaman** | ~53 halaman |
| **BAGIAN Utama** | 4 bagian |
| **Seksi Level 2 (##)** | 14 seksi |
| **Sub-seksi Level 3 (###)** | 58 sub-seksi |
| **Sub-sub-seksi Level 4 (####)** | 64 sub-sub-seksi |

### Breakdown per BAGIAN:

| BAGIAN | Baris | Estimasi Halaman | % dari Total |
|--------|-------|------------------|--------------|
| **1. Clustering & Sampling** | 544 | ~11 hal | 21% |
| **2. Konsistensi Model LLM** | 660 | ~13 hal | 25% |
| **3. Prompt & Agreement** | 682 | ~14 hal | 26% |
| **4. Pembahasan Klinis** | 723 | ~14 hal | 28% |

---

## BAGIAN 1: HASIL CLUSTERING DAN SAMPLING
**~544 baris (~11 halaman) - 21% dari total**

### 📊 4.1 Hasil Evaluasi Clustering

**Tujuan**: Menentukan jumlah cluster optimal (K) menggunakan 3 metrik evaluasi

#### 4.1.1 Hasil Evaluasi Elbow Method
- **Topik**: Identifikasi titik "siku" pada grafik K vs Inertia
- **Data**: Tabel Inertia untuk K=2 hingga K=10
- **Temuan**: Penurunan terbesar di K=2→K=3 (4.4%), diminishing returns setelahnya
- **Konten**: 4 baris intro + 14 baris tabel + 33 baris analisis

#### 4.1.2 Hasil Evaluasi Silhouette Score
- **Topik**: Mengukur kualitas clustering (jarak intra vs inter-cluster)
- **Data**: Tabel Silhouette Score untuk K=2 hingga K=10
- **Temuan**: K=2 mencapai skor tertinggi (0.0798), ~19% lebih baik dari K lainnya
- **Konten**: 4 baris intro + 14 baris tabel + 30 baris analisis

#### 4.1.3 Hasil Evaluasi Davies-Bouldin Index
- **Topik**: Mengukur rata-rata similarity antar cluster
- **Data**: Tabel DB Index untuk K=2 hingga K=10
- **Temuan**: Penurunan konsisten ke K=10, tapi perbaikan marginal
- **Konten**: 4 baris intro + 14 baris tabel + 34 baris analisis

#### 4.1.4 Konsensus Keputusan K Optimal
- **Topik**: Keputusan final berdasarkan konsensus 3 metrik
- **Data**: Ringkasan evaluasi, trade-off analysis
- **Keputusan**: **K=2 dipilih** (2 dari 3 metrik mendukung, interpretabilitas tinggi)
- **Konten**: Tabel ringkasan + 47 baris justifikasi

---

### 🎯 4.2 Hasil Clustering Final dengan K=2

**Tujuan**: Presentasi hasil clustering dengan K=2 yang telah ditentukan

#### 4.2.1 Distribusi Pasien per Cluster
- **Topik**: Pembagian 303 pasien ke 2 cluster
- **Hasil**: Cluster 0 = 145 pasien (47.9%), Cluster 1 = 158 pasien (52.1%)
- **Observasi**: Distribusi hampir seimbang (selisih 4.2%)
- **Konten**: 18 baris

#### 4.2.2 Distribusi Diagnosis per Cluster
- **Topik**: Cross-tabulation cluster vs diagnosis ground truth
- **Hasil**: 
  - Cluster 0: Sehat=68 (46.9%), Sakit=77 (53.1%)
  - Cluster 1: Sehat=78 (49.4%), Sakit=80 (50.6%)
- **Observasi**: Cluster 0 mayoritas sakit, Cluster 1 hampir seimbang
- **Konten**: Tabel + 37 baris interpretasi

#### 4.2.3 Interpretasi Klinis Karakteristik Cluster
- **Topik**: Profil klinis kedua cluster
- **Cluster 0**: Karakteristik heterogen, beragam, sulit diklasifikasi
- **Cluster 1**: Karakteristik distinct, profil risiko lebih jelas
- **Konten**: 2 sub-bagian @ ~14 baris

#### 4.2.4 Metrik Kualitas Clustering
- **Topik**: Evaluasi kualitas clustering final
- **Metrik**: Inertia=3615.99, Silhouette=0.0798, DB Index=3.3232
- **Interpretasi**: Adequate untuk tujuan sampling, meski struktur lemah
- **Konten**: 36 baris

---

### ✅ 4.3 Hasil Sampling Stratified

**Tujuan**: Memilih 100 test cases representatif dari 303 pasien

#### 4.3.1 Perhitungan Alokasi Sampel per Cluster
- **Formula**: Proportional allocation $n_i = \frac{N_i}{N} \times n$
- **Alokasi**: 50 sampel per cluster (50+50=100)
- **Justifikasi**: Kesederhanaan, balance, clean division
- **Konten**: 17 baris + tabel alokasi

#### 4.3.2 Distribusi Sampel Terpilih
- **Per Cluster**: 50 dari Cluster 0, 50 dari Cluster 1
- **Ground Truth**: Sehat=51 (51%), Sakit=49 (49%)
- **Observasi**: Perfect balance 51/49, ideal untuk evaluasi
- **Konten**: 2 tabel + 33 baris analisis

#### 4.3.3 Variasi Karakteristik Sampel
- **Range Numerik**: Full coverage semua parameter (age, BP, cholesterol, dll)
- **Distribusi Kategorikal**: Semua kategori terwakili
- **Konten**: 2 tabel (12+17 baris)

#### 4.3.4 Validasi Representativitas Sampel
- **Validasi 1**: Mean difference <1%, Std difference <4% → PASS
- **Validasi 2**: Proportion difference <3% → PASS
- **Validasi 3**: KS test p>0.05 → PASS (distribusi sama)
- **Konten**: 3 sub-validasi @ ~15 baris

#### 4.3.5 Kesimpulan Validasi Sampling
- **Ringkasan**: Sampel sangat representatif dan beragam
- **Kriteria**: ✅ Representatif, ✅ Beragam, ✅ Seimbang, ✅ Valid
- **Konten**: 33 baris ringkasan

---

## BAGIAN 2: HASIL KONSISTENSI MODEL LLM
**~660 baris (~13 halaman) - 25% dari total**

### 🧪 4.4 Hasil Eksperimen Multi-Run Testing

#### 4.4.1 Ringkasan Eksekusi Eksperimen
- **Protokol**: 3 models × 100 cases × 4 runs × 2 prompts = 2,400 prediksi
- **Status**: ✅ Semua 2,400 prediksi berhasil dikumpulkan
- **Waktu**: ~2.5 jam total eksekusi
- **Konten**: 21 baris

---

### 🔄 4.5 Hasil Konsistensi Intra-Model

**Tujuan**: Mengukur reproducibility setiap model (4 runs per case)

#### 4.5.1 Average Consistency Score per Model
- **GPT-4o**: 99.13% (Combined), 99.25% (Expert), 99.00% (Neutral)
- **Gemini**: 99.38% (Combined), 99.50% (Expert), 99.25% (Neutral)
- **Qwen-Plus**: **99.88%** (Combined), 100.00% (Expert), 99.75% (Neutral)
- **Konten**: Tabel + 28 baris observasi

#### 4.5.2 Perfect Consistency Rate (PCR)
- **GPT-4o**: 97.0% (96% Neutral, 98% Expert)
- **Gemini**: 98.0% (98% both prompts)
- **Qwen-Plus**: **99.5%** (99% Neutral, 100% Expert)
- **Interpretasi**: 96-100% kasus perfectly consistent
- **Konten**: Tabel + 35 baris analisis

#### 4.5.3 Distribusi Consistency Scores
- **Distribusi**: 96-100% kasus C=1.0 (4/4 runs agree)
- **C=0.75**: 0-4 kasus per model-prompt
- **C=0.5**: Hanya 2 kejadian total (probability <0.4%)
- **Konten**: Tabel + visualisasi konseptual + 60 baris analisis + gambar

#### 4.5.4 Analisis Kasus Inkonsisten
- **Total**: GPT 2-4 kasus, Gemini 2 kasus, Qwen 0-1 kasus
- **Overlap**: Rendah antar model (model-specific)
- **Pola**: Tidak ada karakteristik klinis spesifik, tampak random
- **Konten**: 37 baris

#### 4.5.5 Perbandingan Consistency Antar Model
- **Ranking**: Qwen (99.88%) > Gemini (99.38%) > GPT (99.13%)
- **Gap**: <1 percentage point (tidak material)
- **Konten**: Tabel ranking + 30 baris interpretasi

#### 4.5.6 Pengaruh Prompt terhadap Consistency
- **Perbedaan**: Expert vs Neutral ≤0.25% (tidak signifikan)
- **p-value**: >0.05 (tidak statistically significant)
- **Kesimpulan**: Consistency = model property, bukan fungsi prompt
- **Konten**: Tabel + 22 baris analisis

#### 4.5.7 Kesimpulan Hasil Konsistensi
- **Temuan**: 99-100% consistency, minimal variability, prompt-invariant
- **Interpretasi**: Exceptional reproducibility
- **Critical Note**: ⚠️ Consistency ≠ Accuracy
- **Konten**: 41 baris ringkasan

---

### 📉 4.6 Hasil Akurasi Diagnostik

**Tujuan**: Evaluasi apakah prediksi konsisten tersebut BENAR atau SALAH

#### 4.6.1 Overall Diagnostic Accuracy
- **GPT-4o**: 49.0% (49 correct, 51 incorrect)
- **Gemini**: 50.0% (50 correct, 50 incorrect)
- **Qwen**: 48.0% (48 correct, 52 incorrect)
- **Baseline**: 50% (random guessing)
- **Temuan**: ⚠️ **Chance-level performance** - tidak better than random
- **Konten**: Tabel + 36 baris observasi kritis

#### 4.6.2 Confusion Matrix Analysis
- **GPT-4o**: TP=49, TN=0, FP=51, FN=0 (Sens=100%, Spec=0%)
- **Gemini**: TP=49, TN=1, FP=50, FN=0 (Sens=100%, Spec=2%)
- **Qwen**: TP=48, TN=0, FP=51, FN=1 (Sens=98%, Spec=0%)
- **Konten**: 3 confusion matrices @ ~24 baris + Gambar 4.2

#### 4.6.3 Pattern Analisis: Systematic Over-Diagnosis Bias
- **FP:FN Ratio**: GPT ∞ (51:0), Gemini ∞ (50:0), Qwen 51:1
- **Average**: ~152:1 (extreme imbalance)
- **Pattern**: Uniform across all models - systematic issue
- **Konten**: Tabel + 41 baris observasi kritis

#### 4.6.4 Precision, Recall, dan F1-Score
- **Precision**: ~49% (half of positive predictions wrong)
- **Recall**: ~99% (near-perfect disease detection)
- **F1-Score**: ~0.66 (moderate, driven by high recall)
- **Trade-off**: High sensitivity, low specificity
- **Konten**: Tabel + 44 baris analisis

---

## BAGIAN 3: ANALISIS PROMPT DAN INTER-MODEL AGREEMENT
**~682 baris (~14 halaman) - 26% dari total**

### 🔧 4.7 Hasil Perbandingan Prompt (Prompt Engineering Analysis)

**Pertanyaan Kunci**: Apakah prompt engineering dapat meningkatkan performa?

#### 4.7.1 Impact Prompt terhadap Akurasi Diagnostik
- **GPT**: Expert 51% vs Neutral 49% (Δ=-2%)
- **Gemini**: Expert 51% vs Neutral 49% (Δ=-2%)
- **Qwen**: Expert 51% vs Neutral 48% (Δ=-3%)
- **Temuan**: ❌ **Minimal impact** (<3%), kedua prompt ~50% (chance)
- **Konten**: Tabel + 14 baris observasi

#### 4.7.2 Impact Prompt terhadap Confusion Matrix
- **GPT**: Expert (TP=51, FP=49) vs Neutral (TP=49, FP=51)
- **Gemini**: Expert (TP=50, TN=1) vs Neutral (TP=49, TN=0)
- **Qwen**: Expert (TP=51, FP=49) vs Neutral (TP=48, FP=51, FN=1)
- **Interpretasi**: Neutral sedikit lebih agresif (more FP)
- **Konten**: 3 comparisons @ ~26 baris

#### 4.7.3 Impact Prompt terhadap Precision, Recall, dan F1-Score
- **Precision**: Δ=-2 to -2.5% (Neutral lower)
- **Recall**: Δ=±2% (negligible)
- **F1-Score**: Δ=-1.3 to -2.6% (slight decrease)
- **Konten**: Tabel detail + 24 baris analisis

#### 4.7.4 Impact Prompt terhadap Consistency
- **Perbedaan**: Expert vs Neutral <0.3% (sudah dibahas di 4.5.6)
- **Konten**: 20 baris ringkasan

#### 4.7.5 Analisis Prediction Changes
- **Agreement**: 96-98% same prediction antar prompt
- **Change Rate**: 2-4% (hanya 2-4 kasus berbeda)
- **Karakteristik**: Kasus yang berubah tidak ada pola jelas (random)
- **Konten**: Tabel + 21 baris analisis

#### 4.7.6 Kesimpulan Analisis Prompt Engineering
- **Temuan Utama**:
  1. ❌ Tidak efektif untuk akurasi (Δ≤3%)
  2. ❌ Tidak efektif untuk error pattern (over-diagnosis persists)
  3. ✅ Tidak mengganggu consistency (99-100% maintained)
  4. ✅ Prediction robust (96-98% agreement)
- **Implikasi**: ⚠️ **Prompt engineering bukan solusi** untuk akurasi
- **Konten**: 76 baris termasuk Gambar 4.4

---

### 🤝 4.8 Hasil Inter-Model Agreement

**Tujuan**: Menganalisis apakah ketiga model setuju dalam prediksi

#### 4.8.1 Pairwise Agreement Rate
- **GPT ↔ Gemini**: 98% agreement
- **GPT ↔ Qwen**: 97% agreement
- **Gemini ↔ Qwen**: 97% agreement
- **Average**: 97.3% agreement
- **Konten**: Tabel + 13 baris observasi

#### 4.8.2 Three-Way Agreement Analysis
- **All Three Agree**: 96 kasus (96%)
- **Two Agree, One Disagrees**: 4 kasus (4%)
- **All Three Disagree**: 0 kasus (0%)
- **Majority Vote Accuracy**: 2/4 correct (50% - chance level)
- **Konten**: Tabel + breakdown 4 kasus + 32 baris analisis

#### 4.8.3 Cohen's Kappa Analysis
- **κ (Kappa)**: 0.94-0.95 (Almost Perfect Agreement)
- **Observed**: 97% vs Expected by chance: 50%
- **Gap**: 47 percentage points above chance
- **Comparison**: LLMs (κ=0.94) > Humans (κ=0.60-0.80)
- **Konten**: Tabel + scale + 25 baris observasi

#### 4.8.4 Error Correlation Analysis
- **Shared FP**: 48/50 (96% overlap) - same healthy patients misclassified
- **Shared FN**: Sangat jarang (0-1 per model)
- **Correlation**: r=0.95-0.96 (very high)
- **Implikasi**: ❌ **Cannot use ensemble** for error mitigation
- **Konten**: Tabel + 36 baris analisis

#### 4.8.5 Prediction Distribution Comparison
- **Models**: Predict positive 98-99%
- **Ground Truth**: 49% positive, 51% negative
- **Discrepancy**: ~50 percentage points
- **Chi-square**: p<0.001 (highly significant difference)
- **Konten**: Visualisasi + 21 baris observasi

#### 4.8.6 Disagreement Case Analysis
- **Case 23**: GPT+Gemini correct, Qwen wrong
- **Case 47**: Gemini correct (rare!), GPT+Qwen wrong
- **Case 68**: GPT+Gemini correct, Qwen wrong
- **Case 91**: GPT correct (rare!), Gemini+Qwen wrong
- **Konten**: 4 cases @ ~20 baris

#### 4.8.7 Kesimpulan Inter-Model Agreement
- **Temuan Utama**:
  1. ✅ Exceptional agreement (97-98%, κ=0.94)
  2. ✅ Systematic consistency (far beyond chance)
  3. ❌ Shared biases (96% errors sama)
  4. ❌ No ensemble benefit (majority voting 50%)
  5. ❌ Severe miscalibration (predict 99% vs actual 49%)
- **Konten**: 85 baris termasuk Gambar 4.5

---

## BAGIAN 4: PEMBAHASAN DAN INTERPRETASI KLINIS
**~723 baris (~14 halaman) - 28% dari total**

### 💡 4.9 Pembahasan Umum

#### 4.9.1 Ringkasan Temuan Utama
- **1. Exceptional Reproducibility**: 99-100% consistency
- **2. Chance-Level Accuracy**: 48-50% (no better than random)
- **3. Systematic Over-Diagnosis**: FP:FN ~152:1, Sensitivity 99%, Specificity 0%
- **4. Minimal Prompt Impact**: <3% difference
- **5. High Inter-Model Agreement**: 97% agreement, shared errors 96%
- **Konten**: 54 baris dengan 5 temuan detail

#### 4.9.2 The Consistency-Accuracy Dissociation
- **Gap**: ~50 percentage points (Consistency 99% vs Accuracy 49%)
- **Tabel**: Quantifikasi gap per model
- **Gambar 4.6**: Visualisasi dissociation (dual violin plot)
- **Interpretasi**: "Consistently Wrong" phenomenon
- **Analisis Dissociation**:
  - High internal consistency ✓
  - Wrong reasoning path ✗
  - Lack of uncertainty ✗
- **Konten**: 72 baris + analisis 30 baris

#### 4.9.3 Mengapa Akurasi Rendah Meskipun Konsistensi Tinggi?
- **Hipotesis 1**: Oversimplified disease model (IF abnormality THEN disease)
- **Hipotesis 2**: Lack of statistical/probabilistic reasoning (base rates, PPV)
- **Hipotesis 3**: Training data bias (textbooks focus on disease)
- **Hipotesis 4**: Lack of causal reasoning (correlation ≠ causation)
- **Hipotesis 5**: Overconfidence dari temperature=0.7
- **Konten**: 5 hipotesis @ ~14 baris

#### 4.9.4 Perbandingan dengan Literatur
- **Study 1**: LLM on USMLE exams (90%+ accuracy) vs Real diagnosis (50%)
  - Gap: 40 percentage points
  - **Interpretasi**: Exam knowledge ≠ Clinical reasoning
- **Study 2**: Clinical DSS (70-85% accuracy) > LLMs (50%)
  - **Interpretasi**: Traditional ML + domain knowledge better
- **Study 3**: Physician agreement (κ=0.60-0.80) < LLM (κ=0.94)
  - **Interpretasi**: LLM overconfidence problem
- **Konten**: 3 studies @ ~17 baris

---

### 🏥 4.10 Interpretasi Klinis: Consistency-Accuracy Gap

#### 4.10.1 Apa yang Diceritakan oleh Gap ~50 pp?
- **Reliability vs Validity**: High reliability ✓, Low validity ✗
- **Analogi**: Timbangan selalu tunjukkan angka sama (reliable) tapi salah 5kg (not valid)
- **Konten**: 16 baris

#### 4.10.2 Implikasi untuk Clinical Deployment
- **Skenario 1**: Primary Diagnostic Tool → ❌ TIDAK DISARANKAN
  - 50% error rate unacceptable
- **Skenario 2**: Screening Tool → ⚠️ MUNGKIN dengan kondisi
  - High sensitivity ✓, Low specificity ✗, High FP costly
- **Skenario 3**: Supplementary Decision Support → ✅ PALING AMAN
  - Physician maintains control
- **Skenario 4**: Triage System → ⚠️ PERLU threshold optimization
- **Konten**: 4 skenarios @ ~15 baris

#### 4.10.3 Rekomendasi Deployment Berbasis Evidence
- **Level 1**: ❌ TIDAK DIREKOMENDASIKAN
  - Autonomous systems, final decision maker
- **Level 2**: ⚠️ HATI-HATI, PERLU SAFEGUARDS
  - Screening, triage, dengan mandatory human review
- **Level 3**: ✅ DIREKOMENDASIKAN dengan SUPERVISION
  - Supplementary support, consistency check, education
- **Konten**: 3 levels @ ~14 baris

---

### ⚠️ 4.11 Keterbatasan Penelitian

#### 4.11.1 Keterbatasan Dataset
- Single dataset (UCI 303 patients, tahun 1988)
- Binary classification only
- Limited clinical features (13 parameters)
- De-identified data (no temporal info)
- **Konten**: 30 baris (4 limitations)

#### 4.11.2 Keterbatasan Metodologi
- Fixed temperature (0.7)
- Limited prompt variations (2 types only)
- Majority voting for final prediction
- No fine-tuning
- **Konten**: 27 baris (4 limitations)

#### 4.11.3 Keterbatasan Generalisasi
- Specific disease domain (cardiovascular only)
- Specific task (binary diagnosis)
- English language only
- Specific model versions
- **Konten**: 26 baris (4 limitations)

#### 4.11.4 Keterbatasan Evaluasi
- Ground truth assumption
- No clinical context
- No cost-benefit analysis
- Short-term evaluation only
- **Konten**: 29 baris (4 limitations)

---

### 🔮 4.12 Rekomendasi untuk Penelitian Future

#### 4.12.1 Immediate Next Steps
- Multi-dataset validation
- Fine-tuning experiments
- Advanced prompting techniques (chain-of-thought, RAG)
- Temperature and sampling exploration
- **Konten**: 22 baris (4 rekomendasi)

#### 4.12.2 Methodological Improvements
- Uncertainty quantification (confidence scores, calibration)
- Explainable AI (reasoning paths, key features)
- Hybrid systems (LLM + rules + traditional ML)
- Human-AI collaboration studies
- **Konten**: 22 baris (4 rekomendasi)

#### 4.12.3 Extended Clinical Evaluation
- Prospective clinical trials
- Comparative effectiveness (LLM vs physicians)
- Longitudinal studies
- Multi-disease evaluation
- **Konten**: 22 baris (4 rekomendasi)

#### 4.12.4 Theoretical Understanding
- Mechanistic interpretability (why high consistency, low accuracy?)
- Bias and fairness analysis (demographic disparities)
- Calibration studies
- Knowledge provenance (training data sources)
- **Konten**: 24 baris (4 rekomendasi)

---

### 🛠️ 4.13 Implikasi untuk AI Development

#### 4.13.1 Lessons for LLM Developers
- Consistency ≠ Accuracy (prioritize validity)
- Domain-specific training critical
- Uncertainty quantification essential
- Evaluation must match use case
- **Konten**: 22 baris (4 lessons)

#### 4.13.2 Recommendations for Clinical AI
- Transparent limitations
- Human oversight mandatory
- Continuous monitoring
- Ethical deployment
- **Konten**: 24 baris (4 recommendations)

---

### 🎯 4.14 Kesimpulan BAB 4

#### Temuan Kunci
1. High Consistency (99-100%)
2. Low Accuracy (~50%)
3. Massive Gap (~50 pp)
4. Systematic Bias (FP:FN 152:1)
5. No Prompt Impact (<3%)
6. High Inter-Model Agreement (κ=0.94, shared errors 96%)
- **Konten**: 9 baris

#### Implikasi Utama
- **Deployment**: ❌ Tidak autonomous, ⚠️ Hati-hati screening, ✅ Supplementary support
- **Research**: Fokus validity, fine-tuning, multi-dataset
- **Practice**: Human oversight critical, transparency paramount
- **Konten**: 17 baris

#### Kontribusi Penelitian
1. Empirical evidence LLM limitations
2. Methodological framework (consistency vs accuracy)
3. Practical guidance (responsible deployment)
4. Theoretical insight (reliability vs validity)
- **Konten**: 16 baris

---

## FLOW LOGIKA ANTAR BAGIAN

```
BAGIAN 1: Data Preparation
├─ Clustering evaluation → K=2 optimal
├─ Stratified sampling → 100 test cases
└─ Validation → Representative & diverse

        ↓

BAGIAN 2: Model Performance
├─ Consistency evaluation → 99-100% (EXCEPTIONAL)
├─ Accuracy evaluation → 48-50% (CHANCE LEVEL)
└─ Discovery: DISSOCIATION (~50 pp gap)

        ↓

BAGIAN 3: Deep Analysis
├─ Prompt engineering → No effect (<3%)
├─ Inter-model agreement → Very high (97%, κ=0.94)
└─ Finding: SHARED BIASES (96% same errors)

        ↓

BAGIAN 4: Interpretation
├─ Why? → 5 Hypotheses (oversimplified model, lack reasoning, etc)
├─ Comparison → Literature confirms limitations
├─ Clinical implications → ❌ Not for autonomous use
├─ Limitations → Dataset, methodology, generalization
├─ Future work → Fine-tuning, multi-dataset, uncertainty
└─ Conclusion → High consistency ≠ High accuracy
```

---

## HIGHLIGHTS PER BAGIAN

### BAGIAN 1 Highlights:
- ✅ **K=2 dipilih** berdasarkan konsensus 2 dari 3 metrik
- ✅ **100 sampel** perfectly balanced (51 sehat, 49 sakit)
- ✅ **Validasi passed** semua tests (KS p>0.05, mean Δ<1%, prop Δ<3%)

### BAGIAN 2 Highlights:
- 🔥 **99-100% consistency** (exceptional reproducibility)
- ⚠️ **48-50% accuracy** (no better than random!)
- 🚨 **Gap ~50 pp** (consistency-accuracy dissociation)
- 📊 **FP:FN 152:1** (extreme over-diagnosis bias)

### BAGIAN 3 Highlights:
- ❌ **Prompt engineering ineffective** (Δ<3%)
- 🤝 **97% inter-model agreement** (κ=0.94 almost perfect)
- 🔁 **96% shared errors** (same mistakes!)
- 🚫 **No ensemble benefit** (majority voting still 50%)

### BAGIAN 4 Highlights:
- 💡 **5 Hypotheses** explaining low accuracy
- 📚 **Literature confirms**: Exam knowledge ≠ Clinical reasoning
- 🏥 **Clinical deployment**: ✅ Supplementary only, ❌ Not autonomous
- 🔬 **Future work**: Fine-tuning, multi-dataset, uncertainty quantification
- 🎯 **Main contribution**: Empirical evidence of LLM limitations

---

## TABEL DAN GAMBAR

### Tabel (Total: ~35 tabel)

**BAGIAN 1**: 10 tabel
- Tabel Inertia K=2-10
- Tabel Silhouette K=2-10
- Tabel Davies-Bouldin K=2-10
- Tabel Ringkasan 3 Metrik
- Tabel Distribusi Pasien
- Tabel Distribusi Target
- Tabel Alokasi Sampel
- Tabel Validasi (3 tabel)

**BAGIAN 2**: 8 tabel
- Tabel 4.1: Rangkuman Eksekusi
- Tabel 4.2: Consistency Scores
- Tabel 4.3: Perfect Consistency Rate
- Tabel 4.4: Distribusi Consistency
- Tabel 4.6: Akurasi Diagnostik
- Tabel 4.7: Error Pattern
- Tabel 4.8: Precision/Recall/F1

**BAGIAN 3**: 10 tabel
- Tabel 4.9: Prompt Comparison Accuracy
- Tabel 4.10: Prompt Comparison Metrics
- Tabel 4.11: Prompt Consistency
- Tabel 4.12: Prediction Changes
- Tabel 4.13: Pairwise Agreement
- Tabel Three-Way Agreement
- Tabel 4.14: Cohen's Kappa
- Tabel Shared Errors
- Tabel 4.15: Prediction Distribution
- Confusion matrix comparisons (3 tabel)

**BAGIAN 4**: 7 tabel
- Tabel 4.16: Dissociation Gap
- Tabel Trade-off K=2 vs K=10
- Tabel LLM vs Clinician
- Tabel Skenario Deployment
- Tabel Level Recommendations
- Tabel Limitations Summary
- Tabel Future Work

### Gambar (Total: 6 gambar)

1. **Gambar 4.1**: Evaluasi K Optimal (3 panel: Elbow, Silhouette, DB Index)
2. **Gambar 4.2**: Confusion Matrices (3 models)
3. **Gambar 4.3**: Comprehensive Consistency Analysis (violin plots)
4. **Gambar 4.4**: Prompt Comparison (accuracy & agreement)
5. **Gambar 4.5**: Model Comparison & Agreement (4 panel)
6. **Gambar 4.6**: Consistency-Accuracy Dissociation (dual violin)

---

## KEYWORD INDEX

**Metrik Utama**:
- Consistency: 99-100%
- Accuracy: 48-50%
- Sensitivity: 98-100%
- Specificity: 0-2%
- Precision: ~49%
- Recall: ~99%
- F1-Score: ~0.66
- Cohen's Kappa: 0.94

**Bias**:
- Over-diagnosis bias
- FP:FN ratio: 152:1
- False Positive: ~51
- False Negative: ~0-1

**Agreement**:
- Inter-model: 97%
- Shared errors: 96%
- Prompt agreement: 96-98%

**Cluster**:
- K=2 optimal
- Silhouette: 0.0798
- Inertia: 3615.99
- DB Index: 3.3232

**Sample**:
- 100 test cases
- 51 sehat, 49 sakit
- Perfectly balanced

---

**Dokumen ini dapat digunakan untuk:**
1. Navigasi cepat ke bagian spesifik
2. Memahami flow argumentasi
3. Review sebelum presentasi/defense
4. Identifikasi gap atau area yang perlu diperkuat
5. Reference untuk menulis abstract/summary

