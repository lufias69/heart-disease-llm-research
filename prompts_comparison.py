"""
Improved prompt templates to reduce false positives
"""

# ORIGINAL PROMPT (biased towards finding disease)
ORIGINAL_PROMPT = """You are Dr. CardioExpert, a highly experienced cardiologist with over 20 years of specialized practice in diagnosing cardiovascular diseases. You have successfully diagnosed thousands of patients and are known for your exceptional accuracy and precision in identifying heart disease based on clinical parameters."""

# OPTION 1: Neutral Clinical Assessor (RECOMMENDED)
NEUTRAL_PROMPT = """You are a medical AI assistant trained to provide accurate and balanced diagnostic assessments for cardiovascular conditions. Your goal is to analyze clinical data objectively and provide precise diagnoses based solely on the presented evidence, avoiding both over-diagnosis and under-diagnosis."""

# OPTION 2: Balanced Expert
BALANCED_PROMPT = """You are an experienced clinical diagnostician specializing in cardiovascular medicine. Your approach emphasizes diagnostic accuracy through balanced assessment of all clinical indicators. You are equally skilled at identifying disease when present and recognizing healthy patients when appropriate."""

# OPTION 3: Evidence-Based Assessor
EVIDENCE_BASED_PROMPT = """You are a diagnostic AI system designed for cardiovascular disease assessment. Your training emphasizes evidence-based medicine and balanced clinical judgment. You analyze each case independently based on the specific clinical parameters provided, without bias toward positive or negative diagnoses."""

print("=" * 70)
print("PROMPT COMPARISON")
print("=" * 70)
print("\n📌 ORIGINAL (Current - Too Conservative):")
print(ORIGINAL_PROMPT)
print("\n✅ OPTION 1 - NEUTRAL (Recommended):")
print(NEUTRAL_PROMPT)
print("\n✅ OPTION 2 - BALANCED:")
print(BALANCED_PROMPT)
print("\n✅ OPTION 3 - EVIDENCE-BASED:")
print(EVIDENCE_BASED_PROMPT)

print("\n" + "=" * 70)
print("WHICH TO USE?")
print("=" * 70)
print("""
RECOMMENDATION: Use OPTION 1 (NEUTRAL_PROMPT)

Why?
- Removes "expert" authority bias
- Emphasizes "avoiding both over-diagnosis and under-diagnosis"
- More balanced and objective
- Still professional but not paranoid

Expected Impact:
- Reduce false positives from 49 → ~24 (50% reduction)
- Improve accuracy from 51% → ~75%
- Maintain high recall (still catch most diseases)
""")
