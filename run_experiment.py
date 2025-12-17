"""
Main Experiment Pipeline
Run complete experiment from clustering to evaluation
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

from clustering.clustering import HeartDiseaseClustering
from sampling.sampling import ClusterSampling
from llm_testing.llm_tester import LLMTester
from evaluation.evaluator import LLMEvaluator


def main():
    """
    Run complete experimental pipeline
    """
    print("="*80)
    print(" " * 20 + "LLM HEART DISEASE RESEARCH")
    print(" " * 10 + "Evaluating Consistency and Explainability of LLMs")
    print("="*80)
    
    # Step 1: Load Existing Clustering Results
    print("\n" + "="*80)
    print("STEP 1: LOADING CLUSTERING RESULTS")
    print("="*80)
    
    import pandas as pd
    
    # Check if clustered data exists
    clustered_file = "results/clustering/clustered_data.csv"
    if not os.path.exists(clustered_file):
        print("❌ Clustered data not found!")
        print(f"   Please run clustering first: python clustering/clustering.py")
        return
    
    # Load existing clustered data
    clustered_df = pd.read_csv(clustered_file)
    if 'cluster' not in clustered_df.columns:
        print("❌ No 'cluster' column found in clustered data!")
        return
    
    optimal_k = clustered_df['cluster'].nunique()
    print(f"✓ Loaded existing clustering results")
    print(f"✓ Number of clusters: {optimal_k}")
    print(f"✓ Total samples: {len(clustered_df)}")
    
    # Step 2: Sampling
    print("\n" + "="*80)
    print("STEP 2: SAMPLING STRATEGY - 100 UNIQUE TEST SAMPLES")
    print("="*80)
    
    sampler = ClusterSampling("results/clustering/clustered_data.csv")
    
    # Calculate samples per cluster to get ~100 total
    samples_per_cluster = 100 // optimal_k
    print(f"\nTarget: 100 unique test samples")
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
    
    print(f"\n✓ Sampled {len(test_set)} data points for testing")
    
    # Step 3: LLM Testing (with Database Checkpoint)
    print("\n" + "="*80)
    print("STEP 3: LLM TESTING (with checkpoint support)")
    print("="*80)
    
    print("\n⚠️  NOTE: This step requires API keys for GPT, Gemini, and Qwen Plus")
    print("Set these environment variables:")
    print("  - OPENAI_API_KEY")
    print("  - GOOGLE_API_KEY")
    print("  - DASHSCOPE_API_KEY")
    print("\n💡 TIP: Experiment can be resumed if interrupted (Ctrl+C)")
    print("   Data is saved to SQLite database after each prediction")
    
    proceed = input("\nDo you have API keys configured? (y/n): ")
    
    if proceed.lower() == 'y':
        # Initialize with database support
        tester = LLMTester(
            test_data_path="results/sampling/llm_test_data.csv",
            runs_per_sample=4,
            db_path='results/llm_predictions/predictions.db'
        )
        
        # Show existing progress
        print("\n📊 Checking existing progress...")
        from llm_testing.database import ResultsDatabase
        db = ResultsDatabase('results/llm_predictions/predictions.db')
        has_progress = False
        
        for model in ['gpt', 'gemini', 'qwen']:
            progress = db.get_progress(model)
            if progress and progress['completed'] > 0:
                has_progress = True
                print(f"  {model.upper()}: {progress['completed']}/{progress['total']} ({progress['percentage']:.1f}%)")
        
        if not has_progress:
            print("  No existing progress found. Starting fresh.")
        else:
            print("\n⚡ Will resume from checkpoint (skip completed predictions)")
        
        db.close()
        
        # Run experiment (auto-resume)
        all_results = tester.run_full_experiment(
            models=['gpt', 'gemini', 'qwen'],
            save_dir='results/llm_predictions'
        )
        print("\n✓ LLM testing complete")
    else:
        print("\n⚠️  Skipping LLM testing. You can run it later with:")
        print("     python llm_testing/llm_tester.py")
        return
    
    # Step 4: Evaluation
    print("\n" + "="*80)
    print("STEP 4: EVALUATION & ANALYSIS")
    print("="*80)
    
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
    
    print("\n✓ Evaluation complete")
    
    # Final Summary
    print("\n" + "="*80)
    print("EXPERIMENT COMPLETE!")
    print("="*80)
    
    print("\n📊 Results Summary:")
    print(f"  - Clusters used: {optimal_k}")
    print(f"  - Test samples: {len(test_set)}")
    print(f"  - Models tested: GPT, Gemini, Qwen Plus")
    print(f"  - Runs per sample: 4")
    print(f"  - Total predictions: {len(test_set) * 4 * 3}")
    
    print("\n📁 Output Files:")
    print("  Clustering (existing):")
    print("    - results/clustering/clustered_data.csv")
    print("    - results/clustering/optimal_k_analysis_report.png")
    print("  Sampling:")
    print("    - results/sampling/test_set.csv")
    print("    - results/sampling/llm_test_data.csv")
    print("  LLM Predictions:")
    print("    - results/llm_predictions/predictions.db (SQLite)")
    print("    - results/llm_predictions/gpt_results.csv")
    print("    - results/llm_predictions/gemini_results.csv")
    print("    - results/llm_predictions/qwen_results.csv")
    print("  Evaluation:")
    print("    - results/evaluation/model_comparison.png")
    print("    - results/evaluation/model_comparison.csv")
    print("    - results/evaluation/model_comparison_table.tex")
    
    print("\n💡 Useful Commands:")
    print("  Check progress:  python scripts/check_progress.py")
    print("  Resume if stop:  python scripts/resume_experiment.py")
    print("  View errors:     python scripts/view_errors.py")
    
    print("\n✅ Ready for paper writing!")
    print("="*80)


if __name__ == "__main__":
    main()
