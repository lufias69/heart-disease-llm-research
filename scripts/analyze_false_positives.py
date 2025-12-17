"""
Analyze false positives to understand why accuracy is low
"""
import sys
sys.path.append('.')

import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

# Load results
df = pd.read_csv('results/llm_predictions/gpt_results.csv')

# Get ground truth and predictions per test_id
gt = df.groupby('test_id')['ground_truth'].first()
pred = df.groupby('test_id')['prediction'].mean()

print("=" * 70)
print("DISTRIBUTION ANALYSIS")
print("=" * 70)
print("\nGround Truth distribution:")
print(gt.value_counts())
print("\nPrediction distribution (majority vote):")
print((pred >= 0.5).value_counts())

# Confusion Matrix
print("\n" + "=" * 70)
print("CONFUSION MATRIX")
print("=" * 70)
cm = confusion_matrix(gt, (pred >= 0.5).astype(int))
print(f"True Negatives (TN): {cm[0,0]}")
print(f"False Positives (FP): {cm[0,1]} ← PROBLEM!")
print(f"False Negatives (FN): {cm[1,0]}")
print(f"True Positives (TP): {cm[1,1]}")

# Analyze false positives
print("\n" + "=" * 70)
print("FALSE POSITIVES ANALYSIS (Prediksi SAKIT, Sebenarnya SEHAT)")
print("=" * 70)
fp_ids = gt[(gt == 0) & ((pred >= 0.5))].index.tolist()
print(f"\nTotal False Positives: {len(fp_ids)}")
print(f"Test IDs (first 10): {fp_ids[:10]}")

# Show sample false positives with features
print("\n" + "=" * 70)
print("SAMPLE FALSE POSITIVE CASES")
print("=" * 70)
for tid in fp_ids[:5]:
    sample = df[df['test_id'] == tid].iloc[0]
    print(f"\n[Test ID {tid}] Ground Truth: 0 (SEHAT), Predicted: 1 (SAKIT)")
    
    # Get all feature columns
    feature_cols = [col for col in df.columns if col not in ['test_id', 'run_id', 'prediction', 'prediction_binary', 'justification', 'raw_response', 'ground_truth', 'timestamp', 'error']]
    
    print("Features:")
    for col in feature_cols[:10]:  # Show first 10 features
        val = sample.get(col, '?')
        print(f"  {col}: {val}")
    
    # Show justification (first 200 chars)
    if 'justification' in sample:
        just = str(sample['justification'])[:200]
        print(f"\nJustification: {just}...")

print("\n" + "=" * 70)
print("RECOMMENDATION")
print("=" * 70)
print("""
PROBLEM: Model terlalu KONSERVATIF (over-predicting disease)
  → 49 false positives vs 0-1 false negatives
  
POSSIBLE CAUSES:
1. Prompt terlalu mengarahkan ke "better safe than sorry"
2. Model diberi role "expert cardiologist" → bias towards finding disease
3. Threshold 0.5 mungkin tidak optimal
4. Training data imbalanced?

SOLUTIONS:
A. TWEAK PROMPT:
   - Remove "expert cardiologist" role
   - Add "balanced assessment" instruction
   - Emphasize "accurate diagnosis" not "err on side of caution"
   
B. ADJUST THRESHOLD:
   - Try threshold 0.6 or 0.7 instead of 0.5
   - Use ROC curve to find optimal threshold
   
C. ADD CALIBRATION:
   - Use probability calibration (Platt scaling)
   - Adjust based on validation set
   
D. PROMPT ENGINEERING:
   - Add examples of false positives
   - Include "don't over-diagnose" instruction
   - Make prompt more neutral

WANT TO TRY? Choose option A (change prompt) first!
""")
