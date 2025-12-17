"""
LLM Testing Module for Heart Disease Prediction
Purpose: Test GPT, Gemini, and Qwen Plus for consistency and accuracy
"""

import os
import json
import time
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple
import warnings
from llm_testing.database import ResultsDatabase
warnings.filterwarnings('ignore')


class LLMTester:
    """
    Test multiple LLM models for heart disease prediction
    """
    
    def __init__(self, test_data_path, runs_per_sample=10, db_path='results/llm_predictions/predictions.db'):
        """
        Initialize LLM tester
        
        Args:
            test_data_path: Path to test data CSV
            runs_per_sample: Number of predictions per sample for consistency
            db_path: Path to SQLite database for checkpoint support
        """
        self.test_data = pd.read_csv(test_data_path)
        self.runs_per_sample = runs_per_sample
        
        # Initialize database
        self.db = ResultsDatabase(db_path)
        
        # Load API keys from environment
        self.api_keys = {
            'gpt': os.getenv('OPENAI_API_KEY'),
            'gemini': os.getenv('GOOGLE_API_KEY'),
            'qwen': os.getenv('DASHSCOPE_API_KEY')
        }
        
        print(f"✓ Loaded test data: {len(self.test_data)} samples")
        print(f"  Runs per sample: {runs_per_sample}")
        print(f"  Total predictions needed: {len(self.test_data) * runs_per_sample * 3} (3 models)")
        print(f"✓ Database checkpoint enabled: {db_path}")
    
    def create_medical_prompt(self, features_str):
        """
        Create medical diagnosis prompt for LLM
        
        Args:
            features_str: String of patient features
            
        Returns:
            str: Formatted prompt
        """
        prompt = f"""You are a medical AI assistant trained to provide accurate and balanced diagnostic assessments for cardiovascular conditions. Your goal is to analyze clinical data objectively and provide precise diagnoses based solely on the presented evidence, avoiding both over-diagnosis and under-diagnosis.

PATIENT CLINICAL DATA:
{features_str}

CLINICAL PARAMETERS REFERENCE:
- age: Patient's age in years
- sex: 1 = male, 0 = female
- cp (Chest Pain Type): 0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic
- trestbps: Resting blood pressure (mm Hg on admission)
- chol: Serum cholesterol level (mg/dl)
- fbs: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- restecg: Resting electrocardiographic results (0 = normal, 1 = ST-T abnormality, 2 = left ventricular hypertrophy)
- thalach: Maximum heart rate achieved during exercise test
- exang: Exercise-induced angina (1 = yes, 0 = no)
- oldpeak: ST depression induced by exercise relative to rest
- slope: Slope of peak exercise ST segment (0 = upsloping, 1 = flat, 2 = downsloping)
- ca: Number of major vessels (0-4) colored by fluoroscopy
- thal: Thalassemia test result (0 = normal, 1 = fixed defect, 2 = reversible defect, 3 = other)

YOUR DIAGNOSTIC TASK:
Analyze this patient's clinical profile objectively and provide a precise diagnosis based on the evidence presented.

1. DIAGNOSIS: Determine whether this patient has coronary artery disease/heart disease (answer "Yes" or "No")
2. CLINICAL REASONING: Provide your medical justification (2-3 sentences) citing the specific clinical indicators that support your diagnosis, maintaining balanced assessment without bias toward positive or negative outcomes

Format your response EXACTLY as follows:
PREDICTION: [Yes/No]
JUSTIFICATION: [Your clinical reasoning with specific medical indicators]
"""
        return prompt
    
    def test_gpt(self, prompt, temperature=0.7, max_tokens=300):
        """
        Test GPT model
        
        Args:
            prompt: Input prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            
        Returns:
            dict: Prediction result
        """
        try:
            from openai import OpenAI
            
            if not self.api_keys['gpt']:
                return {"error": "OpenAI API key not found", "prediction": None, "justification": None}
            
            client = OpenAI(api_key=self.api_keys['gpt'])
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            full_response = response.choices[0].message.content.strip()
            
            # Parse response
            prediction, justification = self.parse_llm_response(full_response)
            
            return {
                "model": "GPT-4o",
                "prediction": prediction,
                "justification": justification,
                "raw_response": full_response,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "model": "GPT-4o",
                "error": str(e),
                "prediction": None,
                "justification": None
            }
    
    def test_gemini(self, prompt, temperature=0.7, max_tokens=300):
        """
        Test Gemini model
        
        Args:
            prompt: Input prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            
        Returns:
            dict: Prediction result
        """
        try:
            import google.generativeai as genai
            
            if not self.api_keys['gemini']:
                return {"error": "Google API key not found", "prediction": None, "justification": None}
            
            genai.configure(api_key=self.api_keys['gemini'])
            
            # Use gemini-2.0-flash (stable and widely available)
            model = genai.GenerativeModel('gemini-2.0-flash')
            
            # Configure safety settings to be less restrictive
            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
            ]
            
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=max_tokens
                ),
                safety_settings=safety_settings
            )
            
            # Handle potential empty response
            if not response.parts:
                # Try to get feedback about why it was blocked
                if response.prompt_feedback.block_reason:
                    return {
                        "model": "Gemini-2.0-Flash",
                        "error": f"Content blocked: {response.prompt_feedback.block_reason}",
                        "prediction": None,
                        "justification": None
                    }
                return {
                    "model": "Gemini-2.0-Flash",
                    "error": "Empty response from model",
                    "prediction": None,
                    "justification": None
                }
            
            full_response = response.text.strip()
            
            # Parse response
            prediction, justification = self.parse_llm_response(full_response)
            
            return {
                "model": "Gemini-2.0-Flash",
                "prediction": prediction,
                "justification": justification,
                "raw_response": full_response,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "model": "Gemini-2.0-Flash",
                "error": str(e),
                "prediction": None,
                "justification": None
            }
    
    def test_qwen(self, prompt, temperature=0.7, max_tokens=300):
        """
        Test Qwen Plus model using OpenAI-compatible API
        
        Args:
            prompt: Input prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            
        Returns:
            dict: Prediction result
        """
        try:
            from openai import OpenAI
            
            if not self.api_keys['qwen']:
                return {"error": "DashScope API key not found", "prediction": None, "justification": None}
            
            # Use OpenAI-compatible endpoint for Qwen
            client = OpenAI(
                api_key=self.api_keys['qwen'],
                base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
            )
            
            response = client.chat.completions.create(
                model="qwen-plus",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            full_response = response.choices[0].message.content.strip()
            
            # Parse response
            prediction, justification = self.parse_llm_response(full_response)
            
            return {
                "model": "Qwen-Plus",
                "prediction": prediction,
                "justification": justification,
                "raw_response": full_response,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "model": "Qwen-Plus",
                "error": str(e),
                "prediction": None,
                "justification": None
            }
            
        except Exception as e:
            return {
                "model": "Qwen-Plus",
                "error": str(e),
                "prediction": None,
                "justification": None
            }
    
    def parse_llm_response(self, response):
        """
        Parse LLM response to extract prediction and justification
        
        Args:
            response: Raw LLM response
            
        Returns:
            tuple: (prediction, justification)
        """
        try:
            lines = response.split('\n')
            prediction = None
            justification = None
            
            for line in lines:
                line = line.strip()
                if line.upper().startswith('PREDICTION:'):
                    pred_text = line.split(':', 1)[1].strip().lower()
                    if 'yes' in pred_text:
                        prediction = 1
                    elif 'no' in pred_text:
                        prediction = 0
                elif line.upper().startswith('JUSTIFICATION:'):
                    justification = line.split(':', 1)[1].strip()
            
            return prediction, justification
            
        except Exception as e:
            print(f"  Warning: Could not parse response: {str(e)}")
            return None, None
    
    def test_single_sample(self, test_id, features_str, model_name='gpt'):
        """
        Test a single sample once
        
        Args:
            test_id: Test sample ID
            features_str: Feature string
            model_name: Model to test ('gpt', 'gemini', 'qwen')
            
        Returns:
            dict: Test result
        """
        prompt = self.create_medical_prompt(features_str)
        
        if model_name == 'gpt':
            result = self.test_gpt(prompt)
        elif model_name == 'gemini':
            result = self.test_gemini(prompt)
        elif model_name == 'qwen':
            result = self.test_qwen(prompt)
        else:
            return {"error": f"Unknown model: {model_name}"}
        
        result['test_id'] = test_id
        return result
    
    def test_sample_multiple_runs(self, test_id, features_str, ground_truth, model_name='gpt'):
        """
        Test a single sample multiple times for consistency analysis with checkpoint support
        
        Args:
            test_id: Test sample ID
            features_str: Feature string
            ground_truth: True label
            model_name: Model to test
            
        Returns:
            list: List of results from multiple runs
        """
        print(f"  Testing {model_name.upper()} - Test ID {test_id} ({self.runs_per_sample} runs)...", end=' ')
        
        results = []
        skipped = 0
        
        for run in range(1, self.runs_per_sample + 1):
            # Check if prediction already exists (checkpoint)
            if self.db.is_prediction_complete(test_id, run, model_name):
                skipped += 1
                continue
            
            # Run prediction
            result = self.test_single_sample(test_id, features_str, model_name)
            result['run_id'] = run
            
            # Save to database immediately
            self.db.save_prediction(test_id, run, model_name, result, ground_truth)
            results.append(result)
            
            time.sleep(0.5)  # Rate limiting
        
        if skipped > 0:
            print(f"⏭️  Skipped {skipped} (already done)", end=' ')
        
        # Update progress
        total_predictions = len(self.test_data) * self.runs_per_sample
        self.db.update_progress(model_name, total_predictions, test_id, self.runs_per_sample)
        
        # Calculate consistency from database
        df = self.db.get_all_predictions(model_name)
        test_predictions = df[df['test_id'] == test_id]['prediction_binary'].dropna()
        
        if len(test_predictions) > 0:
            most_common = test_predictions.mode()[0] if len(test_predictions.mode()) > 0 else None
            if most_common is not None:
                consistency = (test_predictions == most_common).sum() / len(test_predictions)
                print(f"✓ Consistency: {consistency:.2%}")
            else:
                print("✓")
        else:
            print("✗ Failed")
        
        return results
    
    def run_full_experiment(self, models=['gpt', 'gemini', 'qwen'], save_dir='results/llm_predictions'):
        """
        Run complete experiment on all samples with all models with checkpoint support
        
        Args:
            models: List of models to test
            save_dir: Directory to save results
            
        Returns:
            dict: Complete results
        """
        print("\n" + "="*70)
        print("RUNNING FULL LLM EXPERIMENT (with checkpoint support)")
        print("="*70)
        print(f"Total samples: {len(self.test_data)}")
        print(f"Models: {', '.join([m.upper() for m in models])}")
        print(f"Runs per sample per model: {self.runs_per_sample}")
        print(f"Total API calls: {len(self.test_data) * len(models) * self.runs_per_sample}")
        print("="*70)
        
        # Show existing progress
        print("\n📊 Existing Progress:")
        for model_name in models:
            progress = self.db.get_progress(model_name)
            if progress:
                print(f"  {model_name.upper()}: {progress['completed']}/{progress['total']} ({progress['percentage']:.1f}%)")
            else:
                print(f"  {model_name.upper()}: Not started")
        
        all_results = {}
        
        for model_name in models:
            print(f"\n🤖 Testing {model_name.upper()}...")
            model_results = []
            
            for idx, row in self.test_data.iterrows():
                test_id = row['test_id']
                features_str = row['features']
                ground_truth = row['ground_truth']  # Fixed: was 'target'
                
                # Run multiple tests (with checkpoint support)
                run_results = self.test_sample_multiple_runs(test_id, features_str, ground_truth, model_name)
                model_results.extend(run_results)
            
            all_results[model_name] = model_results
            
            # Export from database to CSV
            save_path = f"{save_dir}/{model_name}_results.csv"
            self.db.export_to_csv(model_name, save_path)
        
        # Show final statistics
        print("\n" + "="*70)
        print("EXPERIMENT COMPLETE")
        print("="*70)
        stats = self.db.get_statistics()
        print(f"Total predictions saved: {stats['total_predictions']}")
        print(f"By model:")
        for model, count in stats['by_model'].items():
            print(f"  {model.upper()}: {count}")
        if stats['errors'] > 0:
            print(f"⚠️  Errors: {stats['errors']}")
        print("="*70)
        
        return all_results


# Placeholder functions for when API keys are not available
def simulate_llm_response(features_str, model_name):
    """Simulate LLM response for testing without API keys"""
    import random
    
    # Parse features to make somewhat realistic predictions
    feature_dict = {}
    for item in features_str.split(', '):
        key, value = item.split('=')
        feature_dict[key] = float(value)
    
    # Simple heuristic: predict disease if multiple risk factors
    risk_score = 0
    if feature_dict.get('age', 0) > 55:
        risk_score += 1
    if feature_dict.get('chol', 0) > 240:
        risk_score += 1
    if feature_dict.get('thalach', 200) < 120:
        risk_score += 1
    if feature_dict.get('exang', 0) == 1:
        risk_score += 1
    
    # Add some randomness for consistency testing
    random_factor = random.random()
    if risk_score >= 2 and random_factor > 0.2:
        prediction = 1
    elif risk_score <= 1 and random_factor > 0.3:
        prediction = 0
    else:
        prediction = random.choice([0, 1])
    
    justification = f"Based on analysis of cardiovascular risk factors including age, cholesterol, and exercise tolerance. Risk score: {risk_score}/4."
    
    return {
        "model": model_name,
        "prediction": prediction,
        "justification": justification,
        "raw_response": f"PREDICTION: {'Yes' if prediction == 1 else 'No'}\nJUSTIFICATION: {justification}",
        "timestamp": datetime.now().isoformat(),
        "simulated": True
    }


if __name__ == "__main__":
    print("="*70)
    print("LLM TESTING MODULE")
    print("="*70)
    print("\nThis module requires API keys for:")
    print("  - OpenAI (GPT-4)")
    print("  - Google (Gemini)")
    print("  - DashScope (Qwen Plus)")
    print("\nSet environment variables:")
    print("  export OPENAI_API_KEY='your-key'")
    print("  export GOOGLE_API_KEY='your-key'")
    print("  export DASHSCOPE_API_KEY='your-key'")
    print("\n" + "="*70)
