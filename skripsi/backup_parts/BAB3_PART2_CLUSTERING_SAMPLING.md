# BAB 3 - METODOLOGI PENELITIAN
## BAGIAN 2: METODE CLUSTERING DAN SAMPLING

---

## 3.3 Metode Clustering

### 3.3.1 K-Means Clustering

Clustering merupakan tahap penting dalam penelitian ini untuk mengidentifikasi kelompok-kelompok alami dalam data sebelum melakukan stratified sampling. Tujuan utama clustering adalah untuk memastikan bahwa sampel yang dipilih untuk testing LLM **representatif** dan **beragam**, mencakup berbagai karakteristik klinis pasien.

#### Tujuan dan Prinsip K-Means

**K-Means Clustering** adalah algoritma unsupervised learning yang mempartisi data menjadi K kelompok (clusters) berdasarkan kesamaan fitur. Prinsip dasar K-Means adalah:

1. **Partisi Data**: Membagi dataset menjadi K kelompok yang saling eksklusif
2. **Kesamaan Intra-Cluster**: Sampel dalam satu cluster memiliki karakteristik yang mirip
3. **Perbedaan Inter-Cluster**: Sampel dari cluster berbeda memiliki karakteristik yang berbeda
4. **Optimasi Jarak**: Meminimalkan jarak total antara sampel dengan centroid cluster-nya

#### Algoritma K-Means

Algoritma K-Means bekerja secara iteratif dengan langkah-langkah sebagai berikut:

```
INPUT: Dataset X dengan n sampel dan d fitur, jumlah cluster K
OUTPUT: Label cluster untuk setiap sampel, posisi K centroids

1. INISIALISASI:
   - Pilih K centroid awal secara acak dari dataset
   - c₁, c₂, ..., cₖ = K centroids initial

2. REPEAT hingga konvergensi:
   
   a. ASSIGNMENT STEP:
      - Untuk setiap sampel xᵢ dalam dataset:
        * Hitung jarak ke semua K centroids
        * Assign xᵢ ke cluster dengan centroid terdekat
        * label(xᵢ) = argmin_{j} d(xᵢ, cⱼ)
   
   b. UPDATE STEP:
      - Untuk setiap cluster j:
        * Hitung centroid baru = rata-rata semua sampel di cluster j
        * cⱼ = (1/|Cⱼ|) Σ_{x∈Cⱼ} x
        * di mana Cⱼ = himpunan sampel di cluster j
   
   c. CHECK CONVERGENCE:
      - Jika posisi centroids tidak berubah: STOP
      - Jika perubahan < threshold epsilon: STOP
      - Jika iterasi maksimum tercapai: STOP
      - Else: CONTINUE to step 2a

3. RETURN:
   - Label cluster untuk setiap sampel
   - Posisi final K centroids
```

#### Persamaan Matematika K-Means

**1. Jarak Euclidean**

Jarak antara sampel $x$ dan centroid $c$ dihitung menggunakan jarak Euclidean:

$$d(x, c) = \sqrt{\sum_{i=1}^{n} (x_i - c_i)^2}$$

di mana:
- $d(x, c)$ = jarak Euclidean antara sampel $x$ dan centroid $c$
- $n$ = jumlah fitur (13 fitur dalam penelitian ini)
- $x_i$ = nilai fitur ke-$i$ dari sampel $x$
- $c_i$ = nilai fitur ke-$i$ dari centroid $c$

**Interpretasi**: Jarak Euclidean mengukur "perbedaan" keseluruhan antara profil klinis pasien dengan karakteristik tipikal cluster. Semakin kecil jarak, semakin mirip pasien dengan cluster tersebut.

**2. Fungsi Objektif (Inertia / Within-Cluster Sum of Squares)**

K-Means berusaha meminimalkan fungsi objektif yang disebut **Inertia**:

$$J = \sum_{j=1}^{K} \sum_{x \in C_j} \|x - \mu_j\|^2$$

di mana:
- $J$ = inertia (within-cluster sum of squares / WCSS)
- $K$ = jumlah cluster
- $C_j$ = himpunan sampel yang termasuk cluster ke-$j$
- $\mu_j$ = centroid cluster ke-$j$
- $\|x - \mu_j\|^2$ = kuadrat jarak Euclidean antara sampel $x$ dan centroid $\mu_j$

**Kegunaan Inertia**:
- Mengukur **kompakness** (kekompakan) cluster
- Nilai inertia kecil = cluster **tight** (sampel berkumpul dekat dengan centroid)
- Nilai inertia besar = cluster **loose** (sampel tersebar jauh dari centroid)
- Digunakan dalam **Elbow Method** untuk menentukan K optimal

**3. Centroid Update Formula**

Posisi centroid diperbarui sebagai rata-rata semua sampel dalam cluster:

$$\mu_j = \frac{1}{|C_j|} \sum_{x \in C_j} x$$

di mana:
- $\mu_j$ = centroid baru cluster ke-$j$
- $|C_j|$ = jumlah sampel dalam cluster $j$
- $\sum_{x \in C_j} x$ = jumlah (vector sum) dari semua sampel di cluster $j$

**Interpretasi**: Centroid merepresentasikan "pasien tipikal" dalam cluster tersebut dengan profil klinis rata-rata.

### 3.3.2 Penentuan Jumlah Cluster Optimal

Salah satu tantangan utama dalam K-Means adalah menentukan jumlah cluster optimal (K). Dalam penelitian ini, dilakukan **evaluasi komprehensif untuk K = 2 hingga K = 10** menggunakan **tiga metrik berbeda** untuk memastikan pemilihan K yang objektif dan tervalidasi.

#### A. Elbow Method (Metode Siku)

**Prinsip**: Elbow Method mencari titik "siku" pada grafik K vs Inertia, yaitu titik di mana penambahan cluster tidak lagi memberikan penurunan inertia yang signifikan.

**Prosedur**:
1. Jalankan K-Means untuk K = 2, 3, 4, ..., 10
2. Untuk setiap K, catat nilai inertia (J)
3. Plot grafik K (sumbu X) vs Inertia (sumbu Y)
4. Identifikasi titik "siku" di mana kurva mulai landai

**Interpretasi**:
- **Sebelum siku**: Penambahan cluster memberikan penurunan inertia yang besar (clustering lebih baik)
- **Di siku**: Titik optimal trade-off antara jumlah cluster dan kualitas clustering
- **Setelah siku**: Penambahan cluster hanya memberikan perbaikan marginal

**Prosedur Evaluasi**:
1. Jalankan K-Means untuk setiap nilai K dari 2 hingga 10
2. Untuk setiap K, catat nilai inertia yang dihasilkan
3. Plot grafik K vs Inertia untuk visualisasi
4. Hitung penurunan persentase inertia antar K berturutan
5. Identifikasi titik "siku" di mana penurunan mulai landai

> **📊 [HASIL EVALUASI ELBOW METHOD AKAN DITAMPILKAN DI BAB 4 - HASIL PENELITIAN]**
>
> Hasil berupa tabel nilai inertia untuk K=2 hingga K=10, grafik elbow, dan analisis titik siku akan disajikan dalam BAB 4 bagian Hasil Clustering.

**Visualisasi Konseptual**:
```
Inertia
  │
  │ ●
  │  ╲
  │   ●  ← "Siku" optimal
  │    ╲___
  │       ●─●─●─●─●─●─●
  │                     
  └─────────────────────── K
    2 3 4 5 6 7 8 9 10
```

#### B. Silhouette Score (Skor Siluet)

**Prinsip**: Silhouette Score mengukur seberapa baik setiap sampel cocok dengan cluster-nya sendiri dibandingkan dengan cluster terdekat lainnya.

**Persamaan**:

Untuk setiap sampel $i$, Silhouette coefficient dihitung sebagai:

$$s(i) = \frac{b(i) - a(i)}{\max\{a(i), b(i)\}}$$

di mana:
- $s(i)$ = Silhouette coefficient untuk sampel $i$
- $a(i)$ = rata-rata jarak intra-cluster (jarak ke sampel lain dalam cluster yang sama)
- $b(i)$ = rata-rata jarak inter-cluster (jarak ke sampel di cluster terdekat yang berbeda)

**Detail Perhitungan $a(i)$**:

$$a(i) = \frac{1}{|C_I| - 1} \sum_{j \in C_I, j \neq i} d(i, j)$$

di mana:
- $C_I$ = cluster yang berisi sampel $i$
- $|C_I|$ = jumlah sampel dalam cluster $I$
- $d(i, j)$ = jarak antara sampel $i$ dan $j$

**Detail Perhitungan $b(i)$**:

$$b(i) = \min_{J \neq I} \frac{1}{|C_J|} \sum_{j \in C_J} d(i, j)$$

di mana:
- $J$ = cluster lain (bukan cluster yang berisi $i$)
- $C_J$ = cluster terdekat (dengan rata-rata jarak terkecil)

**Silhouette Score Keseluruhan**:

$$\text{Silhouette Score} = \frac{1}{n} \sum_{i=1}^{n} s(i)$$

**Range dan Interpretasi**:
- **Range**: -1 hingga +1
- **$s(i) = +1$**: Sampel sangat cocok dengan cluster-nya (jauh dari cluster lain)
- **$s(i) = 0$**: Sampel berada di perbatasan antara dua cluster
- **$s(i) = -1$**: Sampel mungkin salah ditempatkan (lebih dekat dengan cluster lain)
- **Silhouette Score tinggi**: Clustering berkualitas baik (cluster compact dan well-separated)

> **📊 [HASIL EVALUASI SILHOUETTE SCORE AKAN DITAMPILKAN DI BAB 4 - HASIL PENELITIAN]**
>
> Hasil berupa tabel Silhouette Score untuk K=2 hingga K=10, grafik trend, dan interpretasi klinis akan disajikan dalam BAB 4 bagian Hasil Clustering.

#### C. Davies-Bouldin Index

**Prinsip**: Davies-Bouldin Index mengukur rata-rata "similarity" tertinggi antara setiap cluster dengan cluster yang paling mirip. Semakin kecil nilai index, semakin baik separasi antar cluster.

**Persamaan**:

$$DB = \frac{1}{K} \sum_{i=1}^{K} \max_{j \neq i} R_{ij}$$

di mana:

$$R_{ij} = \frac{S_i + S_j}{M_{ij}}$$

**Komponen Persamaan**:

1. **$S_i$**: Rata-rata jarak sampel dalam cluster $i$ ke centroid $i$
   $$S_i = \frac{1}{|C_i|} \sum_{x \in C_i} \|x - \mu_i\|$$

2. **$M_{ij}$**: Jarak antara centroid cluster $i$ dan cluster $j$
   $$M_{ij} = \|\mu_i - \mu_j\|$$

3. **$R_{ij}$**: Rasio similarity antara cluster $i$ dan $j$
   - Numerator ($S_i + S_j$): Total dispersion dalam kedua cluster
   - Denominator ($M_{ij}$): Separasi antar cluster
   - **$R_{ij}$ besar**: Cluster overlapping (dispersion tinggi, separasi rendah)
   - **$R_{ij}$ kecil**: Cluster well-separated (dispersion rendah, separasi tinggi)

**Range dan Interpretasi**:
- **Range**: 0 hingga $\infty$
- **DB = 0**: Clustering ideal (cluster sempurna terpisah dengan dispersi nol)
- **DB kecil**: Clustering baik (cluster compact dan terpisah jauh)
- **DB besar**: Clustering buruk (cluster overlapping atau dispersi tinggi)
- **Interpretasi**: Lebih kecil lebih baik (opposite dari Silhouette Score)

**Prosedur Evaluasi**:
1. Untuk setiap K, hitung dispersion ($S_i$) setiap cluster
2. Hitung separasi ($M_{ij}$) antar semua pasangan cluster
3. Hitung rasio $R_{ij}$ untuk semua kombinasi cluster
4. Davies-Bouldin Index = rata-rata dari maksimum $R_{ij}$ setiap cluster
5. Bandingkan DB Index antar nilai K untuk menentukan clustering terbaik

> **📊 [HASIL EVALUASI DAVIES-BOULDIN INDEX AKAN DITAMPILKAN DI BAB 4 - HASIL PENELITIAN]**
>
> Hasil berupa tabel Davies-Bouldin Index untuk K=2 hingga K=10, grafik trend, analisis perbaikan, dan interpretasi dengan metrik lain akan disajikan dalam BAB 4 bagian Hasil Clustering.

### 3.3.3 Keputusan Pemilihan K Optimal

Berdasarkan evaluasi komprehensif menggunakan tiga metrik berbeda, keputusan pemilihan jumlah cluster optimal dilakukan dengan mempertimbangkan konsensus dari ketiga metrik.

#### Prosedur Pengambilan Keputusan

**Langkah-langkah Keputusan**:

1. **Evaluasi Tiga Metrik**: Analisis hasil Elbow Method, Silhouette Score, dan Davies-Bouldin Index untuk K=2 hingga K=10
2. **Identifikasi Konsensus**: Tentukan nilai K yang direkomendasikan oleh mayoritas metrik (minimal 2 dari 3)
3. **Pertimbangan Interpretabilitas**: Evaluasi kemudahan interpretasi klinis untuk nilai K terpilih
4. **Trade-off Analysis**: Bandingkan kompleksitas model dengan peningkatan performa (marginal gain analysis)
5. **Validasi dengan Tujuan**: Pastikan K terpilih sesuai dengan tujuan sampling dan analisis berikutnya

**Kriteria Pemilihan**:

- **Konsensus Mayoritas**: Nilai K yang dipilih harus didukung oleh minimal 2 dari 3 metrik evaluasi
- **Interpretabilitas Klinis**: Jumlah cluster harus dapat diinterpretasikan dalam konteks klinis penyakit jantung
- **Perbaikan Marginal**: Jika K lebih tinggi hanya memberikan perbaikan marginal (< 5%), pilih K yang lebih sederhana
- **Prinsip Parsimoni**: Mengikuti Occam's Razor - pilih model paling sederhana yang memberikan hasil adequate
- **Tujuan Sampling**: K terpilih harus memfasilitasi stratified sampling yang efektif

> **📊 [HASIL PEMILIHAN K OPTIMAL AKAN DITAMPILKAN DI BAB 4 - HASIL PENELITIAN]**
>
> Hasil berupa tabel ringkasan evaluasi tiga metrik, konsensus keputusan, keputusan final K optimal dengan justifikasi lengkap, dan alasan pemilihan akan disajikan dalam BAB 4 bagian Hasil Clustering.

#### Prosedur Aplikasi Clustering dengan K Terpilih

Setelah K optimal ditentukan melalui evaluasi tiga metrik, clustering K-Means diaplikasikan pada dataset lengkap:

**Langkah-langkah Clustering Final**:

1. **Inisialisasi**: Jalankan K-Means dengan K terpilih dan random_state=42 untuk reproducibility
2. **Fitting**: Train model pada dataset lengkap (303 pasien dengan 13 fitur ternormalisasi)
3. **Assignment**: Assign setiap pasien ke cluster terdekat berdasarkan jarak Euclidean ke centroid
4. **Dokumentasi**: Simpan label cluster untuk setiap pasien dalam dataset untuk tahap sampling berikutnya

**Metrik Kualitas yang Dihitung**:

- **Inertia**: Total within-cluster sum of squares untuk mengukur kompakness
- **Silhouette Score**: Rata-rata skor siluet untuk mengukur separasi
- **Davies-Bouldin Index**: Rasio similarity antar cluster untuk validasi

> **📊 [HASIL CLUSTERING FINAL AKAN DITAMPILKAN DI BAB 4 - HASIL PENELITIAN]**
>
> Hasil berupa distribusi pasien per cluster, distribusi target (diagnosis sehat vs sakit) per cluster, interpretasi klinis karakteristik cluster, dan metrik kualitas clustering (inertia, silhouette, DB index) akan disajikan dalam BAB 4 bagian Hasil Clustering.

---

## 3.4 Metode Sampling Stratified

Setelah clustering, langkah selanjutnya adalah melakukan **stratified sampling** untuk memilih subset representatif dari dataset untuk testing LLM. Tujuan sampling adalah mendapatkan 100 kasus uji yang beragam dan mewakili variasi dalam dataset.

### 3.4.1 Strategi Sampling "Diverse"

Penelitian ini menggunakan **stratified random sampling dengan strategi "diverse"** untuk memilih sampel dari setiap cluster. Strategi ini dipilih untuk memastikan sampel tidak hanya representatif secara statistik, tetapi juga mencakup variasi karakteristik klinis dari yang tipikal hingga yang atipik.

#### Tujuan Sampling

1. **Representatif**: Sampel harus mewakili distribusi karakteristik dalam dataset
2. **Beragam**: Sampel harus mencakup berbagai tingkat keparahan dan profil klinis
3. **Seimbang**: Jumlah sampel dari setiap cluster sebanding dengan ukuran cluster
4. **Komprehensif**: Mencakup kasus dari yang dekat dengan centroid (typical) hingga yang jauh (edge cases)

#### Prinsip Strategi "Diverse"

Strategi "diverse" berbeda dari simple random sampling atau purposive sampling. Pendekatan ini menggunakan **kuintil jarak ke centroid** untuk memastikan sampel tersebar merata di seluruh spektrum karakteristik dalam cluster.

**Langkah-langkah Strategi "Diverse"**:

1. **Hitung Jarak ke Centroid**: Untuk setiap sampel dalam cluster, hitung jarak Euclidean ke centroid cluster
   $$d_i = \|x_i - \mu_c\|$$
   di mana $x_i$ = sampel, $\mu_c$ = centroid cluster

2. **Bagi menjadi 5 Kuintil**: Urutkan sampel berdasarkan jarak, lalu bagi menjadi 5 grup sama besar
   - **Kuintil 1** (0-20%): Sampel sangat dekat dengan centroid (most typical)
   - **Kuintil 2** (20-40%): Sampel cukup dekat
   - **Kuintil 3** (40-60%): Sampel jarak sedang
   - **Kuintil 4** (60-80%): Sampel agak jauh
   - **Kuintil 5** (80-100%): Sampel sangat jauh dari centroid (edge cases)

3. **Random Sampling per Kuintil**: Dari setiap kuintil, ambil sampel secara acak dengan jumlah sama
   - Untuk target n sampel per cluster: n/5 sampel per kuintil
   - Memastikan setiap range jarak terwakili

**Keunggulan Strategi "Diverse"**:

✅ **Mencakup Typical Cases**: Sampel dari kuintil 1-2 merepresentasikan kasus tipikal dalam cluster
✅ **Mencakup Edge Cases**: Sampel dari kuintil 4-5 merepresentasikan kasus atipik atau borderline
✅ **Mencegah Bias**: Tidak terfokus hanya pada centroid atau hanya pada outlier
✅ **Meningkatkan Generalisasi**: Testing LLM pada berbagai tingkat "typicality"

#### Formula Sampling Proportion

Jumlah sampel dari setiap cluster ditentukan secara proporsional dengan ukuran cluster:

$$n_i = \frac{N_i}{N} \times n$$

di mana:
- $n_i$ = jumlah sampel yang diambil dari cluster $i$
- $N_i$ = total sampel dalam cluster $i$
- $N$ = total sampel seluruh dataset
- $n$ = target jumlah sampel (100 dalam penelitian ini)

> **📊 [HASIL PERHITUNGAN PROPORSI SAMPLING AKAN DITAMPILKAN DI BAB 4 - HASIL PENELITIAN]**
>
> Hasil berupa perhitungan jumlah sampel per cluster berdasarkan proporsi ukuran cluster dan keputusan final alokasi sampel akan disajikan dalam BAB 4 bagian Hasil Sampling.

### 3.4.2 Implementasi Sampling

#### Prosedur Sampling untuk Setiap Cluster

Untuk setiap cluster yang dihasilkan dari clustering K-Means, prosedur berikut dijalankan:

```
INPUT: Cluster C dengan N sampel, target m sampel
OUTPUT: m sampel terpilih yang diverse

1. Hitung jarak setiap sampel ke centroid cluster
   untuk setiap x dalam C:
       d(x) = ||x - μ_C||
   
2. Urutkan sampel berdasarkan jarak (ascending)
   C_sorted = sort(C, by=d)

3. Bagi menjadi 5 kuintil
   Q1 = C_sorted[0:20%]      # Most typical
   Q2 = C_sorted[20%:40%]
   Q3 = C_sorted[40%:60%]
   Q4 = C_sorted[60%:80%]
   Q5 = C_sorted[80%:100%]   # Edge cases

4. Sampling random dari setiap kuintil
   untuk setiap Qi (i = 1, 2, 3, 4, 5):
       pilih m/5 sampel secara acak dari Qi
   
5. Gabungkan hasil sampling
   sampel_terpilih = Q1_sample + Q2_sample + ... + Q5_sample
   
6. RETURN sampel_terpilih (m sampel)
```

**Parameter Sampling**:

- **random_state = 42**: Untuk reproducibility hasil sampling
- **Jumlah kuintil = 5**: Pembagian standar untuk memastikan cakupan luas
- **Sampling per kuintil = seimbang**: Setiap kuintil berkontribusi sama besar
- **Metode sampling = random**: Dalam setiap kuintil, pilih sampel secara acak

> **📊 [HASIL SAMPLING AKAN DITAMPILKAN DI BAB 4 - HASIL PENELITIAN]**
>
> Hasil berupa total sampel terpilih, distribusi per cluster, distribusi target (ground truth diagnosis sehat vs sakit), analisis keseimbangan distribusi, dan variasi karakteristik sampel (rentang usia, jenis kelamin, chest pain type, severity, test results) akan disajikan dalam BAB 4 bagian Hasil Sampling.

### 3.4.3 Validasi Kualitas Sampling

Untuk memastikan sampling menghasilkan subset representatif, dilakukan validasi statistik dengan membandingkan distribusi sampel terhadap distribusi populasi asli.

#### Prosedur Validasi Kualitas Sampling

**1. Validasi Distribusi Fitur Numerik**:
- Hitung mean dan standar deviasi untuk fitur numerik (age, trestbps, chol, thalach) pada sampel dan dataset lengkap
- Bandingkan perbedaan mean dan standar deviasi antara sampel dan populasi
- **Kriteria**: Perbedaan < 5% menunjukkan sampel representatif

**2. Validasi Distribusi Fitur Kategorikal**:
- Hitung proporsi setiap kategori untuk fitur kategorikal (sex, cp, exang, dll.) pada sampel dan dataset lengkap
- Bandingkan perbedaan proporsi antara sampel dan populasi
- **Kriteria**: Perbedaan < 5% menunjukkan sampel representatif

**3. Kolmogorov-Smirnov Test**:
- Uji statistik untuk membandingkan distribusi sampel vs populasi
- **Null hypothesis**: Sampel berasal dari distribusi yang sama dengan populasi
- **Kriteria keputusan**: p-value > 0.05 → sampel representatif (gagal tolak H0)
- Dilakukan untuk fitur numerik utama: age, chol, thalach

**Formula Kolmogorov-Smirnov Statistic**:

$$D = \sup_x |F_n(x) - F(x)|$$

di mana:
- $D$ = KS statistic (supremum dari perbedaan absolut)
- $F_n(x)$ = fungsi distribusi kumulatif empiris dari sampel
- $F(x)$ = fungsi distribusi kumulatif dari populasi
- $\sup_x$ = supremum (nilai maksimum) untuk semua nilai x

> **📊 [HASIL VALIDASI KUALITAS SAMPLING AKAN DITAMPILKAN DI BAB 4 - HASIL PENELITIAN]**
>
> Hasil berupa tabel perbandingan distribusi fitur numerik (mean dan std) antara sampel vs dataset, tabel perbandingan distribusi fitur kategorikal (proporsi kategori) antara sampel vs dataset, hasil Kolmogorov-Smirnov Test dengan KS statistic dan p-value, dan kesimpulan validasi akan disajikan dalam BAB 4 bagian Hasil Sampling.

---

**[Lanjut ke BAGIAN 3: Model LLM dan Desain Prompt]**
