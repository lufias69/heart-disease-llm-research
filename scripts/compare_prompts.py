"""
Compare results between OLD PROMPT (biased) vs NEW PROMPT (neutral)
"""
import sys
sys.path.append('.')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from llm_testing.database import ResultsDatabase

print("=" * 80)
print("PROMPT COMPARISON ANALYSIS")
print("=" * 80)

# Load OLD results (biased prompt)
print("\n📂 Loading OLD PROMPT results...")
db_old = ResultsDatabase('results/llm_predictions/predictions_old_prompt.db')
old_gpt = pd.DataFrame(db_old.get_all_predictions('gpt'))
old_gemini = pd.DataFrame(db_old.get_all_predictions('gemini'))
old_qwen = pd.DataFrame(db_old.get_all_predictions('qwen'))
db_old.close()

print(f"  GPT: {len(old_gpt)} predictions")
print(f"  Gemini: {len(old_gemini)} predictions")
print(f"  Qwen: {len(old_qwen)} predictions")

# Load NEW results (neutral prompt)
print("\n📂 Loading NEW PROMPT results...")
db_new = ResultsDatabase('results/llm_predictions/predictions.db')
new_gpt = pd.DataFrame(db_new.get_all_predictions('gpt'))
new_gemini = pd.DataFrame(db_new.get_all_predictions('gemini'))
new_qwen = pd.DataFrame(db_new.get_all_predictions('qwen'))
db_new.close()

print(f"  GPT: {len(new_gpt)} predictions")
print(f"  Gemini: {len(new_gemini)} predictions")
print(f"  Qwen: {len(new_qwen)} predictions")

def calculate_metrics(df):
    """Calculate metrics from predictions dataframe"""
    # Convert prediction to numeric if string
    if df['prediction'].dtype == 'object':
        df['prediction'] = pd.to_numeric(df['prediction'], errors='coerce')
    
    # Get majority vote per test_id
    gt = df.groupby('test_id')['ground_truth'].first()
    pred = df.groupby('test_id')['prediction'].mean()
    pred_binary = (pred >= 0.5).astype(int)
    
    # Metrics
    acc = accuracy_score(gt, pred_binary)
    prec = precision_score(gt, pred_binary, zero_division=0)
    rec = recall_score(gt, pred_binary)
    f1 = f1_score(gt, pred_binary)
    
    # Confusion matrix
    cm = confusion_matrix(gt, pred_binary)
    tn, fp, fn, tp = cm.ravel()
    
    return {
        'accuracy': acc,
        'precision': prec,
        'recall': rec,
        'f1': f1,
        'tn': tn,
        'fp': fp,
        'fn': fn,
        'tp': tp,
        'total': len(gt)
    }

# Calculate metrics for all models
print("\n" + "=" * 80)
print("METRICS COMPARISON")
print("=" * 80)

models = ['GPT', 'Gemini', 'Qwen']
old_dfs = [old_gpt, old_gemini, old_qwen]
new_dfs = [new_gpt, new_gemini, new_qwen]

results = []

for model, old_df, new_df in zip(models, old_dfs, new_dfs):
    print(f"\n{'=' * 80}")
    print(f"{model.upper()}")
    print(f"{'=' * 80}")
    
    old_metrics = calculate_metrics(old_df)
    new_metrics = calculate_metrics(new_df)
    
    print("\n📊 OLD PROMPT (Biased - 'Dr. CardioExpert'):")
    print(f"  Accuracy:  {old_metrics['accuracy']:.4f}")
    print(f"  Precision: {old_metrics['precision']:.4f}")
    print(f"  Recall:    {old_metrics['recall']:.4f}")
    print(f"  F1-Score:  {old_metrics['f1']:.4f}")
    print(f"  Confusion Matrix: TN={old_metrics['tn']}, FP={old_metrics['fp']}, FN={old_metrics['fn']}, TP={old_metrics['tp']}")
    
    print("\n📊 NEW PROMPT (Neutral - 'Balanced AI Assistant'):")
    print(f"  Accuracy:  {new_metrics['accuracy']:.4f}")
    print(f"  Precision: {new_metrics['precision']:.4f}")
    print(f"  Recall:    {new_metrics['recall']:.4f}")
    print(f"  F1-Score:  {new_metrics['f1']:.4f}")
    print(f"  Confusion Matrix: TN={new_metrics['tn']}, FP={new_metrics['fp']}, FN={new_metrics['fn']}, TP={new_metrics['tp']}")
    
    print("\n📈 IMPROVEMENT:")
    print(f"  Accuracy:  {(new_metrics['accuracy'] - old_metrics['accuracy'])*100:+.2f}%")
    print(f"  Precision: {(new_metrics['precision'] - old_metrics['precision'])*100:+.2f}%")
    print(f"  Recall:    {(new_metrics['recall'] - old_metrics['recall'])*100:+.2f}%")
    print(f"  F1-Score:  {(new_metrics['f1'] - old_metrics['f1'])*100:+.2f}%")
    print(f"  False Positives: {old_metrics['fp']} → {new_metrics['fp']} ({new_metrics['fp'] - old_metrics['fp']:+d})")
    
    results.append({
        'model': model,
        'prompt': 'OLD',
        **old_metrics
    })
    results.append({
        'model': model,
        'prompt': 'NEW',
        **new_metrics
    })

# Create comparison dataframe
comparison_df = pd.DataFrame(results)

# Save to CSV
comparison_df.to_csv('results/evaluation/prompt_comparison.csv', index=False)
print(f"\n✅ Saved comparison to: results/evaluation/prompt_comparison.csv")

# Create visualizations
print("\n📊 Creating visualizations...")

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Prompt Comparison: OLD (Biased) vs NEW (Neutral)', fontsize=16, fontweight='bold')

# 1. Accuracy comparison
ax1 = axes[0, 0]
pivot_acc = comparison_df.pivot(index='model', columns='prompt', values='accuracy')
pivot_acc[['OLD', 'NEW']].plot(kind='bar', ax=ax1, color=['#ff6b6b', '#51cf66'])
ax1.set_title('Accuracy Comparison', fontsize=12, fontweight='bold')
ax1.set_ylabel('Accuracy')
ax1.set_ylim([0, 1])
ax1.legend(title='Prompt Type')
ax1.grid(axis='y', alpha=0.3)

# 2. F1-Score comparison
ax2 = axes[0, 1]
pivot_f1 = comparison_df.pivot(index='model', columns='prompt', values='f1')
pivot_f1[['OLD', 'NEW']].plot(kind='bar', ax=ax2, color=['#ff6b6b', '#51cf66'])
ax2.set_title('F1-Score Comparison', fontsize=12, fontweight='bold')
ax2.set_ylabel('F1-Score')
ax2.set_ylim([0, 1])
ax2.legend(title='Prompt Type')
ax2.grid(axis='y', alpha=0.3)

# 3. False Positives comparison
ax3 = axes[1, 0]
pivot_fp = comparison_df.pivot(index='model', columns='prompt', values='fp')
pivot_fp[['OLD', 'NEW']].plot(kind='bar', ax=ax3, color=['#ff6b6b', '#51cf66'])
ax3.set_title('False Positives (Lower is Better)', fontsize=12, fontweight='bold')
ax3.set_ylabel('False Positives')
ax3.legend(title='Prompt Type')
ax3.grid(axis='y', alpha=0.3)

# 4. Precision vs Recall
ax4 = axes[1, 1]
for model in models:
    model_data = comparison_df[comparison_df['model'] == model]
    old_data = model_data[model_data['prompt'] == 'OLD']
    new_data = model_data[model_data['prompt'] == 'NEW']
    
    ax4.scatter(old_data['recall'], old_data['precision'], s=200, alpha=0.6, 
                label=f'{model} OLD', marker='o', edgecolors='black', linewidths=2)
    ax4.scatter(new_data['recall'], new_data['precision'], s=200, alpha=0.6,
                label=f'{model} NEW', marker='s', edgecolors='black', linewidths=2)
    
    # Draw arrow from OLD to NEW
    ax4.annotate('', xy=(new_data['recall'].values[0], new_data['precision'].values[0]),
                xytext=(old_data['recall'].values[0], old_data['precision'].values[0]),
                arrowprops=dict(arrowstyle='->', lw=2, alpha=0.5))

ax4.set_title('Precision vs Recall (Arrows show improvement)', fontsize=12, fontweight='bold')
ax4.set_xlabel('Recall')
ax4.set_ylabel('Precision')
ax4.set_xlim([0.4, 1.05])
ax4.set_ylim([0.4, 1.05])
ax4.legend(loc='best', fontsize=8)
ax4.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('results/evaluation/prompt_comparison.png', dpi=300, bbox_inches='tight')
print(f"✅ Saved visualization to: results/evaluation/prompt_comparison.png")

# Summary statistics
print("\n" + "=" * 80)
print("OVERALL SUMMARY")
print("=" * 80)

avg_old = comparison_df[comparison_df['prompt'] == 'OLD'][['accuracy', 'precision', 'recall', 'f1', 'fp']].mean()
avg_new = comparison_df[comparison_df['prompt'] == 'NEW'][['accuracy', 'precision', 'recall', 'f1', 'fp']].mean()

print("\n📊 AVERAGE ACROSS ALL MODELS:")
print("\nOLD PROMPT:")
print(f"  Accuracy:  {avg_old['accuracy']:.4f}")
print(f"  Precision: {avg_old['precision']:.4f}")
print(f"  Recall:    {avg_old['recall']:.4f}")
print(f"  F1-Score:  {avg_old['f1']:.4f}")
print(f"  Avg False Positives: {avg_old['fp']:.1f}")

print("\nNEW PROMPT:")
print(f"  Accuracy:  {avg_new['accuracy']:.4f}")
print(f"  Precision: {avg_new['precision']:.4f}")
print(f"  Recall:    {avg_new['recall']:.4f}")
print(f"  F1-Score:  {avg_new['f1']:.4f}")
print(f"  Avg False Positives: {avg_new['fp']:.1f}")

print("\n✨ IMPROVEMENT:")
print(f"  Accuracy:  {(avg_new['accuracy'] - avg_old['accuracy'])*100:+.2f}%")
print(f"  Precision: {(avg_new['precision'] - avg_old['precision'])*100:+.2f}%")
print(f"  F1-Score:  {(avg_new['f1'] - avg_old['f1'])*100:+.2f}%")
print(f"  False Positives: {avg_old['fp']:.1f} → {avg_new['fp']:.1f} ({avg_new['fp'] - avg_old['fp']:+.1f})")

# Export for paper
print("\n" + "=" * 80)
print("EXPORTING FOR PAPER")
print("=" * 80)

# LaTeX table
latex_table = comparison_df.pivot_table(
    index='model',
    columns='prompt',
    values=['accuracy', 'precision', 'recall', 'f1', 'fp']
).round(4)

with open('results/evaluation/prompt_comparison_table.tex', 'w') as f:
    f.write('\\begin{table}[h]\n')
    f.write('\\centering\n')
    f.write('\\caption{Comparison of OLD (Biased) vs NEW (Neutral) Prompt}\n')
    f.write('\\label{tab:prompt_comparison}\n')
    f.write(latex_table.to_latex())
    f.write('\\end{table}\n')

print("✅ LaTeX table: results/evaluation/prompt_comparison_table.tex")

print("\n" + "=" * 80)
print("✅ COMPARISON COMPLETE!")
print("=" * 80)
print("\nFiles generated:")
print("  1. results/evaluation/prompt_comparison.csv")
print("  2. results/evaluation/prompt_comparison.png")
print("  3. results/evaluation/prompt_comparison_table.tex")
