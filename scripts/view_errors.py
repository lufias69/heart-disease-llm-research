"""
View errors from database
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm_testing.database import ResultsDatabase
import pandas as pd


def main():
    """View all errors"""
    db_path = 'results/llm_predictions/predictions.db'
    
    if not os.path.exists(db_path):
        print("❌ Database not found.")
        return
    
    db = ResultsDatabase(db_path)
    
    # Get all predictions
    df = db.get_all_predictions()
    
    # Filter errors
    errors = df[df['error'].notna()]
    
    if len(errors) == 0:
        print("✅ No errors found!")
    else:
        print(f"\n⚠️  Found {len(errors)} errors:\n")
        print("="*70)
        
        for idx, row in errors.iterrows():
            print(f"\nTest ID: {row['test_id']}, Run: {row['run_id']}, Model: {row['model']}")
            print(f"Error: {row['error']}")
            print("-"*70)
    
    db.close()


if __name__ == "__main__":
    main()
