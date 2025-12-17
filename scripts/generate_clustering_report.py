"""
Generate Clustering Analysis Report
Creates comprehensive report and visualizations for optimal K selection
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.decomposition import PCA
import os

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def generate_report():
    """Generate comprehensive clustering report"""
    
    print("="*70)
    print("LAPORAN ANALISIS PENENTUAN JUMLAH CLUSTER OPTIMAL")
    print("="*70)
    
    # Load data
    df = pd.read_csv('data/heart.csv')
    X = df.drop('target', axis=1)
    
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print(f"\nDataset: {len(df)} sampel, {X.shape[1]} fitur")
    print("Metode: K-Means Clustering")
    print("Range K yang diuji: 2-10")
    
    # Calculate metrics for different K values
    k_range = range(2, 11)
    inertias = []
    silhouette_scores = []
    db_scores = []
    
    print("\n" + "="*70)
    print("HASIL EVALUASI METRIK UNTUK SETIAP K")
    print("="*70)
    print(f"{'K':<5} {'Inertia':<15} {'Silhouette':<15} {'Davies-Bouldin':<15}")
    print("-"*70)
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X_scaled)
        
        inertia = kmeans.inertia_
        sil = silhouette_score(X_scaled, labels)
        db = davies_bouldin_score(X_scaled, labels)
        
        inertias.append(inertia)
        silhouette_scores.append(sil)
        db_scores.append(db)
        
        print(f"{k:<5} {inertia:<15.2f} {sil:<15.4f} {db:<15.4f}")
    
    print("-"*70)
    
    # Determine optimal K
    optimal_k_sil = k_range[np.argmax(silhouette_scores)]
    optimal_k_db = k_range[np.argmin(db_scores)]
    
    print("\n" + "="*70)
    print("KESIMPULAN")
    print("="*70)
    print("\nInterpretasi Metrik:")
    print("  • Inertia: Semakin rendah semakin baik (within-cluster sum of squares)")
    print("  • Silhouette Score: Semakin tinggi semakin baik (rentang -1 hingga 1)")
    print("  • Davies-Bouldin Index: Semakin rendah semakin baik")
    
    print(f"\nK Optimal berdasarkan Silhouette Score: K = {optimal_k_sil}")
    print(f"  - Silhouette Score: {max(silhouette_scores):.4f}")
    print(f"  - Interpretasi: Cluster memiliki separasi yang optimal")
    
    print(f"\nK Optimal berdasarkan Davies-Bouldin Index: K = {optimal_k_db}")
    print(f"  - Davies-Bouldin Score: {min(db_scores):.4f}")
    
    print(f"\n✓ REKOMENDASI: K = {optimal_k_sil} (berdasarkan Silhouette Score)")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Analisis Penentuan Jumlah Cluster Optimal (K-Means)', 
                 fontsize=16, fontweight='bold')
    
    # Plot 1: Elbow Method (Inertia)
    axes[0, 0].plot(k_range, inertias, 'bo-', linewidth=2, markersize=8)
    axes[0, 0].set_xlabel('Jumlah Cluster (K)', fontsize=11)
    axes[0, 0].set_ylabel('Inertia', fontsize=11)
    axes[0, 0].set_title('(a) Elbow Method - Inertia', fontsize=12, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xticks(k_range)
    
    # Highlight elbow point (K=2)
    axes[0, 0].axvline(x=2, color='r', linestyle='--', alpha=0.5, label='K=2')
    axes[0, 0].legend()
    
    # Plot 2: Silhouette Score
    axes[0, 1].plot(k_range, silhouette_scores, 'go-', linewidth=2, markersize=8)
    axes[0, 1].set_xlabel('Jumlah Cluster (K)', fontsize=11)
    axes[0, 1].set_ylabel('Silhouette Score', fontsize=11)
    axes[0, 1].set_title('(b) Silhouette Score (Semakin Tinggi Semakin Baik)', 
                        fontsize=12, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xticks(k_range)
    
    # Highlight optimal K
    max_idx = np.argmax(silhouette_scores)
    axes[0, 1].scatter(k_range[max_idx], silhouette_scores[max_idx], 
                      s=200, c='red', marker='*', zorder=5, 
                      label=f'Optimal K={optimal_k_sil}')
    axes[0, 1].legend()
    
    # Plot 3: Davies-Bouldin Index
    axes[1, 0].plot(k_range, db_scores, 'ro-', linewidth=2, markersize=8)
    axes[1, 0].set_xlabel('Jumlah Cluster (K)', fontsize=11)
    axes[1, 0].set_ylabel('Davies-Bouldin Index', fontsize=11)
    axes[1, 0].set_title('(c) Davies-Bouldin Index (Semakin Rendah Semakin Baik)', 
                        fontsize=12, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_xticks(k_range)
    
    # Highlight optimal K
    min_idx = np.argmin(db_scores)
    axes[1, 0].scatter(k_range[min_idx], db_scores[min_idx], 
                      s=200, c='green', marker='*', zorder=5, 
                      label=f'Optimal K={optimal_k_db}')
    axes[1, 0].legend()
    
    # Plot 4: Comparison Table
    axes[1, 1].axis('off')
    
    # Create table data
    table_data = []
    table_data.append(['K', 'Silhouette↑', 'Davies-Bouldin↓', 'Rekomendasi'])
    
    for i, k in enumerate(k_range):
        marker = '★ OPTIMAL' if k == optimal_k_sil else ''
        table_data.append([
            str(k),
            f"{silhouette_scores[i]:.4f}",
            f"{db_scores[i]:.4f}",
            marker
        ])
    
    table = axes[1, 1].table(cellText=table_data, cellLoc='center',
                            bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    # Style header row
    for i in range(4):
        table[(0, i)].set_facecolor('#40466e')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Highlight optimal row
    optimal_row = optimal_k_sil - 1
    for i in range(4):
        table[(optimal_row, i)].set_facecolor('#90EE90')
        table[(optimal_row, i)].set_text_props(weight='bold')
    
    axes[1, 1].set_title('(d) Perbandingan Metrik', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    
    # Save figure
    os.makedirs('results/clustering', exist_ok=True)
    fig_path = 'results/clustering/optimal_k_analysis_report.png'
    plt.savefig(fig_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Visualisasi disimpan: {fig_path}")
    
    # Generate clustering with optimal K
    print(f"\n{'='*70}")
    print(f"HASIL CLUSTERING DENGAN K={optimal_k_sil}")
    print("="*70)
    
    kmeans = KMeans(n_clusters=optimal_k_sil, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    
    # Cluster statistics
    clustered_df = df.copy()
    clustered_df['cluster'] = labels
    
    print(f"\nDistribusi Sampel per Cluster:")
    cluster_dist = clustered_df['cluster'].value_counts().sort_index()
    for cluster_id, count in cluster_dist.items():
        percentage = (count / len(clustered_df)) * 100
        print(f"  Cluster {cluster_id}: {count} sampel ({percentage:.1f}%)")
    
    # Compare with true labels
    print(f"\nPerbandingan Cluster dengan Label Asli:")
    comparison = pd.crosstab(clustered_df['cluster'], clustered_df['target'], 
                            rownames=['Cluster'], colnames=['Target'])
    print(comparison)
    
    # Visualize clusters with PCA
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X_scaled)
    
    fig2, axes2 = plt.subplots(1, 2, figsize=(15, 6))
    fig2.suptitle(f'Visualisasi Hasil Clustering (K={optimal_k_sil})', 
                  fontsize=14, fontweight='bold')
    
    # Plot clusters
    scatter1 = axes2[0].scatter(X_pca[:, 0], X_pca[:, 1], c=labels, 
                               cmap='viridis', alpha=0.6, s=50, edgecolors='k')
    axes2[0].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                    c='red', marker='X', s=300, edgecolors='black', linewidths=2,
                    label='Centroid')
    axes2[0].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)', fontsize=11)
    axes2[0].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)', fontsize=11)
    axes2[0].set_title('(a) Hasil Clustering (K-Means)', fontsize=12, fontweight='bold')
    axes2[0].legend()
    axes2[0].grid(True, alpha=0.3)
    plt.colorbar(scatter1, ax=axes2[0], label='Cluster')
    
    # Plot true labels for comparison
    scatter2 = axes2[1].scatter(X_pca[:, 0], X_pca[:, 1], c=df['target'], 
                               cmap='coolwarm', alpha=0.6, s=50, edgecolors='k')
    axes2[1].set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)', fontsize=11)
    axes2[1].set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)', fontsize=11)
    axes2[1].set_title('(b) Label Asli (Target)', fontsize=12, fontweight='bold')
    axes2[1].grid(True, alpha=0.3)
    plt.colorbar(scatter2, ax=axes2[1], label='Target (0=Sehat, 1=Sakit)')
    
    plt.tight_layout()
    
    # Save clustering visualization
    cluster_viz_path = f'results/clustering/kmeans_k{optimal_k_sil}_visualization_report.png'
    plt.savefig(cluster_viz_path, dpi=300, bbox_inches='tight')
    print(f"✓ Visualisasi clustering disimpan: {cluster_viz_path}")
    
    # Save detailed report to text file
    report_path = 'results/clustering/clustering_report.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("LAPORAN ANALISIS PENENTUAN JUMLAH CLUSTER OPTIMAL\n")
        f.write("="*70 + "\n\n")
        
        f.write(f"Dataset: {len(df)} sampel, {X.shape[1]} fitur\n")
        f.write("Metode: K-Means Clustering\n")
        f.write("Range K yang diuji: 2-10\n\n")
        
        f.write("="*70 + "\n")
        f.write("HASIL EVALUASI METRIK\n")
        f.write("="*70 + "\n")
        f.write(f"{'K':<5} {'Inertia':<15} {'Silhouette':<15} {'Davies-Bouldin':<15}\n")
        f.write("-"*70 + "\n")
        
        for i, k in enumerate(k_range):
            f.write(f"{k:<5} {inertias[i]:<15.2f} {silhouette_scores[i]:<15.4f} {db_scores[i]:<15.4f}\n")
        
        f.write("-"*70 + "\n\n")
        
        f.write("="*70 + "\n")
        f.write("KESIMPULAN\n")
        f.write("="*70 + "\n\n")
        
        f.write("Interpretasi Metrik:\n")
        f.write("  • Inertia: Semakin rendah semakin baik\n")
        f.write("  • Silhouette Score: Semakin tinggi semakin baik (rentang -1 hingga 1)\n")
        f.write("  • Davies-Bouldin Index: Semakin rendah semakin baik\n\n")
        
        f.write(f"K Optimal berdasarkan Silhouette Score: K = {optimal_k_sil}\n")
        f.write(f"  - Silhouette Score: {max(silhouette_scores):.4f}\n\n")
        
        f.write(f"REKOMENDASI: K = {optimal_k_sil}\n\n")
        
        f.write("="*70 + "\n")
        f.write(f"HASIL CLUSTERING DENGAN K={optimal_k_sil}\n")
        f.write("="*70 + "\n\n")
        
        f.write("Distribusi Sampel per Cluster:\n")
        for cluster_id, count in cluster_dist.items():
            percentage = (count / len(clustered_df)) * 100
            f.write(f"  Cluster {cluster_id}: {count} sampel ({percentage:.1f}%)\n")
        
        f.write("\nPerbandingan dengan Label Asli:\n")
        f.write(str(comparison) + "\n")
    
    print(f"✓ Laporan teks disimpan: {report_path}")
    
    print("\n" + "="*70)
    print("LAPORAN LENGKAP BERHASIL DIBUAT!")
    print("="*70)
    print("\nFile yang dihasilkan:")
    print(f"  1. {fig_path}")
    print(f"  2. {cluster_viz_path}")
    print(f"  3. {report_path}")
    print("\nFile-file ini dapat digunakan untuk bagian Hasil dan Pembahasan paper.")
    print("="*70)

if __name__ == "__main__":
    generate_report()
