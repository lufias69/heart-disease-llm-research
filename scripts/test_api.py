"""
Quick API Test - Test single prediction from each LLM
"""

import os
import sys

# Add parent directory to path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from dotenv import load_dotenv
load_dotenv()  # Load environment variables

from llm_testing.llm_tester import LLMTester
import pandas as pd

def test_single_sample():
    """Test one sample with all three LLMs"""
    
    print("="*70)
    print("QUICK LLM API TEST")
    print("="*70)
    
    # Create a simple test sample
    test_sample = {
        'age': 63,
        'sex': 1,
        'cp': 3,
        'trestbps': 145,
        'chol': 233,
        'fbs': 1,
        'restecg': 0,
        'thalach': 150,
        'exang': 0,
        'oldpeak': 2.3,
        'slope': 0,
        'ca': 0,
        'thal': 1,
        'target': 1
    }
    
    print("\nTest Patient Data:")
    print("-"*70)
    for key, value in test_sample.items():
        if key != 'target':
            print(f"  {key}: {value}")
    print(f"  True Label: {test_sample['target']} (1=Disease, 0=No Disease)")
    print("-"*70)
    
    # Create temporary test file
    temp_df = pd.DataFrame([test_sample])
    temp_df['features'] = temp_df.apply(
        lambda row: ', '.join([f"{col}={row[col]}" for col in temp_df.columns if col not in ['target', 'features']]),
        axis=1
    )
    temp_file = 'temp_test_sample.csv'
    temp_df.to_csv(temp_file, index=False)
    
    # Initialize tester
    tester = LLMTester(temp_file, runs_per_sample=1)
    
    # Test each model
    models = ['gpt', 'gemini', 'qwen']
    
    for model_name in models:
        print(f"\n{'='*70}")
        print(f"TESTING: {model_name.upper()}")
        print("="*70)
        
        # Create prompt
        features_str = temp_df.iloc[0]['features']
        prompt = tester.create_medical_prompt(features_str)
        
        # Test model
        if model_name == 'gpt':
            result = tester.test_gpt(prompt)
        elif model_name == 'gemini':
            result = tester.test_gemini(prompt)
        elif model_name == 'qwen':
            result = tester.test_qwen(prompt)
        
        # Display results
        if 'error' in result:
            print(f"❌ ERROR: {result['error']}")
        else:
            print(f"✓ Model: {result['model']}")
            print(f"✓ Prediction: {result['prediction']} (True Label: {test_sample['target']})")
            print(f"✓ Justification:")
            print(f"  {result['justification']}")
            
            # Check if prediction matches
            pred_binary = 1 if result['prediction'] == 'Yes' else 0
            match = "✓ CORRECT" if pred_binary == test_sample['target'] else "✗ INCORRECT"
            print(f"\n{match}")
    
    # Cleanup
    import os
    os.remove(temp_file)
    
    print("\n" + "="*70)
    print("API TEST COMPLETED")
    print("="*70)
    print("\nIf all models responded successfully, you can proceed with:")
    print("  python run_experiment.py")
    print("="*70)

if __name__ == "__main__":
    test_single_sample()
