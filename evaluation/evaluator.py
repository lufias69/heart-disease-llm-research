"""
Evaluation Module for LLM Performance Analysis
Purpose: Evaluate consistency, accuracy, and explainability of LLM predictions
"""

import pandas as pd
import numpy as np
import json
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                             f1_score, confusion_matrix, classification_report)
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


class LLMEvaluator:
    """
    Evaluate LLM performance on heart disease prediction
    """
    
    def __init__(self, results_dir='results/llm_predictions', test_data_path='results/sampling/llm_test_data.csv'):
        """
        Initialize evaluator
        
        Args:
            results_dir: Directory containing LLM results
            test_data_path: Path to test data with ground truth
        """
        self.results_dir = results_dir
        self.test_data = pd.read_csv(test_data_path)
        
        print(f"✓ Loaded test data: {len(self.test_data)} samples")
        print(f"  Ground truth distribution: {self.test_data['ground_truth'].value_counts().to_dict()}")
    
    def load_model_results(self, model_name):
        """
        Load results for a specific model
        
        Args:
            model_name: Name of model ('gpt', 'gemini', 'qwen')
            
        Returns:
            pd.DataFrame: Model results
        """
        results_path = f"{self.results_dir}/{model_name}_results.csv"
        try:
            df = pd.read_csv(results_path)
            print(f"✓ Loaded {model_name.upper()} results: {len(df)} predictions")
            return df
        except FileNotFoundError:
            print(f"✗ Results file not found: {results_path}")
            return None
    
    def calculate_consistency(self, model_results):
        """
        Calculate consistency score for each test sample
        
        Args:
            model_results: DataFrame with model results
            
        Returns:
            pd.DataFrame: Consistency scores per sample
        """
        print("\n📊 Calculating consistency scores...")
        
        consistency_data = []
        
        for test_id in model_results['test_id'].unique():
            test_runs = model_results[model_results['test_id'] == test_id]
            
            # Get predictions
            predictions = test_runs['prediction'].dropna().values
            
            if len(predictions) == 0:
                continue
            
            # Calculate consistency (percentage of most common prediction)
            unique, counts = np.unique(predictions, return_counts=True)
            most_common_pred = unique[np.argmax(counts)]
            consistency_score = np.max(counts) / len(predictions)
            
            # Get ground truth
            ground_truth = self.test_data[self.test_data['test_id'] == test_id]['ground_truth'].values[0]
            
            consistency_data.append({
                'test_id': test_id,
                'ground_truth': ground_truth,
                'majority_prediction': most_common_pred,
                'consistency_score': consistency_score,
                'total_runs': len(predictions),
                'prediction_distribution': dict(zip(unique, counts))
            })
        
        consistency_df = pd.DataFrame(consistency_data)
        
        print(f"  Average consistency: {consistency_df['consistency_score'].mean():.2%}")
        print(f"  Median consistency: {consistency_df['consistency_score'].median():.2%}")
        print(f"  Min consistency: {consistency_df['consistency_score'].min():.2%}")
        print(f"  Max consistency: {consistency_df['consistency_score'].max():.2%}")
        
        return consistency_df
    
    def calculate_performance_metrics(self, consistency_df, model_name):
        """
        Calculate performance metrics (accuracy, precision, recall, F1)
        
        Args:
            consistency_df: DataFrame with consistency scores
            model_name: Name of model
            
        Returns:
            dict: Performance metrics
        """
        print(f"\n📈 Calculating performance metrics for {model_name.upper()}...")
        
        y_true = consistency_df['ground_truth'].values
        y_pred = consistency_df['majority_prediction'].values
        
        # Calculate metrics
        metrics = {
            'model': model_name,
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, zero_division=0),
            'recall': recall_score(y_true, y_pred, zero_division=0),
            'f1_score': f1_score(y_true, y_pred, zero_division=0),
            'avg_consistency': consistency_df['consistency_score'].mean(),
            'median_consistency': consistency_df['consistency_score'].median(),
            'total_samples': len(consistency_df)
        }
        
        print(f"  Accuracy:  {metrics['accuracy']:.4f}")
        print(f"  Precision: {metrics['precision']:.4f}")
        print(f"  Recall:    {metrics['recall']:.4f}")
        print(f"  F1-Score:  {metrics['f1_score']:.4f}")
        print(f"  Avg Consistency: {metrics['avg_consistency']:.2%}")
        
        # Confusion matrix
        cm = confusion_matrix(y_true, y_pred)
        print(f"\n  Confusion Matrix:")
        print(f"    TN={cm[0,0]}, FP={cm[0,1]}")
        print(f"    FN={cm[1,0]}, TP={cm[1,1]}")
        
        return metrics
    
    def analyze_consistency_by_cluster(self, consistency_df):
        """
        Analyze consistency scores by cluster
        
        Args:
            consistency_df: DataFrame with consistency scores
            
        Returns:
            pd.DataFrame: Consistency by cluster
        """
        print("\n🔍 Analyzing consistency by cluster...")
        
        # Merge with test data to get cluster info
        merged = consistency_df.merge(
            self.test_data[['test_id', 'cluster', 'sample_type']], 
            on='test_id'
        )
        
        cluster_stats = merged.groupby('cluster').agg({
            'consistency_score': ['mean', 'median', 'std', 'min', 'max'],
            'test_id': 'count'
        }).round(4)
        
        cluster_stats.columns = ['_'.join(col).strip() for col in cluster_stats.columns.values]
        
        print(cluster_stats)
        
        return cluster_stats
    
    def compare_models(self, models=['gpt', 'gemini', 'qwen']):
        """
        Compare performance of multiple models
        
        Args:
            models: List of model names
            
        Returns:
            pd.DataFrame: Comparison table
        """
        print("\n" + "="*70)
        print("MODEL COMPARISON")
        print("="*70)
        
        all_metrics = []
        all_consistency_dfs = {}
        
        for model_name in models:
            results = self.load_model_results(model_name)
            if results is not None:
                consistency_df = self.calculate_consistency(results)
                metrics = self.calculate_performance_metrics(consistency_df, model_name)
                all_metrics.append(metrics)
                all_consistency_dfs[model_name] = consistency_df
        
        comparison_df = pd.DataFrame(all_metrics)
        comparison_df = comparison_df.set_index('model')
        
        print("\n" + "="*70)
        print("FINAL COMPARISON")
        print("="*70)
        print(comparison_df.round(4))
        
        return comparison_df, all_consistency_dfs
    
    def plot_model_comparison(self, comparison_df, save_path=None):
        """
        Plot model comparison
        
        Args:
            comparison_df: Comparison DataFrame
            save_path: Path to save plot
        """
        print("\n📊 Plotting model comparison...")
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # Plot 1: Accuracy metrics
        metrics = ['accuracy', 'precision', 'recall', 'f1_score']
        comparison_df[metrics].plot(kind='bar', ax=axes[0, 0], alpha=0.8)
        axes[0, 0].set_title('Performance Metrics Comparison', fontsize=14, fontweight='bold')
        axes[0, 0].set_ylabel('Score')
        axes[0, 0].set_xlabel('Model')
        axes[0, 0].legend(title='Metrics')
        axes[0, 0].grid(alpha=0.3)
        axes[0, 0].set_ylim([0, 1])
        
        # Plot 2: Consistency scores
        comparison_df[['avg_consistency', 'median_consistency']].plot(kind='bar', ax=axes[0, 1], alpha=0.8)
        axes[0, 1].set_title('Consistency Scores', fontsize=14, fontweight='bold')
        axes[0, 1].set_ylabel('Consistency Score')
        axes[0, 1].set_xlabel('Model')
        axes[0, 1].legend(title='Consistency')
        axes[0, 1].grid(alpha=0.3)
        axes[0, 1].set_ylim([0, 1])
        
        # Plot 3: F1-Score comparison
        axes[1, 0].barh(comparison_df.index, comparison_df['f1_score'], alpha=0.8, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        axes[1, 0].set_title('F1-Score Comparison', fontsize=14, fontweight='bold')
        axes[1, 0].set_xlabel('F1-Score')
        axes[1, 0].set_xlim([0, 1])
        axes[1, 0].grid(alpha=0.3)
        
        # Plot 4: Summary table
        axes[1, 1].axis('off')
        summary_data = comparison_df[['accuracy', 'f1_score', 'avg_consistency']].round(4)
        table = axes[1, 1].table(cellText=summary_data.values,
                                  rowLabels=summary_data.index,
                                  colLabels=summary_data.columns,
                                  cellLoc='center',
                                  loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 2)
        axes[1, 1].set_title('Summary Metrics', fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        
        plt.show()
    
    def plot_consistency_distribution(self, all_consistency_dfs, save_path=None):
        """
        Plot consistency distribution for all models
        
        Args:
            all_consistency_dfs: Dict of consistency DataFrames
            save_path: Path to save plot
        """
        print("\n📊 Plotting consistency distributions...")
        
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))
        
        for idx, (model_name, consistency_df) in enumerate(all_consistency_dfs.items()):
            axes[idx].hist(consistency_df['consistency_score'], bins=20, alpha=0.7, edgecolor='black')
            axes[idx].axvline(consistency_df['consistency_score'].mean(), 
                             color='r', linestyle='--', linewidth=2, 
                             label=f"Mean: {consistency_df['consistency_score'].mean():.2%}")
            axes[idx].axvline(consistency_df['consistency_score'].median(), 
                             color='g', linestyle='--', linewidth=2,
                             label=f"Median: {consistency_df['consistency_score'].median():.2%}")
            axes[idx].set_title(f'{model_name.upper()} Consistency', fontsize=14, fontweight='bold')
            axes[idx].set_xlabel('Consistency Score')
            axes[idx].set_ylabel('Frequency')
            axes[idx].legend()
            axes[idx].grid(alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"✓ Saved: {save_path}")
        
        plt.show()
    
    def export_results_for_paper(self, comparison_df, all_consistency_dfs, output_dir='results/evaluation'):
        """
        Export results in format suitable for academic paper
        
        Args:
            comparison_df: Model comparison DataFrame
            all_consistency_dfs: Dict of consistency DataFrames
            output_dir: Output directory
        """
        print(f"\n📤 Exporting results for paper...")
        
        # Save comparison table (LaTeX format)
        latex_table = comparison_df.to_latex(float_format="%.4f")
        latex_path = f"{output_dir}/model_comparison_table.tex"
        with open(latex_path, 'w') as f:
            f.write(latex_table)
        print(f"✓ LaTeX table: {latex_path}")
        
        # Save as CSV
        csv_path = f"{output_dir}/model_comparison.csv"
        comparison_df.to_csv(csv_path)
        print(f"✓ CSV file: {csv_path}")
        
        # Save detailed consistency data
        for model_name, consistency_df in all_consistency_dfs.items():
            detail_path = f"{output_dir}/{model_name}_detailed_results.csv"
            consistency_df.to_csv(detail_path, index=False)
            print(f"✓ Detailed results: {detail_path}")
        
        print(f"\n✓ All results exported to: {output_dir}")


if __name__ == "__main__":
    print("="*70)
    print("LLM EVALUATION MODULE")
    print("="*70)
    
    evaluator = LLMEvaluator()
    
    # Compare models
    comparison_df, all_consistency_dfs = evaluator.compare_models(['gpt', 'gemini', 'qwen'])
    
    # Plot comparisons
    evaluator.plot_model_comparison(
        comparison_df, 
        save_path='results/evaluation/model_comparison.png'
    )
    
    evaluator.plot_consistency_distribution(
        all_consistency_dfs,
        save_path='results/evaluation/consistency_distributions.png'
    )
    
    # Export for paper
    evaluator.export_results_for_paper(comparison_df, all_consistency_dfs)
    
    print("\n" + "="*70)
    print("✓ EVALUATION COMPLETE")
    print("="*70)
