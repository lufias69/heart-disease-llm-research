"""
Generate missing supplementary figures for paper submission
"""
import sys
sys.path.append('.')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc, confusion_matrix
from llm_testing.database import ResultsDatabase

print("=" * 80)
print("GENERATING SUPPLEMENTARY FIGURES FOR SUBMISSION")
print("=" * 80)

# Load data
db_old = ResultsDatabase('results/llm_predictions/predictions_old_prompt.db')
db_new = ResultsDatabase('results/llm_predictions/predictions.db')

models = ['gpt', 'gemini', 'qwen']
data = {}

for model in models:
    data[f'{model}_old'] = pd.DataFrame(db_old.get_all_predictions(model))
    data[f'{model}_new'] = pd.DataFrame(db_new.get_all_predictions(model))
    data[f'{model}_old']['prediction'] = pd.to_numeric(data[f'{model}_old']['prediction'], errors='coerce')
    data[f'{model}_new']['prediction'] = pd.to_numeric(data[f'{model}_new']['prediction'], errors='coerce')

db_old.close()
db_new.close()

# ============================================================================
# FIGURE S1: ROC CURVES
# ============================================================================
print("\n📊 Generating Supplementary Figure S1: ROC Curves...")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Supplementary Figure S1: ROC Curves and Discrimination Analysis', 
             fontsize=16, fontweight='bold')

for idx, model in enumerate(models):
    ax = axes[idx]
    
    # Use OLD prompt data
    df = data[f'{model}_old']
    
    # Get ground truth and predictions
    gt = df.groupby('test_id')['ground_truth'].first()
    pred_probs = df.groupby('test_id')['prediction'].mean()
    
    # Calculate ROC
    fpr, tpr, thresholds = roc_curve(gt, pred_probs)
    roc_auc = auc(fpr, tpr)
    
    # Plot ROC curve
    ax.plot(fpr, tpr, 'b-', linewidth=3, label=f'ROC curve (AUC = {roc_auc:.3f})')
    ax.plot([0, 1], [0, 1], 'r--', linewidth=2, label='Random classifier (AUC = 0.5)')
    
    # Mark current threshold (0.5)
    idx_threshold = np.argmin(np.abs(thresholds - 0.5))
    ax.plot(fpr[idx_threshold], tpr[idx_threshold], 'go', markersize=15, 
            label=f'Threshold 0.5 (TPR={tpr[idx_threshold]:.2f}, FPR={fpr[idx_threshold]:.2f})')
    
    # Find optimal threshold (Youden's index)
    youden = tpr - fpr
    idx_optimal = np.argmax(youden)
    ax.plot(fpr[idx_optimal], tpr[idx_optimal], 'mo', markersize=15,
            label=f'Optimal (thresh={thresholds[idx_optimal]:.2f})')
    
    ax.set_xlabel('False Positive Rate', fontsize=12, fontweight='bold')
    ax.set_ylabel('True Positive Rate', fontsize=12, fontweight='bold')
    ax.set_title(f'{model.upper()}', fontsize=14, fontweight='bold')
    ax.legend(loc='lower right', fontsize=9)
    ax.grid(alpha=0.3)
    ax.set_xlim([-0.05, 1.05])
    ax.set_ylim([-0.05, 1.05])

plt.tight_layout()
plt.savefig('results/evaluation/supplementary_fig_s1_roc_curves.png', dpi=300, bbox_inches='tight')
print("✅ Saved: results/evaluation/supplementary_fig_s1_roc_curves.png")

# ============================================================================
# FIGURE S2: PREDICTION DISTRIBUTIONS
# ============================================================================
print("\n📊 Generating Supplementary Figure S2: Prediction Distributions...")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Supplementary Figure S2: Prediction Probability Distributions by Ground Truth', 
             fontsize=16, fontweight='bold')

for idx, model in enumerate(models):
    ax = axes[idx]
    
    df = data[f'{model}_old']
    
    # Get ground truth and predictions
    gt = df.groupby('test_id')['ground_truth'].first()
    pred_probs = df.groupby('test_id')['prediction'].mean()
    
    # Separate by ground truth
    pred_disease = pred_probs[gt == 1]
    pred_no_disease = pred_probs[gt == 0]
    
    # Plot distributions
    ax.hist(pred_no_disease, bins=20, alpha=0.6, color='blue', 
            edgecolor='black', linewidth=1.5, label=f'No Disease (n={len(pred_no_disease)})')
    ax.hist(pred_disease, bins=20, alpha=0.6, color='red', 
            edgecolor='black', linewidth=1.5, label=f'Disease (n={len(pred_disease)})')
    
    # Add threshold line
    ax.axvline(x=0.5, color='green', linestyle='--', linewidth=3, 
               label='Decision Threshold (0.5)')
    
    # Statistics
    mean_disease = pred_disease.mean()
    mean_no_disease = pred_no_disease.mean()
    
    ax.text(0.05, 0.95, f'Mean (Disease): {mean_disease:.3f}\nMean (No Disease): {mean_no_disease:.3f}',
            transform=ax.transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    ax.set_xlabel('Prediction Probability', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_title(f'{model.upper()}', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(alpha=0.3, axis='y')
    ax.set_xlim([0, 1])

plt.tight_layout()
plt.savefig('results/evaluation/supplementary_fig_s2_distributions.png', dpi=300, bbox_inches='tight')
print("✅ Saved: results/evaluation/supplementary_fig_s2_distributions.png")

# ============================================================================
# FIGURE S3: FEATURE CORRELATIONS
# ============================================================================
print("\n📊 Generating Supplementary Figure S3: Feature Correlations...")

# Load full test data to get all features
test_data = pd.read_csv('results/sampling/llm_test_data.csv')

# Get average predictions across all models
all_predictions = []
for model in models:
    df = data[f'{model}_old']
    pred = df.groupby('test_id')['prediction'].mean()
    all_predictions.append(pred)

avg_predictions = pd.DataFrame(all_predictions).mean(axis=0)

# Merge with test data
test_data['avg_prediction'] = test_data['test_id'].map(avg_predictions)

# Select relevant features for correlation
feature_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# Calculate correlations
correlations = {}
for col in feature_cols:
    if col in test_data.columns:
        corr = test_data[col].corr(test_data['avg_prediction'])
        correlations[col] = corr

# Create visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Supplementary Figure S3: Feature-Prediction Correlations', 
             fontsize=16, fontweight='bold')

# Bar plot
feature_names = list(correlations.keys())
corr_values = list(correlations.values())
colors = ['red' if c > 0.2 else 'gray' for c in corr_values]

ax1.barh(feature_names, corr_values, color=colors, edgecolor='black', linewidth=1.5)
ax1.axvline(x=0, color='black', linewidth=2)
ax1.axvline(x=0.2, color='green', linestyle='--', alpha=0.5, label='Moderate correlation (r=0.2)')
ax1.set_xlabel('Correlation with Prediction', fontsize=12, fontweight='bold')
ax1.set_ylabel('Clinical Feature', fontsize=12, fontweight='bold')
ax1.set_title('A. Feature Importance for Model Predictions', fontsize=12, fontweight='bold')
ax1.legend()
ax1.grid(alpha=0.3, axis='x')

# Scatter plot for top features
top_features = sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)[:4]

for i, (feat, corr) in enumerate(top_features):
    color = plt.cm.Set1(i)
    ax2.scatter(test_data[feat], test_data['avg_prediction'], 
                alpha=0.6, s=80, label=f'{feat} (r={corr:.3f})', 
                color=color, edgecolors='black', linewidth=1)

ax2.set_xlabel('Feature Value (standardized)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Average Prediction Probability', fontsize=12, fontweight='bold')
ax2.set_title('B. Top 4 Predictive Features', fontsize=12, fontweight='bold')
ax2.legend(loc='best')
ax2.grid(alpha=0.3)
ax2.axhline(y=0.5, color='green', linestyle='--', linewidth=2, label='Decision threshold')

plt.tight_layout()
plt.savefig('results/evaluation/supplementary_fig_s3_feature_correlations.png', dpi=300, bbox_inches='tight')
print("✅ Saved: results/evaluation/supplementary_fig_s3_feature_correlations.png")

# ============================================================================
# FIGURE 2 (MAIN): CONFUSION MATRICES
# ============================================================================
print("\n📊 Generating Main Figure 2: Confusion Matrices...")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Figure 2: Confusion Matrices - Strong Positive Bias Across All Models', 
             fontsize=16, fontweight='bold')

for idx, model in enumerate(models):
    # OLD prompt
    ax_old = axes[0, idx]
    df = data[f'{model}_old']
    gt = df.groupby('test_id')['ground_truth'].first()
    pred = df.groupby('test_id')['prediction'].apply(lambda x: (x >= 0.5).sum() >= 2).astype(int)
    cm = confusion_matrix(gt, pred)
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='RdYlGn_r', 
                xticklabels=['Predicted: No Disease', 'Predicted: Disease'],
                yticklabels=['True: No Disease', 'True: Disease'],
                ax=ax_old, cbar_kws={'label': 'Count'},
                annot_kws={'size': 16, 'weight': 'bold'})
    ax_old.set_title(f'{model.upper()} - OLD Prompt\n(Expert Cardiologist)', 
                     fontsize=12, fontweight='bold')
    
    # Calculate metrics
    tn, fp, fn, tp = cm.ravel()
    acc = (tp + tn) / (tp + tn + fp + fn)
    sens = tp / (tp + fn) if (tp + fn) > 0 else 0
    spec = tn / (tn + fp) if (tn + fp) > 0 else 0
    
    ax_old.text(0.5, -0.15, f'Accuracy: {acc:.1%} | Sensitivity: {sens:.1%} | Specificity: {spec:.1%}',
                transform=ax_old.transAxes, ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    
    # NEW prompt
    ax_new = axes[1, idx]
    df = data[f'{model}_new']
    gt = df.groupby('test_id')['ground_truth'].first()
    pred = df.groupby('test_id')['prediction'].apply(lambda x: (x >= 0.5).sum() >= 2).astype(int)
    cm = confusion_matrix(gt, pred)
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='RdYlGn_r',
                xticklabels=['Predicted: No Disease', 'Predicted: Disease'],
                yticklabels=['True: No Disease', 'True: Disease'],
                ax=ax_new, cbar_kws={'label': 'Count'},
                annot_kws={'size': 16, 'weight': 'bold'})
    ax_new.set_title(f'{model.upper()} - NEW Prompt\n(Neutral Assessor)', 
                     fontsize=12, fontweight='bold')
    
    # Calculate metrics
    tn, fp, fn, tp = cm.ravel()
    acc = (tp + tn) / (tp + tn + fp + fn)
    sens = tp / (tp + fn) if (tp + fn) > 0 else 0
    spec = tn / (tn + fp) if (tn + fp) > 0 else 0
    
    ax_new.text(0.5, -0.15, f'Accuracy: {acc:.1%} | Sensitivity: {sens:.1%} | Specificity: {spec:.1%}',
                transform=ax_new.transAxes, ha='center', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

plt.tight_layout()
plt.savefig('results/evaluation/figure_2_confusion_matrices.png', dpi=300, bbox_inches='tight')
print("✅ Saved: results/evaluation/figure_2_confusion_matrices.png")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 80)
print("✅ ALL SUPPLEMENTARY FIGURES GENERATED!")
print("=" * 80)
print("\nGenerated files:")
print("  Main Figure:")
print("    - figure_2_confusion_matrices.png")
print("\n  Supplementary Figures:")
print("    - supplementary_fig_s1_roc_curves.png")
print("    - supplementary_fig_s2_distributions.png")
print("    - supplementary_fig_s3_feature_correlations.png")
print("\n  Previously Generated:")
print("    - comprehensive_consistency_analysis.png (Figure 1 - 7 panels)")
print("    - prompt_comparison.png (Figure 3)")
print("\n📊 Ready for journal submission!")
