# BAB 3 - METODOLOGI PENELITIAN
## BAGIAN 1: DESAIN PENELITIAN DAN DATA

---

## 3.1 Desain Penelitian

Penelitian ini menggunakan desain eksperimental dengan pendekatan evaluasi kuantitatif untuk menilai konsistensi dan akurasi Large Language Models (LLM) dalam diagnosis medis biner. Penelitian ini dirancang untuk menjawab pertanyaan penelitian mendasar: **Apakah model LLM dapat memberikan prediksi diagnosis yang konsisten dan akurat pada kasus medis yang sama ketika dijalankan berulang kali?**

### 3.1.1 Jenis Penelitian

Penelitian ini merupakan **penelitian eksperimental kuantitatif** dengan karakteristik sebagai berikut:

1. **Eksperimental**: Penelitian ini melakukan pengujian sistematis terhadap tiga model LLM (GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus) dengan mengontrol variabel-variabel tertentu (prompt, parameter model, data input) untuk mengamati pengaruhnya terhadap konsistensi dan akurasi prediksi.

2. **Kuantitatif**: Semua hasil diukur menggunakan metrik numerik yang terstandarisasi, termasuk skor konsistensi (0-1), akurasi diagnostik (0-100%), dan berbagai metrik evaluasi lainnya seperti precision, recall, dan F1-score.

3. **Multi-run Protocol**: Berbeda dengan penelitian evaluasi LLM konvensional yang hanya menjalankan satu kali prediksi per kasus, penelitian ini mengimplementasikan **protokol multi-run** di mana setiap model dijalankan **4 kali** untuk setiap kasus medis. Pendekatan ini memungkinkan pengukuran konsistensi intra-model (reproducibility) yang belum banyak dieksplorasi dalam literatur sebelumnya.

### 3.1.2 Kerangka Konseptual Penelitian

Penelitian ini didasarkan pada kerangka konseptual yang membedakan antara dua dimensi kualitas sistem AI medis:

**Konsistensi (Consistency)**: Kemampuan model untuk memberikan prediksi yang sama ketika diberikan input yang identik pada waktu yang berbeda. Konsistensi tinggi menunjukkan reproducibility dan reliability sistem.

**Akurasi (Accuracy)**: Kemampuan model untuk memberikan prediksi yang sesuai dengan ground truth diagnosis. Akurasi tinggi menunjukkan validitas klinis sistem.

Hipotesis penelitian ini adalah bahwa kedua dimensi ini **tidak selalu berkorelasi positif**. Sebuah model dapat sangat konsisten (selalu memberikan jawaban yang sama) namun tidak akurat (selalu salah), atau sebaliknya. Pemahaman tentang hubungan antara konsistensi dan akurasi ini krusial untuk deployment LLM dalam setting klinis.

### 3.1.3 Alur Penelitian

Penelitian ini dilaksanakan dalam 6 tahap utama yang saling berkaitan:

**Tahap 1: Persiapan Data**
- Pengambilan dataset UCI Heart Disease
- Preprocessing dan normalisasi data
- Pembagian data untuk analisis

**Tahap 2: Clustering**
- Implementasi K-Means clustering
- Evaluasi jumlah cluster optimal (K=2 hingga K=10)
- Analisis karakteristik setiap cluster

**Tahap 3: Stratified Sampling**
- Pengambilan sampel representatif dari setiap cluster
- Implementasi strategi "diverse" sampling
- Pembuatan test set 100 kasus

**Tahap 4: Desain Prompt**
- Pengembangan dua variasi prompt (Expert vs Neutral)
- Validasi struktur dan format prompt
- Persiapan template untuk input data klinis

**Tahap 5: Testing LLM Multi-Run**
- Testing 3 model LLM (GPT-4o, Gemini-2.0-Flash, Qwen-Plus)
- 4 runs per kasus untuk setiap kombinasi (model × prompt)
- Total 2,400 prediksi (100 kasus × 4 runs × 3 models × 2 prompts)
- Implementasi checkpoint system untuk reliability

**Tahap 6: Evaluasi dan Analisis**
- Perhitungan metrik konsistensi (intra-model consistency)
- Perhitungan metrik akurasi (accuracy, precision, recall, F1)
- Analisis inter-model agreement
- Analisis prompt sensitivity
- Interpretasi hasil dan penarikan kesimpulan

### 3.1.4 Diagram Alur Penelitian

```
┌─────────────────────────────────────────────────────────────┐
│                    DATASET UCI HEART DISEASE                 │
│                    303 Pasien, 13 Fitur Klinis              │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    PREPROCESSING DATA                        │
│          • Pengecekan Missing Values                         │
│          • Normalisasi (StandardScaler)                      │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   K-MEANS CLUSTERING                         │
│       Evaluasi K=2 hingga K=10 dengan 3 Metrik:             │
│       • Elbow Method (Inertia)                               │
│       • Silhouette Score                                     │
│       • Davies-Bouldin Index                                 │
│       → Hasil: K=2 Optimal                                   │
└───────────────────────────┬─────────────────────────────────┘
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
    ┌──────────────────┐    ┌──────────────────┐
    │   Cluster 0      │    │   Cluster 1      │
    │   145 pasien     │    │   158 pasien     │
    │   (47.9%)        │    │   (52.1%)        │
    └────────┬─────────┘    └────────┬─────────┘
             │                       │
             │  Stratified Sampling  │
             │  (Diverse Strategy)   │
             │                       │
             ▼                       ▼
    ┌──────────────────┐    ┌──────────────────┐
    │   50 Sampel      │    │   50 Sampel      │
    │   Cluster 0      │    │   Cluster 1      │
    └────────┬─────────┘    └────────┬─────────┘
             │                       │
             └───────────┬───────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │   TEST SET: 100 KASUS  │
            │   51 Positif (Sakit)   │
            │   49 Negatif (Sehat)   │
            └────────┬───────────────┘
                     │
        ┌────────────┼────────────┐
        │                         │
        ▼                         ▼
┌──────────────┐          ┌──────────────┐
│  Prompt A    │          │  Prompt B    │
│  (Expert)    │          │  (Neutral)   │
└──────┬───────┘          └──────┬───────┘
       │                         │
       └────────────┬────────────┘
                    │
                    ▼
    ┌───────────────────────────────────┐
    │   TESTING 3 MODEL LLM             │
    │   • GPT-4o                        │
    │   • Gemini-2.0-Flash              │
    │   • Qwen-Plus                     │
    │                                   │
    │   4 RUNS per kombinasi            │
    │   (model × prompt × kasus)        │
    │                                   │
    │   Total: 2,400 prediksi           │
    └───────────────┬───────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────┐
    │   EVALUASI HASIL                  │
    │   • Intra-Model Consistency       │
    │   • Diagnostic Accuracy           │
    │   • Inter-Model Agreement         │
    │   • Prompt Sensitivity            │
    └───────────────┬───────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────┐
    │   ANALISIS & INTERPRETASI         │
    │   • Consistency-Accuracy Gap      │
    │   • Error Pattern Analysis        │
    │   • Clinical Implications         │
    └───────────────────────────────────┘
```

---

## 3.2 Data dan Sumber Data

### 3.2.1 Dataset UCI Heart Disease

Penelitian ini menggunakan **UCI Heart Disease Dataset** yang merupakan salah satu dataset medis paling terkenal dan banyak digunakan dalam penelitian machine learning untuk diagnosis kardiovaskular. Dataset ini dipilih karena beberapa alasan:

1. **Validitas Klinis**: Data dikumpulkan dari institusi medis terkemuka (Cleveland Clinic Foundation, Hungarian Institute of Cardiology, V.A. Medical Center Long Beach, dan University Hospital Zurich).

2. **Standarisasi**: Dataset telah melalui proses cleaning dan validasi oleh komunitas penelitian internasional.

3. **Representatif**: Mencakup 13 parameter klinis yang umum digunakan dalam diagnosis penyakit jantung di praktik medis nyata.

4. **Aksesibilitas**: Tersedia secara publik dan bebas digunakan untuk penelitian akademis.

#### Karakteristik Dataset

Dataset UCI Heart Disease memiliki karakteristik sebagai berikut:

- **Sumber**: UCI Machine Learning Repository (Dua, D. dan Graff, C., 2019)
- **Jumlah Sampel**: 303 pasien
- **Jumlah Fitur**: 13 parameter klinis (variabel independen)
- **Target Variable**: 1 variabel biner (0 = tidak sakit jantung, 1 = sakit jantung)
- **Distribusi Kelas**:
  * Kelas 0 (Sehat): 138 pasien (45.5%)
  * Kelas 1 (Sakit): 165 pasien (54.5%)
- **Missing Values**: Dataset tidak mengandung missing values
- **Tipe Data**: Campuran numerik (continuous dan categorical)

#### Parameter Klinis (13 Fitur)

Berikut adalah deskripsi lengkap dari 13 parameter klinis yang digunakan dalam penelitian ini:

| No | Parameter | Tipe | Range | Deskripsi | Interpretasi Klinis |
|----|-----------|------|-------|-----------|---------------------|
| 1 | **age** | Numerik | 29-77 tahun | Usia pasien dalam tahun | Usia lanjut merupakan faktor risiko penyakit jantung |
| 2 | **sex** | Kategorikal | 0, 1 | Jenis kelamin pasien | 0 = Perempuan, 1 = Laki-laki. Laki-laki memiliki risiko lebih tinggi |
| 3 | **cp** | Kategorikal | 0-3 | Tipe nyeri dada (chest pain type) | 0 = Typical angina (angina tipikal), 1 = Atypical angina (angina atipikal), 2 = Non-anginal pain (nyeri non-angina), 3 = Asymptomatic (tanpa gejala) |
| 4 | **trestbps** | Numerik | 94-200 mmHg | Tekanan darah istirahat | Tekanan darah tinggi (>140 mmHg) merupakan indikator risiko kardiovaskular |
| 5 | **chol** | Numerik | 126-564 mg/dl | Kadar kolesterol serum | Kolesterol tinggi (>240 mg/dl) meningkatkan risiko penyakit jantung |
| 6 | **fbs** | Kategorikal | 0, 1 | Gula darah puasa > 120 mg/dl | 0 = Tidak (≤120 mg/dl), 1 = Ya (>120 mg/dl). Indikator diabetes |
| 7 | **restecg** | Kategorikal | 0-2 | Hasil elektrokardiografi istirahat | 0 = Normal, 1 = ST-T wave abnormality (kelainan gelombang ST-T), 2 = Left ventricular hypertrophy (hipertrofi ventrikel kiri) |
| 8 | **thalach** | Numerik | 71-202 bpm | Detak jantung maksimum saat tes olahraga | Detak jantung maksimum yang rendah dapat mengindikasikan masalah jantung |
| 9 | **exang** | Kategorikal | 0, 1 | Angina yang dipicu oleh olahraga | 0 = Tidak ada, 1 = Ada. Indikator kuat penyakit arteri koroner |
| 10 | **oldpeak** | Numerik | 0-6.2 | Depresi ST yang dipicu olahraga relatif terhadap istirahat | Nilai positif menunjukkan iskemia miokard (kurang oksigen ke otot jantung) |
| 11 | **slope** | Kategorikal | 0-2 | Kemiringan segmen ST puncak saat olahraga | 0 = Upsloping (naik), 1 = Flat (datar), 2 = Downsloping (turun). Downsloping = risiko tinggi |
| 12 | **ca** | Kategorikal | 0-4 | Jumlah pembuluh darah besar yang terlihat pada fluoroskopi | 0 = Tidak ada penyumbatan, 4 = Penyumbatan maksimal |
| 13 | **thal** | Kategorikal | 0-3 | Hasil tes thalassemia | 0 = Normal, 1 = Fixed defect (cacat permanen), 2 = Reversible defect (cacat reversibel), 3 = Lainnya |

#### Relevansi Klinis Parameter

Setiap parameter dalam dataset memiliki relevansi klinis yang telah terbukti dalam literatur medis:

- **Parameter Demografis** (age, sex): Faktor risiko dasar yang tidak dapat dimodifikasi
- **Parameter Kardiovaskular** (trestbps, chol, thalach): Indikator fungsi jantung dan pembuluh darah
- **Parameter Metabolik** (fbs): Indikator risiko diabetes yang berkaitan dengan penyakit jantung
- **Parameter Diagnostik** (cp, restecg, exang, oldpeak, slope): Hasil pemeriksaan klinis dan tes diagnostik
- **Parameter Anatomis** (ca, thal): Hasil imaging dan tes laboratorium spesifik

### 3.2.2 Preprocessing Data

Sebelum data digunakan untuk clustering dan testing LLM, dilakukan tahapan preprocessing untuk memastikan kualitas dan kesiapan data.

#### Pengecekan Missing Values

Langkah pertama adalah melakukan pengecekan terhadap missing values (nilai yang hilang) dalam dataset. Dataset UCI Heart Disease yang digunakan dalam penelitian ini tidak mengandung missing values, sehingga tidak diperlukan imputasi data.

**Kode Python untuk Pengecekan**:
```python
import pandas as pd

# Load dataset
data = pd.read_csv('data/heart.csv')

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Result: All columns have 0 missing values
```

#### Normalisasi Data (Standardization)

Normalisasi data dilakukan menggunakan **StandardScaler** dari library scikit-learn. Proses ini penting untuk memastikan semua fitur berada dalam skala yang sama, terutama untuk algoritma clustering K-Means yang sensitif terhadap skala fitur.

**Persamaan Normalisasi (Z-Score Standardization)**:

$$z = \frac{x - \mu}{\sigma}$$

di mana:
- $z$ = nilai ternormalisasi (standardized value)
- $x$ = nilai asli (original value)
- $\mu$ = mean (rata-rata) dari fitur
- $\sigma$ = standar deviasi dari fitur

**Interpretasi**:
- Setelah normalisasi, setiap fitur akan memiliki mean = 0 dan standar deviasi = 1
- Nilai $z = 0$ berarti nilai sama dengan mean
- Nilai $z > 0$ berarti nilai di atas mean
- Nilai $z < 0$ berarti nilai di bawah mean
- Sebagian besar nilai akan berada dalam range -3 hingga +3

**Kegunaan Normalisasi**:

1. **Menghilangkan Bias Skala**: Tanpa normalisasi, fitur dengan skala besar (misalnya cholesterol: 126-564) akan mendominasi perhitungan jarak dalam K-Means dibandingkan fitur dengan skala kecil (misalnya sex: 0-1).

2. **Meningkatkan Konvergensi**: K-Means akan konvergen lebih cepat dan stabil dengan fitur yang ternormalisasi.

3. **Memfasilitasi Interpretasi**: Setelah normalisasi, jarak Euclidean antar sampel lebih bermakna karena semua fitur berkontribusi secara seimbang.

**Implementasi Normalisasi**:
```python
from sklearn.preprocessing import StandardScaler

# Separate features and target
X = data.drop('target', axis=1)
y = data['target']

# Initialize StandardScaler
scaler = StandardScaler()

# Fit and transform the features
X_normalized = scaler.fit_transform(X)

# Result: X_normalized has mean ≈ 0 and std ≈ 1 for all features
```

**Contoh Hasil Normalisasi**:

| Fitur | Nilai Asli (Pasien 1) | Nilai Ternormalisasi |
|-------|------------------------|----------------------|
| age | 63 tahun | 0.952 |
| trestbps | 145 mmHg | 0.763 |
| chol | 233 mg/dl | -0.256 |
| thalach | 150 bpm | 0.015 |

#### Verifikasi Kualitas Data

Setelah preprocessing, dilakukan verifikasi untuk memastikan data siap digunakan:

1. **Tidak ada missing values**: ✓ Confirmed
2. **Tidak ada outlier ekstrem**: ✓ Checked (semua nilai dalam range medis yang masuk akal)
3. **Distribusi fitur**: ✓ Visualized (histogram dan boxplot)
4. **Korelasi antar fitur**: ✓ Analyzed (tidak ada multikolinearitas ekstrem)

### 3.2.3 Pembagian Data

Dalam penelitian ini, data **tidak dibagi** menjadi training set dan testing set seperti pada penelitian machine learning konvensional. Alasannya adalah:

1. **Fokus Penelitian**: Penelitian ini tidak melakukan training model baru, melainkan mengevaluasi kemampuan LLM pre-trained yang sudah ada.

2. **Full Dataset untuk Clustering**: Seluruh 303 pasien digunakan untuk proses clustering agar diperoleh representasi yang komprehensif dari variasi dalam dataset.

3. **Stratified Sampling**: Dari hasil clustering, dilakukan stratified sampling untuk memilih 100 kasus yang representatif untuk testing LLM.

Pendekatan ini berbeda dari penelitian machine learning tradisional dan lebih sesuai dengan tujuan penelitian evaluasi LLM.

---

**[Lanjut ke BAGIAN 2: Metode Clustering]**
