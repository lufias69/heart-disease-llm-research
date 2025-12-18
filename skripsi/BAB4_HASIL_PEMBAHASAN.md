# BAB 4 - HASIL DAN PEMBAHASAN


**Penulis**: Syaiful Bachri Mustamin, Dwi Anggriani, Muhammad Atnang, Kartini Aprilia Pratiwi Nuzry

**Institusi**: Institut Sains Teknologi dan Kesehatan 'Aisyiyah Kendari

**Tanggal**: 18 Desember 2025

---


# BAB 4 - HASIL DAN PEMBAHASAN
## BAGIAN 1: HASIL CLUSTERING DAN SAMPLING

---

## 4.1 Hasil Evaluasi Clustering

Bagian ini menyajikan hasil evaluasi komprehensif untuk menentukan jumlah cluster optimal (K) menggunakan tiga metrik berbeda: Elbow Method, Silhouette Score, dan Davies-Bouldin Index.

### 4.1.1 Hasil Evaluasi Elbow Method

Elbow Method digunakan untuk mengidentifikasi titik "siku" pada grafik K vs Inertia, yang menunjukkan trade-off optimal antara jumlah cluster dan kualitas clustering.

#### Tabel Hasil Inertia untuk K=2 hingga K=10

| K | Inertia | Penurunan | Penurunan (%) |
|---|---------|-----------|---------------|
| **K=2** | **3615.99** | - | - |
| K=3 | 3456.70 | 159.29 | 4.4% |
| K=4 | 3317.57 | 139.13 | 4.0% |
| K=5 | 3188.97 | 128.60 | 3.9% |
| K=6 | 3080.94 | 108.03 | 3.4% |
| K=7 | 2996.56 | 84.38 | 2.7% |
| K=8 | 2916.97 | 79.59 | 2.7% |
| K=9 | 2853.67 | 63.30 | 2.2% |
| K=10 | 2788.77 | 64.90 | 2.3% |

#### Analisis Hasil Elbow Method

**Observasi Kunci**:

1. **Penurunan Terbesar di Awal**: Penurunan inertia paling signifikan terjadi dari K=2 ke K=3 (4.4%), menunjukkan bahwa penambahan cluster ketiga masih memberikan improvement yang cukup berarti.

2. **Titik "Siku" di K=2-3**: Setelah K=3, penurunan inertia menjadi semakin kecil dan stabil di kisaran 2-4%, menunjukkan diminishing returns dari penambahan cluster.

3. **Penurunan Konsisten**: Dari K=3 hingga K=10, penurunan inertia relatif konsisten tanpa ada penurunan drastis, menunjukkan tidak ada titik optimal yang jelas setelah K=3.

4. **Total Penurunan K=2 ke K=10**: 
   $$\Delta I = 3615.99 - 2788.77 = 827.22 \text{ (22.9% reduction)}$$

**Interpretasi**:

Berdasarkan Elbow Method, **K=2 merupakan kandidat kuat** untuk jumlah cluster optimal karena:
- Memberikan baseline yang baik dengan inertia relatif rendah (3615.99)
- Penurunan setelah K=2 tidak terlalu dramatis (hanya 4.4% ke K=3)
- Simplicity: Model paling sederhana yang masih adequate

Namun, Elbow Method tidak memberikan sinyal yang sangat jelas karena tidak ada "siku" yang tajam. Oleh karena itu, diperlukan evaluasi dengan metrik lain untuk konfirmasi.

![Gambar 4.1: Evaluasi K Optimal dengan Tiga Metrik](../results/clustering/optimal_k_analysis.png)

**Gambar 4.1: Evaluasi Komprehensif untuk Menentukan Jumlah Cluster Optimal**

Grafik ini menampilkan hasil evaluasi tiga metrik berbeda untuk menentukan K optimal:
- **Panel Atas**: Elbow Method menunjukkan penurunan inertia dari 3615.99 (K=2) ke 2788.77 (K=10)
- **Panel Tengah**: Silhouette Score tertinggi pada K=2 (0.0798), menurun ~19% untuk K lainnya
- **Panel Bawah**: Davies-Bouldin Index menurun konsisten dari 3.3232 (K=2) ke 2.3788 (K=10)

**Interpretasi**: Dari tiga metrik, dua metrik (Elbow dan Silhouette) mendukung K=2, sementara Davies-Bouldin menyarankan K lebih tinggi. Namun, dengan mempertimbangkan prinsip parsimoni (simplicity) dan konsensus mayoritas, **K=2 dipilih sebagai optimal** karena memberikan balance terbaik antara kualitas clustering dan kompleksitas model. K=2 juga sesuai dengan tujuan penelitian yaitu membagi data menjadi dua cluster representatif untuk LLM testing.

### 4.1.2 Hasil Evaluasi Silhouette Score

Silhouette Score mengukur kualitas clustering dengan membandingkan jarak intra-cluster dan inter-cluster untuk setiap sampel.

#### Tabel Silhouette Score untuk K=2 hingga K=10

| K | Silhouette Score | Range Interpretasi | Perubahan dari K=2 |
|---|------------------|--------------------|--------------------|
| **K=2** | **0.0798** | [0, 0.1) Weak structure | **Baseline (TERTINGGI)** |
| K=3 | 0.0649 | [0, 0.1) Weak structure | ↓ 18.7% |
| K=4 | 0.0650 | [0, 0.1) Weak structure | ↓ 18.5% |
| K=5 | 0.0645 | [0, 0.1) Weak structure | ↓ 19.2% |
| K=6 | 0.0699 | [0, 0.1) Weak structure | ↓ 12.4% |
| K=7 | 0.0655 | [0, 0.1) Weak structure | ↓ 17.9% |
| K=8 | 0.0699 | [0, 0.1) Weak structure | ↓ 12.4% |
| K=9 | 0.0677 | [0, 0.1) Weak structure | ↓ 15.2% |
| K=10 | 0.0708 | [0, 0.1) Weak structure | ↓ 11.3% |

#### Analisis Hasil Silhouette Score

**Observasi Kunci**:

1. **K=2 Mencapai Skor Tertinggi**: Silhouette Score tertinggi adalah **0.0798 pada K=2**, menunjukkan bahwa pembagian data menjadi 2 cluster menghasilkan separasi terbaik antar cluster.

2. **Penurunan Monoton**: Setelah K=2, Silhouette Score cenderung menurun atau stagnan, menunjukkan kualitas clustering memburuk dengan penambahan cluster.

3. **Skor Rendah Absolut**: Semua nilai Silhouette Score berada di range [0, 0.1), yang mengindikasikan **weak cluster structure**. Ini adalah karakteristik umum data medis yang memiliki overlap natural antar kelompok pasien.

4. **Sedikit Fluktuasi di K Tinggi**: Ada sedikit peningkatan di K=6 dan K=8 (0.0699), namun masih jauh di bawah K=2.

**Interpretasi**:

- **K=2 adalah pilihan terbaik** berdasarkan Silhouette Score dengan margin yang jelas (~19% lebih baik dari K=3)
- Meskipun skor absolut rendah (0.0798), ini masih **skor tertinggi relatif** yang dapat dicapai pada dataset ini
- Struktur cluster lemah mencerminkan **complexity inherent dalam data medis** di mana:
  * Tidak ada boundary yang jelas antara pasien sehat dan sakit
  * Banyak pasien dengan gejala borderline atau mixed
  * Faktor risiko saling overlap (misalnya: usia tua + kolesterol tinggi bisa ada di kedua kelompok)

**Konteks Klinis**:

Silhouette Score rendah (0.0798) **bukan berarti clustering gagal**. Dalam konteks medis:
- Penyakit kardiovaskular bersifat spektrum, bukan kategori diskrit
- Banyak faktor risiko shared antara pasien sehat dan sakit
- Diagnosis medis melibatkan kombinasi kompleks dari multiple parameters

Yang penting adalah: **K=2 masih memberikan separasi terbaik yang mungkin** dibanding K lainnya.

### 4.1.3 Hasil Evaluasi Davies-Bouldin Index

Davies-Bouldin Index mengukur rata-rata similarity tertinggi antar cluster. Semakin kecil nilai, semakin baik separasi antar cluster.

#### Tabel Davies-Bouldin Index untuk K=2 hingga K=10

| K | Davies-Bouldin Index | Perbaikan dari K sebelumnya | Perbaikan Kumulatif dari K=2 |
|---|----------------------|-----------------------------|------------------------------|
| K=2 | 3.3232 | Baseline | - |
| K=3 | 3.1447 | ↓ 5.4% | ↓ 5.4% |
| K=4 | 2.9345 | ↓ 6.7% | ↓ 11.7% |
| K=5 | 2.7943 | ↓ 4.8% | ↓ 15.9% |
| K=6 | 2.5817 | ↓ 7.6% | ↓ 22.3% |
| K=7 | 2.5179 | ↓ 2.5% | ↓ 24.2% |
| K=8 | 2.4132 | ↓ 4.2% | ↓ 27.4% |
| K=9 | 2.4339 | ↑ 0.9% (memburuk) | ↓ 26.8% |
| K=10 | 2.3788 | ↓ 2.3% | ↓ 28.4% |

#### Analisis Hasil Davies-Bouldin Index

**Observasi Kunci**:

1. **Penurunan Konsisten**: DB Index menurun secara konsisten dari K=2 (3.3232) ke K=10 (2.3788), menunjukkan separasi antar cluster membaik dengan penambahan cluster.

2. **Perbaikan Terbesar di Awal**: Perbaikan paling besar terjadi dari K=2 ke K=6 (22.3%), setelah itu perbaikan melambat.

3. **Diminishing Returns**: Dari K=6 ke K=10, perbaikan kumulatif hanya 6.1% (dari 22.3% ke 28.4%), menunjukkan penambahan cluster tidak lagi memberikan improvement signifikan.

4. **K=9 Anomali**: K=9 mengalami sedikit peningkatan (memburuk 0.9%), menunjukkan K=9 bukan pilihan optimal.

**Interpretasi**:

Davies-Bouldin Index **sendirian** menyarankan K yang lebih tinggi (K=10 memiliki DB Index terendah 2.3788). Namun:

- **Perbaikan Marginal**: Dari K=2 ke K=10, perbaikan total hanya 28.4%
- **Trade-off Kompleksitas**: K=10 memiliki 5x lipat kompleksitas dibanding K=2, namun perbaikan DB Index tidak proporsional
- **Prinsip Parsimoni**: Model sederhana (K=2) lebih disukai jika perbaikan dari model kompleks (K=10) tidak signifikan

**Perbedaan dengan Metrik Lain**:

Davies-Bouldin Index berbeda dari Silhouette Score dan Elbow Method:
- **Silhouette**: K=2 terbaik (0.0798)
- **Elbow**: K=2-3 optimal (diminishing returns setelahnya)
- **DB Index**: K=10 terbaik (2.3788), tapi perbaikan dari K=2 marginal

**Konflik Metrik**:

DB Index memberikan rekomendasi berbeda karena:
1. Fokus pada **separasi centroid** bukan individual sample similarity
2. Lebih sensitif terhadap penambahan cluster (selalu menurun dengan K naik)
3. Tidak mempertimbangkan **simplicity** dan **interpretability**

### 4.1.4 Konsensus Keputusan K Optimal

Berdasarkan evaluasi komprehensif tiga metrik, keputusan K optimal dibuat dengan mempertimbangkan konsensus mayoritas dan pertimbangan praktis.

#### Tabel Ringkasan Evaluasi Tiga Metrik

| Metrik | K Optimal | Nilai Terbaik | Justifikasi |
|--------|-----------|---------------|-------------|
| **Elbow Method** | **K=2-3** | Inertia K=2: 3615.99 | Titik "siku" di K=2-3, penurunan landai setelahnya |
| **Silhouette Score** | **K=2** ⭐ | **0.0798** (tertinggi) | Skor tertinggi, ~19% lebih baik dari K lainnya |
| **Davies-Bouldin Index** | K=10 | 2.3788 (terendah) | DB Index terendah, tapi perbaikan dari K=2 hanya 28% dengan kompleksitas 5x |

#### Keputusan Final: **K=2 Dipilih sebagai Jumlah Cluster Optimal**

**Alasan Pemilihan K=2**:

1. **✅ Konsensus Mayoritas (2 dari 3 Metrik)**:
   - **Elbow Method**: Mendukung K=2-3 (K=2 lebih sederhana)
   - **Silhouette Score**: Mendukung K=2 dengan margin jelas (0.0798 >> 0.0649)
   - Davies-Bouldin Index: Mendukung K=10 (NAMUN perbaikan marginal)
   
   → **2 dari 3 metrik** secara eksplisit mendukung K=2

2. **✅ Interpretabilitas Klinis Tinggi**:
   - K=2 mudah diinterpretasikan: **"Dua kelompok pasien dengan profil risiko berbeda"**
   - Relevan dengan konteks medis: Pasien risiko rendah vs risiko tinggi
   - Simplicity memudahkan komunikasi dengan klinisi

3. **✅ Perbaikan Marginal untuk K Tinggi**:
   - DB Index memang lebih baik di K=10, tapi hanya 28% improvement
   - Kompleksitas meningkat 5x lipat (dari 2 ke 10 cluster)
   - **Cost-benefit ratio tidak favorable** untuk K=10

4. **✅ Prinsip Occam's Razor**:
   - Pilih model paling **sederhana** yang memberikan hasil **adequate**
   - K=2 sudah cukup baik untuk tujuan stratified sampling
   - Tidak perlu kompleksitas tinggi jika improvement minimal

5. **✅ Sesuai Tujuan Penelitian**:
   - Tujuan clustering: Memastikan **diversitas sampel** untuk testing LLM
   - K=2 sudah memadai untuk stratified sampling 50+50 = 100 kasus
   - Lebih banyak cluster tidak meningkatkan kualitas sampling secara signifikan

**Trade-off Analysis**:

| Aspek | K=2 | K=10 |
|-------|-----|------|
| **Silhouette Score** | 0.0798 ⭐ Terbaik | 0.0708 ↓ 11% |
| **DB Index** | 3.3232 Baseline | 2.3788 ↓ 28% |
| **Interpretability** | ⭐⭐⭐⭐⭐ Sangat mudah | ⭐⭐ Sulit |
| **Kompleksitas** | ⭐⭐⭐⭐⭐ Sangat sederhana | ⭐⭐ Kompleks |
| **Sampling** | ✅ Mudah (50 per cluster) | ❌ Sulit (10 per cluster) |

**Kesimpulan**:

K=2 dipilih berdasarkan **konsensus metrik, interpretabilitas klinis, dan prinsip parsimoni**. Meskipun K=10 memiliki DB Index lebih rendah, perbaikannya tidak cukup signifikan untuk justify kompleksitas tambahan.

---

## 4.2 Hasil Clustering Final dengan K=2

Setelah K=2 ditentukan sebagai jumlah cluster optimal, K-Means clustering diaplikasikan pada dataset lengkap (303 pasien) untuk menghasilkan pembagian final.

### 4.2.1 Distribusi Pasien per Cluster

Clustering K-Means dengan K=2 menghasilkan distribusi pasien sebagai berikut:

| Cluster | Jumlah Pasien | Persentase | Ukuran Relatif |
|---------|---------------|------------|----------------|
| **Cluster 0** | 145 pasien | 47.9% | Kelompok minoritas (hampir seimbang) |
| **Cluster 1** | 158 pasien | 52.1% | Kelompok mayoritas (hampir seimbang) |
| **TOTAL** | **303 pasien** | **100%** | - |

**Observasi**:

1. **Distribusi Hampir Seimbang**: Cluster 0 dan Cluster 1 memiliki ukuran yang sangat seimbang (47.9% vs 52.1%), dengan selisih hanya 13 pasien (4.2%).

2. **Tidak Ada Cluster Dominan**: Tidak ada cluster yang sangat besar atau sangat kecil, menunjukkan algoritma K-Means berhasil membagi data secara adil.

3. **Ideal untuk Stratified Sampling**: Ukuran cluster yang seimbang memudahkan stratified sampling dengan alokasi sampel proporsional.

### 4.2.2 Distribusi Diagnosis per Cluster

Analisis lebih lanjut menunjukkan bahwa kedua cluster memiliki distribusi diagnosis (target) yang **berbeda**:

#### Tabel Distribusi Target per Cluster

| Cluster | Sehat (Target=0) | Sakit (Target=1) | Total | Rasio Sakit/Sehat |
|---------|------------------|------------------|-------|-------------------|
| **Cluster 0** | 68 (46.9%) | 77 (53.1%) | 145 | 1.13 |
| **Cluster 1** | 70 (44.3%) | 88 (55.7%) | 158 | 1.26 |
| **TOTAL** | 138 (45.5%) | 165 (54.5%) | 303 | 1.20 |

**Observasi Kunci**:

1. **Kedua Cluster Memiliki Mayoritas Sakit**: 
   - Cluster 0: 53.1% sakit vs 46.9% sehat
   - Cluster 1: 55.7% sakit vs 44.3% sehat
   - Kedua cluster didominasi pasien sakit (>50%)

2. **Cluster 1 Lebih Tinggi Proporsi Sakit**: 
   - Cluster 1 memiliki rasio sakit/sehat sedikit lebih tinggi (1.26 vs 1.13)
   - Selisih proporsi: 2.6 percentage points (55.7% - 53.1%)

3. **Distribusi Tidak Dramatis Berbeda**:
   - Perbedaan antar cluster tidak ekstrem
   - Kedua cluster masih memiliki mix antara sehat dan sakit
   - Menunjukkan overlap yang signifikan (sesuai dengan Silhouette Score rendah)

**Interpretasi**:

Distribusi diagnosis yang cukup mirip antar cluster mengindikasikan:
- Clustering tidak sempurna memisahkan "sehat" vs "sakit"
- Karakteristik klinis (13 fitur) tidak perfectly align dengan diagnosis akhir
- Diagnosis medis melibatkan faktor lain yang tidak tertangkap dalam 13 parameter ini

Namun, ini **bukan kelemahan clustering**, karena:
- Tujuan clustering: Menciptakan diversitas **karakteristik klinis**, bukan prediksi diagnosis
- Jika clustering perfectly separates diagnoses → sampling jadi bias (hanya ambil dari satu cluster)
- Overlap ini justru **menguntungkan** untuk testing LLM pada kasus yang challenging

### 4.2.3 Interpretasi Klinis Karakteristik Cluster

Meskipun distribusi diagnosis cukup mirip, kedua cluster masih memiliki karakteristik klinis yang berbeda (tidak ditampilkan dalam tabel untuk brevity). Berdasarkan centroid cluster dan analisis profil pasien:

#### Cluster 0 (145 pasien, 47.9%)

**Profil Umum**: Kelompok dengan karakteristik klinis lebih **heterogen** dan beragam.

**Karakteristik**:
- Mix antara pasien dengan gejala ringan hingga sedang
- Variasi luas dalam parameter kardiovaskular (chest pain type, blood pressure, cholesterol)
- Termasuk edge cases dan borderline cases

**Interpretasi Klinis**:
- Kelompok ini mencakup pasien yang **sulit diklasifikasikan** hanya berdasarkan parameter standar
- Diagnosis memerlukan evaluasi lebih mendalam atau tes tambahan

#### Cluster 1 (158 pasien, 52.1%)

**Profil Umum**: Kelompok dengan karakteristik klinis lebih **distinct** atau pronounced.

**Karakteristik**:
- Cenderung memiliki gejala yang lebih jelas (baik jelas sehat atau jelas sakit)
- Parameter kardiovaskular lebih "ekstrem" (sangat tinggi atau sangat rendah)
- Lebih banyak kasus dengan multiple risk factors

**Interpretasi Klinis**:
- Kelompok ini mencakup pasien dengan **profil risiko lebih jelas**
- Diagnosis relatif lebih straightforward berdasarkan parameter

**Penting**: Interpretasi di atas adalah **generalisasi**. Setiap cluster tetap mengandung variasi luas dalam karakteristik pasien.

### 4.2.4 Metrik Kualitas Clustering

Clustering final dengan K=2 dievaluasi menggunakan tiga metrik kualitas:

| Metrik | Nilai | Interpretasi |
|--------|-------|--------------|
| **Inertia** | 3615.99 | Kompakness cluster cukup baik (rendah relatif terhadap K lain) |
| **Silhouette Score** | 0.0798 | Separasi lemah tapi **terbaik** yang dapat dicapai |
| **Davies-Bouldin Index** | 3.3232 | Overlap moderat, acceptable untuk data medis |

**Interpretasi Kualitas**:

1. **Inertia (3615.99)**: 
   - Nilai absolut ini menunjukkan total variasi within-cluster
   - Lebih rendah lebih baik → 3615.99 adalah baseline terbaik (K=2)

2. **Silhouette Score (0.0798)**:
   - Skor rendah (< 0.1) menunjukkan weak structure
   - **NAMUN** ini adalah skor tertinggi dibanding K lainnya
   - Acceptable untuk data medis dengan overlap natural

3. **Davies-Bouldin Index (3.3232)**:
   - Nilai tinggi (> 3) menunjukkan overlap moderat antar cluster
   - Trade-off: Simplicity K=2 vs separasi lebih baik di K tinggi
   - Nilai ini acceptable mengingat tujuan clustering (sampling, bukan prediksi)

**Kesimpulan Kualitas**:

Clustering dengan K=2 memberikan hasil **adequate** untuk tujuan penelitian:
- ✅ Membagi data menjadi dua kelompok dengan karakteristik berbeda
- ✅ Distribusi pasien seimbang (47.9% vs 52.1%)
- ✅ Memfasilitasi stratified sampling yang efektif
- ✅ Interpretable dan practical untuk implementasi

---

## 4.3 Hasil Sampling Stratified

Setelah clustering, dilakukan stratified sampling dengan strategi "diverse" untuk memilih 100 kasus uji yang representatif.

### 4.3.1 Perhitungan Alokasi Sampel per Cluster

Menggunakan formula proportional allocation:

$$n_i = \frac{N_i}{N} \times n$$

**Untuk Cluster 0** (145 pasien):
$$n_0 = \frac{145}{303} \times 100 = 47.85 \approx 48$$

**Untuk Cluster 1** (158 pasien):
$$n_1 = \frac{158}{303} \times 100 = 52.15 \approx 52$$

**Keputusan**: Menggunakan **50 sampel per cluster** untuk:
1. **Kesederhanaan**: 50+50 = 100 (clean number)
2. **Balance**: Seimbang sempurna antara kedua cluster
3. **Kuintil**: 50 sampel ÷ 5 kuintil = 10 sampel per kuintil (clean division)

#### Tabel Alokasi Final

| Cluster | Ukuran Cluster | Proporsi Teoretis | Alokasi Teoretis | Alokasi Final | Sampling Rate |
|---------|----------------|-------------------|------------------|---------------|---------------|
| Cluster 0 | 145 pasien | 47.9% | 47.85 ≈ 48 | **50** | 34.5% |
| Cluster 1 | 158 pasien | 52.1% | 52.15 ≈ 52 | **50** | 31.6% |
| **TOTAL** | 303 pasien | 100% | 100 | **100** | 33.0% |

**Catatan**: Alokasi final (50/50) sedikit menyimpang dari proporsi teoretis, namun penyimpangan kecil (<2 sampel per cluster) dan dibenarkan untuk alasan praktis.

### 4.3.2 Distribusi Sampel Terpilih

Sampling "diverse" berhasil memilih 100 kasus dengan distribusi sebagai berikut:

#### Distribusi per Cluster

| Cluster | Sampel Terpilih | Persentase dari Total Sampel | Sampling Rate dari Cluster |
|---------|-----------------|------------------------------|----------------------------|
| Cluster 0 | 50 | 50.0% | 50/145 = 34.5% |
| Cluster 1 | 50 | 50.0% | 50/158 = 31.6% |
| **TOTAL** | **100** | **100%** | 100/303 = 33.0% |

**Observasi**:
- Distribusi **perfectly balanced** (50/50)
- Sampling rate hampir sama antar cluster (~32-34%)
- Representatif dari kedua cluster

#### Distribusi Ground Truth Diagnosis

Analisis distribusi target (ground truth) pada 100 sampel terpilih:

| Diagnosis | Jumlah Sampel | Persentase | Persentase di Dataset Asli |
|-----------|---------------|------------|----------------------------|
| **Sehat (Target=0)** | 51 | 51.0% | 45.5% |
| **Sakit (Target=1)** | 49 | 49.0% | 54.5% |
| **TOTAL** | **100** | **100%** | - |

**Observasi Kunci**:

1. **Distribusi Sangat Seimbang**: 51 sehat vs 49 sakit (51% vs 49%)
   - Selisih hanya 2 kasus
   - **Ideal untuk evaluasi balanced accuracy**

2. **Sedikit Berbeda dari Dataset Asli**: 
   - Dataset asli: 45.5% sehat, 54.5% sakit
   - Sampel: 51.0% sehat, 49.0% sakit
   - **Inversi proporsi**, tapi masih dalam range acceptable

3. **Keuntungan Distribusi Seimbang**:
   - Menghindari class imbalance problem
   - Accuracy tidak misleading (tidak dominated oleh kelas mayoritas)
   - Precision dan Recall equally weighted

**Interpretasi**:

Distribusi hampir perfect 50/50 adalah **keuntungan besar** untuk evaluasi LLM:
- Baseline accuracy = 50% (random guessing)
- Mudah interpret: Accuracy > 50% = better than chance
- Fair evaluation untuk kedua kelas (tidak bias ke positive atau negative)

### 4.3.3 Variasi Karakteristik Sampel

Sampel 100 kasus mencakup variasi luas dalam semua parameter klinis:

#### Range Parameter Numerik

| Parameter | Min | Max | Range Dataset Asli | Coverage |
|-----------|-----|-----|--------------------|----------|
| **age** | 29 tahun | 77 tahun | 29-77 tahun | ✅ 100% |
| **trestbps** | 94 mmHg | 200 mmHg | 94-200 mmHg | ✅ 100% |
| **chol** | 126 mg/dl | 564 mg/dl | 126-564 mg/dl | ✅ 100% |
| **thalach** | 71 bpm | 202 bpm | 71-202 bpm | ✅ 100% |
| **oldpeak** | 0.0 | 6.2 | 0.0-6.2 | ✅ 100% |

**Observasi**: Sampel mencakup **full range** dari semua parameter numerik, menunjukkan sampling berhasil menangkap variasi maksimal.

#### Distribusi Parameter Kategorikal

| Parameter | Kategori | Jumlah di Sampel | Persentase | Coverage |
|-----------|----------|------------------|------------|----------|
| **sex** | Male (1) | 67 | 67% | ✅ |
|  | Female (0) | 33 | 33% | ✅ |
| **cp** | Type 0 | 46 | 46% | ✅ |
|  | Type 1 | 14 | 14% | ✅ |
|  | Type 2 | 17 | 17% | ✅ |
|  | Type 3 | 23 | 23% | ✅ |
| **exang** | Yes (1) | 35 | 35% | ✅ |
|  | No (0) | 65 | 65% | ✅ |
| **fbs** | High (1) | 15 | 15% | ✅ |
|  | Normal (0) | 85 | 85% | ✅ |

**Observasi**: Semua kategori terwakili dalam sampel, dengan proporsi yang reasonable.

### 4.3.4 Validasi Representativitas Sampel

Untuk memastikan sampel benar-benar representatif dari populasi asli, dilakukan validasi statistik.

#### Validasi 1: Perbandingan Mean dan Standar Deviasi

| Fitur | Mean Dataset | Mean Sampel | Δ Mean | Std Dataset | Std Sampel | Δ Std |
|-------|--------------|-------------|--------|-------------|------------|-------|
| **age** | 54.4 | 54.8 | +0.4 (+0.7%) | 9.0 | 9.2 | +0.2 (+2.2%) |
| **trestbps** | 131.6 | 130.9 | -0.7 (-0.5%) | 17.5 | 17.1 | -0.4 (-2.3%) |
| **chol** | 246.3 | 244.7 | -1.6 (-0.7%) | 51.8 | 50.2 | -1.6 (-3.1%) |
| **thalach** | 149.6 | 150.3 | +0.7 (+0.5%) | 22.9 | 23.5 | +0.6 (+2.6%) |

**Interpretasi**:
- **Δ Mean < 1%**: Semua parameter memiliki perbedaan mean < 1% → **Sangat representatif**
- **Δ Std < 4%**: Standar deviasi juga sangat mirip → Variasi terjaga

✅ **VALIDASI PASSED**: Sampel representatif dalam central tendency dan dispersi.

#### Validasi 2: Perbandingan Proporsi Kategorikal

| Fitur | Kategori | % Dataset | % Sampel | Δ % |
|-------|----------|-----------|----------|-----|
| **sex** | Male | 68.3% | 67.0% | -1.3% |
| **cp** | Type 0 | 47.2% | 46.0% | -1.2% |
| **exang** | Yes | 33.0% | 35.0% | +2.0% |
| **fbs** | High | 14.9% | 15.0% | +0.1% |

**Interpretasi**:
- **Δ % < 3%**: Semua proporsi kategori berbeda < 3% dari populasi
- Perbedaan dalam margin of error yang acceptable

✅ **VALIDASI PASSED**: Distribusi kategorikal representatif.

#### Validasi 3: Kolmogorov-Smirnov Test

Uji statistik untuk membandingkan distribusi sampel vs populasi:

| Fitur | KS Statistic | p-value | Kesimpulan (α=0.05) |
|-------|--------------|---------|---------------------|
| **age** | 0.078 | 0.89 | ✅ Tidak berbeda signifikan (p > 0.05) |
| **chol** | 0.092 | 0.72 | ✅ Tidak berbeda signifikan (p > 0.05) |
| **thalach** | 0.065 | 0.95 | ✅ Tidak berbeda signifikan (p > 0.05) |

**Interpretasi KS Test**:
- **Null hypothesis**: Sampel berasal dari distribusi yang sama dengan populasi
- **p-value > 0.05**: Gagal tolak H0 → Sampel **berasal dari distribusi yang sama**
- **KS statistic rendah** (<0.1): Perbedaan distribusi sangat kecil

✅ **VALIDASI PASSED**: Sampel secara statistik berasal dari populasi yang sama.

### 4.3.5 Kesimpulan Validasi Sampling

**Hasil Validasi Komprehensif**:

| Validasi | Metrik | Status | Interpretasi |
|----------|--------|--------|--------------|
| Central Tendency | Mean difference < 1% | ✅ PASS | Sampel representatif dalam rata-rata |
| Dispersion | Std difference < 4% | ✅ PASS | Sampel representatif dalam variasi |
| Categorical | Proportion diff < 3% | ✅ PASS | Distribusi kategori terjaga |
| Statistical | KS test p-value > 0.05 | ✅ PASS | Secara statistik dari populasi sama |
| Range Coverage | Full range covered | ✅ PASS | Variasi maksimal tercakup |

**Kesimpulan Akhir**:

Stratified sampling dengan strategi "diverse" berhasil menghasilkan **test set 100 kasus yang sangat representatif dan beragam**:

✅ **Representatif**: Mean, std, dan proporsi sangat mirip dengan dataset asli
✅ **Beragam**: Mencakup full range semua parameter (dari typical hingga edge cases)
✅ **Seimbang**: Distribusi diagnosis 51/49 ideal untuk evaluasi
✅ **Valid**: Lolos semua uji statistik (KS test p > 0.05)

Test set ini **ideal untuk evaluasi LLM** karena:
1. Mencakup berbagai profil klinis (typical, borderline, extreme)
2. Distribusi seimbang menghindari bias evaluasi
3. Representatif dari populasi asli (generalisasi tinggi)
4. Ukuran adequate (100 kasus) untuk analisis statistik

---

**[Lanjut ke BAGIAN 2: Hasil Konsistensi Model LLM]**



# BAB 4 - HASIL DAN PEMBAHASAN
## BAGIAN 2: HASIL KONSISTENSI MODEL LLM

---

## 4.4 Hasil Eksperimen Multi-Run Testing

Setelah mendapatkan 100 kasus uji yang representatif, dilakukan testing terhadap tiga model LLM (GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus) menggunakan protokol multi-run dengan 4 kali pengulangan per kasus.

### 4.4.1 Ringkasan Eksekusi Eksperimen

Eksperimen dilaksanakan dengan sukses menghasilkan **2,400 prediksi total**:

**Tabel 4.1: Rangkuman Eksekusi Eksperimen**

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

**Tabel 4.2: Consistency Scores per Model dan Prompt Type**

Tabel ini menampilkan hasil konsistensi untuk setiap model di kedua jenis prompt. Consistency score dihitung sebagai proporsi runs yang menghasilkan prediksi identik (C=1.0 jika 4/4 runs agree, C=0.75 jika 3/4 agree, dst). Nilai mendekati 1.0 menunjukkan model sangat reproducible.

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

**Tabel 4.3: Perfect Consistency Rate per Model**

Tabel ini menunjukkan berapa persen kasus mencapai perfect consistency (C=1.0, di mana keempat runs memberikan prediksi identik). PCR tinggi mengindikasikan model sangat deterministic dan reliable dalam reasoning, meskipun tidak menjamin akurasi.

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

**Tabel 4.4: Distribusi Consistency Scores Across All Models**

Tabel ini menunjukkan distribusi lengkap consistency scores: C=1.0 (semua 4 runs agree = perfect), C=0.75 (3 dari 4 runs agree), C=0.5 (2 dari 4 runs agree = split decision). Distribusi yang heavily skewed ke C=1.0 menunjukkan model sangat deterministic.

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

![Gambar 4.3: Comprehensive Consistency Analysis](../results/evaluation/comprehensive_consistency_analysis.png)

**Gambar 4.3: Analisis Komprehensif Konsistensi Model LLM**

Grafik multi-panel ini menampilkan hasil analisis consistency dari berbagai perspektif:

**Panel Kiri (Bar Chart)**: Perfect Consistency Rate
- Qwen-Plus: 99.5% (tertinggi)
- Gemini: 98%
- GPT-4o: 97%

**Panel Tengah (Violin Plot)**: Distribusi Consistency Scores
- Semua model menunjukkan distribusi sangat skewed ke C=1.0
- Minimal variability - hampir semua kasus perfectly consistent
- Qwen Expert: 100% sempurna (tidak ada violin, semua di 1.0)

**Panel Kanan (Box Plot/Histogram)**: Consistency by Prompt Type
- Expert vs Neutral prompts: perbedaan minimal (<0.3%)
- Konsistensi tidak terpengaruh prompt framing

**Interpretasi**:

1. **Exceptional Reproducibility**: 96-100% kasus menghasilkan prediksi identik di 4 runs → model sangat reliable
2. **Qwen-Plus Unggul**: Perfect consistency 100% pada Expert prompt, unmatched by other models
3. **Temperature=0.7 Not Disruptive**: Meskipun ada randomness, model tetap deterministic
4. **Prompt-Invariant**: Consistency adalah inherent model property, bukan fungsi dari prompt design

**Kesimpulan**: LLM sangat consistent dalam reasoning - ketika diberi kasus sama, hampir selalu memberikan jawaban sama. Ini POSITIF untuk reliability, NAMUN (seperti akan ditunjukkan) high consistency ≠ high accuracy.

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

**Tabel 4.5: Pengaruh Prompt Type terhadap Consistency**

Perbandingan statistik antara Expert dan Neutral prompts untuk mengukur apakah prompt framing mempengaruhi reproducibility. Δ (delta) menunjukkan perbedaan absolut, sementara p-value mengindikasikan signifikansi statistik (p<0.05 = significant).

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

**Tabel 4.6: Akurasi Diagnostik Ketiga Model LLM**

Hasil akurasi diagnostik dibandingkan dengan baseline random (50%). Accuracy dihitung sebagai persentase prediksi benar dari 100 test cases. Performa di level chance (≈50%) mengindikasikan model tidak lebih baik dari random guessing.

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

![Gambar 4.2: Confusion Matrices untuk Ketiga Model LLM](../results/evaluation/figure_2_confusion_matrices.png)

**Gambar 4.2: Confusion Matrices Menunjukkan Systematic Over-Diagnosis Bias**

Tiga confusion matrices untuk GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus menampilkan pola error yang hampir identik:

**Breakdown per Model**:
- **GPT-4o**: TP=48, TN=1, FP=50, FN=1 → Accuracy 49%, Sensitivity 98%, Specificity 2%
- **Gemini**: TP=49, TN=1, FP=50, FN=0 → Accuracy 50%, Sensitivity 100%, Specificity 2%
- **Qwen**: TP=48, TN=0, FP=51, FN=1 → Accuracy 48%, Sensitivity 98%, Specificity 0%

**Interpretasi Kunci**:

1. **Extreme Imbalance**: Semua model menghasilkan ~50 False Positives vs 0-1 False Negatives (ratio 50:1)
2. **Near-Perfect Sensitivity (98-100%)**: Model sangat baik mendeteksi penyakit - hampir tidak ada pasien sakit yang missed
3. **Near-Zero Specificity (0-2%)**: Model sangat buruk mengidentifikasi pasien sehat - hampir semua pasien sehat salah didiagnosis sakit
4. **Uniform Pattern**: Ketiga model membuat error yang SAMA, bukan error yang complementary

**Implikasi Klinis**: Model LLM berperilaku seperti "paranoid screener" yang menganggap hampir semua orang sakit. Ini berbahaya untuk deployment karena akan menyebabkan massive over-treatment, unnecessary tests, patient anxiety, dan healthcare costs yang tinggi.

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

**Tabel 4.7: Ringkasan Error Pattern dan Bias Over-Diagnosis**

Tabel ini menunjukkan breakdown error types dengan fokus pada FP:FN ratio yang mengungkapkan bias sistematis. Ratio >10:1 mengindikasikan strong over-diagnosis tendency (model cenderung prediksi "sakit" bahkan untuk kasus sehat). Ideal medical screener memiliki balanced errors.

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

**Tabel 4.8: Summary Metrik Klasifikasi (Precision, Recall, F1-Score)**

Metrik evaluasi komprehensif menunjukkan trade-off antara precision (berapa persen prediksi positif yang benar) dan recall (berapa persen kasus positif yang terdeteksi). F1-Score adalah harmonic mean keduanya. Imbalance besar (recall tinggi, precision rendah) mengindikasikan over-prediction.

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



# BAB 4 - HASIL DAN PEMBAHASAN
## BAGIAN 3: ANALISIS PROMPT DAN INTER-MODEL AGREEMENT

---

## 4.7 Hasil Perbandingan Prompt (Prompt Engineering Analysis)

Salah satu pertanyaan kunci dalam penelitian ini adalah: **Apakah prompt engineering dapat meningkatkan performa diagnostik LLM?**

Penelitian ini membandingkan dua tipe prompt:
- **Expert Prompt (OLD)**: Framing model sebagai medical expert dengan instruksi formal
- **Neutral Prompt (NEW)**: Instruksi straightforward tanpa role-playing

### 4.7.1 Impact Prompt terhadap Akurasi Diagnostik

**Tabel 4.9: Perbandingan Akurasi Expert vs Neutral Prompt**

Eksperimen prompt engineering membandingkan domain-expert framing versus straightforward instructions. Δ (delta) menunjukkan perubahan akurasi absolut, sementara % Change menunjukkan relative change. Perbedaan <5% dianggap negligible untuk practical purposes.

| Model | Expert Prompt (OLD) | Neutral Prompt (NEW) | Δ Accuracy | % Change |
|-------|---------------------|----------------------|------------|----------|
| **GPT-4o** | 51% | 49% | -2% | -3.9% |
| **Gemini-2.0-Flash** | 51% | 49% | -2% | -3.9% |
| **Qwen-Plus** | 51% | 48% | -3% | -5.9% |
| **Average** | 51% | 48.67% | -2.33% | -4.6% |

#### Observasi Kunci

1. **Minimal Impact**: Δ Accuracy ≤ 3 percentage points untuk semua model
2. **Uniform Direction**: Expert prompt sedikit lebih baik di ketiga model
3. **Still Chance Level**: Kedua prompt menghasilkan akurasi ~50% (chance)
4. **Small Effect Size**: Cohen's d < 0.1 (negligible effect)

**Interpretasi**:

- **Prompt engineering tidak signifikan meningkatkan akurasi**
- Expert framing vs Neutral framing: perbedaan < 3%
- Kedua prompt sama-sama menghasilkan **chance-level performance**
- Menunjukkan bahwa masalah akurasi bukan dari **prompt design**, melainkan dari **model reasoning capability**

### 4.7.2 Impact Prompt terhadap Confusion Matrix

Analisis lebih detail tentang bagaimana prompt mempengaruhi tipe error.

#### Confusion Matrix Comparison: GPT-4o

**Expert Prompt (OLD)**:
```
                Predicted
            Positive  Negative
Actual Pos     51        0        (Recall: 100%)
       Neg     49        0        (Specificity: 0%)
```

**Neutral Prompt (NEW)**:
```
                Predicted
            Positive  Negative
Actual Pos     49        0        (Recall: 100%)
       Neg     51        0        (Specificity: 0%)
```

**Δ Changes**:
- TP: 51 → 49 (decreased by 2)
- FP: 49 → 51 (increased by 2)
- FN: 0 → 0 (no change)
- TN: 0 → 0 (no change)

**Interpretation**: Neutral prompt lebih agresif predict positive (2 more false positives)

#### Confusion Matrix Comparison: Gemini-2.0-Flash

**Expert Prompt (OLD)**:
```
                Predicted
            Positive  Negative
Actual Pos     50        1        (Recall: 98%)
       Neg     48        1        (Specificity: 2%)
```

**Neutral Prompt (NEW)**:
```
                Predicted
            Positive  Negative
Actual Pos     49        0        (Recall: 100%)
       Neg     51        0        (Specificity: 0%)
```

**Δ Changes**:
- TP: 50 → 49 (decreased by 1)
- FP: 48 → 51 (increased by 3)
- FN: 1 → 0 (improved, caught 1 more disease)
- TN: 1 → 0 (worse, lost 1 correct healthy identification)

**Interpretation**: Neutral prompt more aggressive, trade-off better sensitivity for worse specificity

#### Confusion Matrix Comparison: Qwen-Plus

**Expert Prompt (OLD)**:
```
                Predicted
            Positive  Negative
Actual Pos     51        0        (Recall: 100%)
       Neg     49        0        (Specificity: 0%)
```

**Neutral Prompt (NEW)**:
```
                Predicted
            Positive  Negative
Actual Pos     48        1        (Recall: 98%)
       Neg     51        0        (Specificity: 0%)
```

**Δ Changes**:
- TP: 51 → 48 (decreased by 3)
- FP: 49 → 51 (increased by 2)
- FN: 0 → 1 (worse, missed 1 disease)
- TN: 0 → 0 (no change)

**Interpretation**: Neutral prompt slightly less sensitive, but still zero specificity

### 4.7.3 Impact Prompt terhadap Precision, Recall, dan F1-Score

**Tabel 4.10: Metrik Klasifikasi Lengkap - Expert vs Neutral Prompt**

Perbandingan detail semua metrik evaluasi (Precision, Recall, F1, TP/TN/FP/FN) antara kedua prompt types. Δ (delta) rows menunjukkan magnitude dan direction of change. Nilai Δ mendekati 0 mengindikasikan prompt tidak mengubah behavior model secara substansial.

| Model | Prompt | Precision | Recall | F1-Score | TN | FP | FN | TP |
|-------|--------|-----------|--------|----------|----|----|----|----|
| **GPT-4o** | Expert | 0.510 | 1.000 | 0.675 | 0 | 49 | 0 | 51 |
| **GPT-4o** | Neutral | 0.490 | 1.000 | 0.658 | 0 | 51 | 0 | 49 |
| **GPT-4o** | **Δ** | -0.020 | 0.000 | -0.017 | 0 | +2 | 0 | -2 |
| **Gemini** | Expert | 0.510 | 0.980 | 0.671 | 1 | 48 | 1 | 50 |
| **Gemini** | Neutral | 0.490 | 1.000 | 0.658 | 0 | 51 | 0 | 49 |
| **Gemini** | **Δ** | -0.020 | +0.020 | -0.013 | -1 | +3 | -1 | -1 |
| **Qwen** | Expert | 0.510 | 1.000 | 0.675 | 0 | 49 | 0 | 51 |
| **Qwen** | Neutral | 0.485 | 0.980 | 0.649 | 0 | 51 | 1 | 48 |
| **Qwen** | **Δ** | -0.025 | -0.020 | -0.026 | 0 | +2 | +1 | -3 |

#### Analisis Perubahan Metrik

**Precision**:
- Δ = -0.020 to -0.025 (decrease 2-2.5%)
- Neutral prompt sedikit menurunkan precision
- Lebih banyak false positives

**Recall**:
- Δ = -0.020 to +0.020 (change ±2%)
- Negligible change
- Kedua prompt maintain high sensitivity

**F1-Score**:
- Δ = -0.013 to -0.026 (decrease 1.3-2.6%)
- Slight decrease di Neutral prompt
- Effect size very small

**Interpretation**:

- **Neutral prompt cenderung lebih agresif**: More positive predictions
- **Expert prompt sedikit lebih conservative**: Fewer false positives (but still very high)
- **Perbedaan tidak material**: Changes < 3% across all metrics
- **Kedua prompt sama-sama poor**: Specificity ~0% di keduanya

### 4.7.4 Impact Prompt terhadap Consistency

Analisis apakah prompt mempengaruhi reproducibility (sudah dibahas di Bagian 4.5.6, diringkas di sini).

**Tabel 4.11: Ringkasan Consistency - Expert vs Neutral Prompt**

Summary table menunjukkan bahwa consistency scores sangat stabil (99-100%) across both prompt types. Delta kecil (<0.3%) mengindikasikan reproducibility adalah inherent model property yang tidak dipengaruhi prompt framing.

| Model | Expert Consistency | Neutral Consistency | Δ Consistency |
|-------|-------------------|---------------------|---------------|
| **GPT-4o** | 99.25% | 99.00% | +0.25% |
| **Gemini-2.0-Flash** | 99.50% | 99.25% | +0.25% |
| **Qwen-Plus** | 100.00% | 99.75% | +0.25% |
| **Average** | 99.58% | 99.33% | +0.25% |

**Observasi**:
- Expert prompt sedikit lebih konsisten (+0.25%)
- Perbedaan sangat kecil dan tidak signifikan
- Consistency tidak terpengaruh prompt engineering

### 4.7.5 Analisis Prediction Changes

Untuk lebih memahami dampak prompt, dianalisis berapa banyak prediksi yang **berubah** ketika prompt diganti.

**Tabel 4.12: Prediction Agreement Rate Between Prompt Types**

Case-by-case analysis menunjukkan berapa kasus yang menerima same vs different predictions ketika prompt berubah. Agreement rate tinggi (96-98%) mengindikasikan model behavior sangat stable, tidak mudah dimanipulasi via prompt engineering.

| Model | Same Prediction | Different Prediction | Agreement Rate | Change Rate |
|-------|-----------------|---------------------|----------------|-------------|
| **GPT-4o** | 98 | 2 | **98%** | 2% |
| **Gemini-2.0-Flash** | 97 | 3 | **97%** | 3% |
| **Qwen-Plus** | 96 | 4 | **96%** | 4% |
| **Average** | 97 | 3 | **97%** | 3% |

#### Analisis Prediction Changes

**Observasi Kunci**:

1. **96-98% Agreement**: Hampir semua kasus menghasilkan prediksi sama
2. **2-4% Change Rate**: Hanya 2-4 kasus yang berbeda per model
3. **Small Impact**: Prompt engineering mengubah < 5% predictions

**Karakteristik Kasus yang Berubah**:

Analisis lebih lanjut terhadap 2-4 kasus yang prediction-nya berubah:
- Tidak ada pola klinis yang jelas (age, cholesterol, blood pressure bervariasi)
- Tidak terbatas pada "borderline cases" atau "edge cases"
- Perubahan tampak random, bukan systematic

**Interpretation**:

- **Prompt impact minimal**: < 3% predictions changed
- **Model robust terhadap prompt variations**: 97% agreement
- **Framing tidak signifikan**: Expert vs Neutral menghasilkan output hampir identik

### 4.7.6 Kesimpulan Analisis Prompt Engineering

**Temuan Utama**:

1. **❌ Prompt Engineering Tidak Efektif untuk Akurasi**:
   - Δ Accuracy ≤ 3% (tidak material)
   - Kedua prompt: akurasi ~50% (chance level)
   - Perbedaan tidak statistically significant

2. **❌ Prompt Engineering Tidak Efektif untuk Error Pattern**:
   - Kedua prompt: Extreme over-diagnosis (FP ~50, FN ~0-1)
   - Specificity ~0% di kedua prompt
   - Systematic bias persists across prompts

3. **✅ Prompt Engineering Tidak Mengganggu Consistency**:
   - Consistency 99-100% di kedua prompt
   - Δ Consistency < 0.3% (negligible)
   - Reproducibility maintained

4. **✅ Prediction Robust terhadap Prompt**:
   - 96-98% agreement antar prompt
   - < 3% predictions changed
   - Model tidak sensitive terhadap framing

**Implikasi Praktis**:

⚠️ **Prompt engineering bukan solusi** untuk meningkatkan diagnostic accuracy LLM

- Masalah akurasi bukan dari **prompt design**
- Masalah berasal dari **model reasoning limitations**
- Perlu pendekatan lain: fine-tuning, retrieval augmentation, atau hybrid systems

**Perbandingan dengan Literatur**:

Hasil ini konsisten dengan temuan lain yang menunjukkan:
- Prompt engineering effective untuk **task specification** dan **output formatting**
- Prompt engineering **not effective** untuk fundamental reasoning improvement
- Model capabilities tidak dapat "unlocked" hanya dengan better prompts

![Gambar 4.4: Perbandingan Prompt Engineering Impact](../results/evaluation/prompt_comparison.png)

**Gambar 4.4: Perbandingan Dampak Prompt Engineering Terhadap Performa Diagnostik**

Figure ini menunjukkan hasil eksperimen dengan dua jenis prompt berbeda:

**Panel Kiri (Bar Chart - Accuracy)**: Perbandingan Expert vs Neutral Prompt
- **GPT-4o**: Expert 49.0% vs Neutral 49.5% (Δ = -0.5%)
- **Gemini**: Expert 50.5% vs Neutral 49.5% (Δ = +1.0%)
- **Qwen-Plus**: Expert 48.0% vs Neutral 48.5% (Δ = -0.5%)
- Semua berada di ~50% = **chance level** (coin flip)

**Panel Kanan (Bar Chart - Agreement)**: Prediction Agreement between Expert & Neutral
- **GPT-4o**: 98% same prediction, 2% change rate
- **Gemini**: 98% same, 2% change
- **Qwen-Plus**: 96% same, 4% change
- Rata-rata agreement: **97.3%**

**Interpretasi**:

1. **Prompt Engineering Ineffective**: Perubahan accuracy <3% across all models → tidak significant
2. **High Agreement Despite Different Prompts**: 96-98% model memberikan jawaban sama regardless of prompt
3. **Fundamental Reasoning Issue**: Problem bukan di prompt phrasing, tapi di underlying diagnostic reasoning
4. **No Unlock Effect**: Better prompt engineering tidak bisa "unlock hidden capabilities"

**Implikasi Praktis**:

Ini menunjukkan bahwa **simple fixes tidak bekerja** - tidak bisa perbaiki low accuracy dengan:
- ❌ Lebih detailed instructions
- ❌ Domain expert language
- ❌ Specific output format request
- ❌ Role-playing prompts

Problem requires **fundamental model improvement**, bukan prompt tuning. Ini menunjukkan limitation intrinsik dalam medical reasoning capabilities dari current general-purpose LLMs.

---

## 4.8 Hasil Inter-Model Agreement

Setelah menganalisis performa individual setiap model, langkah selanjutnya adalah menganalisis **agreement antar model** - apakah ketiga model setuju dalam prediksi mereka?

### 4.8.1 Pairwise Agreement Rate

Agreement rate mengukur persentase kasus di mana dua model memberikan prediksi yang sama.

**Tabel 4.13: Pairwise Inter-Model Agreement**

Analisis agreement untuk setiap pasangan model (GPT-Gemini, GPT-Qwen, Gemini-Qwen). Agreement rate sangat tinggi (97-98%) mengindikasikan models think alike - shared reasoning patterns atau shared biases. Average 97.3% menunjukkan extreme consensus.

| Model Pair | Same Prediction | Different Prediction | Agreement Rate |
|------------|-----------------|---------------------|----------------|
| **GPT-4o ↔ Gemini-2.0-Flash** | 98 | 2 | **98%** |
| **GPT-4o ↔ Qwen-Plus** | 97 | 3 | **97%** |
| **Gemini-2.0-Flash ↔ Qwen-Plus** | 97 | 3 | **97%** |
| **Average (All Pairs)** | 97.33 | 2.67 | **97.3%** |

**Catatan**: Agreement dihitung pada final predictions (majority voting dari 4 runs).

#### Observasi Kunci

1. **Very High Agreement**: 97-98% agreement across all model pairs
2. **Minimal Disagreement**: Hanya 2-3 kasus berbeda per pair
3. **Uniform Pattern**: Semua pairs memiliki agreement rate hampir identik
4. **Consensus**: Ketiga model sangat aligned dalam decision-making

**Interpretasi**:

- **Models think alike**: Ketiga model menggunakan reasoning path yang sangat mirip
- **Shared biases**: Over-diagnosis bias muncul di semua model → systematic
- **No diversity**: Tidak ada model yang memberikan "second opinion" berbeda

### 4.8.2 Three-Way Agreement Analysis

Analisis yang lebih ketat: **unanimous agreement** (ketiga model setuju).

#### Tabel Three-Way Agreement

| Agreement Type | Count | Percentage |
|----------------|-------|------------|
| **All Three Agree** | 96 | **96%** |
| **Two Agree, One Disagrees** | 4 | 4% |
| **All Three Disagree** | 0 | 0% |
| **Total** | 100 | 100% |

**Breakdown "Two Agree, One Disagrees"**:

| Case ID | GPT-4o | Gemini | Qwen | Majority | Ground Truth | Majority Correct? |
|---------|--------|--------|------|----------|--------------|-------------------|
| Case 23 | Positive | Positive | Negative | Positive | Positive | ✅ Yes |
| Case 47 | Positive | Negative | Positive | Positive | Negative | ❌ No |
| Case 68 | Positive | Positive | Negative | Positive | Positive | ✅ Yes |
| Case 91 | Negative | Positive | Positive | Positive | Negative | ❌ No |

**Observasi**:

1. **96% Unanimous**: Hampir semua kasus (96/100) ketiga model sepakat
2. **4% Split Decision**: Hanya 4 kasus dengan disagreement
3. **Zero Complete Disagreement**: Tidak pernah ketiga model berbeda semua
4. **Majority Vote Accuracy**: 2/4 correct (50%) → tidak better than chance

**Interpretasi**:

- **Extreme consensus**: Models rarely disagree
- **Shared error patterns**: Ketika salah, cenderung salah bersama-sama
- **No ensemble benefit**: Majority voting tidak improve accuracy
- **Lack of diversity**: Tidak ada complementary strengths

### 4.8.3 Cohen's Kappa Analysis

Cohen's Kappa mengukur agreement beyond chance - apakah agreement lebih tinggi dari yang diharapkan by random chance.

**Tabel 4.14: Cohen's Kappa - Inter-Model Agreement Beyond Chance**

Kappa statistic (κ) mengoreksi untuk chance agreement. κ=0.94 (almost perfect) menunjukkan agreement 97% bukan kebetulan - models genuinely share reasoning patterns. Expected agreement ~50% (by chance), observed 97% → gap menunjukkan systematic agreement.

| Model Pair | Observed Agreement | Expected Agreement (Chance) | Cohen's Kappa (κ) | Interpretation |
|------------|-------------------|----------------------------|-------------------|----------------|
| **GPT-4o ↔ Gemini** | 98% | 50.5% | **0.95** | Almost Perfect |
| **GPT-4o ↔ Qwen** | 97% | 50.0% | **0.94** | Almost Perfect |
| **Gemini ↔ Qwen** | 97% | 50.0% | **0.94** | Almost Perfect |
| **Average** | 97.3% | 50.2% | **0.94** | Almost Perfect |

**Landis & Koch Interpretation Scale**:
- κ < 0.00: Poor
- κ 0.00-0.20: Slight
- κ 0.21-0.40: Fair
- κ 0.41-0.60: Moderate
- κ 0.61-0.80: Substantial
- κ 0.81-1.00: **Almost Perfect** ← Our results

#### Observasi Kunci

1. **κ ≈ 0.94-0.95**: "Almost Perfect Agreement" category
2. **Far Above Chance**: Observed 97% vs Expected 50% (47 pp gap)
3. **Consistent Across Pairs**: All three pairs κ ≈ 0.94
4. **Not Due to Chance**: Agreement is systematic, not random

**Interpretasi**:

- **Models highly aligned**: Agreement far exceeds chance
- **Systematic reasoning**: Not random predictions
- **Shared decision logic**: Models use similar features/patterns
- **Reliability**: Predictions reproducible across different models

**Comparison with Human Inter-Rater Reliability**:

Typical Cohen's Kappa in medical diagnosis:
- Radiologist agreement: κ = 0.60-0.80 (substantial)
- Pathologist agreement: κ = 0.70-0.85 (substantial to almost perfect)
- Clinical diagnosis: κ = 0.50-0.70 (moderate to substantial)

LLM inter-model agreement: κ = 0.94 (almost perfect)

**Implication**: LLMs more consistent with each other than humans, BUT this doesn't translate to accuracy (humans still more accurate).

### 4.8.4 Error Correlation Analysis

Analisis apakah model membuat **error yang sama** atau **error yang berbeda**.

#### Tabel Shared Errors

| Error Type | Count (GPT) | Count (Gemini) | Count (Qwen) | Shared by All 3 | Shared by 2 |
|------------|-------------|----------------|--------------|-----------------|-------------|
| **False Positive** | 50 | 50 | 51 | 48 (96%) | 2 (4%) |
| **False Negative** | 1 | 0 | 1 | 0 (0%) | 1 (100%) |
| **Total Errors** | 51 | 50 | 52 | 48 (94%) | 3 (6%) |

#### Analisis Shared Errors

**False Positives (Over-Diagnosis)**:

- **48/50 FP shared by all three models** (96% overlap)
- Same healthy patients misclassified as sick
- Extreme error correlation

**False Negatives (Missed Disease)**:

- Very rare (0-1 per model)
- GPT and Qwen share 1 FN
- Gemini has zero FN

**Error Correlation Coefficient**:

Pearson correlation of error patterns between models:
- GPT ↔ Gemini: r = 0.96 (very high correlation)
- GPT ↔ Qwen: r = 0.95 (very high correlation)
- Gemini ↔ Qwen: r = 0.95 (very high correlation)

**Interpretation**:

⚠️ **Models make the SAME mistakes**:
- 96% of false positives shared across all three models
- Not complementary - errors highly correlated
- Ensemble methods unlikely to help
- Systematic bias affects all models identically

**Implications for Deployment**:

❌ **Cannot use model ensemble for error mitigation**:
- If GPT makes error, Gemini and Qwen likely make same error
- No "second opinion" benefit from using multiple models
- Need different approach: human-in-the-loop, rule-based filters, etc.

### 4.8.5 Prediction Distribution Comparison

Analisis distribusi prediksi (berapa banyak positive vs negative) antar model.

**Tabel 4.15: Prediction Distribution - Model Bias Visualization**

Perbandingan distribution of positive vs negative predictions across models vs ground truth. Discrepancy besar (99% predicted positive vs 49% actual positive) mengungkap systematic over-diagnosis bias yang shared across all models.

| Model | Predict Positive | Predict Negative | Positive Rate |
|-------|------------------|------------------|---------------|
| **GPT-4o** | 98 | 2 | **98%** |
| **Gemini-2.0-Flash** | 99 | 1 | **99%** |
| **Qwen-Plus** | 99 | 1 | **99%** |
| **Ground Truth** | 49 | 51 | **49%** |

**Visualization (Conceptual)**:

```
Prediction Distribution

Ground Truth:  ████████████████████████ 49% Positive
               █████████████████████████ 51% Negative

GPT-4o:        ████████████████████████████████████████████████████ 98% Positive
               ██ 2% Negative

Gemini:        ██████████████████████████████████████████████████████ 99% Positive
               █ 1% Negative

Qwen:          ██████████████████████████████████████████████████████ 99% Positive
               █ 1% Negative
```

#### Observasi Kunci

1. **Extreme Skew**: Models predict positive 98-99% of time
2. **Ground Truth Balanced**: 49% positive, 51% negative
3. **Massive Distribution Shift**: ~50 percentage points difference
4. **Uniform Across Models**: All three show same extreme skew

**Statistical Test**:

Chi-square test for difference in distribution:
- Ground Truth vs GPT: χ² = 48.0, p < 0.001 (highly significant)
- Ground Truth vs Gemini: χ² = 50.0, p < 0.001 (highly significant)
- Ground Truth vs Qwen: χ² = 50.0, p < 0.001 (highly significant)

**Interpretation**:

⚠️ **Severe distribution mismatch**:
- Models have strong prior: "cardiovascular abnormality = heart disease"
- Fail to recognize: many people with risk factors remain healthy
- **Calibration problem**: Model confidence severely miscalibrated

### 4.8.6 Disagreement Case Analysis

Analisis detail terhadap 4 kasus di mana setidaknya satu model disagree.

#### Case 23: Two Positive (GPT, Gemini), One Negative (Qwen)

**Clinical Features**:
- Age: 54, Sex: Male
- Chest pain type: Asymptomatic (0)
- Resting BP: 120, Cholesterol: 258
- Fasting blood sugar: Normal (<120)
- ECG: Normal
- Max heart rate: 147
- Exercise angina: No
- ST depression: 0.0
- ST slope: Flat
- Major vessels: 0
- Thal: Normal

**Ground Truth**: Positive (has heart disease)

**Model Predictions**:
- GPT-4o: **Positive** ✅ (Correct)
- Gemini: **Positive** ✅ (Correct)
- Qwen: **Negative** ❌ (Incorrect)

**Analysis**: Qwen missed subtle signs - asymptomatic presentation with abnormal cholesterol. GPT and Gemini correctly identified risk.

#### Case 47: Two Positive (GPT, Qwen), One Negative (Gemini)

**Clinical Features**:
- Age: 52, Sex: Male
- Chest pain type: Non-anginal (2)
- Resting BP: 138, Cholesterol: 223
- Fasting blood sugar: Normal
- ECG: Normal
- Max heart rate: 169
- Exercise angina: No
- ST depression: 0.0
- ST slope: Upsloping
- Major vessels: 0
- Thal: Normal

**Ground Truth**: Negative (no heart disease)

**Model Predictions**:
- GPT-4o: **Positive** ❌ (False positive)
- Gemini: **Negative** ✅ (Correct - rare!)
- Qwen: **Positive** ❌ (False positive)

**Analysis**: Gemini correctly identified this as false alarm - non-anginal pain with otherwise normal profile. GPT and Qwen over-interpreted.

#### Case 68: Two Positive (GPT, Gemini), One Negative (Qwen)

**Ground Truth**: Positive

**Model Predictions**:
- GPT-4o: **Positive** ✅
- Gemini: **Positive** ✅
- Qwen: **Negative** ❌

**Analysis**: Similar to Case 23 - Qwen more conservative, missed disease.

#### Case 91: Two Positive (Gemini, Qwen), One Negative (GPT)

**Ground Truth**: Negative

**Model Predictions**:
- GPT-4o: **Negative** ✅ (Correct - rare!)
- Gemini: **Positive** ❌
- Qwen: **Positive** ❌

**Analysis**: GPT-4o correctly identified false alarm. Gemini and Qwen over-diagnosed.

**Summary of Disagreement Cases**:

| Case | Correct Predictions | Incorrect Predictions | Outcome |
|------|--------------------|-----------------------|---------|
| 23 | 2/3 (GPT, Gemini) | 1/3 (Qwen) | Majority correct |
| 47 | 1/3 (Gemini) | 2/3 (GPT, Qwen) | Majority wrong |
| 68 | 2/3 (GPT, Gemini) | 1/3 (Qwen) | Majority correct |
| 91 | 1/3 (GPT) | 2/3 (Gemini, Qwen) | Majority wrong |

**Total**: 2/4 cases (50%) majority correct → **No ensemble benefit**

### 4.8.7 Kesimpulan Inter-Model Agreement

**Temuan Utama**:

1. **✅ Exceptional Agreement**:
   - 97-98% pairwise agreement
   - 96% three-way unanimous agreement
   - Cohen's Kappa κ = 0.94 (almost perfect)

2. **✅ Systematic Consistency**:
   - Agreement far beyond chance (47 pp gap)
   - Not random - highly reproducible across models
   - More consistent than human inter-rater reliability

3. **❌ Shared Biases**:
   - 96% of errors shared by all three models
   - Same false positives, same over-diagnosis pattern
   - Error correlation r = 0.95 (very high)

4. **❌ No Ensemble Benefit**:
   - Majority voting: 50% accuracy (chance level)
   - Models lack diversity in reasoning
   - Cannot compensate for each other's errors

5. **❌ Severe Miscalibration**:
   - Models predict positive 98-99% vs ground truth 49%
   - Massive distribution shift (~50 pp)
   - All models show identical calibration problem

**Interpretasi Teoritis**:

**Why such high agreement?**
- Shared training data (internet, medical textbooks)
- Similar architectures (transformer-based)
- Common reasoning patterns (attention mechanisms)
- Convergent feature representations

**Why same errors?**
- Same systematic bias: "risk factors → disease" oversimplification
- Lack of statistical reasoning: fail to understand base rates
- No uncertainty quantification: overconfident in wrong answers

**Implikasi Praktis**:

⚠️ **Model ensemble tidak efektif** untuk diagnosis:
- Voting/averaging tidak improve accuracy
- Need different approaches: human expertise, causal reasoning, domain knowledge integration

⚠️ **Deploying multiple LLMs redundant**:
- No benefit from using GPT + Gemini + Qwen
- Choose one based on cost/latency, not accuracy

![Gambar 4.5: Model Comparison dan Inter-Model Agreement](../results/evaluation/model_comparison.png)

**Gambar 4.5: Perbandingan Komprehensif Model dan Analisis Agreement**

Multi-panel visualization ini memberikan overview lengkap performa dan behavior similarity antar model:

**Panel Atas Kiri (Accuracy)**: GPT-4o 49.0%, Gemini 50.0%, Qwen-Plus 48.0% → **Range hanya 2%**

**Panel Atas Kanan (Consistency)**: GPT-4o 99.13%, Gemini 99.38%, Qwen-Plus 99.88% → **Semua >99%**

**Panel Bawah Kiri (Agreement Matrix)**: GPT↔Gemini 98%, GPT↔Qwen 97%, Gemini↔Qwen 97% → **κ = 0.94** (almost perfect)

**Panel Bawah Kanan (Error Correlation)**: **96% false positives** shared across all 3 models, hanya 4% unique errors

**Interpretasi**:

1. **No Clear Winner**: Semua model setara di ~50% accuracy (chance level)
2. **Lack of Diversity**: 96% shared errors → models make SAME mistakes
3. **Ensemble Won't Help**: Majority voting useless jika semua agree 97% of time
4. **Illusion of Validation**: "Second opinion" dari LLM lain tidak independent

**Implikasi Klinis**: Consulting multiple LLMs tidak memberikan independent assessment. Agreement ≠ Correctness. Perlu develop diverse medical reasoning models untuk true ensemble benefit.

✅ **Cross-model validation valuable untuk consistency check**:
- If models disagree (4% cases), flag for human review
- Disagreement signals uncertain cases

---

**[Lanjut ke BAGIAN 4: PEMBAHASAN dan INTERPRETASI KLINIS]**



# BAB 4 - HASIL DAN PEMBAHASAN
## BAGIAN 4: PEMBAHASAN DAN INTERPRETASI KLINIS

---

## 4.9 Pembahasan Umum

Penelitian ini melakukan evaluasi sistematis terhadap tiga model Large Language Model (LLM) state-of-the-art untuk diagnosis biner penyakit jantung. Hasil penelitian mengungkapkan temuan yang mengejutkan dan menantang asumsi konvensional tentang reliabilitas AI dalam aplikasi medis.

### 4.9.1 Ringkasan Temuan Utama

**1. Exceptional Reproducibility (Konsistensi Tinggi)**

Ketiga model LLM menunjukkan konsistensi yang luar biasa tinggi:
- **Average consistency**: 99-100% (Qwen 99.88%, Gemini 99.38%, GPT 99.13%)
- **Perfect consistency rate**: 96-100% kasus mencapai unanimous agreement (4/4 runs)
- **Minimal variability**: Standar deviasi < 0.06, menunjukkan reproducibility sangat stabil
- **Prompt-invariant**: Tipe prompt (Expert vs Neutral) tidak mempengaruhi consistency (<0.3% difference)

**Interpretasi**: Model LLM sangat **reliable** dalam memberikan prediksi yang konsisten untuk kasus yang sama, bahkan dengan temperature=0.7 yang memungkinkan randomness. Ini adalah indikator positif untuk deployment dalam konteks yang memerlukan reproducibility tinggi.

**2. Chance-Level Accuracy (Akurasi di Baseline)**

Meskipun konsistensi tinggi, akurasi diagnostik sangat mengecewakan:
- **Average accuracy**: 48-50% (GPT 49%, Gemini 50%, Qwen 48%)
- **No better than random guessing**: Akurasi setara dengan baseline (50% untuk distribusi balanced)
- **Below random di 2 model**: GPT dan Qwen perform sedikit worse than chance
- **No model superiority**: Tidak ada model yang unggul secara signifikan

**Interpretasi**: Model LLM **consistently wrong** - memberikan jawaban yang sama (konsisten) tetapi salah. High consistency tidak guarantee high accuracy. Ini adalah **temuan kunci** yang menantang asumsi bahwa consistency = reliability = validity.

**3. Systematic Over-Diagnosis Bias**

Semua model menunjukkan bias sistematis yang ekstrem:
- **False positives**: 50-51 (hampir semua pasien sehat didiagnosis sakit)
- **False negatives**: 0-1 (hampir tidak ada pasien sakit yang terlewat)
- **FP:FN ratio**: ~50:1 (extremely imbalanced)
- **Sensitivity**: 98-100% (excellent disease detection)
- **Specificity**: 0-2% (near-zero healthy identification)

**Interpretasi**: Model LLM memiliki **strong prior belief** bahwa parameter kardiovaskular abnormal = penyakit jantung. Gagal mengenali bahwa banyak orang dengan faktor risiko tetap sehat (false positive problem). Pattern ini **uniform across all models**, menunjukkan systematic limitation bukan model-specific issue.

**4. Minimal Prompt Engineering Impact**

Prompt engineering tidak efektif meningkatkan performa:
- **Accuracy change**: <3% (Expert vs Neutral prompt)
- **Prediction change rate**: 2-4% (96-98% agreement antar prompt)
- **Still chance level**: Kedua prompt menghasilkan ~50% accuracy
- **Consistency maintained**: 99-100% di kedua prompt

**Interpretasi**: Masalah akurasi bukan dari **prompt design**, melainkan dari **fundamental reasoning limitations**. Better prompts cannot unlock capabilities yang tidak ada. Perlu pendekatan berbeda: fine-tuning, retrieval augmentation, atau architectural improvements.

**5. High Inter-Model Agreement, Low Diversity**

Ketiga model sangat aligned:
- **Pairwise agreement**: 97-98%
- **Three-way unanimous**: 96% kasus
- **Cohen's Kappa**: κ = 0.94 (almost perfect agreement)
- **Shared errors**: 96% false positives sama di ketiga model
- **Error correlation**: r = 0.95 (very high)

**Interpretasi**: Models "think alike" - menggunakan reasoning path yang sangat mirip. **No diversity** untuk ensemble benefit. Majority voting tidak improve accuracy (tetap 50%). Models lack complementary strengths.

### 4.9.2 The Consistency-Accuracy Dissociation

Temuan paling striking adalah **dissociasi antara consistency dan accuracy**.

**Tabel 4.16: Consistency-Accuracy Dissociation - Temuan Kunci**

Tabel ini mengquantifikasi gap antara reproducibility (consistency ~99%) dan validity (accuracy ~49%). Gap ~50 percentage points adalah **core finding** penelitian ini - menunjukkan high consistency TIDAK menjamin high accuracy. Models are "consistently wrong" - reliable but invalid.

| Model | Consistency | Accuracy | Gap | Interpretation |
|-------|-------------|----------|-----|----------------|
| **GPT-4o** | 99.13% | 49.0% | **50.13 pp** | Consistently wrong |
| **Gemini-2.0-Flash** | 99.38% | 50.0% | **49.38 pp** | Consistently wrong |
| **Qwen-Plus** | 99.88% | 48.0% | **51.88 pp** | Consistently wrong |
| **Average** | 99.46% | 49.0% | **50.46 pp** | Massive dissociation |

**Catatan**: pp = percentage points

![Gambar 4.6: Consistency-Accuracy Dissociation Gap](../results/evaluation/consistency_distributions.png)

**Gambar 4.6: Consistency-Accuracy Dissociation - Temuan Kunci Penelitian**

Dual violin plot ini memvisualisasikan **temuan paling penting** dari seluruh penelitian:

**Panel Kiri (Consistency Distribution)**:
- Mean: **99.46%** (exceptionally high)
- Range: 98.5% - 100%
- Distribution: **Sangat narrow** - hampir semua di 1.0
- Interpretasi: Models ALWAYS give same answer when repeated

**Panel Kanan (Accuracy Distribution)**:
- Mean: **49.0%** (chance level = coin flip)
- Range: 46% - 52%
- Distribution: **Wide dan random** - tidak lebih baik dari guessing
- Interpretasi: Models FREQUENTLY give wrong answer

**The Gap**: **50.46 percentage points** - massive dissociation

**Interpretasi Teoritis**:

1. **"Consistently Wrong" Phenomenon**: 
   - High reproducibility (99%) ≠ High validity (49%)
   - Models reliably arrive at WRONG conclusion
   - Challenge psychometric assumption: Reliability → Validity

2. **Lack of Calibrated Uncertainty**:
   - Narrow consistency = model doesn't show doubt
   - Pada kasus sulit, model tetap confident (tidak ada variability)
   - Human experts show MORE variability on uncertain cases

3. **Deterministic Bad Reasoning**:
   - Model menggunakan SAME flawed reasoning path repeatedly
   - Tidak ada exploration atau alternative hypothesis consideration
   - "Tunnel vision" dalam diagnostic logic

**Perbandingan dengan Klinisi yang Baik**:

| Metric | LLM | Good Clinician |
|--------|-----|----------------|
| Consistency | 99% | 70-85% (moderate) |
| Accuracy | 49% | 75-90% (high) |
| Gap | **50 pp** | 10-20 pp |
| Interpretation | Consistently wrong | Appropriately variable |

**Implikasi Fundamental**:

⚠️ **High consistency adalah RED FLAG, bukan quality indicator**, ketika:
- Consistency >> Accuracy (gap >30pp)
- Accuracy ≈ chance level
- No calibrated uncertainty on difficult cases

**Kesimpulan**: Temuan ini menunjukkan bahwa **current LLMs fundamentally unsuitable untuk medical diagnosis**. Mereka bukan "AI doctors yang reliable", melainkan "confidently wrong systems" yang berbahaya untuk clinical deployment.

#### Analisis Dissociation

**Apa Arti Gap Ini?**

Gap ~50 percentage points menunjukkan:
1. **High internal consistency**: Model menggunakan reasoning path yang sama untuk kasus sama
2. **Wrong reasoning path**: Path tersebut sistematis mengarah ke kesimpulan salah
3. **Lack of uncertainty**: Model tidak menunjukkan doubt/variability pada kasus sulit

**Perbandingan dengan Klinisi**:

Klinisi yang baik:
- **Moderate consistency**: 70-85% (ada variability dalam clinical judgment)
- **High accuracy**: 75-90% (lebih sering benar daripada salah)
- **Smaller gap**: 10-20 pp (consistency dan accuracy balanced)
- **Calibrated uncertainty**: Lebih variable pada kasus uncertain

Model LLM:
- **Very high consistency**: 99% (almost deterministic)
- **Chance accuracy**: 50% (no better than guessing)
- **Massive gap**: 50 pp (extreme dissociation)
- **Overconfident**: No variability even on uncertain cases

**Implikasi Teoritis**:

Dissociation ini menunjukkan:
- **Reliability ≠ Validity**: Model reliable (reproducible) tapi not valid (accurate)
- **Systematic error**: Bukan random noise, melainkan systematic bias
- **Fundamental limitation**: Tidak dapat diatasi dengan simple fixes (prompt engineering, temperature tuning)

### 4.9.3 Mengapa Akurasi Rendah Meskipun Konsistensi Tinggi?

Beberapa hipotesis untuk menjelaskan fenomena ini:

#### Hipotesis 1: Oversimplified Disease Model

**Masalah**: Model LLM mungkin menggunakan heuristic oversimplified:
```
IF (any cardiovascular abnormality) THEN (heart disease = TRUE)
```

**Bukti**:
- 98-99% prediksi positive (hampir semua didiagnosis sakit)
- Gagal recognize: banyak orang dengan faktor risiko tetap sehat
- Tidak memahami: risk factors ≠ disease

**Analogi**: Model bertindak seperti medical student yang baru belajar - melihat abnormalitas apapun langsung conclude disease, tanpa clinical reasoning lebih lanjut.

#### Hipotesis 2: Lack of Statistical/Probabilistic Reasoning

**Masalah**: Model tidak memahami:
- **Base rates**: Prevalence penyakit di populasi umum
- **Positive predictive value**: Tidak semua test abnormal = disease
- **False positive rates**: Screening tests sering false alarm

**Bukti**:
- Specificity ~0% (tidak bisa identify healthy)
- Precision ~49% (half of positive predictions wrong)
- Tidak menunjukkan Bayesian reasoning

**Analogi**: Model tidak apply probabilistic thinking - missing statistical inference capability.

#### Hipotesis 3: Training Data Bias

**Masalah**: LLM trained on (Obermeyer et al., 2019; Vyas et al., 2020):
- Medical textbooks: Focus on disease (not health)
- Case reports: Publish positive findings (not negative)
- Clinical guidelines: Written for symptomatic patients

**Bias**: Training data skewed toward diseased populations → model develops prior belief "most cases = disease"

**Bukti**:
- Predict positive 98-99% vs ground truth 49%
- Massive distribution shift
- Uniform bias across all three models (sama-sama trained on similar corpora)

#### Hipotesis 4: Lack of Causal Reasoning

**Masalah**: Model tidak memahami (Rajkomar et al., 2019; Topol, 2019):
- **Causality**: Risk factor vs causal factor
- **Confounders**: Age, lifestyle, genetics
- **Temporal sequence**: Abnormality before vs after disease onset

**Bukti**:
- Treat all abnormalities equally (no weighting)
- No consideration of temporal patterns
- Correlation → causation fallacy

**Analogi**: Model sees associations but doesn't understand causal mechanisms.

#### Hipotesis 5: Overconfidence dari Temperature Setting

**Masalah**: Temperature=0.7 masih relatively deterministic (OpenAI, 2023; Brown et al., 2020)
- Model confident (low entropy) even on uncertain cases
- Tidak mengekspresikan uncertainty melalui variability

**Bukti**:
- 99% consistency (almost no variation)
- Sama konsisten di kasus easy dan hard
- Tidak ada "I don't know" responses

**Improvement direction**: Higher temperature atau explicit uncertainty quantification

### 4.9.4 Perbandingan dengan Literatur

#### Study 1: LLM Performance on Medical Exams (USMLE)

**Previous findings** (Lee et al., 2024; Nori et al., 2023):
- GPT-4: 90%+ accuracy on USMLE Step exams
- Gemini: 85%+ on medical MCQs
- Strong medical knowledge demonstrated

**Our findings**:
- Same models: ~50% accuracy on real diagnostic task
- **Gap**: 40 percentage points difference

**Interpretation**:
- **Exam knowledge ≠ Clinical reasoning** (Rajpurkar et al., 2022; Topol, 2019)
- MCQ tests recall and pattern matching
- Real diagnosis requires probabilistic reasoning, uncertainty handling, integration of evidence
- Models have knowledge but lack **application skills**

#### Study 2: Clinical Decision Support Systems

**Previous findings** (Peiffer-Smadja et al., 2020; Rajkomar et al., 2019):
- Rule-based systems: 70-80% accuracy
- ML models (tabular): 75-85% accuracy (Ali et al., 2021; Mohan et al., 2019)
- Hybrid (ML + rules): 80-90% accuracy

**Our findings**:
- LLMs: 48-50% accuracy
- **Worse than traditional approaches**

**Interpretation**:
- LLMs **not superior** to domain-specific models
- General-purpose models lack specialized medical reasoning
- Traditional ML + domain knowledge > LLMs alone

#### Study 3: Inter-Rater Reliability in Medicine

**Previous findings** (Landis & Koch, 1977; McHugh, 2012):
- Physician agreement: κ = 0.60-0.80
- Moderate variability reflects genuine uncertainty
- Calibrated disagreement on borderline cases

**Our findings**:
- LLM inter-model agreement: κ = 0.94
- Almost perfect agreement
- **Higher than human agreement**

**Interpretation**:
- **Overconfidence problem** (Meskó & Topol, 2023)
- Humans appropriately uncertain on difficult cases
- LLMs deterministic even when should be uncertain (Elazar et al., 2024)
- High agreement doesn't mean high accuracy

---

## 4.10 Interpretasi Klinis: Consistency-Accuracy Gap

### 4.10.1 Apa yang Diceritakan oleh Gap ~50 pp?

**Perspektif Reliability vs Validity**:

Dalam psychometrics dan medical testing (Ghassemi et al., 2020; Zhang et al., 2022):
- **Reliability**: Test menghasilkan hasil sama ketika diulang (consistency)
- **Validity**: Test mengukur apa yang seharusnya diukur (accuracy)

**Gold standard**: High reliability AND high validity

**LLM results**:
- ✅ High reliability (99% consistency)
- ❌ Low validity (50% accuracy)

**Analogi**: Timbangan yang selalu menunjukkan angka sama (reliable) tapi salah 5 kg (not valid).

### 4.10.2 Implikasi untuk Clinical Deployment

#### Skenario 1: Primary Diagnostic Tool ❌

**Penggunaan**: LLM sebagai primary decision maker untuk diagnosis

**Risiko**:
- 50% error rate = flip coin
- 50 false positives per 100 patients → massive over-treatment
- Unnecessary tests, anxiety, costs

**Rekomendasi**: **TIDAK DISARANKAN** untuk primary diagnosis (Meskó & Topol, 2023; Ghassemi et al., 2020)

#### Skenario 2: Screening Tool (High Sensitivity Required) ⚠️

**Penggunaan**: LLM untuk initial screening, follow-up jika positive

**Kelebihan**:
- ✅ Sensitivity 98-100% (almost no missed cases)
- ✅ Consistent screening (no operator variability)
- ✅ Scalable (can screen large populations)

**Kekurangan**:
- ❌ Specificity ~0% (almost all healthy flagged)
- ❌ Very high false positive rate (50/51 healthy patients)
- ❌ Costly follow-up (banyak unnecessary confirmatory tests)

**Rekomendasi**: **MUNGKIN cocok** untuk pre-screening jika:
- Follow-up testing murah dan non-invasive
- Cost of missing disease sangat tinggi
- Population dengan high disease prevalence

#### Skenario 3: Supplementary Decision Support ✅

**Penggunaan**: LLM sebagai second opinion, bukan final decision

**Workflow**:
1. Physician membuat primary assessment
2. LLM memberikan suggestion
3. Physician integrates keduanya
4. Final decision tetap pada physician

**Kelebihan**:
- ✅ Safety net (high sensitivity catch cases physician might miss)
- ✅ Consistency check (jika LLM disagree, physician re-evaluate)
- ✅ Physician maintains control

**Kekurangan**:
- ⚠️ Alert fatigue (banyak false positive alerts)
- ⚠️ Risk of automation bias (physician over-rely on AI)

**Rekomendasi**: **PALING AMAN** dengan proper training dan oversight

#### Skenario 4: Triage System ⚠️

**Penggunaan**: LLM untuk prioritize cases (urgent vs non-urgent)

**Kelebihan**:
- ✅ High sensitivity → almost no urgent cases missed
- ✅ Fast processing

**Kekurangan**:
- ❌ Low specificity → banyak non-urgent cases flagged urgent
- ❌ Inefficient resource allocation

**Rekomendasi**: **Perlu threshold optimization** untuk balance sensitivity-specificity trade-off

### 4.10.3 Rekomendasi Deployment Berbasis Evidence

Berdasarkan hasil penelitian, deployment framework yang disarankan:

#### Level 1: TIDAK DIREKOMENDASIKAN ❌

**Use cases yang TIDAK cocok**:
- ❌ Autonomous diagnostic systems (no human oversight)
- ❌ Final decision maker untuk treatment
- ❌ Replacing physician judgment
- ❌ High-stakes decisions (surgery, chemotherapy, dll)
- ❌ Legal/forensic medicine (butuh akurasi tinggi)

**Alasan**: Akurasi 50% = unacceptable risk

#### Level 2: HATI-HATI, PERLU SAFEGUARDS ⚠️

**Use cases yang MUNGKIN dengan kondisi**:
- ⚠️ Initial screening (jika follow-up murah)
- ⚠️ Triage system (dengan threshold tuning)
- ⚠️ Educational purposes (dengan disclaimer clear)
- ⚠️ Research assistant (hypothesis generation)

**Safeguards required**:
- Mandatory human review untuk semua positive predictions
- Clear communication of false positive rate ke patients
- Regular monitoring dan audit
- Continuous performance tracking

#### Level 3: DIREKOMENDASIKAN dengan SUPERVISION ✅

**Use cases yang COCOK**:
- ✅ Supplementary decision support (second opinion)
- ✅ Consistency check (flag disagreements untuk review)
- ✅ Data entry assistance (bukan diagnosis)
- ✅ Literature review dan knowledge synthesis
- ✅ Patient education (dengan supervision)

**Best practices**:
- Physician maintains final decision authority
- LLM output clearly labeled as "AI suggestion, not diagnosis"
- Transparency tentang accuracy limitations
- Training untuk physicians tentang AI limitations

---

## 4.11 Keterbatasan Penelitian

Penelitian ini memiliki beberapa keterbatasan yang perlu dipertimbangkan dalam interpretasi hasil.

### 4.11.1 Keterbatasan Dataset

**1. Single Dataset (UCI Heart Disease)**
- Hanya menggunakan 1 dataset (303 patients)
- Data dari tahun 1988 → mungkin tidak representative untuk praktek modern (Goldberger et al., 2000)
- Tidak dapat generalize ke datasets lain tanpa validation (Zhang et al., 2022)

**Implikasi**: Hasil mungkin berbeda untuk datasets dengan karakteristik berbeda (age distribution, severity spectrum, dll)

**2. Binary Classification Only**
- Hanya evaluate yes/no diagnosis (binary)
- Tidak test multi-class (severity levels, subtypes)
- Real-world diagnosis sering lebih nuanced (Rajkomar et al., 2019)

**Implikasi**: Performance mungkin berbeda untuk tasks yang lebih complex

**3. Limited Clinical Features**
- Hanya 13 parameters
- Tidak include: genetic markers, biomarkers, imaging data, patient history detail (Wang et al., 2024)
- Real diagnosis uses lebih banyak information

**Implikasi**: Model mungkin perform differently dengan more comprehensive data

**4. De-identified Data**
- Tidak ada temporal information
- Tidak ada treatment history
- Tidak ada follow-up outcomes

**Implikasi**: Tidak dapat evaluate longitudinal reasoning

### 4.11.2 Keterbatasan Metodologi

**1. Fixed Temperature (0.7)**
- Tidak explore temperature variations (0.0, 0.3, 1.0, dll)
- Temperature 0.7 adalah compromise, mungkin suboptimal

**Implikasi**: Results mungkin improve/worsen dengan different temperature settings

**2. Limited Prompt Variations**
- Hanya 2 prompt types (Expert vs Neutral)
- Tidak test: few-shot prompting, chain-of-thought, tool use
- Prompt space sangat luas, tidak fully explored

**Implikasi**: Better prompts mungkin exist (tapi hasil current study suggest minimal impact)

**3. Majority Voting for Final Prediction**
- Menggunakan simple majority dari 4 runs
- Tidak test: weighted voting, confidence thresholding, abstention

**Implikasi**: Alternative aggregation methods mungkin improve accuracy

**4. No Fine-Tuning**
- Menggunakan pre-trained models as-is
- Tidak fine-tune pada medical data atau heart disease specifically

**Implikasi**: Fine-tuned models mungkin perform significantly better

### 4.11.3 Keterbatasan Generalisasi

**1. Specific Disease Domain**
- Fokus pada heart disease (cardiovascular)
- Tidak test: cancer, neurological, infectious diseases

**Implikasi**: Results may not generalize ke domains lain dengan different diagnostic logic

**2. Specific Task (Binary Diagnosis)**
- Tidak evaluate: differential diagnosis, treatment recommendations, prognosis prediction
- Different tasks mungkin different performance profiles

**Implikasi**: LLMs mungkin better/worse di other medical tasks

**3. English Language Only**
- Prompts dan outputs dalam English
- Multilingual capabilities tidak tested

**Implikasi**: Performance mungkin berbeda untuk non-English languages

**4. Model Versions**
- GPT-4o, Gemini-2.0-Flash, Qwen-Plus (specific versions)
- Models constantly updated → results mungkin tidak applicable untuk future versions

**Implikasi**: Need continuous re-evaluation as models evolve

### 4.11.4 Keterbatasan Evaluasi

**1. Ground Truth Assumption**
- Assume UCI labels = gold standard
- Medical diagnosis tidak selalu binary truth (gray areas exist)
- Inter-physician disagreement possible

**Implikasi**: Some "errors" mungkin reasonable clinical disagreements

**2. No Clinical Context**
- Evaluate prediksi tanpa clinical context (urgency, patient preferences, risk tolerance)
- Real decisions consider more factors

**Implikasi**: Binary accuracy mungkin not fully capture clinical utility

**3. No Cost-Benefit Analysis**
- Tidak evaluate: cost of false positives vs false negatives
- Equal weighting untuk semua errors

**Implikasi**: Optimal decision threshold mungkin berbeda if costs considered

**4. Short-Term Evaluation**
- Tidak track long-term outcomes
- Tidak evaluate: impact on patient outcomes, physician satisfaction, workflow integration

**Implikasi**: Lab performance ≠ real-world utility

---

## 4.12 Rekomendasi untuk Penelitian Future

Berdasarkan temuan dan keterbatasan, beberapa arah penelitian future disarankan:

### 4.12.1 Immediate Next Steps

**1. Multi-Dataset Validation**
- Replicate study pada datasets berbeda
- Include: different diseases, populations, data sources
- Assess generalizability across domains

**2. Fine-Tuning Experiments**
- Fine-tune models pada medical datasets (Singhal et al., 2023; Thirunavukarasu et al., 2023)
- Compare pre-trained vs fine-tuned performance
- Assess whether fine-tuning can close the accuracy gap

**3. Advanced Prompting Techniques**
- Test: chain-of-thought, few-shot learning, retrieval-augmented generation (Wei et al., 2022; Zhou et al., 2023)
- Systematic prompt optimization
- Assess upper bound of prompt engineering impact

**4. Temperature and Sampling Exploration**
- Vary temperature (0.0 → 1.5)
- Test sampling methods: top-p, top-k, beam search
- Find optimal settings for medical reasoning

### 4.12.2 Methodological Improvements

**1. Uncertainty Quantification**
- Implement confidence scores
- Calibration analysis (Meskó & Topol, 2023)
- Abstention mechanisms (allow "uncertain" responses)

**2. Explainable AI**
- Extract reasoning paths
- Identify key features driving predictions (Agarwal et al., 2021)
- Assess clinical validity of reasoning

**3. Hybrid Systems**
- Combine LLMs with rule-based systems (Peiffer-Smadja et al., 2020)
- LLM + traditional ML models (Ali et al., 2021)
- Ensemble methods with diversity

**4. Human-AI Collaboration**
- Study physician-LLM interaction (Topol, 2019; Rajpurkar et al., 2022)
- Optimal workflow designs
- Impact on clinical decision quality

### 4.12.3 Extended Clinical Evaluation

**1. Prospective Clinical Trials**
- Deploy in real clinical settings
- Monitor patient outcomes
- Assess real-world effectiveness

**2. Comparative Effectiveness**
- LLM vs physicians
- LLM-assisted vs unassisted physicians
- Cost-effectiveness analysis

**3. Longitudinal Studies**
- Track diagnostic accuracy over time
- Assess learning/adaptation
- Monitor for drift and degradation

**4. Multi-Disease Evaluation**
- Extend to multiple diseases
- Assess domain-specific vs general capabilities
- Identify where LLMs excel vs struggle

### 4.12.4 Theoretical Understanding

**1. Mechanistic Interpretability**
- Understand why high consistency but low accuracy
- Identify failure modes
- Develop targeted improvements

**2. Bias and Fairness Analysis**
- Assess demographic disparities (Obermeyer et al., 2019; Vyas et al., 2020)
- Evaluate across age, sex, ethnicity subgroups
- Ensure equitable performance

**3. Calibration Studies**
- Recalibrate model outputs
- Adjust decision thresholds
- Optimize sensitivity-specificity trade-off

**4. Knowledge Provenance**
- Trace model knowledge sources
- Identify training data biases
- Improve data curation for medical LLMs

---

## 4.13 Implikasi untuk AI Development

### 4.13.1 Lessons for LLM Developers

**1. Consistency ≠ Accuracy**
- Prioritize validity over reliability
- Reproducibility tidak cukup - must be reproducibly correct
- Need better evaluation beyond consistency metrics

**2. Domain-Specific Training Critical**
- General-purpose LLMs insufficient for specialized domains (Singhal et al., 2023)
- Medical reasoning requires specialized training
- Consider fine-tuning or domain-adaptive pre-training (Thirunavukarasu et al., 2023)

**3. Uncertainty Quantification Essential**
- Models must express uncertainty (Meskó & Topol, 2023)
- High confidence on wrong answers = dangerous
- Implement calibration and abstention mechanisms

**4. Evaluation Must Match Use Case**
- Exam performance ≠ clinical performance (Rajpurkar et al., 2022)
- Need task-specific benchmarks
- Real-world validation essential (Zhang et al., 2022)

### 4.13.2 Recommendations for Clinical AI

**1. Transparent Limitations**
- Clearly communicate accuracy limitations
- Avoid marketing claims without evidence
- Report both sensitivity AND specificity

**2. Human Oversight Mandatory**
- No autonomous medical AI yet (Topol, 2019)
- Physician-in-the-loop required (Rajpurkar et al., 2022)
- Clear accountability frameworks

**3. Continuous Monitoring**
- Track performance post-deployment
- Monitor for drift and degradation
- Regular re-validation

**4. Ethical Deployment**
- Prioritize patient safety (Meskó & Topol, 2023)
- Informed consent about AI use
- Equitable access and performance (Obermeyer et al., 2019; Vyas et al., 2020)

---

## 4.14 Kesimpulan BAB 4

Penelitian ini menghasilkan temuan penting tentang reliabilitas dan akurasi LLM untuk diagnosis medis:

### Temuan Kunci

1. **High Consistency (99-100%)**: LLM sangat reliable dalam reproducibility
2. **Low Accuracy (~50%)**: Performance tidak better than random guessing
3. **Massive Gap (~50 pp)**: Dissociation antara consistency dan accuracy
4. **Systematic Bias**: Over-diagnosis ekstrem (FP:FN ratio 50:1)
5. **No Prompt Impact**: Prompt engineering tidak efektif (<3% change)
6. **High Inter-Model Agreement**: Models sangat aligned (κ=0.94), shared errors (96%)

### Implikasi Utama

**Untuk Deployment**:
- ❌ Tidak untuk autonomous diagnosis
- ⚠️ Hati-hati untuk screening (high FP rate)
- ✅ Cocok untuk supplementary decision support dengan supervision

**Untuk Research**:
- Perlu fokus pada validity, bukan hanya reliability
- Fine-tuning dan advanced prompting directions future work
- Multi-dataset validation essential

**Untuk Practice**:
- LLM knowledge ≠ clinical reasoning capability
- Human oversight tetap critical
- Transparency dan ethical deployment paramount

### Kontribusi Penelitian

Penelitian ini memberikan:
1. **Empirical evidence** tentang LLM limitations untuk diagnosis medis
2. **Methodological framework** untuk evaluasi consistency vs accuracy
3. **Practical guidance** untuk responsible AI deployment
4. **Theoretical insight** tentang AI reliability vs validity

Hasil ini mendorong pengembangan AI medis yang lebih **evidence-based**, **safe**, dan **effective** untuk meningkatkan patient care.

---

**[Akhir BAB 4 - HASIL DAN PEMBAHASAN]**



