"""
Threshold optimization - find best threshold for accuracy
"""
import sys
sys.path.append('.')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
from llm_testing.database import ResultsDatabase

print("=" * 80)
print("THRESHOLD OPTIMIZATION")
print("=" * 80)

# Load OLD results
db = ResultsDatabase('results/llm_predictions/predictions_old_prompt.db')
gpt_df = pd.DataFrame(db.get_all_predictions('gpt'))
db.close()

# Convert to numeric
gpt_df['prediction'] = pd.to_numeric(gpt_df['prediction'], errors='coerce')

# Get average prediction per test_id
gt = gpt_df.groupby('test_id')['ground_truth'].first()
pred_probs = gpt_df.groupby('test_id')['prediction'].mean()

print(f"\nTotal samples: {len(gt)}")
print(f"Ground truth distribution: {gt.value_counts().to_dict()}")

# Try different thresholds
thresholds = np.arange(0.1, 1.0, 0.05)
results = []

print("\n" + "=" * 80)
print("TESTING DIFFERENT THRESHOLDS")
print("=" * 80)

for thresh in thresholds:
    pred_binary = (pred_probs >= thresh).astype(int)
    
    acc = accuracy_score(gt, pred_binary)
    prec = precision_score(gt, pred_binary, zero_division=0)
    rec = recall_score(gt, pred_binary, zero_division=0)
    f1 = f1_score(gt, pred_binary, zero_division=0)
    
    # Count FP and FN
    fp = ((pred_binary == 1) & (gt == 0)).sum()
    fn = ((pred_binary == 0) & (gt == 1)).sum()
    
    results.append({
        'threshold': thresh,
        'accuracy': acc,
        'precision': prec,
        'recall': rec,
        'f1': f1,
        'fp': fp,
        'fn': fn
    })
    
    if thresh in [0.3, 0.5, 0.7, 0.9]:
        print(f"\nThreshold: {thresh:.2f}")
        print(f"  Accuracy:  {acc:.4f}")
        print(f"  Precision: {prec:.4f}")
        print(f"  Recall:    {rec:.4f}")
        print(f"  F1-Score:  {f1:.4f}")
        print(f"  FP: {fp}, FN: {fn}")

results_df = pd.DataFrame(results)

# Find best thresholds
best_acc = results_df.loc[results_df['accuracy'].idxmax()]
best_f1 = results_df.loc[results_df['f1'].idxmax()]

print("\n" + "=" * 80)
print("OPTIMAL THRESHOLDS")
print("=" * 80)

print(f"\n🎯 BEST ACCURACY: Threshold = {best_acc['threshold']:.2f}")
print(f"  Accuracy:  {best_acc['accuracy']:.4f}")
print(f"  Precision: {best_acc['precision']:.4f}")
print(f"  Recall:    {best_acc['recall']:.4f}")
print(f"  F1-Score:  {best_acc['f1']:.4f}")
print(f"  FP: {int(best_acc['fp'])}, FN: {int(best_acc['fn'])}")

print(f"\n🎯 BEST F1-SCORE: Threshold = {best_f1['threshold']:.2f}")
print(f"  Accuracy:  {best_f1['accuracy']:.4f}")
print(f"  Precision: {best_f1['precision']:.4f}")
print(f"  Recall:    {best_f1['recall']:.4f}")
print(f"  F1-Score:  {best_f1['f1']:.4f}")
print(f"  FP: {int(best_f1['fp'])}, FN: {int(best_f1['fn'])}")

# Visualize
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Threshold Optimization Analysis', fontsize=16, fontweight='bold')

# 1. All metrics vs threshold
ax1 = axes[0, 0]
ax1.plot(results_df['threshold'], results_df['accuracy'], 'o-', label='Accuracy', linewidth=2)
ax1.plot(results_df['threshold'], results_df['precision'], 's-', label='Precision', linewidth=2)
ax1.plot(results_df['threshold'], results_df['recall'], '^-', label='Recall', linewidth=2)
ax1.plot(results_df['threshold'], results_df['f1'], 'd-', label='F1-Score', linewidth=2)
ax1.axvline(x=0.5, color='red', linestyle='--', alpha=0.5, label='Current (0.5)')
ax1.axvline(x=best_acc['threshold'], color='green', linestyle='--', alpha=0.5, label=f'Best Acc ({best_acc["threshold"]:.2f})')
ax1.set_xlabel('Threshold')
ax1.set_ylabel('Score')
ax1.set_title('Metrics vs Threshold')
ax1.legend(loc='best')
ax1.grid(alpha=0.3)

# 2. FP and FN vs threshold
ax2 = axes[0, 1]
ax2.plot(results_df['threshold'], results_df['fp'], 'o-', label='False Positives', linewidth=2, color='red')
ax2.plot(results_df['threshold'], results_df['fn'], 's-', label='False Negatives', linewidth=2, color='orange')
ax2.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5)
ax2.axvline(x=best_acc['threshold'], color='green', linestyle='--', alpha=0.5)
ax2.set_xlabel('Threshold')
ax2.set_ylabel('Count')
ax2.set_title('False Positives/Negatives vs Threshold')
ax2.legend(loc='best')
ax2.grid(alpha=0.3)

# 3. ROC Curve
ax3 = axes[1, 0]
fpr, tpr, _ = roc_curve(gt, pred_probs)
roc_auc = auc(fpr, tpr)
ax3.plot(fpr, tpr, 'b-', linewidth=2, label=f'ROC curve (AUC = {roc_auc:.3f})')
ax3.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random')
ax3.set_xlabel('False Positive Rate')
ax3.set_ylabel('True Positive Rate')
ax3.set_title('ROC Curve')
ax3.legend(loc='best')
ax3.grid(alpha=0.3)

# 4. Prediction distribution
ax4 = axes[1, 1]
ax4.hist(pred_probs[gt == 0], bins=20, alpha=0.6, label='No Disease (0)', color='blue', edgecolor='black')
ax4.hist(pred_probs[gt == 1], bins=20, alpha=0.6, label='Disease (1)', color='red', edgecolor='black')
ax4.axvline(x=0.5, color='gray', linestyle='--', linewidth=2, label='Current threshold (0.5)')
ax4.axvline(x=best_acc['threshold'], color='green', linestyle='--', linewidth=2, label=f'Optimal ({best_acc["threshold"]:.2f})')
ax4.set_xlabel('Prediction Probability')
ax4.set_ylabel('Frequency')
ax4.set_title('Prediction Distribution by Ground Truth')
ax4.legend(loc='best')
ax4.grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('results/evaluation/threshold_optimization.png', dpi=300, bbox_inches='tight')
print(f"\n✅ Saved visualization: results/evaluation/threshold_optimization.png")

# Save results
results_df.to_csv('results/evaluation/threshold_optimization.csv', index=False)
print(f"✅ Saved results: results/evaluation/threshold_optimization.csv")

print("\n" + "=" * 80)
print("CONCLUSION")
print("=" * 80)
print(f"""
Current threshold (0.5):
  - Accuracy: {results_df[results_df['threshold'] == 0.5]['accuracy'].values[0]:.4f}
  - FP: {int(results_df[results_df['threshold'] == 0.5]['fp'].values[0])}, FN: {int(results_df[results_df['threshold'] == 0.5]['fn'].values[0])}

Optimal threshold ({best_acc['threshold']:.2f}):
  - Accuracy: {best_acc['accuracy']:.4f}
  - FP: {int(best_acc['fp'])}, FN: {int(best_acc['fn'])}
  
⚠️ IMPORTANT: Models still predicting almost all positive!
This suggests the problem is NOT just threshold.
The models are genuinely biased or the task is inherently difficult.
""")
