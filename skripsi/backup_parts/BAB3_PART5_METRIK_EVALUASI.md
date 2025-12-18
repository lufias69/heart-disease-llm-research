# BAB 3 - METODOLOGI PENELITIAN
## BAGIAN 5: METRIK EVALUASI

---

## 3.9 Metrik Evaluasi

Penelitian ini menggunakan berbagai metrik evaluasi untuk mengukur tiga aspek utama: **konsistensi intra-model**, **akurasi diagnostik**, dan **agreement inter-model**. Setiap metrik dirancang untuk menjawab pertanyaan penelitian spesifik tentang reliability dan validity LLM dalam diagnosis medis.

### 3.9.1 Intra-Model Consistency

**Intra-model consistency** mengukur seberapa konsisten sebuah model memberikan prediksi yang sama ketika diberikan input identik pada waktu berbeda. Ini adalah metrik utama untuk menilai **reproducibility** dan **reliability** model.

#### Definisi Konseptual

Konsistensi intra-model mengukur tingkat agreement antara multiple runs dari model yang sama pada kasus yang sama:

- **Konsistensi Tinggi**: Model selalu (atau hampir selalu) memberikan prediksi sama → Reliable
- **Konsistensi Rendah**: Model memberikan prediksi berbeda antar runs → Unreliable

#### Metrik 1: Consistency Score per Kasus

Untuk setiap kasus $i$, consistency score dihitung sebagai proporsi prediksi yang sama dengan majority vote:

$$C(i) = \frac{\max(\text{count}(p_{i1}, p_{i2}, p_{i3}, p_{i4}))}{4}$$

di mana:
- $C(i)$ = consistency score untuk kasus $i$
- $p_{ij}$ = prediksi run ke-$j$ untuk kasus $i$ ($j = 1, 2, 3, 4$)
- $\max(\text{count}(...))$ = jumlah prediksi terbanyak (majority count)

**Range**: 0.5 hingga 1.0
- **C(i) = 1.0**: Perfect consistency (4/4 agree) - semua run memberikan prediksi sama
- **C(i) = 0.75**: High consistency (3/4 agree) - mayoritas runs konsisten
- **C(i) = 0.5**: Low consistency (2/4 agree) - tidak ada mayoritas jelas

**Contoh Perhitungan**:

**Kasus 1**: Run1=Yes, Run2=Yes, Run3=Yes, Run4=Yes
- Count: Yes=4, No=0
- $C(1) = 4/4 = 1.0$ (Perfect consistency)

**Kasus 2**: Run1=Yes, Run2=Yes, Run3=Yes, Run4=No
- Count: Yes=3, No=1
- $C(2) = 3/4 = 0.75$ (High consistency)

**Kasus 3**: Run1=Yes, Run2=No, Run3=Yes, Run4=No
- Count: Yes=2, No=2
- $C(3) = 2/4 = 0.5$ (Low consistency)

**Interpretasi Klinis**:
- C=1.0: Model sangat reliable, diagnosis dapat dipercaya
- C=0.75: Model cukup reliable, tapi ada sedikit uncertainty
- C=0.5: Model tidak reliable, diagnosis tidak dapat dipercaya

#### Metrik 2: Average Consistency

Average consistency mengukur konsistensi keseluruhan model di semua kasus:

$$C_{avg} = \frac{1}{N} \sum_{i=1}^{N} C(i)$$

di mana:
- $C_{avg}$ = average consistency score
- $N$ = jumlah total kasus (100)
- $C(i)$ = consistency score kasus $i$

**Range**: 0.5 hingga 1.0

**Interpretasi**:
- $C_{avg} > 0.9$: Excellent consistency (model sangat reliable)
- $0.8 \leq C_{avg} \leq 0.9$: Good consistency (model reliable)
- $0.7 \leq C_{avg} < 0.8$: Moderate consistency (model cukup reliable)
- $C_{avg} < 0.7$: Poor consistency (model tidak reliable)

**Kegunaan**: Metrik tunggal untuk membandingkan reliability antar model.

#### Metrik 3: Perfect Consistency Rate (PCR)

Perfect Consistency Rate mengukur persentase kasus yang mencapai konsistensi sempurna:

$$\text{PCR} = \frac{\text{Jumlah kasus dengan } C(i) = 1.0}{N} \times 100\%$$

**Range**: 0% hingga 100%

**Interpretasi**:
- PCR = 100%: Semua kasus perfectly consistent
- PCR = 90%: 90 dari 100 kasus perfectly consistent
- PCR = 50%: Hanya setengah kasus yang consistent

**Contoh**:
Jika dari 100 kasus, 99 kasus memiliki C(i)=1.0:
$$\text{PCR} = \frac{99}{100} \times 100\% = 99\%$$

**Kegunaan**: Mengukur seberapa sering model "benar-benar consistent", bukan hanya rata-rata.

#### Metrik 4: Consistency Distribution

Distribusi consistency scores memberikan gambaran lengkap pola konsistensi:

| Consistency Score | Jumlah Kasus | Persentase |
|-------------------|--------------|------------|
| 1.00 (4/4 agree) | ? | ?% |
| 0.75 (3/4 agree) | ? | ?% |
| 0.50 (2/4 agree) | ? | ?% |

**Analisis**:
- Distribusi ideal: Mayoritas kasus di C=1.0
- Distribusi bermasalah: Banyak kasus di C=0.5

### 3.9.2 Diagnostic Accuracy Metrics

Setelah menghitung consistency score untuk setiap kasus, prediksi final ditentukan menggunakan **majority voting**. Prediksi final kemudian dibandingkan dengan ground truth untuk menghitung metrik akurasi.

#### Majority Voting

Untuk setiap kasus $i$, prediksi final adalah prediksi yang paling sering muncul:

$$P_{\text{final}}(i) = \text{mode}(p_{i1}, p_{i2}, p_{i3}, p_{i4})$$

di mana:
- $P_{\text{final}}(i)$ = prediksi final untuk kasus $i$
- $\text{mode}(...)$ = nilai yang paling sering muncul

**Contoh**:
- Runs: [Yes, Yes, Yes, No] → $P_{\text{final}}$ = Yes (muncul 3x)
- Runs: [No, No, No, Yes] → $P_{\text{final}}$ = No (muncul 3x)

**Tie Handling**: Jika tie (2-2), pilih randomly atau pilih "Yes" (conservative untuk diagnosis)

#### Confusion Matrix

Confusion matrix adalah tabel 2×2 yang membandingkan prediksi dengan ground truth:

```
                    Predicted
                Positive  Negative
Actual   Pos       TP        FN
         Neg       FP        TN
```

**Komponen**:
- **TP (True Positive)**: Prediksi "Sakit" dan benar sakit
- **TN (True Negative)**: Prediksi "Sehat" dan benar sehat
- **FP (False Positive)**: Prediksi "Sakit" tapi sebenarnya sehat (Type I Error)
- **FN (False Negative)**: Prediksi "Sehat" tapi sebenarnya sakit (Type II Error)

**Total Cases**:
$$N = \text{TP} + \text{TN} + \text{FP} + \text{FN} = 100$$

#### Metrik 1: Accuracy (Akurasi)

Accuracy mengukur proporsi prediksi yang benar dari total prediksi:

$$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}} \times 100\%$$

**Simplified**:
$$\text{Accuracy} = \frac{\text{Jumlah Prediksi Benar}}{\text{Total Prediksi}} \times 100\%$$

**Range**: 0% (semua salah) hingga 100% (semua benar)

**Interpretasi**:
- Accuracy = 100%: Perfect prediction
- Accuracy = 50%: Random guessing (baseline untuk binary classification)
- Accuracy < 50%: Worse than random (model biased)

**Contoh**:
Dari 100 kasus: TP=45, TN=43, FP=8, FN=4
$$\text{Accuracy} = \frac{45 + 43}{100} \times 100\% = 88\%$$

**Limitasi**: Accuracy bisa misleading jika data imbalanced.

#### Metrik 2: Sensitivity (Recall / True Positive Rate)

Sensitivity mengukur kemampuan model mendeteksi kasus positif (sakit):

$$\text{Sensitivity} = \frac{\text{TP}}{\text{TP} + \text{FN}} \times 100\%$$

**Interpretasi**:
- Dari semua pasien yang **benar-benar sakit**, berapa persen yang **terdeteksi** oleh model?
- Sensitivity tinggi = model jarang "miss" penyakit (FN rendah)
- Sensitivity rendah = model sering "miss" penyakit (FN tinggi)

**Range**: 0% hingga 100%

**Contoh**:
Total pasien sakit = 49 (TP + FN)
Model deteksi 48 (TP = 48, FN = 1)
$$\text{Sensitivity} = \frac{48}{48 + 1} \times 100\% = 97.96\%$$

**Kepentingan Klinis**: Sangat penting untuk diagnosis medis karena **missed diagnosis** (FN) bisa fatal.

**Trade-off**: Sensitivity tinggi sering disertai FP tinggi (over-diagnosis).

#### Metrik 3: Specificity (True Negative Rate)

Specificity mengukur kemampuan model mendeteksi kasus negatif (sehat):

$$\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}} \times 100\%$$

**Interpretasi**:
- Dari semua pasien yang **benar-benar sehat**, berapa persen yang **benar diidentifikasi sehat**?
- Specificity tinggi = model jarang "false alarm" (FP rendah)
- Specificity rendah = model sering "false alarm" (FP tinggi)

**Range**: 0% hingga 100%

**Contoh**:
Total pasien sehat = 51 (TN + FP)
Model identifikasi 2 sebagai sehat (TN = 2, FP = 49)
$$\text{Specificity} = \frac{2}{2 + 49} \times 100\% = 3.92\%$$

**Kepentingan Klinis**: Penting untuk menghindari over-diagnosis dan unnecessary treatment.

**Trade-off**: Specificity tinggi sering disertai FN tinggi (under-diagnosis).

#### Metrik 4: Precision (Positive Predictive Value / PPV)

Precision mengukur ketepatan prediksi positif:

$$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} \times 100\%$$

**Interpretasi**:
- Dari semua yang **diprediksi sakit**, berapa persen yang **benar-benar sakit**?
- Precision tinggi = prediksi "sakit" dapat dipercaya
- Precision rendah = banyak false alarm

**Range**: 0% hingga 100%

**Contoh**:
Model prediksi 97 pasien sakit (TP + FP)
Yang benar sakit hanya 48 (TP = 48, FP = 49)
$$\text{Precision} = \frac{48}{48 + 49} \times 100\% = 49.48\%$$

**Perbedaan dengan Sensitivity**:
- Sensitivity: "Dari yang sakit, berapa terdeteksi?"
- Precision: "Dari yang diprediksi sakit, berapa yang benar sakit?"

#### Metrik 5: F1-Score

F1-Score adalah harmonic mean dari Precision dan Recall (Sensitivity):

$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

**Alternative Formula**:
$$F_1 = \frac{2 \times \text{TP}}{2 \times \text{TP} + \text{FP} + \text{FN}}$$

**Range**: 0 (worst) hingga 1 (best)

**Interpretasi**:
- $F_1 = 1.0$: Perfect precision dan recall
- $F_1 = 0.7$: Good balance
- $F_1 < 0.5$: Poor performance

**Kegunaan**: Single metric yang menyeimbangkan precision dan recall.

**Contoh**:
Precision = 49.48%, Recall = 97.96%
$$F_1 = 2 \times \frac{0.4948 \times 0.9796}{0.4948 + 0.9796} = 0.656$$

**Mengapa Harmonic Mean?**
- Arithmetic mean: $(0.49 + 0.98)/2 = 0.735$ (terlalu tinggi, tidak mencerminkan imbalance)
- Harmonic mean: Lebih sensitif terhadap nilai rendah, memberikan penalty jika salah satu metrik buruk

### 3.9.3 Inter-Model Agreement

Inter-model agreement mengukur tingkat kesamaan prediksi antar model yang berbeda. Jika semua model sepakat, confidence terhadap prediksi lebih tinggi.

#### Metrik 1: Pairwise Agreement

Pairwise agreement mengukur persentase kasus di mana dua model memberikan prediksi sama:

$$A(M_1, M_2) = \frac{\text{Jumlah kasus dengan prediksi sama}}{N} \times 100\%$$

di mana:
- $M_1, M_2$ = dua model yang dibandingkan
- $N$ = total kasus (100)
- Prediksi sama = majority vote dari 4 runs sama

**Pasangan Model**:
1. GPT-4o vs Gemini-2.0-Flash
2. GPT-4o vs Qwen-Plus
3. Gemini-2.0-Flash vs Qwen-Plus

**Range**: 0% hingga 100%

**Interpretasi**:
- Agreement > 90%: Sangat tinggi (model hampir selalu sepakat)
- Agreement 70-90%: Tinggi (model sering sepakat)
- Agreement < 70%: Rendah (model sering berbeda pendapat)

**Contoh**:
GPT dan Gemini sepakat pada 98 dari 100 kasus:
$$A(\text{GPT}, \text{Gemini}) = \frac{98}{100} \times 100\% = 98\%$$

#### Metrik 2: Cohen's Kappa (κ)

Cohen's Kappa mengukur inter-rater agreement dengan mempertimbangkan chance agreement:

$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

di mana:
- $p_o$ = observed agreement (proporsi agreement aktual)
- $p_e$ = expected agreement by chance (agreement yang diharapkan secara random)

**Perhitungan $p_o$**:
$$p_o = \frac{\text{TP} + \text{TN}}{N}$$

**Perhitungan $p_e$**:
$$p_e = \frac{(a_1 + b_1)(a_1 + b_2) + (a_2 + b_1)(a_2 + b_2)}{N^2}$$

di mana $a_1, a_2, b_1, b_2$ adalah marginal totals dari confusion matrix

**Range**: -1 hingga +1

**Interpretasi (Landis & Koch, 1977)**:
| Kappa Value | Interpretation |
|-------------|----------------|
| < 0 | No agreement (worse than chance) |
| 0.01 - 0.20 | Slight agreement |
| 0.21 - 0.40 | Fair agreement |
| 0.41 - 0.60 | Moderate agreement |
| 0.61 - 0.80 | Substantial agreement |
| 0.81 - 1.00 | Almost perfect agreement |

**Keunggulan**: Lebih robust daripada simple agreement karena mengoreksi chance agreement.

**Contoh**:
Jika dua model sepakat 98%, tapi chance agreement 50%:
$$\kappa = \frac{0.98 - 0.50}{1 - 0.50} = \frac{0.48}{0.50} = 0.96$$
(Almost perfect agreement)

#### Metrik 3: Three-Way Agreement

Three-way agreement mengukur consensus dari ketiga model:

$$A_{3\text{-way}} = \frac{\text{Jumlah kasus ketiga model sepakat}}{N} \times 100\%$$

**Range**: 0% hingga 100%

**Interpretasi**:
- $A_{3\text{-way}} = 100\%$: Complete consensus
- $A_{3\text{-way}} = 95\%$: High consensus (sangat baik)
- $A_{3\text{-way}} < 80\%$: Low consensus (model divergent)

**Kegunaan**: Mengidentifikasi kasus "controversial" di mana model tidak sepakat.

### 3.9.4 Prompt Sensitivity Analysis

Prompt sensitivity mengukur seberapa besar perubahan prompt mempengaruhi prediksi model.

#### Metrik 1: Prediction Change Rate (PCR)

Prediction Change Rate mengukur persentase kasus yang prediksinya berubah ketika prompt diubah:

$$\text{PCR} = \frac{\text{Jumlah kasus dengan prediksi berbeda}}{N} \times 100\%$$

di mana "prediksi berbeda" = majority vote Prompt A ≠ Prompt B

**Range**: 0% hingga 100%

**Interpretasi**:
- PCR = 0%: Tidak sensitif sama sekali (robust)
- PCR < 5%: Sangat robust
- PCR = 10-20%: Moderately sensitive
- PCR > 30%: Highly sensitive (problematic)

**Kegunaan**: Mengukur robustness model terhadap prompt engineering.

#### Metrik 2: Consistency Change

Membandingkan consistency score antara dua prompt:

$$\Delta C = C_{\text{avg}}(\text{Prompt B}) - C_{\text{avg}}(\text{Prompt A})$$

**Interpretasi**:
- $\Delta C > 0$: Prompt B lebih konsisten
- $\Delta C < 0$: Prompt A lebih konsisten
- $|\Delta C| < 0.05$: Tidak ada perbedaan signifikan

### 3.9.5 Consistency-Accuracy Gap

Metrik novel untuk mengukur dissociation antara consistency dan accuracy:

$$\text{Gap} = C_{\text{avg}} - \text{Accuracy}$$

**Range**: -1.0 hingga +1.0

**Interpretasi**:
- Gap ≈ 0: Consistency selaras dengan accuracy (ideal)
- Gap > 0: **High consistency, low accuracy** (consistently wrong)
- Gap < 0: High accuracy, low consistency (lucky but unreliable)

**Contoh**:
Model dengan $C_{\text{avg}} = 99\%$ dan Accuracy = 50%:
$$\text{Gap} = 0.99 - 0.50 = 0.49 \text{ (49 percentage points)}$$

Ini menunjukkan model **sangat konsisten tapi tidak akurat** - selalu memberikan jawaban sama, tapi jawaban tersebut salah.

---

## 3.10 Analisis Statistik

### 3.10.1 Uji Signifikansi

Untuk menentukan apakah perbedaan antar model signifikan secara statistik:

**McNemar's Test**: Membandingkan dua model pada dataset yang sama
- H₀: Tidak ada perbedaan antara kedua model
- H₁: Ada perbedaan signifikan
- Significance level: α = 0.05

**Wilcoxon Signed-Rank Test**: Membandingkan consistency scores antar model
- Non-parametric test untuk paired samples
- H₀: Median consistency sama
- H₁: Median consistency berbeda

### 3.10.2 Confidence Intervals

Untuk setiap metrik, hitung 95% confidence interval menggunakan bootstrap:

$$\text{CI}_{95\%} = [\text{metric} - 1.96 \times \text{SE}, \text{metric} + 1.96 \times \text{SE}]$$

di mana SE = standard error dari bootstrap resampling (1000 iterations)

---

## 3.11 Rangkuman Metodologi

**Alur Penelitian Lengkap**:

1. **Data Preparation**:
   - UCI Heart Disease dataset (303 pasien)
   - Preprocessing dan normalisasi

2. **Clustering**:
   - K-Means dengan K=2-10 evaluation
   - K=2 selected (Silhouette Score tertinggi)

3. **Sampling**:
   - Stratified diverse sampling
   - 50 per cluster = 100 test cases

4. **LLM Testing**:
   - 3 models: GPT-4o, Gemini-2.0-Flash, Qwen-Plus
   - 2 prompts: Expert vs Neutral
   - 4 runs per kombinasi
   - Total: 2,400 predictions

5. **Evaluation**:
   - Intra-model consistency
   - Diagnostic accuracy
   - Inter-model agreement
   - Prompt sensitivity
   - Consistency-accuracy gap

**Total Metrik**: 15+ metrik evaluasi komprehensif untuk analisis mendalam.

---

**Akhir BAB 3 - METODOLOGI PENELITIAN**
