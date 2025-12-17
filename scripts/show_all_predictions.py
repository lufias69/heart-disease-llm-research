"""
Show all individual predictions in database
"""
import sqlite3

conn = sqlite3.connect('results/llm_predictions/test_checkpoint.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT test_id, run_id, model, prediction, prediction_binary, 
           justification, timestamp 
    FROM predictions 
    ORDER BY model, test_id, run_id
''')
rows = cursor.fetchall()

print("=== ALL PREDICTIONS STORED IN DATABASE ===\n")
print(f"Total: {len(rows)} individual predictions\n")

for i, row in enumerate(rows, 1):
    test_id, run_id, model, pred, pred_bin, justification, timestamp = row
    print(f"{i}. Model={model.upper()}, Test={test_id}, Run={run_id}, Prediction={pred}")
    print(f"   Timestamp: {timestamp}")
    if justification:
        print(f"   Justification: {justification[:100]}...")
    print()

conn.close()

print("\n" + "="*70)
print("✅ SETIAP 1 PREDIKSI TERSIMPAN INDIVIDUAL!")
print("="*70)
print("\nContoh skenario error:")
print("  - GPT Run 1: ✓ Saved")
print("  - GPT Run 2: ✓ Saved")
print("  - GPT Run 3: ❌ Error (internet putus)")
print("  - Resume: Skip Run 1 & 2, langsung Run 3")
print("\n✅ Tidak perlu ulang dari awal!")
