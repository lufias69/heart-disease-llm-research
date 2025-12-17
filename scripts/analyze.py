"""
Analisis Data Heart Disease - Python Script Version
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('husl')

print("="*70)
print("ANALISIS DATA HEART DISEASE")
print("="*70)

# Load dataset
print("\n1. LOADING DATASET...")
df = pd.read_csv('../data/heart.csv')
print(f"✓ Dataset loaded successfully!")
print(f"  Shape: {df.shape}")

# Basic info
print("\n2. INFORMASI DATASET:")
print(f"  - Total sampel: {len(df)}")
print(f"  - Total fitur: {len(df.columns)}")
print(f"  - Missing values: {df.isnull().sum().sum()}")
print(f"  - Data duplikat: {df.duplicated().sum()}")

# Display columns
print(f"\n  Kolom-kolom:")
for i, col in enumerate(df.columns, 1):
    print(f"    {i}. {col}")

# First few rows
print("\n3. PREVIEW DATA (5 baris pertama):")
print(df.head())

# Data types
print("\n4. TIPE DATA:")
print(df.dtypes)

# Numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"\n5. STATISTIK DESKRIPTIF ({len(numeric_cols)} kolom numerik):")
print(df[numeric_cols].describe().round(2))

# Target distribution
if 'target' in df.columns:
    print("\n6. DISTRIBUSI TARGET VARIABLE:")
    target_dist = df['target'].value_counts()
    for val, count in target_dist.items():
        pct = (count / len(df)) * 100
        print(f"  - Target {val}: {count} ({pct:.2f}%)")

# Correlation with target
if 'target' in df.columns and len(numeric_cols) > 1:
    print("\n7. KORELASI DENGAN TARGET (Top 10):")
    correlations = df[numeric_cols].corr()['target'].drop('target').abs().sort_values(ascending=False)
    print(correlations.head(10).round(3))

# Check for outliers (using IQR method)
print("\n8. DETEKSI OUTLIERS (metode IQR):")
outlier_counts = {}
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outlier_counts[col] = len(outliers)

for col, count in sorted(outlier_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
    if count > 0:
        print(f"  - {col}: {count} outliers")

# Feature ranges
print("\n9. RENTANG NILAI FITUR:")
for col in numeric_cols[:10]:  # Show first 10
    min_val = df[col].min()
    max_val = df[col].max()
    mean_val = df[col].mean()
    print(f"  - {col}: [{min_val:.2f} - {max_val:.2f}], mean={mean_val:.2f}")

print("\n" + "="*70)
print("VISUALISASI")
print("="*70)

# Create visualizations
print("\n📊 Membuat visualisasi...")

# 1. Target distribution
if 'target' in df.columns:
    plt.figure(figsize=(8, 5))
    df['target'].value_counts().plot(kind='bar', color=['#FF6B6B', '#4ECDC4'])
    plt.title('Distribusi Target Variable', fontsize=14, fontweight='bold')
    plt.xlabel('Target')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=0)
    for i, v in enumerate(df['target'].value_counts()):
        plt.text(i, v + 5, str(v), ha='center', fontweight='bold')
    plt.tight_layout()
    plt.savefig('../visualizations/01_target_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: visualizations/01_target_distribution.png")
    plt.close()

# 2. Correlation heatmap
if len(numeric_cols) > 1:
    plt.figure(figsize=(14, 12))
    correlation_matrix = df[numeric_cols].corr()
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm',
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Matrix', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('../visualizations/02_correlation_matrix.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: visualizations/02_correlation_matrix.png")
    plt.close()

# 3. Distribution of numeric features
n_cols = 4
n_rows = (len(numeric_cols) + n_cols - 1) // n_cols
fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, n_rows * 3))
axes = axes.flatten()

for idx, col in enumerate(numeric_cols):
    axes[idx].hist(df[col].dropna(), bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    axes[idx].set_title(f'{col}', fontweight='bold')
    axes[idx].set_xlabel(col)
    axes[idx].set_ylabel('Frekuensi')
    axes[idx].grid(alpha=0.3)

for idx in range(len(numeric_cols), len(axes)):
    axes[idx].axis('off')

plt.tight_layout()
plt.savefig('../visualizations/03_feature_distributions.png', dpi=300, bbox_inches='tight')
print("✓ Saved: visualizations/03_feature_distributions.png")
plt.close()

# 4. Box plots
n_cols = 4
n_rows = (len(numeric_cols) + n_cols - 1) // n_cols
fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, n_rows * 3))
axes = axes.flatten()

for idx, col in enumerate(numeric_cols):
    axes[idx].boxplot(df[col].dropna(), vert=True)
    axes[idx].set_title(f'{col}', fontweight='bold')
    axes[idx].set_ylabel(col)
    axes[idx].grid(alpha=0.3)

for idx in range(len(numeric_cols), len(axes)):
    axes[idx].axis('off')

plt.tight_layout()
plt.savefig('../visualizations/04_box_plots.png', dpi=300, bbox_inches='tight')
print("✓ Saved: visualizations/04_box_plots.png")
plt.close()

# 5. Correlation with target
if 'target' in df.columns and len(numeric_cols) > 1:
    plt.figure(figsize=(10, 8))
    target_correlation = df[numeric_cols].corr()['target'].drop('target').sort_values(ascending=False)
    target_correlation.plot(kind='barh', color='coral')
    plt.title('Korelasi dengan Target', fontsize=14, fontweight='bold')
    plt.xlabel('Korelasi')
    plt.ylabel('Fitur')
    plt.axvline(x=0, color='black', linestyle='--', linewidth=0.8)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('../visualizations/05_target_correlation.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: visualizations/05_target_correlation.png")
    plt.close()

# 6. Feature comparison by target
if 'target' in df.columns:
    numeric_features = [col for col in numeric_cols if col != 'target']
    
    if len(numeric_features) > 0:
        n_cols = 3
        n_rows = (len(numeric_features) + n_cols - 1) // n_cols
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))
        axes = axes.flatten()
        
        for idx, col in enumerate(numeric_features):
            for target_val in df['target'].unique():
                data = df[df['target'] == target_val][col].dropna()
                axes[idx].hist(data, bins=20, alpha=0.6, label=f'Target={target_val}')
            
            axes[idx].set_title(f'{col} by Target', fontweight='bold')
            axes[idx].set_xlabel(col)
            axes[idx].set_ylabel('Frekuensi')
            axes[idx].legend()
            axes[idx].grid(alpha=0.3)
        
        for idx in range(len(numeric_features), len(axes)):
            axes[idx].axis('off')
        
        plt.tight_layout()
        plt.savefig('../visualizations/06_features_by_target.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: visualizations/06_features_by_target.png")
        plt.close()

print("\n" + "="*70)
print("KESIMPULAN DAN INSIGHT")
print("="*70)

print("\n✓ ANALISIS SELESAI!")
print("\nHasil analisis:")
print("  1. Dataset statistik: Lihat output di atas")
print("  2. Visualisasi: 6 file PNG telah dibuat")
print("\nFile yang dihasilkan:")
print("  - visualizations/01_target_distribution.png")
print("  - visualizations/02_correlation_matrix.png")
print("  - visualizations/03_feature_distributions.png")
print("  - visualizations/04_box_plots.png")
print("  - visualizations/05_target_correlation.png")
print("  - visualizations/06_features_by_target.png")

print("\nLangkah selanjutnya:")
print("  - Buka file PNG untuk melihat visualisasi")
print("  - Jalankan heart_disease_analysis.ipynb untuk analisis interaktif")
print("  - Download dataset asli dari Kaggle untuk analisis real")

print("\n" + "="*70)
