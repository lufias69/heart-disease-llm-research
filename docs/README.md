# Analisis Data Heart Disease

Dataset dari: https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download Dataset

**Opsi A: Manual Download**
1. Kunjungi https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data
2. Klik tombol "Download"
3. Extract file ZIP ke folder ini
4. Pastikan file `heart.csv` ada di folder yang sama dengan notebook

**Opsi B: Menggunakan Kaggle API** (jika sudah setup)
```bash
kaggle datasets download -d redwankarimsony/heart-disease-data
unzip heart-disease-data.zip
```

### 3. Setup Kaggle API (Optional)
Jika ingin menggunakan Kaggle API:
1. Buat account di Kaggle.com
2. Masuk ke Account Settings → API → Create New API Token
3. Download file `kaggle.json`
4. Simpan di `~/.kaggle/kaggle.json` (Linux/Mac) atau `C:\Users\<username>\.kaggle\kaggle.json` (Windows)

## Menjalankan Analisis

1. Buka Jupyter Notebook:
```bash
jupyter notebook
```

2. Atau jalankan di VS Code:
   - Buka file `heart_disease_analysis.ipynb`
   - Pilih Python kernel
   - Jalankan cell satu per satu

## Struktur Analisis

1. **Import Libraries** - Setup environment
2. **Load Dataset** - Membaca data
3. **Eksplorasi Data Awal** - Info, missing values, duplikat
4. **Statistik Deskriptif** - Analisis statistik dasar
5. **Visualisasi Data** - Distribusi dan box plots
6. **Analisis Korelasi** - Correlation matrix
7. **Analisis Target** - Perbandingan berdasarkan target
8. **Analisis Kategorikal** - Variabel kategorikal
9. **Insight dan Kesimpulan** - Ringkasan temuan
10. **Rekomendasi** - Langkah selanjutnya

## Dataset Information

Dataset ini berisi data terkait penyakit jantung dengan berbagai fitur medis seperti:
- Age (Usia)
- Sex (Jenis Kelamin)
- Chest Pain Type
- Blood Pressure
- Cholesterol
- Dan fitur lainnya

Target variable menunjukkan ada/tidaknya penyakit jantung.
