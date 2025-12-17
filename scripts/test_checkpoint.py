"""
Test Database Checkpoint System
Run on 1 sample only to verify checkpoint works
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()

from llm_testing.llm_tester import LLMTester
from llm_testing.database import ResultsDatabase
import pandas as pd


def main():
    """Test checkpoint system with 1 sample"""
    print("\n" + "="*70)
    print("TESTING DATABASE CHECKPOINT SYSTEM")
    print("="*70)
    
    # Load test data
    test_data = pd.read_csv('results/sampling/llm_test_data.csv')
    
    # Create mini test set (1 sample only)
    mini_test = test_data.head(1).copy()
    mini_test.to_csv('results/sampling/mini_test.csv', index=False)
    print(f"✓ Created mini test set: 1 sample")
    print(f"  Test ID: {mini_test.iloc[0]['test_id']}")
    print(f"  Ground Truth: {mini_test.iloc[0]['ground_truth']} ({mini_test.iloc[0]['ground_truth_label']})")
    
    # Initialize tester with mini dataset
    tester = LLMTester(
        test_data_path='results/sampling/mini_test.csv',
        runs_per_sample=4,
        db_path='results/llm_predictions/test_checkpoint.db'
    )
    
    print("\n" + "="*70)
    print("PHASE 1: Run 2 models (GPT and Gemini)")
    print("="*70)
    
    # Run only 2 models first
    tester.run_full_experiment(
        models=['gpt', 'gemini'],
        save_dir='results/llm_predictions'
    )
    
    print("\n" + "="*70)
    print("PHASE 2: Check progress")
    print("="*70)
    
    db = ResultsDatabase('results/llm_predictions/test_checkpoint.db')
    stats = db.get_statistics()
    print(f"\n📊 Statistics:")
    print(f"  Total predictions: {stats['total_predictions']}")
    print(f"  By model: {stats['by_model']}")
    
    for model in ['gpt', 'gemini', 'qwen']:
        progress = db.get_progress(model)
        if progress:
            print(f"\n{model.upper()}:")
            print(f"  Completed: {progress['completed']}/{progress['total']} ({progress['percentage']:.1f}%)")
    
    db.close()
    
    print("\n" + "="*70)
    print("PHASE 3: Resume - Add Qwen (should skip GPT and Gemini)")
    print("="*70)
    
    # Re-initialize tester (simulating resume)
    tester2 = LLMTester(
        test_data_path='results/sampling/mini_test.csv',
        runs_per_sample=4,
        db_path='results/llm_predictions/test_checkpoint.db'
    )
    
    # Run all 3 models (should skip GPT and Gemini)
    tester2.run_full_experiment(
        models=['gpt', 'gemini', 'qwen'],
        save_dir='results/llm_predictions'
    )
    
    print("\n" + "="*70)
    print("PHASE 4: Final verification")
    print("="*70)
    
    db = ResultsDatabase('results/llm_predictions/test_checkpoint.db')
    stats = db.get_statistics()
    
    print(f"\n📊 Final Statistics:")
    print(f"  Total predictions: {stats['total_predictions']}")
    print(f"  Expected: {1 * 4 * 3} (1 sample × 4 runs × 3 models)")
    
    for model in ['gpt', 'gemini', 'qwen']:
        progress = db.get_progress(model)
        if progress:
            status = "✅" if progress['percentage'] == 100 else "⚠️"
            print(f"  {status} {model.upper()}: {progress['completed']}/{progress['total']} ({progress['percentage']:.1f}%)")
    
    # Export to check data
    print(f"\n📁 Exported files:")
    for model in ['gpt', 'gemini', 'qwen']:
        output_file = f'results/llm_predictions/test_{model}_results.csv'
        db.export_to_csv(model, output_file)
    
    db.close()
    
    print("\n" + "="*70)
    print("✅ CHECKPOINT SYSTEM TEST COMPLETE")
    print("="*70)
    print("\nVerify:")
    print("  1. GPT and Gemini were skipped in Phase 3")
    print("  2. Only Qwen ran in Phase 3")
    print("  3. Total predictions = 12 (1×4×3)")
    print("  4. All CSVs exported successfully")


if __name__ == "__main__":
    main()
