"""
Reset Database - Delete all predictions and start fresh
Use this if you want to completely restart the experiment
"""

import os
import sys


def main():
    """Reset database"""
    db_path = 'results/llm_predictions/predictions.db'
    
    if not os.path.exists(db_path):
        print("✅ No database found. Nothing to reset.")
        return
    
    print("\n" + "="*70)
    print("⚠️  WARNING: RESET DATABASE")
    print("="*70)
    print("\nThis will:")
    print("  - Delete all saved predictions")
    print("  - Reset progress to 0%")
    print("  - Remove checkpoint data")
    print(f"\nDatabase file: {db_path}")
    
    # Show current stats
    try:
        from llm_testing.database import ResultsDatabase
        db = ResultsDatabase(db_path)
        stats = db.get_statistics()
        
        print(f"\n📊 Current Status:")
        print(f"  Total predictions: {stats['total_predictions']}")
        if stats['total_predictions'] > 0:
            print(f"  By model:")
            for model, count in stats['by_model'].items():
                print(f"    {model.upper()}: {count}")
        
        db.close()
    except Exception as e:
        print(f"\nCould not read database: {e}")
    
    print("\n" + "="*70)
    confirm = input("Type 'RESET' to confirm deletion: ")
    
    if confirm == 'RESET':
        try:
            os.remove(db_path)
            print("\n✅ Database deleted successfully!")
            print("\nYou can now run:")
            print("  python run_experiment.py")
        except Exception as e:
            print(f"\n❌ Error deleting database: {e}")
    else:
        print("\n❌ Reset cancelled.")


if __name__ == "__main__":
    main()
