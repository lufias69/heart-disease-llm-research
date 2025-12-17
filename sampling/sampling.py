"""
Sampling Module for Heart Disease Research
Purpose: Sample representative points from each cluster for LLM testing
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import euclidean_distances
import warnings
warnings.filterwarnings('ignore')


class ClusterSampling:
    """
    Sample representative and edge case data points from each cluster
    """
    
    def __init__(self, clustered_data_path, target_column='target'):
        """
        Initialize sampling module
        
        Args:
            clustered_data_path: Path to CSV with cluster labels
            target_column: Name of target column
        """
        self.df = pd.read_csv(clustered_data_path)
        self.target_column = target_column
        
        # Check if cluster column exists
        if 'cluster' not in self.df.columns:
            raise ValueError("Input data must have 'cluster' column")
        
        print(f"✓ Loaded clustered data: {len(self.df)} samples")
        print(f"  Clusters found: {sorted(self.df['cluster'].unique())}")
    
    def get_cluster_centroid_sample(self, cluster_id):
        """
        Get sample closest to cluster centroid
        
        Args:
            cluster_id: Cluster ID
            
        Returns:
            tuple: (sample_index, sample_data, distance_to_centroid)
        """
        # Get cluster data
        cluster_mask = self.df['cluster'] == cluster_id
        cluster_data = self.df[cluster_mask]
        
        if len(cluster_data) == 0:
            return None, None, None
        
        # Extract features (exclude target and cluster columns)
        feature_cols = [col for col in self.df.columns if col not in [self.target_column, 'cluster']]
        X_cluster = cluster_data[feature_cols].values
        
        # Calculate centroid
        centroid = X_cluster.mean(axis=0)
        
        # Find sample closest to centroid
        distances = euclidean_distances(X_cluster, [centroid]).flatten()
        closest_idx = distances.argmin()
        
        # Get original index
        original_idx = cluster_data.index[closest_idx]
        sample_data = self.df.loc[original_idx]
        
        return original_idx, sample_data, distances[closest_idx]
    
    def get_cluster_farthest_sample(self, cluster_id):
        """
        Get sample farthest from cluster centroid (but still in cluster)
        
        Args:
            cluster_id: Cluster ID
            
        Returns:
            tuple: (sample_index, sample_data, distance_to_centroid)
        """
        # Get cluster data
        cluster_mask = self.df['cluster'] == cluster_id
        cluster_data = self.df[cluster_mask]
        
        if len(cluster_data) == 0:
            return None, None, None
        
        # Extract features
        feature_cols = [col for col in self.df.columns if col not in [self.target_column, 'cluster']]
        X_cluster = cluster_data[feature_cols].values
        
        # Calculate centroid
        centroid = X_cluster.mean(axis=0)
        
        # Find sample farthest from centroid
        distances = euclidean_distances(X_cluster, [centroid]).flatten()
        farthest_idx = distances.argmax()
        
        # Get original index
        original_idx = cluster_data.index[farthest_idx]
        sample_data = self.df.loc[original_idx]
        
        return original_idx, sample_data, distances[farthest_idx]
    
    def sample_all_clusters(self, samples_per_cluster=2, strategy='diverse'):
        """
        Sample from all clusters with different strategies
        
        Args:
            samples_per_cluster: Number of samples per cluster
            strategy: Sampling strategy
                - 'centroid_farthest': Original (centroid + farthest)
                - 'diverse': Sample diverse points across cluster (for larger samples)
                - 'stratified': Stratified sampling by distance from centroid
            
        Returns:
            pd.DataFrame: Sampled data with metadata
        """
        print(f"\n📊 Sampling {samples_per_cluster} samples per cluster (strategy: {strategy})...")
        
        sampled_data = []
        unique_clusters = sorted(self.df['cluster'].unique())
        
        for cluster_id in unique_clusters:
            if cluster_id == -1:  # Skip noise from DBSCAN
                continue
            
            print(f"\n  Cluster {cluster_id}:")
            cluster_mask = self.df['cluster'] == cluster_id
            cluster_data = self.df[cluster_mask]
            cluster_size = len(cluster_data)
            print(f"    Cluster size: {cluster_size}")
            
            # Extract features
            feature_cols = [col for col in self.df.columns if col not in [self.target_column, 'cluster']]
            X_cluster = cluster_data[feature_cols].values
            centroid = X_cluster.mean(axis=0)
            
            if strategy == 'diverse' and samples_per_cluster > 2:
                # Diverse sampling using distance-based selection
                distances = euclidean_distances(X_cluster, [centroid]).flatten()
                
                # Create distance bins
                n_samples = min(samples_per_cluster, cluster_size)
                
                # Use percentile-based sampling for diversity
                percentiles = np.linspace(0, 100, n_samples + 1)
                selected_indices = []
                
                for i in range(n_samples):
                    # Find samples in this percentile range
                    low_pct = np.percentile(distances, percentiles[i])
                    high_pct = np.percentile(distances, percentiles[i+1])
                    
                    in_range = np.where((distances >= low_pct) & (distances <= high_pct))[0]
                    
                    if len(in_range) > 0:
                        # Randomly select one from this range
                        selected_idx = np.random.choice(in_range)
                        if selected_idx not in selected_indices:
                            selected_indices.append(selected_idx)
                
                # If we need more samples, fill with random selection
                remaining = n_samples - len(selected_indices)
                if remaining > 0:
                    available = [i for i in range(len(X_cluster)) if i not in selected_indices]
                    if len(available) >= remaining:
                        additional = np.random.choice(available, remaining, replace=False)
                        selected_indices.extend(additional)
                
                # Add selected samples
                for local_idx in selected_indices:
                    original_idx = cluster_data.index[local_idx]
                    sample_data = self.df.loc[original_idx]
                    
                    sample_info = sample_data.to_dict()
                    sample_info['sample_type'] = 'diverse'
                    sample_info['distance_to_centroid'] = distances[local_idx]
                    sample_info['original_index'] = original_idx
                    sampled_data.append(sample_info)
                
                print(f"    ✓ Selected {len(selected_indices)} diverse samples")
                
            elif strategy == 'stratified':
                # Stratified sampling by distance quartiles
                distances = euclidean_distances(X_cluster, [centroid]).flatten()
                n_samples = min(samples_per_cluster, cluster_size)
                
                # Divide into quartiles and sample from each
                quartiles = np.percentile(distances, [25, 50, 75])
                strata = ['near', 'mid-near', 'mid-far', 'far']
                samples_per_stratum = max(1, n_samples // 4)
                
                selected_indices = []
                
                for i, stratum_name in enumerate(strata):
                    if i == 0:
                        stratum_mask = distances <= quartiles[0]
                    elif i == 1:
                        stratum_mask = (distances > quartiles[0]) & (distances <= quartiles[1])
                    elif i == 2:
                        stratum_mask = (distances > quartiles[1]) & (distances <= quartiles[2])
                    else:
                        stratum_mask = distances > quartiles[2]
                    
                    stratum_indices = np.where(stratum_mask)[0]
                    
                    if len(stratum_indices) > 0:
                        n_select = min(samples_per_stratum, len(stratum_indices))
                        selected = np.random.choice(stratum_indices, n_select, replace=False)
                        
                        for local_idx in selected:
                            if len(selected_indices) < n_samples:
                                original_idx = cluster_data.index[local_idx]
                                sample_data = self.df.loc[original_idx]
                                
                                sample_info = sample_data.to_dict()
                                sample_info['sample_type'] = f'stratified_{stratum_name}'
                                sample_info['distance_to_centroid'] = distances[local_idx]
                                sample_info['original_index'] = original_idx
                                sampled_data.append(sample_info)
                                selected_indices.append(local_idx)
                
                print(f"    ✓ Selected {len(selected_indices)} stratified samples")
                
            else:  # Default: centroid_farthest
                # Get centroid sample
                distances = euclidean_distances(X_cluster, [centroid]).flatten()
                closest_idx = distances.argmin()
                original_idx = cluster_data.index[closest_idx]
                centroid_sample = self.df.loc[original_idx]
                
                sample_info = centroid_sample.to_dict()
                sample_info['sample_type'] = 'centroid'
                sample_info['distance_to_centroid'] = distances[closest_idx]
                sample_info['original_index'] = original_idx
                sampled_data.append(sample_info)
                print(f"    ✓ Centroid sample: index={original_idx}")
                
                # Get farthest sample if samples_per_cluster >= 2
                if samples_per_cluster >= 2:
                    farthest_idx = distances.argmax()
                    original_idx = cluster_data.index[farthest_idx]
                    farthest_sample = self.df.loc[original_idx]
                    
                    sample_info = farthest_sample.to_dict()
                    sample_info['sample_type'] = 'farthest'
                    sample_info['distance_to_centroid'] = distances[farthest_idx]
                    sample_info['original_index'] = original_idx
                    sampled_data.append(sample_info)
                    print(f"    ✓ Farthest sample: index={original_idx}")
        
        # Create DataFrame
        sampled_df = pd.DataFrame(sampled_data)
        
        print(f"\n✓ Total samples selected: {len(sampled_df)}")
        if 'sample_type' in sampled_df.columns:
            print(f"\nSample type distribution:")
            for stype in sampled_df['sample_type'].unique():
                count = (sampled_df['sample_type'] == stype).sum()
                print(f"  - {stype}: {count}")
        
        # Ensure all samples are unique
        if 'original_index' in sampled_df.columns:
            duplicates = sampled_df['original_index'].duplicated().sum()
            if duplicates > 0:
                print(f"\n⚠️  Warning: {duplicates} duplicate samples detected, removing...")
                sampled_df = sampled_df.drop_duplicates(subset='original_index', keep='first')
                print(f"✓ Unique samples after deduplication: {len(sampled_df)}")
        
        return sampled_df
    
    def create_test_set(self, sampled_df, save_path=None):
        """
        Create test set for LLM evaluation
        
        Args:
            sampled_df: DataFrame with sampled data
            save_path: Path to save test set
            
        Returns:
            pd.DataFrame: Test set with metadata
        """
        print("\n📝 Creating test set...")
        
        # Prepare test set
        test_set = sampled_df.copy()
        
        # Add test ID
        test_set['test_id'] = range(len(test_set))
        
        # Reorder columns
        metadata_cols = ['test_id', 'cluster', 'sample_type', 'distance_to_centroid', 
                        'original_index', self.target_column]
        feature_cols = [col for col in test_set.columns if col not in metadata_cols]
        
        test_set = test_set[metadata_cols + feature_cols]
        
        # Save if path provided
        if save_path:
            test_set.to_csv(save_path, index=False)
            print(f"✓ Test set saved to: {save_path}")
        
        # Print summary
        print(f"\nTest Set Summary:")
        print(f"  Total samples: {len(test_set)}")
        print(f"  Clusters represented: {test_set['cluster'].nunique()}")
        print(f"  Target distribution:")
        print(f"    - No disease (0): {(test_set[self.target_column] == 0).sum()}")
        print(f"    - Disease (1): {(test_set[self.target_column] == 1).sum()}")
        
        return test_set
    
    def export_for_llm_testing(self, test_set, output_path):
        """
        Export test set in format suitable for LLM testing
        
        Args:
            test_set: Test set DataFrame
            output_path: Path to save formatted test set
        """
        print(f"\n📤 Exporting test set for LLM testing...")
        
        # Create feature description for each sample
        feature_cols = [col for col in test_set.columns 
                       if col not in ['test_id', 'cluster', 'sample_type', 
                                     'distance_to_centroid', 'original_index', self.target_column]]
        
        llm_test_data = []
        
        for idx, row in test_set.iterrows():
            # Create feature string
            feature_str = ", ".join([f"{col}={row[col]}" for col in feature_cols])
            
            test_record = {
                'test_id': row['test_id'],
                'cluster': row['cluster'],
                'sample_type': row['sample_type'],
                'features': feature_str,
                'ground_truth': row[self.target_column],
                'ground_truth_label': 'Disease' if row[self.target_column] == 1 else 'No Disease'
            }
            
            llm_test_data.append(test_record)
        
        # Save
        llm_df = pd.DataFrame(llm_test_data)
        llm_df.to_csv(output_path, index=False)
        
        print(f"✓ LLM test data saved to: {output_path}")
        print(f"  Format: test_id, cluster, sample_type, features, ground_truth")
        
        return llm_df


if __name__ == "__main__":
    print("="*70)
    print("CLUSTER SAMPLING FOR LLM TESTING - 100 UNIQUE SAMPLES")
    print("="*70)
    
    # Initialize sampling
    sampler = ClusterSampling("results/clustering/clustered_data.csv")
    
    # Calculate samples per cluster to get ~100 total
    n_clusters = sampler.df['cluster'].nunique()
    samples_per_cluster = 100 // n_clusters
    
    print(f"\nTarget: 100 unique test samples")
    print(f"Clusters: {n_clusters}")
    print(f"Samples per cluster: {samples_per_cluster}")
    
    # Sample from all clusters using diverse strategy
    sampled_df = sampler.sample_all_clusters(
        samples_per_cluster=samples_per_cluster,
        strategy='diverse'
    )
    
    # Create test set
    test_set = sampler.create_test_set(
        sampled_df,
        save_path="results/sampling/test_set.csv"
    )
    
    # Export for LLM testing
    llm_test_data = sampler.export_for_llm_testing(
        test_set,
        output_path="results/sampling/llm_test_data.csv"
    )
    
    print("\n" + "="*70)
    print("✓ SAMPLING COMPLETE")
    print("="*70)
    print(f"\nTotal unique test samples: {len(test_set)}")
    print("\nFiles created:")
    print("  - results/sampling/test_set.csv")
    print("  - results/sampling/llm_test_data.csv")
    print("\nNext step: Run LLM testing with llm_test_data.csv")
