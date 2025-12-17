"""
Check SQLite database contents
"""
import sqlite3

conn = sqlite3.connect('results/llm_predictions/test_checkpoint.db')
cursor = conn.cursor()

print("=== SQLite Database Info ===")
print("File: test_checkpoint.db")
print("Type: SQLite3 Database")

# Get tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("\nTables:")
for table in tables:
    print(f"  - {table[0]}")

# Count predictions
cursor.execute("SELECT COUNT(*) FROM predictions")
count = cursor.fetchone()[0]
print(f"\nTotal predictions: {count}")

# Show sample
cursor.execute("SELECT test_id, run_id, model, prediction_binary, ground_truth FROM predictions LIMIT 3")
rows = cursor.fetchall()
print("\nSample data:")
for row in rows:
    print(f"  Test {row[0]}, Run {row[1]}, Model: {row[2]}, Prediction: {row[3]}, Truth: {row[4]}")

conn.close()
