"""
Resume interrupted experiment
Usage: python scripts/resume_experiment.py
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

from llm_testing.llm_tester import LLMTester


def main():
    """Resume experiment from checkpoint"""
    print("\n" + "="*70)
    print("RESUMING EXPERIMENT FROM CHECKPOINT")
    print("="*70)
    
    # Initialize tester (will connect to existing database)
    tester = LLMTester(
        test_data_path='results/sampling/llm_test_data.csv',
        runs_per_sample=4,
        db_path='results/llm_predictions/predictions.db'
    )
    
    # Check current progress
    print("\n📊 Current Progress:")
    for model in ['gpt', 'gemini', 'qwen']:
        progress = tester.db.get_progress(model)
        if progress:
            print(f"  {model.upper()}: {progress['completed']}/{progress['total']} ({progress['percentage']:.1f}%)")
        else:
            print(f"  {model.upper()}: Not started")
    
    print("\n⚡ Resuming experiment (will skip completed predictions)...\n")
    
    # Run experiment (will auto-skip completed predictions)
    results = tester.run_full_experiment(
        models=['gpt', 'gemini', 'qwen'],
        save_dir='results/llm_predictions'
    )
    
    print("\n✅ Experiment resumed and completed!")
    print("📁 Results saved to: results/llm_predictions/")
    print("\nNext steps:")
    print("  1. Check progress: python scripts/check_progress.py")
    print("  2. Run evaluation: python evaluation/evaluator.py")


if __name__ == "__main__":
    main()
