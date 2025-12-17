"""
Clustering Module for Heart Disease Research
Purpose: Unsupervised clustering to find natural groupings in data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')


class HeartDiseaseClustering:
    """
    Perform clustering on heart disease data to identify natural groupings
    """
    
    def __init__(self, data_path, target_column='target', random_state=42):
        """
        Initialize clustering module
        
        Args:
            data_path: Path to heart disease CSV file
            target_column: Name of target column (excluded from clustering)
            random_state: Random seed for reproducibility
        """
        self.data_path = data_path
        self.target_column = target_column
        self.random_state = random_state
        
        # Load and prepare data
        self.df = pd.read_csv(data_path)
        self.X = self.df.drop(columns=[target_column])
        self.y = self.df[target_column]
        
        # Standardize features
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(self.X)
        
        print(f"✓ Loaded dataset: {self.X.shape[0]} samples, {self.X.shape[1]} features")
    
    def find_optimal_k_elbow(self, k_range=(2, 11)):
        """
        Find optimal K using Elbow method
        
        Args:
            k_range: Range of K values to test
            
        Returns:
            dict: Inertia values for each K
        """
        print("\n🔍 Finding optimal K using Elbow method...")
        
        inertias = {}
        for k in range(k_range[0], k_range[1]):
            kmeans = KMeans(n_clusters=k, random_state=self.random_state, n_init=10)
            kmeans.fit(self.X_scaled)
            inertias[k] = kmeans.inertia_
            print(f"  K={k}: Inertia={kmeans.inertia_:.2f}")
        
        return inertias
    
    def find_optimal_k_silhouette(self, k_range=(2, 11)):
        """
        Find optimal K using Silhouette Score
        
        Args:
            k_range: Range of K values to test
            
        Returns:
            dict: Silhouette scores for each K
        """
        print("\n🔍 Finding optimal K using Silhouette Score...")
        
        silhouette_scores = {}
        for k in range(k_range[0], k_range[1]):
            kmeans = KMeans(n_clusters=k, random_state=self.random_state, n_init=10)
            labels = kmeans.fit_predict(self.X_scaled)
            score = silhouette_score(self.X_scaled, labels)
            silhouette_scores[k] = score
            print(f"  K={k}: Silhouette Score={score:.4f}")
        
        optimal_k = max(silhouette_scores, key=silhouette_scores.get)
        print(f"\n✓ Optimal K (Silhouette): {optimal_k} (score={silhouette_scores[optimal_k]:.4f})")
        
        return silhouette_scores, optimal_k
    
    def find_optimal_k_davies_bouldin(self, k_range=(2, 11)):
        """
        Find optimal K using Davies-Bouldin Index (lower is better)
        
        Args:
            k_range: Range of K values to test
            
        Returns:
            dict: Davies-Bouldin scores for each K
        """
        print("\n🔍 Finding optimal K using Davies-Bouldin Index...")
        
        db_scores = {}
        for k in range(k_range[0], k_range[1]):
            kmeans = KMeans(n_clusters=k, random_state=self.random_state, n_init=10)
            labels = kmeans.fit_predict(self.X_scaled)
            score = davies_bouldin_score(self.X_scaled, labels)
            db_scores[k] = score
            print(f"  K={k}: Davies-Bouldin Index={score:.4f}")
        
        optimal_k = min(db_scores, key=db_scores.get)
        print(f"\n✓ Optimal K (Davies-Bouldin): {optimal_k} (score={db_scores[optimal_k]:.4f})")
        
        return db_scores, optimal_k
    
    def perform_kmeans(self, n_clusters):
        """
        Perform K-Means clustering
        
        Args:
            n_clusters: Number of clusters
            
        Returns:
            tuple: (model, labels, cluster_centers)
        """
        print(f"\n🔬 Performing K-Means clustering with K={n_clusters}...")
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=self.random_state, n_init=10)
        labels = kmeans.fit_predict(self.X_scaled)
        
        # Calculate metrics
        silhouette = silhouette_score(self.X_scaled, labels)
        db_score = davies_bouldin_score(self.X_scaled, labels)
        
        print(f"  Silhouette Score: {silhouette:.4f}")
        print(f"  Davies-Bouldin Index: {db_score:.4f}")
        print(f"  Cluster distribution: {np.bincount(labels)}")
        
        return kmeans, labels, kmeans.cluster_centers_
    
    def perform_hierarchical(self, n_clusters, linkage='ward'):
        """
        Perform Hierarchical clustering
        
        Args:
            n_clusters: Number of clusters
            linkage: Linkage method ('ward', 'complete', 'average')
            
        Returns:
            tuple: (model, labels)
        """
        print(f"\n🔬 Performing Hierarchical clustering with K={n_clusters}, linkage={linkage}...")
        
        hierarchical = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
        labels = hierarchical.fit_predict(self.X_scaled)
        
        # Calculate metrics
        silhouette = silhouette_score(self.X_scaled, labels)
        db_score = davies_bouldin_score(self.X_scaled, labels)
        
        print(f"  Silhouette Score: {silhouette:.4f}")
        print(f"  Davies-Bouldin Index: {db_score:.4f}")
        print(f"  Cluster distribution: {np.bincount(labels)}")
        
        return hierarchical, labels
    
    def perform_dbscan(self, eps=0.5, min_samples=5):
        """
        Perform DBSCAN clustering
        
        Args:
            eps: Maximum distance between samples
            min_samples: Minimum samples in neighborhood
            
        Returns:
            tuple: (model, labels)
        """
        print(f"\n🔬 Performing DBSCAN clustering (eps={eps}, min_samples={min_samples})...")
        
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        labels = dbscan.fit_predict(self.X_scaled)
        
        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        n_noise = list(labels).count(-1)
        
        print(f"  Number of clusters: {n_clusters}")
        print(f"  Number of noise points: {n_noise}")
        
        if n_clusters > 1:
            # Exclude noise points for metrics
            mask = labels != -1
            if mask.sum() > 0:
                silhouette = silhouette_score(self.X_scaled[mask], labels[mask])
                db_score = davies_bouldin_score(self.X_scaled[mask], labels[mask])
                print(f"  Silhouette Score: {silhouette:.4f}")
                print(f"  Davies-Bouldin Index: {db_score:.4f}")
        
        return dbscan, labels
    
    def visualize_clusters(self, labels, method_name="K-Means", save_path=None):
        """
        Visualize clusters using PCA for 2D projection
        
        Args:
            labels: Cluster labels
            method_name: Name of clustering method
            save_path: Path to save plot
        """
        print(f"\n📊 Visualizing {method_name} clusters...")
        
        # PCA for 2D visualization
        pca = PCA(n_components=2, random_state=self.random_state)
        X_pca = pca.fit_transform(self.X_scaled)
        
        plt.figure(figsize=(12, 5))
        
        # Plot 1: Clusters without true labels
        plt.subplot(1, 2, 1)
        scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', alpha=0.6, edgecolors='k')
        plt.colorbar(scatter, label='Cluster')
        plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%} variance)')
        plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%} variance)')
        plt.title(f'{method_name} Clustering Results')
        plt.grid(alpha=0.3)
        
        # Plot 2: True labels for comparison
        plt.subplot(1, 2, 2)
        scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=self.y, cmap='RdYlGn', alpha=0.6, edgecolors='k')
        plt.colorbar(scatter, label='True Label (0=No Disease, 1=Disease)')
        plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%} variance)')
        plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%} variance)')
        plt.title('True Labels (for reference)')
        plt.grid(alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        
        plt.show()
    
    def plot_optimal_k_analysis(self, inertias, silhouette_scores, db_scores, save_path=None):
        """
        Plot all optimal K analysis results
        
        Args:
            inertias: Dict of inertia values
            silhouette_scores: Dict of silhouette scores
            db_scores: Dict of Davies-Bouldin scores
            save_path: Path to save plot
        """
        print("\n📊 Plotting optimal K analysis...")
        
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        
        # Elbow plot
        k_values = list(inertias.keys())
        axes[0].plot(k_values, list(inertias.values()), 'bo-', linewidth=2, markersize=8)
        axes[0].set_xlabel('Number of Clusters (K)', fontsize=12)
        axes[0].set_ylabel('Inertia', fontsize=12)
        axes[0].set_title('Elbow Method', fontsize=14, fontweight='bold')
        axes[0].grid(alpha=0.3)
        axes[0].set_xticks(k_values)
        
        # Silhouette plot
        k_values = list(silhouette_scores.keys())
        axes[1].plot(k_values, list(silhouette_scores.values()), 'go-', linewidth=2, markersize=8)
        axes[1].set_xlabel('Number of Clusters (K)', fontsize=12)
        axes[1].set_ylabel('Silhouette Score', fontsize=12)
        axes[1].set_title('Silhouette Score (Higher is Better)', fontsize=14, fontweight='bold')
        axes[1].grid(alpha=0.3)
        axes[1].set_xticks(k_values)
        
        # Add optimal K marker
        optimal_k = max(silhouette_scores, key=silhouette_scores.get)
        axes[1].axvline(x=optimal_k, color='r', linestyle='--', label=f'Optimal K={optimal_k}')
        axes[1].legend()
        
        # Davies-Bouldin plot
        k_values = list(db_scores.keys())
        axes[2].plot(k_values, list(db_scores.values()), 'ro-', linewidth=2, markersize=8)
        axes[2].set_xlabel('Number of Clusters (K)', fontsize=12)
        axes[2].set_ylabel('Davies-Bouldin Index', fontsize=12)
        axes[2].set_title('Davies-Bouldin Index (Lower is Better)', fontsize=14, fontweight='bold')
        axes[2].grid(alpha=0.3)
        axes[2].set_xticks(k_values)
        
        # Add optimal K marker
        optimal_k = min(db_scores, key=db_scores.get)
        axes[2].axvline(x=optimal_k, color='g', linestyle='--', label=f'Optimal K={optimal_k}')
        axes[2].legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        
        plt.show()
    
    def analyze_cluster_characteristics(self, labels, cluster_id):
        """
        Analyze characteristics of a specific cluster
        
        Args:
            labels: Cluster labels
            cluster_id: ID of cluster to analyze
            
        Returns:
            dict: Cluster statistics
        """
        mask = labels == cluster_id
        cluster_data = self.df[mask]
        
        stats = {
            'cluster_id': cluster_id,
            'size': mask.sum(),
            'percentage': (mask.sum() / len(self.df)) * 100,
            'target_distribution': cluster_data[self.target_column].value_counts().to_dict(),
            'feature_means': cluster_data.drop(columns=[self.target_column]).mean().to_dict()
        }
        
        return stats
    
    def get_all_cluster_stats(self, labels):
        """
        Get statistics for all clusters
        
        Args:
            labels: Cluster labels
            
        Returns:
            list: List of cluster statistics
        """
        unique_labels = sorted(set(labels))
        if -1 in unique_labels:  # Remove noise label from DBSCAN
            unique_labels.remove(-1)
        
        all_stats = []
        for cluster_id in unique_labels:
            stats = self.analyze_cluster_characteristics(labels, cluster_id)
            all_stats.append(stats)
        
        return all_stats


if __name__ == "__main__":
    # Example usage
    print("="*70)
    print("HEART DISEASE CLUSTERING ANALYSIS - K-MEANS")
    print("="*70)
    
    # Initialize
    clustering = HeartDiseaseClustering("data/heart.csv")
    
    # Find optimal K using K-Means only
    print("\n" + "="*70)
    print("FINDING OPTIMAL K FOR K-MEANS")
    print("="*70)
    
    inertias = clustering.find_optimal_k_elbow(k_range=(2, 11))
    silhouette_scores, optimal_k_sil = clustering.find_optimal_k_silhouette(k_range=(2, 11))
    db_scores, optimal_k_db = clustering.find_optimal_k_davies_bouldin(k_range=(2, 11))
    
    # Plot optimal K analysis
    clustering.plot_optimal_k_analysis(
        inertias, silhouette_scores, db_scores,
        save_path="results/clustering/optimal_k_analysis.png"
    )
    
    # Perform K-Means clustering with optimal K
    optimal_k = optimal_k_sil  # Use silhouette's recommendation
    print(f"\n" + "="*70)
    print(f"SELECTED OPTIMAL K = {optimal_k}")
    print("="*70)
    
    kmeans, labels, centers = clustering.perform_kmeans(optimal_k)
    
    # Visualize
    clustering.visualize_clusters(
        labels, 
        method_name=f"K-Means (K={optimal_k})",
        save_path=f"results/clustering/kmeans_k{optimal_k}_visualization.png"
    )
    
    # Get cluster statistics
    cluster_stats = clustering.get_all_cluster_stats(labels)
    
    print("\n" + "="*70)
    print("CLUSTER STATISTICS")
    print("="*70)
    for stats in cluster_stats:
        print(f"\nCluster {stats['cluster_id']}:")
        print(f"  Size: {stats['size']} ({stats['percentage']:.2f}%)")
        print(f"  Target distribution: {stats['target_distribution']}")
    
    # Save results
    results_df = clustering.df.copy()
    results_df['cluster'] = labels
    results_df.to_csv("results/clustering/clustered_data.csv", index=False)
    print(f"\n✓ Saved clustered data to: results/clustering/clustered_data.csv")
    
    print("\n" + "="*70)
    print("✓ CLUSTERING ANALYSIS COMPLETE")
    print("="*70)
