"""
Check experiment progress from database
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm_testing.database import ResultsDatabase


def main():
    """Check current progress"""
    db_path = 'results/llm_predictions/predictions.db'
    
    if not os.path.exists(db_path):
        print("❌ Database not found. Experiment hasn't started yet.")
        return
    
    db = ResultsDatabase(db_path)
    
    print("\n" + "="*70)
    print("EXPERIMENT PROGRESS")
    print("="*70)
    
    # Overall statistics
    stats = db.get_statistics()
    print(f"\n📊 Overall Statistics:")
    print(f"  Total predictions: {stats['total_predictions']}")
    
    if stats['total_predictions'] > 0:
        print(f"\n🤖 By Model:")
        for model, count in stats['by_model'].items():
            print(f"  {model.upper()}: {count} predictions")
            
            # Get progress
            progress = db.get_progress(model)
            if progress:
                percentage = progress['percentage']
                completed = progress['completed']
                total = progress['total']
                
                # Progress bar
                bar_length = 40
                filled = int(bar_length * percentage / 100)
                bar = '█' * filled + '░' * (bar_length - filled)
                
                print(f"    Progress: [{bar}] {percentage:.1f}% ({completed}/{total})")
                
                if progress.get('last_test_id'):
                    print(f"    Last completed: Test ID {progress['last_test_id']}, Run {progress['last_run_id']}")
        
        if stats['errors'] > 0:
            print(f"\n⚠️  Errors: {stats['errors']}")
            print("  Run this to see error details:")
            print("  python scripts/view_errors.py")
    else:
        print("\n⚠️  No predictions recorded yet.")
    
    print("\n" + "="*70)
    
    db.close()


if __name__ == "__main__":
    main()
