"""
Script untuk membuat sample data Heart Disease untuk testing
Jika dataset asli belum didownload
"""

import pandas as pd
import numpy as np

print("Membuat sample data Heart Disease...")

# Set random seed untuk reproducibility
np.random.seed(42)

# Jumlah sampel
n_samples = 303

# Generate sample data
data = {
    'age': np.random.randint(29, 78, n_samples),
    'sex': np.random.choice([0, 1], n_samples),  # 0=female, 1=male
    'cp': np.random.choice([0, 1, 2, 3], n_samples),  # chest pain type
    'trestbps': np.random.randint(94, 200, n_samples),  # resting blood pressure
    'chol': np.random.randint(126, 564, n_samples),  # serum cholesterol
    'fbs': np.random.choice([0, 1], n_samples),  # fasting blood sugar > 120 mg/dl
    'restecg': np.random.choice([0, 1, 2], n_samples),  # resting ECG results
    'thalach': np.random.randint(71, 202, n_samples),  # max heart rate achieved
    'exang': np.random.choice([0, 1], n_samples),  # exercise induced angina
    'oldpeak': np.random.uniform(0, 6.2, n_samples).round(1),  # ST depression
    'slope': np.random.choice([0, 1, 2], n_samples),  # slope of peak exercise ST
    'ca': np.random.choice([0, 1, 2, 3, 4], n_samples),  # number of major vessels
    'thal': np.random.choice([0, 1, 2, 3], n_samples),  # thalassemia
    'target': np.random.choice([0, 1], n_samples, p=[0.46, 0.54])  # 0=no disease, 1=disease
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('../data/heart.csv', index=False)

print(f"✓ Sample data berhasil dibuat!")
print(f"  File: data/heart.csv")
print(f"  Jumlah baris: {len(df)}")
print(f"  Jumlah kolom: {len(df.columns)}")
print(f"\n  Kolom: {', '.join(df.columns.tolist())}")
print(f"\n⚠ CATATAN: Ini adalah sample data untuk testing.")
print(f"  Untuk analisis nyata, download dataset asli dari Kaggle.")
