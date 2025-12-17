"""
Export predictions from database to various formats
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm_testing.database import ResultsDatabase
import pandas as pd
import json


def main():
    """Export predictions"""
    db_path = 'results/llm_predictions/predictions.db'
    
    if not os.path.exists(db_path):
        print("❌ Database not found. Run experiment first.")
        return
    
    db = ResultsDatabase(db_path)
    
    print("\n" + "="*70)
    print("EXPORT PREDICTIONS")
    print("="*70)
    
    # Get stats
    stats = db.get_statistics()
    print(f"\n📊 Database Statistics:")
    print(f"  Total predictions: {stats['total_predictions']}")
    
    if stats['total_predictions'] == 0:
        print("\n⚠️  No predictions to export.")
        db.close()
        return
    
    print(f"\n  By model:")
    for model, count in stats['by_model'].items():
        print(f"    {model.upper()}: {count}")
    
    # Export options
    print("\n" + "="*70)
    print("Export Options:")
    print("="*70)
    print("1. CSV per model (gpt.csv, gemini.csv, qwen.csv)")
    print("2. Combined CSV (all_predictions.csv)")
    print("3. JSON format (predictions.json)")
    print("4. Summary report (summary.txt)")
    print("5. All formats")
    
    choice = input("\nSelect option (1-5): ")
    
    output_dir = 'results/llm_predictions/exports'
    os.makedirs(output_dir, exist_ok=True)
    
    if choice in ['1', '5']:
        print("\n📤 Exporting CSV per model...")
        for model in ['gpt', 'gemini', 'qwen']:
            df = db.get_all_predictions(model)
            if len(df) > 0:
                output_file = f'{output_dir}/{model}_predictions.csv'
                df.to_csv(output_file, index=False)
                print(f"  ✓ {model.upper()}: {output_file} ({len(df)} rows)")
    
    if choice in ['2', '5']:
        print("\n📤 Exporting combined CSV...")
        df = db.get_all_predictions()
        output_file = f'{output_dir}/all_predictions.csv'
        df.to_csv(output_file, index=False)
        print(f"  ✓ Combined: {output_file} ({len(df)} rows)")
    
    if choice in ['3', '5']:
        print("\n📤 Exporting JSON...")
        df = db.get_all_predictions()
        output_file = f'{output_dir}/predictions.json'
        
        # Convert to JSON-friendly format
        records = df.to_dict('records')
        with open(output_file, 'w') as f:
            json.dump(records, f, indent=2)
        print(f"  ✓ JSON: {output_file} ({len(records)} records)")
    
    if choice in ['4', '5']:
        print("\n📤 Generating summary report...")
        output_file = f'{output_dir}/summary_report.txt'
        
        with open(output_file, 'w') as f:
            f.write("="*70 + "\n")
            f.write("LLM PREDICTIONS SUMMARY REPORT\n")
            f.write("="*70 + "\n\n")
            
            f.write(f"Total Predictions: {stats['total_predictions']}\n")
            f.write(f"Errors: {stats['errors']}\n\n")
            
            f.write("By Model:\n")
            for model in ['gpt', 'gemini', 'qwen']:
                df = db.get_all_predictions(model)
                if len(df) > 0:
                    f.write(f"\n{model.upper()}:\n")
                    f.write(f"  Total predictions: {len(df)}\n")
                    
                    # Accuracy
                    correct = (df['prediction_binary'] == df['ground_truth']).sum()
                    accuracy = correct / len(df) * 100
                    f.write(f"  Accuracy: {accuracy:.2f}%\n")
                    
                    # Distribution
                    pred_dist = df['prediction_binary'].value_counts()
                    f.write(f"  Predictions:\n")
                    f.write(f"    Disease (1): {pred_dist.get(1, 0)}\n")
                    f.write(f"    No Disease (0): {pred_dist.get(0, 0)}\n")
                    
                    # Errors
                    errors = df['error'].notna().sum()
                    if errors > 0:
                        f.write(f"  Errors: {errors}\n")
        
        print(f"  ✓ Summary: {output_file}")
    
    db.close()
    
    print("\n" + "="*70)
    print("✅ EXPORT COMPLETE")
    print("="*70)
    print(f"\n📁 Output directory: {output_dir}/")


if __name__ == "__main__":
    main()
