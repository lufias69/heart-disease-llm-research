"""
Script untuk download dataset Heart Disease dari Kaggle
Alternatif jika Kaggle API tidak tersedia
"""

import os
import urllib.request
import zipfile

print("=" * 70)
print("DOWNLOAD DATASET HEART DISEASE")
print("=" * 70)

print("\n📋 INSTRUKSI DOWNLOAD MANUAL:")
print("\n1. Buka browser dan kunjungi:")
print("   https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data")
print("\n2. Login ke akun Kaggle (buat akun jika belum punya)")
print("\n3. Klik tombol 'Download' di halaman dataset")
print("\n4. Simpan file ZIP yang terdownload")
print("\n5. Extract file ZIP tersebut ke folder ini:")
print(f"   {os.path.dirname(os.getcwd())}")
print("\n6. Pastikan file 'heart.csv' ada di folder 'data'")

print("\n" + "=" * 70)
print("\n✓ Setelah download selesai, jalankan notebook:")
print("  notebooks/heart_disease_analysis.ipynb")
print("\n" + "=" * 70)

# Check if dataset already exists
data_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'heart.csv')
if os.path.exists(data_path):
    print("\n✓ Dataset 'data/heart.csv' sudah ada!")
    print("  Anda bisa langsung menjalankan analisis.")
else:
    print("\n⚠ Dataset belum tersedia.")
    print("  Silakan download mengikuti instruksi di atas.")
