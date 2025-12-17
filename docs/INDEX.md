# 🫀 Heart Disease Data Analysis

Proyek analisis data penyakit jantung menggunakan dataset dari Kaggle.

## 📁 Struktur Project

```
heart-disease/
├── 📊 DATA
│   └── heart.csv                    # Dataset (303 samples, 14 features)
│
├── 📓 NOTEBOOKS & SCRIPTS
│   ├── heart_disease_analysis.ipynb # Jupyter notebook interaktif
│   ├── analyze.py                   # Script analisis lengkap
│   ├── create_sample_data.py        # Generator sample data
│   └── download_dataset.py          # Helper download dataset
│
├── 📈 VISUALISASI (PNG files)
│   ├── 01_target_distribution.png   # Distribusi target
│   ├── 02_correlation_matrix.png    # Heatmap korelasi
│   ├── 03_feature_distributions.png # Histogram fitur
│   ├── 04_box_plots.png             # Box plots outliers
│   ├── 05_target_correlation.png    # Korelasi dengan target
│   └── 06_features_by_target.png    # Perbandingan per target
│
├── 📄 DOKUMENTASI
│   ├── README.md                    # Panduan setup
│   ├── ANALYSIS_REPORT.md           # Laporan lengkap
│   ├── INDEX.md                     # File ini
│   └── SUMMARY.py                   # Ringkasan hasil
│
└── 📦 DEPENDENCIES
    └── requirements.txt             # Python packages
```

---

## 🚀 Quick Start

### 1. Lihat Ringkasan Hasil
```bash
python SUMMARY.py
```

### 2. Jalankan Analisis Lengkap
```bash
python analyze.py
```

### 3. Buka Jupyter Notebook
```bash
jupyter notebook heart_disease_analysis.ipynb
```

---

## 📊 Ringkasan Hasil

### Dataset Overview
- **303 samples** dengan **14 features**
- **Tidak ada missing values** ✓
- **Target balanced**: 48% vs 52%

### Key Statistics
- Rata-rata usia: **52.95 tahun**
- Tekanan darah: **146.36 mm Hg**
- Kolesterol: **352.03 mg/dl**
- Max heart rate: **136.08 bpm**

### Fitur-Fitur
1. Age, Sex, Chest Pain Type
2. Blood Pressure, Cholesterol
3. Fasting Blood Sugar, ECG
4. Max Heart Rate, Exercise Angina
5. ST Depression, Slope
6. Major Vessels, Thalassemia
7. **Target** (Heart Disease)

---

## 📈 Visualisasi Tersedia

| File | Deskripsi |
|------|-----------|
| `01_target_distribution.png` | Distribusi penyakit jantung (ya/tidak) |
| `02_correlation_matrix.png` | Korelasi antar semua fitur |
| `03_feature_distributions.png` | Distribusi 14 fitur |
| `04_box_plots.png` | Deteksi outliers |
| `05_target_correlation.png` | Fitur yang berkorelasi dengan target |
| `06_features_by_target.png` | Perbandingan fitur per target |

---

## 🔍 Workflow Analisis

```
1. Data Loading
   ↓
2. Data Exploration
   • Shape, types, missing values
   • Descriptive statistics
   ↓
3. Data Visualization
   • Distributions
   • Correlations
   • Comparisons
   ↓
4. Statistical Analysis
   • Correlation matrix
   • Outlier detection
   • Feature relationships
   ↓
5. Insights & Conclusions
   • Key findings
   • Recommendations
```

---

## 🎯 Next Steps

### Untuk Analisis Lebih Lanjut
- [ ] Download dataset asli dari Kaggle
- [ ] Feature engineering
- [ ] Feature selection
- [ ] Handle outliers (jika ada)

### Untuk Machine Learning
- [ ] Data preprocessing
  - Feature scaling
  - Encoding
  - Train-test split
- [ ] Model training
  - Logistic Regression
  - Random Forest
  - XGBoost
  - Neural Networks
- [ ] Model evaluation
  - Cross-validation
  - Metrics (Accuracy, Precision, Recall, F1, ROC-AUC)
  - Feature importance
- [ ] Model deployment

---

## 📚 Dokumentasi Lengkap

### Untuk Detail Lengkap
Baca: **[ANALYSIS_REPORT.md](ANALYSIS_REPORT.md)**

Isi laporan:
1. Ringkasan Eksekutif
2. Informasi Dataset
3. Distribusi Target
4. Statistik Deskriptif
5. Analisis Korelasi
6. Analisis Outliers
7. Visualisasi
8. Key Findings
9. Rekomendasi
10. Referensi

---

## 🔗 Links & Resources

- **Dataset**: https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data
- **UCI ML Repository**: https://archive.ics.uci.edu/ml/datasets/heart+disease
- **Python**: pandas, numpy, matplotlib, seaborn, scikit-learn

---

## ⚠️ Important Notes

**DISCLAIMER**: Analisis ini menggunakan **sample data** untuk demonstrasi. Untuk hasil yang akurat dan insight yang bermakna:

1. Download dataset asli dari Kaggle
2. Replace file `heart.csv`
3. Jalankan ulang analisis

---

## 🛠️ Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
```

Install dengan:
```bash
pip install -r requirements.txt
```

---

## 📧 Contact & Support

Untuk pertanyaan atau masalah, silakan:
- Cek dokumentasi di folder ini
- Review ANALYSIS_REPORT.md untuk detail
- Jalankan SUMMARY.py untuk ringkasan

---

**Last Updated**: December 8, 2025  
**Version**: 1.0  
**Status**: ✓ Analysis Complete
