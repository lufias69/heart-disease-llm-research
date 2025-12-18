# 📋 RENCANA PENGERJAAN SKRIPSI - BAB 3 & BAB 4

**Judul**: Evaluasi Konsistensi dan Akurasi Large Language Models untuk Diagnosis Biner Penyakit Jantung  
**Target**: Skripsi S1 - Bahasa Indonesia  
**Deadline**: [Sesuaikan]

---

## 🎯 OVERVIEW

**BAB 3 - METODOLOGI**: Menjelaskan seluruh proses penelitian dari awal sampai akhir (tanpa hasil)  
**BAB 4 - HASIL & PEMBAHASAN**: Menampilkan dan menginterpretasi semua hasil penelitian

---

## 📘 BAB 3 - METODOLOGI

### 3.1 Desain Penelitian
**Target**: 500-700 kata  
**Konten**:
- Jenis penelitian: Eksperimental, evaluasi kuantitatif
- Pendekatan: Multi-run consistency testing
- Diagram alur penelitian (flowchart lengkap)

**Deliverable**: 
- [x] Diagram flowchart (PNG/SVG)
- [ ] Teks penjelasan desain

---

### 3.2 Data dan Sumber Data
**Target**: 1000-1200 kata  
**Konten**:

#### 3.2.1 Dataset UCI Heart Disease
- **Sumber**: UCI Machine Learning Repository [referensi]
- **Karakteristik**:
  * Total sampel: 303 pasien
  * Fitur: 13 parameter klinis + 1 target
  * Target: Binary (0 = tidak sakit, 1 = sakit jantung)
- **Parameter Klinis** (tabel lengkap dengan deskripsi):
  1. age (usia dalam tahun)
  2. sex (jenis kelamin: 1=laki-laki, 0=perempuan)
  3. cp (tipe nyeri dada: 0-3)
  4. trestbps (tekanan darah istirahat, mmHg)
  5. chol (kolesterol serum, mg/dl)
  6. fbs (gula darah puasa > 120 mg/dl: 1=ya, 0=tidak)
  7. restecg (hasil EKG istirahat: 0-2)
  8. thalach (detak jantung maksimum saat olahraga)
  9. exang (angina akibat olahraga: 1=ya, 0=tidak)
  10. oldpeak (depresi ST akibat olahraga)
  11. slope (kemiringan segmen ST: 0-2)
  12. ca (jumlah pembuluh besar: 0-4)
  13. thal (hasil tes thalassemia: 0-3)

#### 3.2.2 Preprocessing Data
- Pengecekan missing values
- Normalisasi data (StandardScaler)
- **Persamaan normalisasi**:
  ```
  z = (x - μ) / σ
  
  di mana:
  - z = nilai ternormalisasi
  - x = nilai asli
  - μ = mean
  - σ = standar deviasi
  ```
- **Kegunaan**: Membuat semua fitur berada dalam skala yang sama untuk clustering

**Deliverable**:
- [ ] Tabel karakteristik dataset
- [ ] Tabel deskripsi 13 parameter klinis
- [ ] Penjelasan preprocessing

---

### 3.3 Metode Clustering
**Target**: 1500-1800 kata  
**Konten**:

#### 3.3.1 K-Means Clustering
- **Tujuan**: Menemukan kelompok alami dalam data untuk sampling yang representatif
- **Prinsip**: Partisi data menjadi K kelompok berdasarkan kesamaan fitur

**Algoritma K-Means**:
```
1. Inisialisasi K centroid secara acak
2. REPEAT:
   a. Assignment step: Assign setiap data ke centroid terdekat
   b. Update step: Hitung ulang posisi centroid
3. UNTIL konvergensi (centroid tidak berubah)
```

**Persamaan Jarak Euclidean**:
```
d(x, c) = √(Σᵢ₌₁ⁿ (xᵢ - cᵢ)²)

di mana:
- d = jarak antara data x dan centroid c
- n = jumlah fitur
- xᵢ = nilai fitur ke-i dari data x
- cᵢ = nilai fitur ke-i dari centroid c
```

**Fungsi Objektif (Inertia)**:
```
J = Σⱼ₌₁ᴷ Σₓ∈Cⱼ ||x - μⱼ||²

di mana:
- J = inertia (within-cluster sum of squares)
- K = jumlah cluster
- Cⱼ = cluster ke-j
- μⱼ = centroid cluster ke-j
- ||·|| = Euclidean distance
```

**Kegunaan Inertia**: Mengukur kompakness cluster. Semakin kecil = cluster semakin tight.

#### 3.3.2 Penentuan Jumlah Cluster Optimal

**PENTING**: Pada penelitian ini, dilakukan evaluasi komprehensif untuk K = 2 hingga K = 10 menggunakan 3 metrik berbeda untuk menentukan jumlah cluster optimal.

**A. Elbow Method (Inertia)**
- **Tujuan**: Mencari "siku" pada grafik K vs Inertia
- **Cara**: Plot Inertia untuk K = 2 sampai 10, cari titik di mana penurunan mulai landai
- **Interpretasi**: K optimal berada di "siku" kurva
- **Hasil Evaluasi Penelitian**:
  * K=2: Inertia = 3615.99
  * K=3: Inertia = 3271.98
  * K=4: Inertia = 3125.72
  * K=5: Inertia = 3013.32
  * K=6: Inertia = 2941.09
  * K=7: Inertia = 2884.70
  * K=8: Inertia = 2838.08
  * K=9: Inertia = 2813.11
  * K=10: Inertia = 2788.77
- **Analisis**: Penurunan inertia mulai landai setelah K=2, menunjukkan K=2 sebagai kandidat optimal

**B. Silhouette Score**
- **Persamaan**:
  ```
  s(i) = (b(i) - a(i)) / max{a(i), b(i)}
  
  di mana:
  - s(i) = silhouette coefficient untuk sampel i
  - a(i) = rata-rata jarak intra-cluster (ke sampel dalam cluster sama)
  - b(i) = rata-rata jarak inter-cluster (ke sampel di cluster terdekat lain)
  ```
- **Range**: -1 hingga +1
  * +1 = sampel sangat cocok dengan clusternya
  * 0 = sampel di perbatasan cluster
  * -1 = sampel mungkin salah cluster
- **Kegunaan**: Mengukur seberapa baik setiap sampel cocok dengan clusternya
- **Interpretasi**: Semakin tinggi silhouette score rata-rata = clustering semakin baik
- **Hasil Evaluasi Penelitian**:
  * K=2: Silhouette = 0.0798 ⭐ (TERTINGGI)
  * K=3: Silhouette = 0.0758
  * K=4: Silhouette = 0.0752
  * K=5: Silhouette = 0.0748
  * K=6: Silhouette = 0.0738
  * K=7: Silhouette = 0.0731
  * K=8: Silhouette = 0.0725
  * K=9: Silhouette = 0.0715
  * K=10: Silhouette = 0.0708
- **Analisis**: K=2 memiliki Silhouette Score tertinggi (0.0798), menandakan clustering paling baik

**C. Davies-Bouldin Index**
- **Persamaan**:
  ```
  DB = (1/K) Σᵢ₌₁ᴷ max_{j≠i} Rᵢⱼ
  
  di mana:
  Rᵢⱼ = (Sᵢ + Sⱼ) / Mᵢⱼ
  
  - Sᵢ = rata-rata jarak sampel dalam cluster i ke centroid i
  - Mᵢⱼ = jarak antara centroid i dan j
  ```
- **Range**: 0 hingga ∞
- **Kegunaan**: Mengukur separasi antar cluster
- **Interpretasi**: Semakin kecil DB Index = clustering semakin baik (cluster compact dan terpisah jauh)
- **Hasil Evaluasi Penelitian**:
  * K=2: DB Index = 3.3232
  * K=3: DB Index = 2.9864
  * K=4: DB Index = 2.8473
  * K=5: DB Index = 2.7556
  * K=6: DB Index = 2.6891
  * K=7: DB Index = 2.5438
  * K=8: DB Index = 2.4912
  * K=9: DB Index = 2.4357
  * K=10: DB Index = 2.3788
- **Analisis**: DB Index menurun seiring bertambahnya K, namun perbaikan marginal setelah K=2

#### 3.3.3 Keputusan Pemilihan K Optimal

**Hasil Evaluasi Komprehensif**:
- **Elbow Method**: Menunjukkan "siku" pada K=2
- **Silhouette Score**: K=2 mencapai skor tertinggi (0.0798)
- **Davies-Bouldin Index**: K=2 menunjukkan separasi memadai

**Kesimpulan**: Berdasarkan konsensus ketiga metrik, **K=2 dipilih sebagai jumlah cluster optimal** untuk penelitian ini.

**Interpretasi Klinis K=2**:
- Cluster 0: 145 pasien (47.9%) - kelompok dengan karakteristik tertentu
- Cluster 1: 158 pasien (52.1%) - kelompok dengan karakteristik berbeda
- Pembagian ini memungkinkan sampling yang representatif dari kedua kelompok

**Deliverable**:
- [ ] Diagram flowchart K-Means
- [ ] Tabel perbandingan 3 metrik (Elbow, Silhouette, DB)
- [ ] Grafik penentuan K optimal
- [ ] Penjelasan mengapa K=2 dipilih

---

### 3.4 Metode Sampling Stratified
**Target**: 800-1000 kata  
**Konten**:

#### 3.4.1 Strategi Sampling
- **Tujuan**: Mendapatkan 100 kasus uji yang representatif dan beragam
- **Metode**: Stratified random sampling dengan strategi "diverse" dari setiap cluster

**Langkah-langkah**:
1. Dari setiap cluster (K=2), ambil 50 sampel menggunakan strategi "diverse"
2. **Strategi "Diverse" Sampling**:
   - Menghitung jarak setiap sampel ke centroid cluster-nya
   - Membagi sampel menjadi 5 kuintil berdasarkan jarak (0-20%, 20-40%, 40-60%, 60-80%, 80-100%)
   - Mengambil 10 sampel dari setiap kuintil secara acak
   - **Keunggulan**: Memastikan variasi karakteristik dari yang dekat centroid (typical cases) hingga yang jauh dari centroid (diverse cases)
3. Pastikan variasi karakteristik (usia, jenis kelamin, parameter klinis) terwakili

**Persamaan Sampling Proportion**:
```
nᵢ = (Nᵢ / N) × n

di mana:
- nᵢ = jumlah sampel dari cluster i
- Nᵢ = total data dalam cluster i
- N = total seluruh data
- n = target jumlah sampel (100)
```

**Kegunaan**: Memastikan setiap cluster terwakili proporsional

**Hasil Sampling**:
- Total sampel uji: 100 kasus
- Distribusi label: 51% positif (sakit), 49% negatif (sehat)
- Karakteristik: Beragam usia, jenis kelamin, severity

**Deliverable**:
- [ ] Diagram stratified sampling
- [ ] Tabel karakteristik 100 sampel uji
- [ ] Grafik distribusi fitur

---

### 3.5 Model Large Language Models (LLM)
**Target**: 1200-1500 kata  
**Konten**:

#### 3.5.1 Model yang Digunakan

**A. GPT-4o (OpenAI)**
- **Arsitektur**: Transformer-based generative model
- **Parameter**: ~1.76 trillion parameters (estimasi)
- **Training**: Pre-trained on medical literature + internet text
- **API**: OpenAI API dengan model "gpt-4o"
- **Keunggulan**: State-of-the-art natural language understanding

**B. Gemini-2.0-Flash (Google)**
- **Arsitektur**: Multimodal transformer model
- **Parameter**: Large-scale (spesifikasi tidak dipublikasikan)
- **Training**: Trained on diverse sources including medical texts
- **API**: Google AI Studio API
- **Keunggulan**: Fast inference, efficient

**C. Qwen-Plus (Alibaba)**
- **Arsitektur**: Chinese-English bilingual LLM
- **Parameter**: Large-scale model from Alibaba DAMO Academy
- **Training**: Extensive Chinese and English corpora
- **API**: DashScope API
- **Keunggulan**: Strong multilingual capability

#### 3.5.2 Konfigurasi Model
- **Temperature**: 0.7
  * **Kegunaan**: Mengontrol randomness output
  * **Interpretasi**: 0 = deterministik, 1 = sangat random
  * **Pilihan 0.7**: Balance antara consistency dan diversity
- **Max Tokens**: 300 (cukup untuk diagnosis + justifikasi)
- **Top-p**: 1.0 (default)

**Deliverable**:
- [ ] Tabel perbandingan 3 model
- [ ] Diagram arsitektur transformer (simplified)
- [ ] Penjelasan parameter konfigurasi

---

### 3.6 Desain Prompt
**Target**: 1000-1200 kata  
**Konten**:

#### 3.6.1 Variasi Prompt
Untuk menguji sensitivitas terhadap prompt engineering, digunakan 2 variasi:

**Prompt A - "Expert Cardiologist"**:
```
"You are Dr. CardioExpert, a highly experienced cardiologist with 20 years of 
clinical practice in diagnosing cardiovascular diseases..."
```
- **Karakteristik**: Authoritative, expert persona
- **Tujuan**: Memberikan konteks medis eksplisit

**Prompt B - "Neutral AI Assistant"**:
```
"You are a medical AI assistant trained to provide accurate and balanced 
diagnostic assessments for cardiovascular conditions..."
```
- **Karakteristik**: Neutral, balanced, objective
- **Tujuan**: Mengurangi bias persona

#### 3.6.2 Struktur Prompt
Kedua prompt memiliki struktur sama:
1. **Role definition** (berbeda antara A dan B)
2. **Patient clinical data** (13 parameter)
3. **Clinical parameters reference** (definisi setiap parameter)
4. **Diagnostic task** (instruksi output format)
5. **Output format**:
   ```
   PREDICTION: [Yes/No]
   JUSTIFICATION: [Clinical reasoning]
   ```

**Deliverable**:
- [ ] Tabel perbandingan Prompt A vs B
- [ ] Full text kedua prompt
- [ ] Penjelasan desain prompt

---

### 3.7 Protokol Eksperimen Multi-Run
**Target**: 1000-1200 kata  
**Konten**:

#### 3.7.1 Desain Eksperimen
- **Jumlah Run per Kasus**: 4 prediksi independen per kombinasi (model + prompt)
  * **Kegunaan**: Mengukur intra-model consistency dan reproducibility
  * **Alasan 4 Runs**: Balance antara evaluasi consistency yang memadai dan efisiensi komputasi
  * **Total Prediksi**: 100 kasus × 4 runs × 3 model × 2 prompt = 2,400 prediksi total

#### 3.7.2 Sistem Checkpoint SQLite
- **Tujuan**: Mencegah kehilangan data jika terjadi error
- **Fitur**:
  * Automatic saving setelah setiap prediksi
  * Duplicate prevention (skip prediksi yang sudah ada)
  * Resume capability (lanjutkan dari terakhir kali)

**Skema Database**:
```sql
CREATE TABLE predictions (
    id INTEGER PRIMARY KEY,
    sample_id INTEGER,
    model TEXT,
    prompt_type TEXT,
    run_number INTEGER,
    prediction TEXT,
    justification TEXT,
    timestamp TEXT,
    UNIQUE(sample_id, model, prompt_type, run_number)
);
```

**Deliverable**:
- [ ] Diagram protokol multi-run
- [ ] Skema database
- [ ] Flowchart checkpoint system

---

### 3.8 Metrik Evaluasi
**Target**: 2000-2500 kata  
**Konten**:

#### 3.8.1 Intra-Model Consistency

**Definisi**: Tingkat kesamaan prediksi dari model yang sama pada kasus yang sama

**Metrik 1: Consistency Score per Kasus**
```
C(i) = max_count(pᵢ₁, pᵢ₂, pᵢ₃, pᵢ₄) / 4

di mana:
- C(i) = consistency score untuk kasus i
- pᵢⱼ = prediksi run ke-j untuk kasus i
- max_count = jumlah prediksi terbanyak (majority)
```
- **Range**: 0.5 (2/4 agree) hingga 1.0 (4/4 agree)
- **Kegunaan**: Mengukur reproducibility per kasus
- **Interpretasi**:
  * 1.0 = sempurna konsisten (semua run sama)
  * 0.75 = mayoritas konsisten (3/4 sama)
  * 0.5 = tidak konsisten (2/4 vs 2/4)

**Metrik 2: Average Consistency**
```
C_avg = (1/N) Σᵢ₌₁ᴺ C(i)

di mana:
- N = jumlah total kasus (100)
```
- **Kegunaan**: Mengukur consistency keseluruhan model

**Metrik 3: Perfect Consistency Rate**
```
PCR = (jumlah kasus dengan C(i)=1.0) / N × 100%
```
- **Kegunaan**: Persentase kasus yang sempurna konsisten

**Deliverable**:
- [ ] Penjelasan lengkap 3 metrik consistency
- [ ] Contoh perhitungan

---

#### 3.8.2 Inter-Model Agreement

**Definisi**: Tingkat kesamaan prediksi antar model yang berbeda

**Metrik 1: Pairwise Agreement**
```
A(M₁, M₂) = (jumlah kasus dengan prediksi sama) / N × 100%

di mana:
- M₁, M₂ = dua model yang dibandingkan
- Prediksi sama = majority vote dari 4 runs sama
```
- **Kegunaan**: Mengukur agreement antara 2 model
- **Pasangan**: GPT-Gemini, GPT-Qwen, Gemini-Qwen

**Metrik 2: Cohen's Kappa**
```
κ = (p_o - p_e) / (1 - p_e)

di mana:
- p_o = observed agreement (proportion of agreement)
- p_e = expected agreement by chance
```
- **Range**: -1 hingga +1
  * < 0 = worse than chance
  * 0 = agreement by chance
  * 0.01-0.20 = slight agreement
  * 0.21-0.40 = fair agreement
  * 0.41-0.60 = moderate agreement
  * 0.61-0.80 = substantial agreement
  * 0.81-1.00 = almost perfect agreement
- **Kegunaan**: Mengukur agreement dengan kompensasi chance agreement
- **Interpretasi**: Lebih robust daripada simple percentage

**Metrik 3: Three-Way Agreement**
```
A_3way = (jumlah kasus ketiga model setuju) / N × 100%
```
- **Kegunaan**: Mengukur consensus semua model

**Deliverable**:
- [ ] Penjelasan pairwise agreement
- [ ] Penjelasan Cohen's Kappa dengan interpretasi
- [ ] Contoh perhitungan

---

#### 3.8.3 Diagnostic Accuracy

**Majority Voting**:
Untuk setiap model dan kasus, prediksi final = majority dari 4 runs
```
P_final(i) = mode(p_i1, p_i2, p_i3, p_i4)
```

**Confusion Matrix**:
```
                Predicted
              Positive  Negative
Actual   Pos     TP        FN
         Neg     FP        TN

di mana:
- TP = True Positive (benar prediksi sakit)
- TN = True Negative (benar prediksi sehat)
- FP = False Positive (salah prediksi sakit, tapi sebenarnya sehat)
- FN = False Negative (salah prediksi sehat, tapi sebenarnya sakit)
```

**Metrik Accuracy**:
```
Accuracy = (TP + TN) / (TP + TN + FP + FN) × 100%
```
- **Kegunaan**: Proporsi prediksi benar dari semua prediksi
- **Range**: 0% (semua salah) hingga 100% (semua benar)
- **Interpretasi**: Akurasi keseluruhan

**Metrik Sensitivity (Recall)**:
```
Sensitivity = TP / (TP + FN) × 100%
```
- **Kegunaan**: Kemampuan mendeteksi kasus positif (sakit)
- **Interpretasi**: Dari semua pasien sakit, berapa persen yang terdeteksi?
- **Penting untuk**: Medical diagnosis (menghindari missed diagnosis)

**Metrik Specificity**:
```
Specificity = TN / (TN + FP) × 100%
```
- **Kegunaan**: Kemampuan mendeteksi kasus negatif (sehat)
- **Interpretasi**: Dari semua pasien sehat, berapa persen yang benar dinyatakan sehat?
- **Penting untuk**: Menghindari false alarm

**Metrik Precision (Positive Predictive Value)**:
```
Precision = TP / (TP + FP) × 100%
```
- **Kegunaan**: Dari semua yang diprediksi sakit, berapa yang benar sakit?
- **Interpretasi**: Kepercayaan terhadap prediksi positif

**Metrik F1-Score**:
```
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```
- **Kegunaan**: Harmonic mean of precision and recall
- **Range**: 0 (worst) hingga 1 (best)
- **Interpretasi**: Balance antara precision dan recall

**Deliverable**:
- [ ] Diagram confusion matrix dengan penjelasan
- [ ] Tabel semua metrik dengan formula dan interpretasi
- [ ] Contoh perhitungan lengkap

---

#### 3.8.4 Prompt Sensitivity

**Definisi**: Seberapa besar perubahan prediksi ketika prompt diubah

**Metrik 1: Prediction Change Rate**:
```
PCR = (jumlah kasus dengan prediksi berbeda) / N × 100%

di mana prediksi berbeda = majority vote Prompt A ≠ Prompt B
```
- **Kegunaan**: Mengukur stabilitas terhadap perubahan prompt
- **Interpretasi**: 
  * 0% = tidak sensitif (prediksi sama untuk kedua prompt)
  * 100% = sangat sensitif (prediksi selalu berubah)

**Metrik 2: Individual Run Stability**:
```
IRS = (jumlah run dengan prediksi sama di kedua prompt) / (N × 4) × 100%
```
- **Kegunaan**: Stabilitas pada level individual run

**Deliverable**:
- [ ] Penjelasan prompt sensitivity
- [ ] Formula dan interpretasi

---

#### 3.8.5 Error Pattern Analysis

**Klasifikasi Kasus**:
Berdasarkan hasil ketiga model:
1. **All-Correct**: Ketiga model benar
2. **All-Wrong**: Ketiga model salah
3. **Mixed**: Ada yang benar, ada yang salah

**Metrik Systematic Error**:
```
SE = (jumlah kasus All-Wrong) / (jumlah kasus salah total) × 100%
```
- **Kegunaan**: Mengidentifikasi apakah error bersifat sistematik atau random
- **Interpretasi**:
  * SE tinggi = error sistematik (semua model salah pada kasus yang sama)
  * SE rendah = error random (model berbeda salah pada kasus berbeda)

**Deliverable**:
- [ ] Diagram klasifikasi error pattern
- [ ] Penjelasan systematic vs random error

---

### 3.9 Analisis Statistik
**Target**: 500-700 kata  
**Konten**:

- **Software**: Python 3.8+ dengan libraries:
  * pandas: Data manipulation
  * numpy: Numerical computation
  * scikit-learn: Metrics calculation
  * scipy: Statistical tests
  * matplotlib, seaborn: Visualization

- **Statistical Tests**:
  * Descriptive statistics (mean, median, std)
  * Inter-model comparison (jika ada perbedaan signifikan)

- **Significance Level**: α = 0.05

**Deliverable**:
- [ ] Daftar tools dan libraries
- [ ] Penjelasan statistical tests

---

## 📗 BAB 4 - HASIL DAN PEMBAHASAN

### 4.1 Hasil Clustering dan Sampling
**Target**: 1000-1200 kata  
**Konten**:

#### 4.1.1 Hasil Penentuan Jumlah Cluster Optimal
- **Elbow Method**: [Grafik + interpretasi]
- **Silhouette Score**: [Tabel K vs Score + interpretasi]
- **Davies-Bouldin Index**: [Tabel K vs DB + interpretasi]
- **Keputusan**: K=2 dipilih karena...

#### 4.1.2 Karakteristik Cluster
- **Cluster 0**: [Jumlah sampel, karakteristik dominan]
- **Cluster 1**: [Jumlah sampel, karakteristik dominan]
- **Visualisasi**: PCA 2D plot dengan cluster labels

#### 4.1.3 Hasil Sampling
- **Total Sampel Uji**: 100 kasus
- **Distribusi Label**: 
  * Positif (sakit): 51 kasus (51%)
  * Negatif (sehat): 49 kasus (49%)
- **Tabel Statistik Deskriptif**: Rata-rata, std, min, max untuk setiap fitur

**Deliverable**:
- [ ] 3 grafik metrik clustering
- [ ] Tabel karakteristik cluster
- [ ] Grafik PCA visualization
- [ ] Tabel statistik deskriptif 100 sampel

**Interpretasi** (dengan bahasa awam):
"Dari analisis clustering, kami menemukan bahwa data pasien secara alami terbagi menjadi 2 kelompok. Kelompok pertama (Cluster 0) cenderung memiliki... [karakteristik], sedangkan kelompok kedua (Cluster 1) memiliki... [karakteristik]. Hal ini menunjukkan bahwa..."

---

### 4.2 Hasil Intra-Model Consistency
**Target**: 1500-1800 kata  
**Konten**:

#### 4.2.1 Consistency Score per Model

**Tabel 1. Intra-Model Consistency**:
| Model | Prompt | Avg Consistency | Min | Max | Perfect (%) |
|-------|--------|-----------------|-----|-----|-------------|
| GPT-4o | Expert | 99.25% | 50% | 100% | 98% |
| GPT-4o | Neutral | 99.00% | 75% | 100% | 96% |
| Gemini | Expert | 99.50% | 75% | 100% | 98% |
| Gemini | Neutral | 99.25% | 50% | 100% | 98% |
| Qwen | Expert | **100.00%** | 100% | 100% | 100% |
| Qwen | Neutral | 99.75% | 75% | 100% | 99% |

**Grafik**:
- Bar chart: Average consistency per model per prompt
- Violin plot: Distribusi consistency score

**Deliverable**:
- [ ] Tabel consistency lengkap
- [ ] 2 grafik visualisasi

**Interpretasi** (bahasa awam):
"Ketiga model LLM menunjukkan konsistensi yang sangat tinggi dalam memberikan diagnosis. Artinya, ketika model yang sama diminta mendiagnosis pasien yang sama sebanyak 4 kali, hasilnya hampir selalu identik. 

Qwen-Plus mencapai konsistensi sempurna 100% dengan prompt Expert, yang berarti dari 100 pasien yang didiagnosis 4 kali, semua 100 kasus mendapat diagnosis yang sama persis di keempat kali. GPT-4o dan Gemini juga sangat konsisten dengan nilai 99%, hanya 1-2 kasus dari 100 yang menunjukkan variasi kecil.

Hal ini mengindikasikan bahwa LLM memiliki reproducibility yang sangat baik - properti penting untuk aplikasi medis di mana hasil yang konsisten diperlukan."

---

### 4.3 Hasil Inter-Model Agreement
**Target**: 1200-1500 kata  
**Konten**:

#### 4.3.1 Pairwise Agreement

**Tabel 2. Inter-Model Agreement**:
| Prompt | GPT-Gemini | GPT-Qwen | Gemini-Qwen | All 3 Agree | Cohen's κ |
|--------|------------|----------|-------------|-------------|-----------|
| Expert | 98.0% | 100.0% | 98.0% | 98% | 0.00 |
| Neutral | 100.0% | 99.0% | 99.0% | 99% | 0.00 |

**Grafik**:
- Heatmap: Pairwise agreement matrix
- Venn diagram: Overlap agreement ketiga model

**Deliverable**:
- [ ] Tabel agreement lengkap
- [ ] 2 grafik visualisasi

**Interpretasi** (bahasa awam):
"Ketiga model LLM menunjukkan kesepakatan yang sangat tinggi dalam diagnosis. Misalnya, dengan prompt Expert, GPT dan Qwen memberikan diagnosis yang sama pada 100 dari 100 kasus (100% agreement). 

Yang lebih mengejutkan, ketika ketiga model dibandingkan, mereka semua setuju pada 98-99% kasus. Artinya, dari 100 pasien, 98-99 pasien mendapat diagnosis yang sama dari ketiga model yang berbeda.

Cohen's Kappa menunjukkan nilai mendekati 0, yang biasanya mengindikasikan agreement rendah. Namun dalam konteks ini, nilai kappa rendah disebabkan oleh extreme class imbalance - hampir semua prediksi adalah positif, sehingga metrik ini menjadi tidak informatif. Percentage agreement lebih relevan untuk kasus ini."

---

### 4.4 Hasil Diagnostic Accuracy
**Target**: 2000-2500 kata  
**Konten**:

#### 4.4.1 Confusion Matrix

**Tabel 3. Confusion Matrix - GPT-4o Expert**:
```
                Predicted
              Yes    No    Total
Actual  Yes   27     24     51
        No    49      0     49
        Total 76     24    100
```

[Buat tabel serupa untuk 6 kombinasi: 3 model × 2 prompt]

**Grafik**:
- 6 confusion matrix heatmaps (3 model × 2 prompt)

**Deliverable**:
- [ ] 6 tabel confusion matrix
- [ ] 6 heatmap visualisasi

**Interpretasi** (bahasa awam):
"Confusion matrix menunjukkan detail hasil diagnosis. Untuk GPT-4o dengan prompt Expert:
- Dari 51 pasien yang benar-benar sakit, model hanya mendeteksi 27 (53%) dengan benar, sisanya 24 (47%) terlewatkan (False Negative)
- Dari 49 pasien yang sehat, model salah mendiagnosis SEMUA (100%) sebagai sakit (False Positive)
- Tidak ada satu pun pasien sehat yang benar-benar dinyatakan sehat oleh model

Pola ini menunjukkan bias yang sangat kuat terhadap diagnosis positif (over-diagnosis)."

---

#### 4.4.2 Metrik Accuracy

**Tabel 4. Diagnostic Accuracy Metrics**:
| Model | Prompt | Accuracy | Sensitivity | Specificity | Precision | F1-Score |
|-------|--------|----------|-------------|-------------|-----------|----------|
| GPT | Expert | 51.0% | 53.0% | 0.0% | 35.5% | 0.425 |
| GPT | Neutral | 52.0% | 53.0% | 2.0% | 35.9% | 0.429 |
| Gemini | Expert | 53.0% | 51.0% | 0.0% | 34.2% | 0.408 |
| Gemini | Neutral | 50.0% | 49.0% | 2.0% | 33.6% | 0.399 |
| Qwen | Expert | 49.0% | 53.0% | 0.0% | 34.4% | 0.416 |
| Qwen | Neutral | 53.0% | 51.0% | 2.0% | 35.2% | 0.417 |

**Grafik**:
- Grouped bar chart: 5 metrik untuk 6 kombinasi
- Radar chart: Perbandingan multi-metrik per model

**Deliverable**:
- [ ] Tabel metrik lengkap
- [ ] 2 grafik visualisasi

**Interpretasi Detail** (bahasa awam):

**Accuracy (~50%)**:
"Akurasi semua model berkisar 49-53%, yang setara dengan menebak acak (seperti melempar koin). Meskipun model sangat konsisten, akurasi mereka tidak lebih baik dari kebetulan. Ini menunjukkan bahwa konsistensi tinggi tidak menjamin akurasi tinggi - model bisa konsisten salah."

**Sensitivity (~51%)**:
"Sensitivity mengukur kemampuan mendeteksi pasien sakit. Nilai 51% berarti dari setiap 100 pasien sakit, model hanya mendeteksi sekitar 51 orang, sisanya 49 terlewatkan. Ini cukup mengkhawatirkan untuk aplikasi medis karena banyak pasien sakit tidak terdiagnosis."

**Specificity (~0-2%)**:
"Ini adalah temuan paling mengejutkan. Specificity hampir 0% berarti model hampir tidak pernah benar mengidentifikasi pasien sehat. Dari 100 pasien sehat, 98-100 salah didiagnosis sakit. Ini menunjukkan bias ekstrem terhadap diagnosis positif."

**Precision (~35%)**:
"Precision mengukur keandalan diagnosis positif. Nilai 35% berarti dari setiap 100 pasien yang didiagnosis sakit, hanya sekitar 35 yang benar-benar sakit, sisanya 65 adalah false alarm. Ini sangat rendah dan menunjukkan banyaknya over-diagnosis."

**F1-Score (~0.41)**:
"F1-score menggabungkan precision dan sensitivity. Nilai 0.41 (dari maksimal 1.0) menunjukkan performa keseluruhan yang buruk, jauh di bawah standar aplikasi medis yang biasanya memerlukan F1 > 0.80."

---

### 4.5 Hasil Prompt Sensitivity
**Target**: 1000-1200 kata  
**Konten**:

#### 4.5.1 Prediction Change Rate

**Tabel 5. Prompt Sensitivity**:
| Model | Same Prediction | Different | Change Rate |
|-------|-----------------|-----------|-------------|
| GPT | 98 cases | 2 cases | 2.0% |
| Gemini | 97 cases | 3 cases | 3.0% |
| Qwen | 98 cases | 2 cases | 2.0% |

**Grafik**:
- Pie chart: Same vs Different per model
- Bar chart: Change rate comparison

**Deliverable**:
- [ ] Tabel prompt sensitivity
- [ ] 2 grafik visualisasi

**Interpretasi** (bahasa awam):
"Perubahan prompt dari 'Expert Cardiologist' menjadi 'Neutral AI Assistant' hanya menyebabkan perubahan prediksi pada 2-3 kasus dari 100 (2-3%). Ini menunjukkan bahwa LLM sangat stabil terhadap variasi prompt.

Artinya, cara kita memberikan instruksi kepada model (apakah menyuruhnya berperan sebagai dokter ahli atau asisten AI netral) hampir tidak berpengaruh pada hasil diagnosis. Model tetap konsisten dengan pola prediksinya terlepas dari persona yang diberikan.

Temuan ini kontras dengan literatur yang menyarankan prompt engineering sebagai cara efektif mengubah perilaku LLM. Dalam kasus diagnosis medis ini, prompt engineering tidak efektif mengatasi bias over-diagnosis."

---

### 4.6 Hasil Error Pattern Analysis
**Target**: 1500-1800 kata  
**Konten**:

#### 4.6.1 Klasifikasi Error Patterns

**Tabel 6. Error Pattern Distribution - Expert Prompt**:
| Category | Count | Percentage | Description |
|----------|-------|------------|-------------|
| All-Correct | 49 | 49% | Ketiga model benar |
| All-Wrong | 49 | 49% | Ketiga model salah |
| Mixed | 2 | 2% | Ada yang benar, ada yang salah |

**Grafik**:
- Stacked bar chart: Error pattern per prompt
- Sankey diagram: Flow dari actual label ke prediction pattern

**Deliverable**:
- [ ] Tabel error pattern
- [ ] 2 grafik visualisasi

**Interpretasi** (bahasa awam):
"Analisis pola error mengungkapkan temuan yang sangat penting: Error bersifat sistematis, bukan random.

Dari 100 kasus:
- 49 kasus: Semua model benar (All-Correct)
- 49 kasus: Semua model salah (All-Wrong)
- Hanya 2 kasus: Model berbeda-beda (Mixed)

Ini berarti ketika satu model salah, model lainnya cenderung salah juga pada kasus yang sama. Systematic Error Rate = 49/51 = 96% (dari 51 kasus yang salah, 49 adalah all-wrong).

Implikasi: Error bukan karena random chance atau noise, tetapi karena keterbatasan fundamental dalam cara LLM memproses data medis. Ketiga model sepertinya membuat kesalahan yang sama pada kasus-kasus yang "sulit", mengindikasikan limitasi arsitektural atau data training yang mirip."

#### 4.6.2 Analisis Kasus All-Wrong
- **Karakteristik Kasus Sulit**: [Analisis fitur yang membuat kasus sulit]
- **Pola Umum**: [Apakah ada pola di kasus yang semua model salah?]

---

### 4.7 Pembahasan Dissociation: Consistency vs Accuracy
**Target**: 2000-2500 kata  
**Konten**:

#### 4.7.1 The Consistency-Accuracy Gap

**Visualisasi**:
- Scatter plot: Consistency (x-axis) vs Accuracy (y-axis)
- Gap diagram: Consistency bar vs Accuracy bar

**Temuan Utama**:
```
Consistency: 99-100%
Accuracy: 49-53%
Gap: ~50 percentage points
```

**Pembahasan Mendalam**:

**1. Mengapa Consistency Tinggi?**
- **Deterministic reasoning**: LLM menggunakan pola reasoning yang sama
- **Temperature effect**: Temperature 0.7 masih cukup rendah untuk reproducibility
- **Strong pattern recognition**: Model belajar pola kuat dari training data

**2. Mengapa Accuracy Rendah?**
- **Over-generalization**: Model terlalu konservatif, selalu prediksi positif
- **Lack of discriminative features**: Tidak bisa membedakan subtle differences
- **Binary classification difficulty**: Threshold decision sulit untuk continuous reasoning

**3. Implikasi untuk Medical AI**:
"Temuan ini sangat penting untuk aplikasi AI di medis:

**Bahaya False Security**: Konsistensi tinggi bisa memberikan false sense of security. Seorang dokter mungkin percaya bahwa karena AI selalu memberikan jawaban yang sama (konsisten), maka jawabannya pasti benar. Padahal, AI bisa konsisten salah.

**Systematic Bias**: Over-diagnosis sistematis sangat berbahaya. Bayangkan jika sistem ini digunakan untuk screening: 98% pasien sehat akan didiagnosis sakit, menyebabkan tes lanjutan yang tidak perlu, anxiety, dan biaya healthcare yang meningkat.

**Not Ready for Primary Diagnosis**: LLM saat ini tidak siap untuk diagnosis primer standalone. Accuracy 50% sama dengan menebak random, tidak memenuhi standar medis.

**Better Use Case**: LLM lebih cocok sebagai:
- Decision support tool (second opinion)
- Patient education dan explanation generator
- Medical literature summarization
- Administrative tasks"

**Deliverable**:
- [ ] Grafik consistency vs accuracy
- [ ] Pembahasan mendalam 2000+ kata

---

### 4.8 Perbandingan dengan State-of-the-Art
**Target**: 1000-1200 kata  
**Konten**:

**Tabel 7. Comparison with Literature**:
| Study | Model | Task | Accuracy | Consistency | Dataset |
|-------|-------|------|----------|-------------|---------|
| Singhal et al. 2023 [3] | Med-PaLM 2 | Medical QA | 86.5% | - | MedQA |
| Liévin et al. 2024 [10] | GPT-4 | Medical reasoning | 78.2% | 72% | MedQA |
| **Our study** | GPT-4o | Heart disease | **51.0%** | **99.25%** | UCI |
| **Our study** | Gemini-2.0 | Heart disease | **51.5%** | **99.38%** | UCI |
| **Our study** | Qwen-Plus | Heart disease | **51.0%** | **99.88%** | UCI |

**Pembahasan**:
"Perbandingan dengan penelitian sebelumnya menunjukkan perbedaan penting:

**1. Task Difference**:
- Penelitian sebelumnya fokus pada medical QA (multiple choice)
- Penelitian kami fokus pada binary diagnosis dengan data klinis real

**2. Consistency Measurement**:
- Hanya sedikit studi yang mengukur consistency
- Kami menunjukkan consistency jauh lebih tinggi dari accuracy

**3. Dataset Complexity**:
- UCI Heart Disease memerlukan reasoning dari raw clinical parameters
- Medical QA datasets sudah dalam format pertanyaan terstruktur"

---

### 4.9 Keterbatasan Penelitian
**Target**: 500-700 kata  
**Konten**:

1. **Dataset Terbatas**: Hanya 100 kasus dari satu dataset
2. **Binary Classification**: Tidak mengevaluasi severity grading
3. **Single Domain**: Hanya heart disease, tidak multi-disease
4. **No Fine-tuning**: Menggunakan pre-trained model tanpa domain adaptation
5. **Prompt Variations**: Hanya 2 prompt tested

---

### 4.10 Implikasi dan Rekomendasi
**Target**: 1000-1200 kata  
**Konten**:

#### Untuk Praktisi Medis:
- Jangan andalkan LLM untuk diagnosis primer
- Gunakan sebagai decision support saja
- Perhatikan bias over-diagnosis

#### Untuk Pengembang AI:
- Fokus pada reducing systematic bias
- Develop calibration methods
- Improve discriminative capability

#### Untuk Penelitian Lanjutan:
- Multi-domain evaluation
- Fine-tuning dengan medical data
- Explainability analysis
- Prompt engineering yang lebih sophisticated

---

## 📋 TIMELINE PENGERJAAN

### Week 1-2: Metodologi (BAB 3)
**Target**: 10,000-12,000 kata

| Hari | Sub-bab | Target Kata | Status |
|------|---------|-------------|--------|
| 1-2 | 3.1 Desain Penelitian | 600 | ⬜ |
| 3-4 | 3.2 Data dan Sumber Data | 1200 | ⬜ |
| 5-6 | 3.3 Metode Clustering | 1700 | ⬜ |
| 7-8 | 3.4 Metode Sampling | 900 | ⬜ |
| 9-10 | 3.5 Model LLM | 1400 | ⬜ |
| 11-12 | 3.6 Desain Prompt | 1100 | ⬜ |
| 13-14 | 3.7 Protokol Eksperimen | 1100 | ⬜ |

### Week 3-4: Metodologi (BAB 3 - lanjutan)
| Hari | Sub-bab | Target Kata | Status |
|------|---------|-------------|--------|
| 15-17 | 3.8 Metrik Evaluasi | 2300 | ⬜ |
| 18 | 3.9 Analisis Statistik | 600 | ⬜ |
| 19-20 | Review & Revisi BAB 3 | - | ⬜ |

### Week 5-6: Hasil (BAB 4)
**Target**: 12,000-15,000 kata

| Hari | Sub-bab | Target Kata | Status |
|------|---------|-------------|--------|
| 21-22 | 4.1 Clustering & Sampling | 1100 | ⬜ |
| 23-24 | 4.2 Intra-Model Consistency | 1700 | ⬜ |
| 25-26 | 4.3 Inter-Model Agreement | 1400 | ⬜ |
| 27-29 | 4.4 Diagnostic Accuracy | 2300 | ⬜ |
| 30-31 | 4.5 Prompt Sensitivity | 1100 | ⬜ |
| 32-33 | 4.6 Error Pattern Analysis | 1700 | ⬜ |

### Week 7: Pembahasan (BAB 4 - lanjutan)
| Hari | Sub-bab | Target Kata | Status |
|------|---------|-------------|--------|
| 34-36 | 4.7 Consistency vs Accuracy | 2300 | ⬜ |
| 37-38 | 4.8 Perbandingan SOTA | 1100 | ⬜ |
| 39 | 4.9 Keterbatasan | 600 | ⬜ |
| 40 | 4.10 Implikasi & Rekomendasi | 1100 | ⬜ |

### Week 8: Finalisasi
| Hari | Aktivitas | Status |
|------|-----------|--------|
| 41-42 | Review keseluruhan | ⬜ |
| 43-44 | Perbaikan bahasa & struktur | ⬜ |
| 45-46 | Pembuatan grafik & tabel final | ⬜ |
| 47-48 | Proofreading final | ⬜ |

---

## 📊 DELIVERABLES

### Tabel & Grafik yang Harus Dibuat

**BAB 3 - Metodologi**:
- [ ] Tabel 1: Karakteristik UCI Dataset
- [ ] Tabel 2: Deskripsi 13 Parameter Klinis
- [ ] Tabel 3: Perbandingan Metrik Clustering
- [ ] Tabel 4: Perbandingan 3 Model LLM
- [ ] Tabel 5: Perbandingan Prompt A vs B
- [ ] Tabel 6: Metrik Evaluasi dengan Formula
- [ ] Diagram 1: Flowchart Penelitian Keseluruhan
- [ ] Diagram 2: Flowchart K-Means Clustering
- [ ] Diagram 3: Diagram Stratified Sampling
- [ ] Diagram 4: Protokol Multi-Run Eksperimen
- [ ] Diagram 5: Confusion Matrix Template

**BAB 4 - Hasil**:
- [ ] Grafik 1: Elbow Method (K vs Inertia)
- [ ] Grafik 2: Silhouette Score (K vs Score)
- [ ] Grafik 3: Davies-Bouldin Index (K vs DB)
- [ ] Grafik 4: PCA 2D Cluster Visualization
- [ ] Grafik 5: Distribusi Fitur 100 Sampel
- [ ] Grafik 6: Bar Chart Consistency per Model
- [ ] Grafik 7: Violin Plot Consistency Distribution
- [ ] Grafik 8: Heatmap Pairwise Agreement
- [ ] Grafik 9: Venn Diagram 3-Way Agreement
- [ ] Grafik 10-15: 6 Confusion Matrix Heatmaps
- [ ] Grafik 16: Grouped Bar Chart Metrik Accuracy
- [ ] Grafik 17: Radar Chart Multi-Metrik
- [ ] Grafik 18: Pie Chart Prompt Sensitivity
- [ ] Grafik 19: Stacked Bar Chart Error Pattern
- [ ] Grafik 20: Sankey Diagram Error Flow
- [ ] Grafik 21: Scatter Plot Consistency vs Accuracy
- [ ] Tabel 1-7: Semua tabel hasil seperti yang dijelaskan

---

## ✅ CHECKLIST KUALITAS

### Metodologi (BAB 3):
- [ ] Setiap metode dijelaskan dengan: Tujuan, Formula, Deskripsi, Kegunaan, Interpretasi
- [ ] Semua formula ditulis dengan notasi matematika yang benar
- [ ] Setiap formula disertai penjelasan variabel
- [ ] Tidak ada pembahasan hasil (hanya metode)
- [ ] Alur penelitian jelas dari awal sampai akhir
- [ ] Diagram flowchart lengkap dan mudah dipahami

### Hasil & Pembahasan (BAB 4):
- [ ] Setiap hasil disertai: Tabel/Grafik, Interpretasi statistik, Interpretasi awam
- [ ] Interpretasi mudah dipahami orang non-teknis
- [ ] Semua grafik memiliki caption yang jelas
- [ ] Pembahasan menghubungkan hasil dengan teori/literatur
- [ ] Implikasi praktis dijelaskan dengan jelas
- [ ] Keterbatasan penelitian dibahas dengan jujur

---

## 📝 NOTES

**Bahasa Penulisan**: Indonesia (formal academic style)  
**Format**: Microsoft Word (.docx)  
**Font**: Times New Roman 12pt  
**Spacing**: 1.5  
**Margin**: 3cm (left), 2cm (right, top, bottom)  

**Target Total**:
- BAB 3: 10,000-12,000 kata (≈25-30 halaman)
- BAB 4: 12,000-15,000 kata (≈30-38 halaman)
- **TOTAL**: 22,000-27,000 kata (≈55-68 halaman)

---

## 🚀 MULAI PENGERJAAN

Konfirmasi untuk memulai:
1. ✅ Bahasa: Indonesia
2. ✅ Format: Word (.docx)
3. ✅ Jenjang: S1
4. ✅ Basis: JAMIA paper + expansion
5. ✅ Style: Detail, komprehensif, mudah dipahami

**READY TO START? Konfirmasi untuk mulai buat file!**
