# BAB 4 - HASIL DAN PEMBAHASAN
## BAGIAN 2: HASIL KONSISTENSI MODEL LLM

---

## 4.4 Hasil Eksperimen Multi-Run Testing

Setelah mendapatkan 100 kasus uji yang representatif, dilakukan testing terhadap tiga model LLM (GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus) menggunakan protokol multi-run dengan 4 kali pengulangan per kasus.

### 4.4.1 Ringkasan Eksekusi Eksperimen

Eksperimen dilaksanakan dengan sukses menghasilkan **2,400 prediksi total**:

| Model | Kasus | Runs per Kasus | Prompts | Total Prediksi per Model |
|-------|-------|----------------|---------|--------------------------|
| GPT-4o | 100 | 4 | 2 | 800 |
| Gemini-2.0-Flash | 100 | 4 | 2 | 800 |
| Qwen-Plus | 100 | 4 | 2 | 800 |
| **TOTAL** | 100 | 4 | 2 | **2,400** |

**Status Eksekusi**:
- ✅ Semua 2,400 prediksi berhasil dikumpulkan
- ✅ Tidak ada missing data atau API failures yang tidak tertangani
- ✅ Checkpoint system berfungsi dengan baik untuk recovery
- ✅ Waktu total eksekusi: ~2.5 jam

---

## 4.5 Hasil Konsistensi Intra-Model

Konsistensi intra-model mengukur seberapa reliable setiap model dalam memberikan prediksi yang sama ketika dijalankan berulang kali pada kasus yang identik.

### 4.5.1 Average Consistency Score per Model

Tabel berikut menunjukkan average consistency score untuk setiap kombinasi model dan prompt:

| Model | Prompt Type | Average Consistency | Std Dev | Min Consistency | Max Consistency |
|-------|-------------|---------------------|---------|-----------------|-----------------|
| **GPT-4o** | Expert | 0.9925 | 0.0554 | 0.5 | 1.0 |
| **GPT-4o** | Neutral | 0.9900 | 0.0490 | 0.75 | 1.0 |
| **GPT-4o** | **Combined** | **0.9913** | 0.0522 | 0.5 | 1.0 |
| **Gemini-2.0-Flash** | Expert | 0.9950 | 0.0350 | 0.75 | 1.0 |
| **Gemini-2.0-Flash** | Neutral | 0.9925 | 0.0554 | 0.5 | 1.0 |
| **Gemini-2.0-Flash** | **Combined** | **0.9938** | 0.0454 | 0.5 | 1.0 |
| **Qwen-Plus** | Expert | 1.0000 | 0.0000 | 1.0 | 1.0 |
| **Qwen-Plus** | Neutral | 0.9975 | 0.0249 | 0.75 | 1.0 |
| **Qwen-Plus** | **Combined** | **0.9988** | 0.0175 | 0.75 | 1.0 |

**Catatan**: Combined = rata-rata dari kedua prompt type untuk setiap model.

#### Observasi Kunci

1. **Konsistensi Sangat Tinggi di Semua Model**:
   - GPT-4o: 99.13% average consistency
   - Gemini-2.0-Flash: 99.38% average consistency
   - Qwen-Plus: **99.88% average consistency** (tertinggi)

2. **Qwen-Plus Paling Konsisten**:
   - Mencapai **perfect consistency (100%)** pada Expert prompt
   - Hanya 1 kasus dengan consistency < 1.0 pada Neutral prompt (99.75%)
   - Standar deviasi terendah (0.0175)

3. **Variasi Minimal Antar Prompt**:
   - Perbedaan consistency antara Expert vs Neutral: < 0.3% untuk semua model
   - Prompt type tidak signifikan mempengaruhi consistency

4. **Min Consistency Berbeda**:
   - GPT-4o: Min = 0.5 (ada kasus 2-2 split)
   - Gemini: Min = 0.5 (ada kasus 2-2 split)
   - Qwen: Min = 0.75 (worst case 3-1 split)

**Interpretasi**:

Hasil ini menunjukkan bahwa **ketiga model LLM sangat reliable dalam memberikan prediksi konsisten**:
- ~99-100% consistency = hampir selalu memberikan jawaban sama pada kasus yang sama
- Temperature=0.7 (randomness moderat) tidak mengganggu consistency secara signifikan
- Ini adalah **temuan positif** untuk reliability LLM, NAMUN belum tentu akurat (akan dibahas di bagian 4.6)

### 4.5.2 Perfect Consistency Rate (PCR)

Perfect Consistency Rate mengukur persentase kasus yang mencapai konsistensi sempurna (C=1.0, yaitu 4/4 runs agree).

#### Tabel Perfect Consistency Rate

| Model | Prompt Type | Perfect Consistency Cases | Total Cases | PCR (%) |
|-------|-------------|---------------------------|-------------|---------|
| **GPT-4o** | Expert | 98 | 100 | **98.0%** |
| **GPT-4o** | Neutral | 96 | 100 | **96.0%** |
| **GPT-4o** | **Average** | 97 | 100 | **97.0%** |
| **Gemini-2.0-Flash** | Expert | 98 | 100 | **98.0%** |
| **Gemini-2.0-Flash** | Neutral | 98 | 100 | **98.0%** |
| **Gemini-2.0-Flash** | **Average** | 98 | 100 | **98.0%** |
| **Qwen-Plus** | Expert | 100 | 100 | **100.0%** |
| **Qwen-Plus** | Neutral | 99 | 100 | **99.0%** |
| **Qwen-Plus** | **Average** | 99.5 | 100 | **99.5%** |

#### Analisis Perfect Consistency Rate

**Observasi Kunci**:

1. **Qwen-Plus Unggul dengan 99.5% PCR**:
   - 100% perfect consistency pada Expert prompt
   - 99% pada Neutral prompt
   - Hanya 0.5 kasus rata-rata yang tidak perfect consistent

2. **Gemini Stabil di 98% PCR**:
   - Konsisten 98% di kedua prompt
   - 2 kasus per prompt tidak perfectly consistent

3. **GPT-4o Sedikit Lebih Rendah (97% PCR)**:
   - 98% di Expert, 96% di Neutral
   - 3-4 kasus tidak perfectly consistent

4. **Variasi Antar Prompt Minimal**:
   - GPT-4o: 2% difference (Expert lebih baik)
   - Gemini: 0% difference (identik)
   - Qwen: 1% difference (Expert lebih baik)

**Interpretasi**:

- **96-100% PCR adalah exceptional** untuk sistem AI dengan temperature > 0
- Sebagian besar kasus (97-100%) menghasilkan prediksi identik di semua 4 runs
- Hanya 0-4 kasus per model-prompt yang menunjukkan inkonsistensi

**Perbandingan dengan Baseline**:

Jika model completely random (temperature sangat tinggi):
- Expected PCR = ~37.5% (probabilitas 4 runs agree by chance)
- Observed PCR = 96-100%
- **Gap = ~60 percentage points** → Model sangat non-random

### 4.5.3 Distribusi Consistency Scores

Analisis distribusi consistency scores memberikan gambaran lebih lengkap tentang pola konsistensi.

#### Tabel Distribusi Consistency Scores

| Model | C=1.0 (4/4) | C=0.75 (3/4) | C=0.5 (2/4) | Total |
|-------|-------------|--------------|-------------|-------|
| **GPT-4o (Expert)** | 98 (98.0%) | 1 (1.0%) | 1 (1.0%) | 100 |
| **GPT-4o (Neutral)** | 96 (96.0%) | 4 (4.0%) | 0 (0.0%) | 100 |
| **Gemini (Expert)** | 98 (98.0%) | 2 (2.0%) | 0 (0.0%) | 100 |
| **Gemini (Neutral)** | 98 (98.0%) | 1 (1.0%) | 1 (1.0%) | 100 |
| **Qwen (Expert)** | 100 (100.0%) | 0 (0.0%) | 0 (0.0%) | 100 |
| **Qwen (Neutral)** | 99 (99.0%) | 1 (1.0%) | 0 (0.0%) | 100 |

#### Visualisasi Distribusi (Konseptual)

```
Consistency Score Distribution

GPT-4o Expert:    ████████████████████████████████████████████████████ 98% (C=1.0)
                  █ 1% (C=0.75)
                  █ 1% (C=0.5)

GPT-4o Neutral:   ████████████████████████████████████████████████ 96% (C=1.0)
                  ████ 4% (C=0.75)

Gemini Expert:    ████████████████████████████████████████████████████ 98% (C=1.0)
                  ██ 2% (C=0.75)

Gemini Neutral:   ████████████████████████████████████████████████████ 98% (C=1.0)
                  █ 1% (C=0.75)
                  █ 1% (C=0.5)

Qwen Expert:      ██████████████████████████████████████████████████████ 100% (C=1.0)

Qwen Neutral:     ████████████████████████████████████████████████████ 99% (C=1.0)
                  █ 1% (C=0.75)
```

#### Analisis Distribusi

**Observasi Kunci**:

1. **Dominasi C=1.0 (Perfect Consistency)**:
   - 96-100% kasus memiliki perfect consistency
   - Distribusi sangat skewed ke kanan (high consistency)

2. **Sangat Sedikit Kasus C=0.75**:
   - GPT-4o: 1-4 kasus (1-4%)
   - Gemini: 1-2 kasus (1-2%)
   - Qwen: 0-1 kasus (0-1%)

3. **Extremely Rare C=0.5**:
   - Hanya 2 kejadian total (dari 600 kombinasi model-prompt-case)
   - GPT-4o Expert: 1 kasus
   - Gemini Neutral: 1 kasus
   - **Probability < 0.4%**

4. **Qwen Expert: Zero Inconsistency**:
   - 100/100 kasus perfect consistency
   - Tidak ada satupun kasus dengan C < 1.0
   - **Outstanding reproducibility**

**Interpretasi**:

Distribusi yang sangat skewed ini menunjukkan:
- **Consistency bukan masalah** untuk ketiga model
- Model LLM modern dengan temperature=0.7 masih sangat deterministic
- Inkonsistensi (C < 1.0) adalah **exception**, bukan norm

### 4.5.4 Analisis Kasus Inkonsisten

Meskipun sangat jarang, beberapa kasus menunjukkan inkonsistensi. Analisis terhadap kasus-kasus ini memberikan insight tentang situasi di mana model tidak reliable.

#### Karakteristik Kasus Inkonsisten

**Total Kasus Inkonsisten (C < 1.0)**:
- GPT-4o Expert: 2 kasus (1 dengan C=0.75, 1 dengan C=0.5)
- GPT-4o Neutral: 4 kasus (4 dengan C=0.75)
- Gemini Expert: 2 kasus (2 dengan C=0.75)
- Gemini Neutral: 2 kasus (1 dengan C=0.75, 1 dengan C=0.5)
- Qwen Expert: 0 kasus
- Qwen Neutral: 1 kasus (1 dengan C=0.75)

**Analisis Overlap**:
- Apakah kasus yang inkonsisten **sama** antar model?
- Apakah ada karakteristik klinis tertentu yang membuat kasus sulit?

**Temuan**:

1. **Overlap Rendah Antar Model**:
   - Kasus yang inkonsisten di GPT tidak selalu inkonsisten di Gemini/Qwen
   - Menunjukkan inkonsistensi bersifat **model-specific**, bukan inherent case difficulty

2. **Tidak Ada Pola Klinis Jelas**:
   - Kasus inkonsisten tidak memiliki karakteristik klinis yang spesifik
   - Mencakup berbagai range parameter (age, cholesterol, blood pressure, dll)
   - Tidak terbatas pada "borderline cases" atau "edge cases"

3. **Inkonsistensi Tampak Random**:
   - Tidak dapat diprediksi dari fitur klinis
   - Kemungkinan besar disebabkan oleh **stochastic sampling** pada temperature=0.7

**Interpretasi**:

Inkonsistensi yang sangat jarang dan tampak random menunjukkan:
- Bukan masalah sistematis dalam model reasoning
- Lebih ke **noise stokastik** dari sampling process
- Dengan temperature=0.7, sedikit randomness diharapkan
- **Acceptable trade-off** untuk menghindari complete determinism (T=0.0)

### 4.5.5 Perbandingan Consistency Antar Model

Ringkasan perbandingan konsistensi ketiga model:

| Metrik | GPT-4o | Gemini-2.0-Flash | Qwen-Plus | Winner |
|--------|--------|------------------|-----------|--------|
| **Avg Consistency** | 99.13% | 99.38% | **99.88%** | 🥇 Qwen |
| **Perfect Consistency Rate** | 97.0% | 98.0% | **99.5%** | 🥇 Qwen |
| **Std Dev (Lower better)** | 0.0522 | 0.0454 | **0.0175** | 🥇 Qwen |
| **Min Consistency** | 0.5 | 0.5 | **0.75** | 🥇 Qwen |
| **Max Inconsistent Cases** | 4 | 2 | **1** | 🥇 Qwen |

#### Ranking Consistency

1. **🥇 Qwen-Plus**: 99.88% consistency
   - Perfect consistency (100%) pada Expert prompt
   - Hanya 1 kasus inconsistent di Neutral prompt
   - Standar deviasi terendah
   - **Most reliable model**

2. **🥈 Gemini-2.0-Flash**: 99.38% consistency
   - 98% perfect consistency rate di kedua prompt
   - 2-4 kasus inconsistent
   - Performa stabil antar prompt

3. **🥉 GPT-4o**: 99.13% consistency
   - 96-98% perfect consistency rate
   - 2-4 kasus inconsistent per prompt
   - Sedikit lebih variabel dibanding Gemini

**Perbedaan Antar Model**:
- **Qwen vs GPT-4o**: +0.75 percentage points (99.88% vs 99.13%)
- **Qwen vs Gemini**: +0.50 percentage points (99.88% vs 99.38%)
- **Gemini vs GPT-4o**: +0.25 percentage points (99.38% vs 99.13%)

**Interpretasi**:

Meskipun ada ranking, **perbedaan sangat kecil** (<1 percentage point):
- Semua tiga model **exceptional** dalam consistency
- Perbedaan tidak material untuk aplikasi praktis
- **Ketiga model reliable** untuk diagnosis yang konsisten

### 4.5.6 Pengaruh Prompt terhadap Consistency

Analisis apakah tipe prompt (Expert vs Neutral) mempengaruhi consistency score.

#### Tabel Perbandingan Consistency: Expert vs Neutral

| Model | Expert Consistency | Neutral Consistency | Δ Consistency | p-value (t-test) |
|-------|-------------------|---------------------|---------------|------------------|
| **GPT-4o** | 99.25% | 99.00% | +0.25% | p > 0.05 (not significant) |
| **Gemini-2.0-Flash** | 99.50% | 99.25% | +0.25% | p > 0.05 (not significant) |
| **Qwen-Plus** | 100.00% | 99.75% | +0.25% | p > 0.05 (not significant) |
| **Average** | 99.58% | 99.33% | +0.25% | p > 0.05 (not significant) |

#### Analisis Pengaruh Prompt

**Observasi**:

1. **Perbedaan Sangat Kecil**: Δ Consistency ≤ 0.25% untuk semua model
2. **Trend Konsisten**: Expert prompt sedikit lebih konsisten di ketiga model
3. **Not Statistically Significant**: p > 0.05 untuk semua perbandingan
4. **Effect Size Negligible**: Cohen's d < 0.1 (very small effect)

**Interpretasi**:

- **Prompt type tidak berpengaruh signifikan** terhadap consistency
- Expert persona vs Neutral persona menghasilkan consistency yang hampir identik
- Model LLM tidak menjadi lebih/kurang konsisten karena framing prompt
- Consistency adalah **karakteristik inherent model**, bukan fungsi dari prompt

**Implikasi**:

✅ **Consistency adalah model property**: Tidak terpengaruh oleh prompt engineering
✅ **Robustness**: Model konsisten across berbagai prompt styles
✅ **Simplifikasi deployment**: Tidak perlu optimize prompt untuk consistency

### 4.5.7 Kesimpulan Hasil Konsistensi

**Temuan Utama Konsistensi**:

1. **✅ Exceptional Reproducibility**:
   - Semua model mencapai 99-100% average consistency
   - 96-100% kasus perfectly consistent (4/4 runs agree)
   - Qwen-Plus unggul dengan 99.88% consistency

2. **✅ Minimal Variability**:
   - Standar deviasi consistency: 0.018-0.052 (sangat kecil)
   - Min consistency: 0.5-0.75 (worst cases sangat jarang)
   - Inkonsistensi terjadi di < 4% kasus

3. **✅ Prompt-Invariant**:
   - Expert vs Neutral: perbedaan < 0.3%
   - Consistency tidak terpengaruh prompt framing
   - Robust across prompt variations

4. **✅ Model Hierarchy**:
   - Qwen-Plus > Gemini-2.0-Flash > GPT-4o
   - Perbedaan sangat kecil (<1 percentage point)
   - Ketiga model equally reliable untuk praktis

**Interpretasi Teoritis**:

Konsistensi tinggi ini menunjukkan:
- **Deterministic reasoning paths**: Model mengikuti logika yang sama untuk kasus sama
- **Well-trained representations**: Internal representations stabil
- **Temperature=0.7 not too high**: Randomness tidak mengganggu consistency secara signifikan

**Pertanyaan Kritis**:

⚠️ **Consistency tinggi ≠ Accuracy tinggi**

Sebuah model dapat sangat konsisten (selalu memberikan jawaban sama) namun **consistently wrong** (selalu salah). 

Oleh karena itu, **akurasi diagnostik** perlu dievaluasi secara terpisah (Bagian 4.6).

---

## 4.6 Hasil Akurasi Diagnostik

Setelah mengonfirmasi bahwa ketiga model sangat konsisten, langkah selanjutnya adalah mengevaluasi **akurasi diagnostik** - apakah prediksi yang konsisten tersebut **benar** atau **salah**.

### 4.6.1 Overall Diagnostic Accuracy

Untuk setiap model, prediksi final ditentukan menggunakan **majority voting** dari 4 runs, kemudian dibandingkan dengan ground truth diagnosis.

#### Tabel Akurasi Diagnostik per Model

| Model | Correct Predictions | Incorrect Predictions | Accuracy (%) | Baseline (Random) |
|-------|---------------------|----------------------|--------------|-------------------|
| **GPT-4o** | 49 | 51 | **49.0%** | 50% |
| **Gemini-2.0-Flash** | 50 | 50 | **50.0%** | 50% |
| **Qwen-Plus** | 48 | 52 | **48.0%** | 50% |
| **Average** | 49 | 51 | **49.0%** | 50% |

**Catatan**: Baseline = 50% karena distribusi ground truth hampir seimbang (51% sehat, 49% sakit).

#### Observasi Kunci

1. **⚠️ Akurasi di Chance Level**:
   - GPT-4o: 49% (1% di bawah random guessing)
   - Gemini: 50% (sama dengan random guessing)
   - Qwen: 48% (2% di bawah random guessing)
   - **Tidak ada model yang significantly better than chance**

2. **Consistency-Accuracy Dissociation**:
   - **Consistency**: 99-100% (exceptional)
   - **Accuracy**: 48-50% (chance level)
   - **Gap**: ~50 percentage points
   - Model **consistently wrong**, bukan inconsistently wrong

3. **Tidak Ada Model Unggul**:
   - Perbedaan akurasi antar model: ≤ 2 percentage points
   - Semua model perform equally poor
   - Tidak ada "winner" dalam diagnostic accuracy

4. **Below Random di 2 dari 3 Model**:
   - GPT-4o dan Qwen sedikit worse than random
   - Menunjukkan possible **systematic bias**

**Interpretasi**:

Hasil ini sangat mengejutkan karena:
- Model LLM state-of-the-art yang telah proven di medical exams (USMLE scores 90%+)
- Namun perform **no better than random guessing** pada real diagnostic task
- Menunjukkan gap antara **exam knowledge** vs **clinical reasoning**

**Implikasi Kritis**:

⚠️ **High consistency does NOT guarantee accuracy**

Model dapat sangat reliable (consistent) tapi **not valid** (inaccurate). Ini adalah temuan utama penelitian yang menantang asumsi umum bahwa consistency = reliability = accuracy.

### 4.6.2 Confusion Matrix Analysis

Confusion matrix memberikan breakdown detail tentang tipe error yang dibuat model.

#### Confusion Matrix: GPT-4o

```
                    Predicted
                Positive  Negative
Actual   Pos       48        1        (49 actual positive)
         Neg       50        1        (51 actual negative)
```

| Metric | Value | Calculation |
|--------|-------|-------------|
| **True Positive (TP)** | 48 | Correctly predicted sick |
| **True Negative (TN)** | 1 | Correctly predicted healthy |
| **False Positive (FP)** | 50 | Predicted sick, actually healthy |
| **False Negative (FN)** | 1 | Predicted healthy, actually sick |
| **Total** | 100 | - |

**Derived Metrics**:
- **Accuracy**: (48+1)/100 = **49.0%**
- **Sensitivity (Recall)**: 48/49 = **97.96%** (excellent at detecting disease)
- **Specificity**: 1/51 = **1.96%** (terrible at identifying healthy)
- **Precision**: 48/98 = **48.98%** (about half of positive predictions correct)
- **F1-Score**: 2×(0.4898×0.9796)/(0.4898+0.9796) = **0.6507**

#### Confusion Matrix: Gemini-2.0-Flash

```
                    Predicted
                Positive  Negative
Actual   Pos       49        0        (49 actual positive)
         Neg       50        1        (51 actual negative)
```

| Metric | Value | Calculation |
|--------|-------|-------------|
| **True Positive (TP)** | 49 | Correctly predicted sick |
| **True Negative (TN)** | 1 | Correctly predicted healthy |
| **False Positive (FP)** | 50 | Predicted sick, actually healthy |
| **False Negative (FN)** | 0 | Predicted healthy, actually sick |
| **Total** | 100 | - |

**Derived Metrics**:
- **Accuracy**: (49+1)/100 = **50.0%**
- **Sensitivity (Recall)**: 49/49 = **100.0%** (perfect detection, caught all disease)
- **Specificity**: 1/51 = **1.96%** (almost zero specificity)
- **Precision**: 49/99 = **49.49%** (half of positive predictions correct)
- **F1-Score**: 2×(0.4949×1.0)/(0.4949+1.0) = **0.6615**

#### Confusion Matrix: Qwen-Plus

```
                    Predicted
                Positive  Negative
Actual   Pos       48        1        (49 actual positive)
         Neg       51        0        (51 actual negative)
```

| Metric | Value | Calculation |
|--------|-------|-------------|
| **True Positive (TP)** | 48 | Correctly predicted sick |
| **True Negative (TN)** | 0 | Correctly predicted healthy |
| **False Positive (FP)** | 51 | Predicted sick, actually healthy |
| **False Negative (FN)** | 1 | Predicted healthy, actually sick |
| **Total** | 100 | - |

**Derived Metrics**:
- **Accuracy**: (48+0)/100 = **48.0%**
- **Sensitivity (Recall)**: 48/49 = **97.96%** (excellent at detecting disease)
- **Specificity**: 0/51 = **0.0%** (zero specificity, never identifies healthy)
- **Precision**: 48/99 = **48.48%** (less than half correct)
- **F1-Score**: 2×(0.4848×0.9796)/(0.4848+0.9796) = **0.6477**

### 4.6.3 Pattern Analisis: Systematic Over-Diagnosis Bias

#### Tabel Ringkasan Error Pattern

| Model | TP | TN | FP | FN | FP:FN Ratio |
|-------|----|----|----|----|-------------|
| **GPT-4o** | 48 | 1 | 50 | 1 | **50:1** |
| **Gemini-2.0-Flash** | 49 | 1 | 50 | 0 | **∞ (50:0)** |
| **Qwen-Plus** | 48 | 0 | 51 | 1 | **51:1** |
| **Average** | 48.3 | 0.7 | 50.3 | 0.7 | **~71:1** |

#### Observasi Kritis

1. **⚠️ Extreme Over-Diagnosis Bias**:
   - **False Positives**: 50-51 (almost all healthy patients misclassified)
   - **False Negatives**: 0-1 (almost no sick patients missed)
   - **Ratio FP:FN ≈ 50:1** - extremely skewed

2. **Near-Zero True Negatives**:
   - GPT-4o: TN=1 (only 1 healthy correctly identified)
   - Gemini: TN=1 (only 1 healthy correctly identified)
   - Qwen: TN=0 (**zero healthy correctly identified**)
   - **Models almost never predict "healthy"**

3. **Near-Perfect Sensitivity, Near-Zero Specificity**:
   - Sensitivity (detect disease): 98-100%
   - Specificity (identify healthy): 0-2%
   - **Massive imbalance** in performance

4. **Uniform Pattern Across All Models**:
   - All three models exhibit **identical bias pattern**
   - Not model-specific, appears to be **systematic**

**Interpretasi**:

Pola ini menunjukkan bahwa model LLM memiliki **strong prior belief** bahwa pasien dengan parameter kardiovaskular abnormal = sakit jantung. Model gagal mengenali bahwa:
- Banyak orang dengan faktor risiko tidak sakit
- False positive rate sangat tinggi di real-world screening
- Over-diagnosis adalah masalah serius dalam kedokteran

**Perbandingan dengan Klinisi**:

Klinisi yang baik seharusnya:
- Sensitivity ~80-90% (catch most disease, tapi tidak semua)
- Specificity ~70-80% (identify most healthy, avoid false alarm)
- **Balance** antara mendeteksi penyakit dan menghindari over-diagnosis

Model LLM:
- Sensitivity ~100% (catch ALL disease)
- Specificity ~0% (call almost EVERYONE sick)
- **Tidak ada balance** - lebih mirip "paranoid screener" daripada clinical decision maker

### 4.6.4 Precision, Recall, dan F1-Score

Ringkasan metrik evaluasi untuk semua model:

| Model | Precision | Recall (Sensitivity) | F1-Score | Interpretation |
|-------|-----------|----------------------|----------|----------------|
| **GPT-4o** | 48.98% | 97.96% | 0.6507 | High recall, very low precision |
| **Gemini-2.0-Flash** | 49.49% | 100.0% | 0.6615 | Perfect recall, low precision |
| **Qwen-Plus** | 48.48% | 97.96% | 0.6477 | High recall, very low precision |
| **Average** | 48.98% | 98.64% | 0.6533 | Extremely imbalanced |

#### Analisis Metrics

**Precision (~49%)**:
- Hanya sekitar **setengah dari prediksi "sakit" yang benar**
- **50% false alarm rate** - sangat tinggi untuk aplikasi medis
- Banyak pasien sehat akan didiagnosis sakit

**Recall (~99%)**:
- **Near-perfect disease detection**
- Hampir tidak ada sick patients yang missed
- Excellent sensitivity jika goal adalah screening

**F1-Score (~0.65)**:
- Harmonic mean dari precision dan recall
- Moderate score (0.65/1.0)
- Didorong tinggi oleh recall yang sangat tinggi
- **Tidak mencerminkan imbalance** - precision sangat rendah masih menghasilkan F1 moderate

**Trade-off Analisis**:

Dalam konteks medis:
- **High recall important untuk screening**: Don't miss disease
- **High precision important untuk diagnosis**: Don't over-treat

Model LLM:
- ✅ Cocok untuk **initial screening** (high sensitivity)
- ❌ Tidak cocok untuk **final diagnosis** (low specificity)
- Memerlukan **follow-up testing** untuk confirm positive results

**Kesimpulan Bagian 4.6**:

1. **Akurasi di chance level** (48-50%) - tidak better than random
2. **Extreme over-diagnosis bias** - FP:FN ratio ~50:1
3. **Near-zero specificity** (0-2%) - gagal identify healthy patients
4. **Pattern uniform** across all three models - systematic issue

**Next**: Analisis prompt comparison dan inter-model agreement (Bagian 4.7)

---

**[Lanjut ke BAGIAN 3: Analisis Prompt dan Inter-Model Agreement]**
