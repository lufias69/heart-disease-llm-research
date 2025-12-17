# LAPORAN ANALISIS DATA HEART DISEASE

**Tanggal Analisis**: 8 Desember 2025  
**Dataset**: Heart Disease Data (Sample)  
**Sumber**: https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data

---

## 📊 RINGKASAN EKSEKUTIF

Analisis ini dilakukan terhadap dataset penyakit jantung yang berisi 303 sampel dengan 14 fitur medis. Tujuan utama adalah memahami karakteristik data dan mengidentifikasi faktor-faktor yang berkorelasi dengan penyakit jantung.

---

## 1. INFORMASI DATASET

### Karakteristik Dasar
- **Total Sampel**: 303 pasien
- **Total Fitur**: 14 variabel
- **Missing Values**: 0 (dataset bersih)
- **Data Duplikat**: 0
- **Tipe Data**: 13 integer, 1 float

### Daftar Fitur
1. **age** - Usia pasien (tahun)
2. **sex** - Jenis kelamin (0=perempuan, 1=laki-laki)
3. **cp** - Tipe nyeri dada (0-3)
4. **trestbps** - Tekanan darah istirahat (mm Hg)
5. **chol** - Kolesterol serum (mg/dl)
6. **fbs** - Gula darah puasa > 120 mg/dl (0=tidak, 1=ya)
7. **restecg** - Hasil elektrokardiografi istirahat (0-2)
8. **thalach** - Detak jantung maksimum
9. **exang** - Angina akibat olahraga (0=tidak, 1=ya)
10. **oldpeak** - Depresi ST
11. **slope** - Kemiringan segmen ST puncak
12. **ca** - Jumlah pembuluh darah mayor (0-4)
13. **thal** - Thalassemia (0-3)
14. **target** - Penyakit jantung (0=tidak, 1=ya)

---

## 2. DISTRIBUSI TARGET VARIABLE

### Keseimbangan Kelas
- **Target 0 (Tidak Sakit)**: 146 pasien (48.18%)
- **Target 1 (Sakit)**: 157 pasien (51.82%)

**Kesimpulan**: Dataset cukup seimbang dengan distribusi hampir 50:50, yang baik untuk pemodelan machine learning.

---

## 3. STATISTIK DESKRIPTIF

### Fitur Utama (Mean ± Std)

| Fitur | Mean | Std | Min | Max |
|-------|------|-----|-----|-----|
| **age** | 52.95 ± 14.37 | 29 | 77 |
| **trestbps** | 146.36 ± 31.11 | 94 | 199 |
| **chol** | 352.03 ± 128.48 | 126 | 563 |
| **thalach** | 136.08 ± 39.04 | 71 | 201 |
| **oldpeak** | 3.11 ± 1.80 | 0.0 | 6.2 |

### Distribusi Kategorikal
- **Sex**: 55% laki-laki, 45% perempuan
- **Chest Pain Type (cp)**: Mean = 1.43 (variasi 0-3)
- **Fasting Blood Sugar (fbs)**: 48% memiliki fbs > 120 mg/dl

---

## 4. ANALISIS KORELASI

### Korelasi dengan Target (Top 5)

1. **chol** (Kolesterol): 0.091
2. **restecg** (ECG): 0.084
3. **trestbps** (Tekanan Darah): 0.060
4. **slope**: 0.059
5. **sex**: 0.040

**⚠️ CATATAN**: Ini adalah sample data random untuk demonstrasi. Pada dataset asli, korelasi akan berbeda dan lebih bermakna.

### Insight Korelasi
- Korelasi antara fitur dengan target relatif rendah pada sample data ini
- Perlu analisis lebih mendalam dengan dataset asli
- Beberapa fitur menunjukkan korelasi positif dengan penyakit jantung

---

## 5. ANALISIS OUTLIERS

### Deteksi Outliers (Metode IQR)
- Tidak ditemukan outliers signifikan dalam sample data ini
- Semua nilai berada dalam range yang wajar
- Distribusi data cukup normal

---

## 6. VISUALISASI YANG DIHASILKAN

### File Visualisasi
1. **01_target_distribution.png** - Distribusi target variable
2. **02_correlation_matrix.png** - Heatmap korelasi antar fitur
3. **03_feature_distributions.png** - Histogram semua fitur
4. **04_box_plots.png** - Box plot untuk deteksi outliers
5. **05_target_correlation.png** - Bar chart korelasi dengan target
6. **06_features_by_target.png** - Perbandingan distribusi per target

---

## 7. KEY FINDINGS

### ✅ Kualitas Data
- Dataset bersih tanpa missing values
- Tidak ada duplikasi data
- Distribusi target seimbang

### 📈 Karakteristik Pasien
- Rata-rata usia: ~53 tahun
- Rentang usia: 29-77 tahun
- Mayoritas laki-laki (55%)

### 🔍 Faktor Risiko Potensial
- Kolesterol tinggi (mean: 352 mg/dl)
- Tekanan darah bervariasi (94-199 mm Hg)
- Detak jantung maksimum bervariasi luas

---

## 8. REKOMENDASI

### Untuk Analisis Lanjutan
1. **Download Dataset Asli** dari Kaggle untuk analisis yang lebih akurat
2. **Feature Engineering**:
   - Buat kategori usia (muda, dewasa, tua)
   - Normalisasi fitur numerik
   - Encode fitur kategorikal
3. **Analisis Mendalam**:
   - Analisis survival
   - Segmentasi pasien (clustering)
   - Identifikasi profil risiko tinggi

### Untuk Machine Learning
1. **Preprocessing**:
   - Feature scaling (StandardScaler/MinMaxScaler)
   - Train-test split (80:20 atau 70:30)
   - Cross-validation (K-Fold)

2. **Model Recommendation**:
   - Logistic Regression (baseline)
   - Random Forest
   - XGBoost/LightGBM
   - Neural Networks
   - Ensemble methods

3. **Evaluasi**:
   - Accuracy, Precision, Recall, F1-Score
   - ROC-AUC curve
   - Confusion Matrix
   - Feature importance

---

## 9. CATATAN PENTING

⚠️ **DISCLAIMER**: 
- Analisis ini menggunakan **SAMPLE DATA** yang di-generate secara random untuk demonstrasi
- Untuk analisis yang akurat dan insight yang bermakna, gunakan **DATASET ASLI** dari Kaggle
- Sample data ini hanya untuk menunjukkan workflow dan metodologi analisis

### Cara Mendapatkan Dataset Asli
1. Kunjungi: https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data
2. Login ke akun Kaggle
3. Download dataset
4. Replace file `heart.csv` dengan dataset asli
5. Jalankan ulang analisis

---

## 10. FILES YANG TERSEDIA

### Script Python
- `analyze.py` - Script analisis lengkap
- `create_sample_data.py` - Generator sample data
- `download_dataset.py` - Helper untuk download

### Notebook
- `heart_disease_analysis.ipynb` - Jupyter notebook interaktif

### Data
- `heart.csv` - Dataset (sample/asli)

### Visualisasi
- 6 file PNG dengan berbagai visualisasi

### Dokumentasi
- `README.md` - Panduan setup
- `ANALYSIS_REPORT.md` - Laporan ini
- `requirements.txt` - Dependencies

---

## 📞 KONTAK & REFERENSI

**Dataset Source**: https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data

**Referensi**:
- UCI Machine Learning Repository - Heart Disease Dataset
- Cleveland Clinic Foundation
- Hungarian Institute of Cardiology
- V.A. Medical Center, Long Beach and Cleveland Clinic Foundation

---

**Generated by**: Heart Disease Analysis Script  
**Date**: December 8, 2025  
**Version**: 1.0
