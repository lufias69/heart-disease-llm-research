# BAB 4 - HASIL DAN PEMBAHASAN
## BAGIAN 4: PEMBAHASAN DAN INTERPRETASI KLINIS

---

## 4.9 Pembahasan Umum

Penelitian ini melakukan evaluasi sistematis terhadap tiga model Large Language Model (LLM) state-of-the-art untuk diagnosis biner penyakit jantung. Hasil penelitian mengungkapkan temuan yang mengejutkan dan menantang asumsi konvensional tentang reliabilitas AI dalam aplikasi medis.

### 4.9.1 Ringkasan Temuan Utama

**1. Exceptional Reproducibility (Konsistensi Tinggi)**

Ketiga model LLM menunjukkan konsistensi yang luar biasa tinggi:
- **Average consistency**: 99-100% (Qwen 99.88%, Gemini 99.38%, GPT 99.13%)
- **Perfect consistency rate**: 96-100% kasus mencapai unanimous agreement (4/4 runs)
- **Minimal variability**: Standar deviasi < 0.06, menunjukkan reproducibility sangat stabil
- **Prompt-invariant**: Tipe prompt (Expert vs Neutral) tidak mempengaruhi consistency (<0.3% difference)

**Interpretasi**: Model LLM sangat **reliable** dalam memberikan prediksi yang konsisten untuk kasus yang sama, bahkan dengan temperature=0.7 yang memungkinkan randomness. Ini adalah indikator positif untuk deployment dalam konteks yang memerlukan reproducibility tinggi.

**2. Chance-Level Accuracy (Akurasi di Baseline)**

Meskipun konsistensi tinggi, akurasi diagnostik sangat mengecewakan:
- **Average accuracy**: 48-50% (GPT 49%, Gemini 50%, Qwen 48%)
- **No better than random guessing**: Akurasi setara dengan baseline (50% untuk distribusi balanced)
- **Below random di 2 model**: GPT dan Qwen perform sedikit worse than chance
- **No model superiority**: Tidak ada model yang unggul secara signifikan

**Interpretasi**: Model LLM **consistently wrong** - memberikan jawaban yang sama (konsisten) tetapi salah. High consistency tidak guarantee high accuracy. Ini adalah **temuan kunci** yang menantang asumsi bahwa consistency = reliability = validity.

**3. Systematic Over-Diagnosis Bias**

Semua model menunjukkan bias sistematis yang ekstrem:
- **False positives**: 50-51 (hampir semua pasien sehat didiagnosis sakit)
- **False negatives**: 0-1 (hampir tidak ada pasien sakit yang terlewat)
- **FP:FN ratio**: ~50:1 (extremely imbalanced)
- **Sensitivity**: 98-100% (excellent disease detection)
- **Specificity**: 0-2% (near-zero healthy identification)

**Interpretasi**: Model LLM memiliki **strong prior belief** bahwa parameter kardiovaskular abnormal = penyakit jantung. Gagal mengenali bahwa banyak orang dengan faktor risiko tetap sehat (false positive problem). Pattern ini **uniform across all models**, menunjukkan systematic limitation bukan model-specific issue.

**4. Minimal Prompt Engineering Impact**

Prompt engineering tidak efektif meningkatkan performa:
- **Accuracy change**: <3% (Expert vs Neutral prompt)
- **Prediction change rate**: 2-4% (96-98% agreement antar prompt)
- **Still chance level**: Kedua prompt menghasilkan ~50% accuracy
- **Consistency maintained**: 99-100% di kedua prompt

**Interpretasi**: Masalah akurasi bukan dari **prompt design**, melainkan dari **fundamental reasoning limitations**. Better prompts cannot unlock capabilities yang tidak ada. Perlu pendekatan berbeda: fine-tuning, retrieval augmentation, atau architectural improvements.

**5. High Inter-Model Agreement, Low Diversity**

Ketiga model sangat aligned:
- **Pairwise agreement**: 97-98%
- **Three-way unanimous**: 96% kasus
- **Cohen's Kappa**: κ = 0.94 (almost perfect agreement)
- **Shared errors**: 96% false positives sama di ketiga model
- **Error correlation**: r = 0.95 (very high)

**Interpretasi**: Models "think alike" - menggunakan reasoning path yang sangat mirip. **No diversity** untuk ensemble benefit. Majority voting tidak improve accuracy (tetap 50%). Models lack complementary strengths.

### 4.9.2 The Consistency-Accuracy Dissociation

Temuan paling striking adalah **dissociasi antara consistency dan accuracy**.

#### Tabel Consistency-Accuracy Gap

| Model | Consistency | Accuracy | Gap | Interpretation |
|-------|-------------|----------|-----|----------------|
| **GPT-4o** | 99.13% | 49.0% | **50.13 pp** | Consistently wrong |
| **Gemini-2.0-Flash** | 99.38% | 50.0% | **49.38 pp** | Consistently wrong |
| **Qwen-Plus** | 99.88% | 48.0% | **51.88 pp** | Consistently wrong |
| **Average** | 99.46% | 49.0% | **50.46 pp** | Massive dissociation |

**Catatan**: pp = percentage points

#### Visualisasi Gap (Konseptual)

```
                    Consistency vs Accuracy

Consistency:  ███████████████████████████████████████████████████ 99.46%

Accuracy:     ████████████████████████ 49.0%

              ╞═══════════════════════════════════════════════╡
              <------------ ~50 pp GAP ------------>
```

#### Analisis Dissociation

**Apa Arti Gap Ini?**

Gap ~50 percentage points menunjukkan:
1. **High internal consistency**: Model menggunakan reasoning path yang sama untuk kasus sama
2. **Wrong reasoning path**: Path tersebut sistematis mengarah ke kesimpulan salah
3. **Lack of uncertainty**: Model tidak menunjukkan doubt/variability pada kasus sulit

**Perbandingan dengan Klinisi**:

Klinisi yang baik:
- **Moderate consistency**: 70-85% (ada variability dalam clinical judgment)
- **High accuracy**: 75-90% (lebih sering benar daripada salah)
- **Smaller gap**: 10-20 pp (consistency dan accuracy balanced)
- **Calibrated uncertainty**: Lebih variable pada kasus uncertain

Model LLM:
- **Very high consistency**: 99% (almost deterministic)
- **Chance accuracy**: 50% (no better than guessing)
- **Massive gap**: 50 pp (extreme dissociation)
- **Overconfident**: No variability even on uncertain cases

**Implikasi Teoritis**:

Dissociation ini menunjukkan:
- **Reliability ≠ Validity**: Model reliable (reproducible) tapi not valid (accurate)
- **Systematic error**: Bukan random noise, melainkan systematic bias
- **Fundamental limitation**: Tidak dapat diatasi dengan simple fixes (prompt engineering, temperature tuning)

### 4.9.3 Mengapa Akurasi Rendah Meskipun Konsistensi Tinggi?

Beberapa hipotesis untuk menjelaskan fenomena ini:

#### Hipotesis 1: Oversimplified Disease Model

**Masalah**: Model LLM mungkin menggunakan heuristic oversimplified:
```
IF (any cardiovascular abnormality) THEN (heart disease = TRUE)
```

**Bukti**:
- 98-99% prediksi positive (hampir semua didiagnosis sakit)
- Gagal recognize: banyak orang dengan faktor risiko tetap sehat
- Tidak memahami: risk factors ≠ disease

**Analogi**: Model bertindak seperti medical student yang baru belajar - melihat abnormalitas apapun langsung conclude disease, tanpa clinical reasoning lebih lanjut.

#### Hipotesis 2: Lack of Statistical/Probabilistic Reasoning

**Masalah**: Model tidak memahami:
- **Base rates**: Prevalence penyakit di populasi umum
- **Positive predictive value**: Tidak semua test abnormal = disease
- **False positive rates**: Screening tests sering false alarm

**Bukti**:
- Specificity ~0% (tidak bisa identify healthy)
- Precision ~49% (half of positive predictions wrong)
- Tidak menunjukkan Bayesian reasoning

**Analogi**: Model tidak apply probabilistic thinking - missing statistical inference capability.

#### Hipotesis 3: Training Data Bias

**Masalah**: LLM trained on:
- Medical textbooks: Focus on disease (not health)
- Case reports: Publish positive findings (not negative)
- Clinical guidelines: Written for symptomatic patients

**Bias**: Training data skewed toward diseased populations → model develops prior belief "most cases = disease"

**Bukti**:
- Predict positive 98-99% vs ground truth 49%
- Massive distribution shift
- Uniform bias across all three models (sama-sama trained on similar corpora)

#### Hipotesis 4: Lack of Causal Reasoning

**Masalah**: Model tidak memahami:
- **Causality**: Risk factor vs causal factor
- **Confounders**: Age, lifestyle, genetics
- **Temporal sequence**: Abnormality before vs after disease onset

**Bukti**:
- Treat all abnormalities equally (no weighting)
- No consideration of temporal patterns
- Correlation → causation fallacy

**Analogi**: Model sees associations but doesn't understand causal mechanisms.

#### Hipotesis 5: Overconfidence dari Temperature Setting

**Masalah**: Temperature=0.7 masih relatively deterministic
- Model confident (low entropy) even on uncertain cases
- Tidak mengekspresikan uncertainty melalui variability

**Bukti**:
- 99% consistency (almost no variation)
- Sama konsisten di kasus easy dan hard
- Tidak ada "I don't know" responses

**Improvement direction**: Higher temperature atau explicit uncertainty quantification

### 4.9.4 Perbandingan dengan Literatur

#### Study 1: LLM Performance on Medical Exams (USMLE)

**Previous findings**:
- GPT-4: 90%+ accuracy on USMLE Step exams
- Gemini: 85%+ on medical MCQs
- Strong medical knowledge demonstrated

**Our findings**:
- Same models: ~50% accuracy on real diagnostic task
- **Gap**: 40 percentage points difference

**Interpretation**:
- **Exam knowledge ≠ Clinical reasoning**
- MCQ tests recall and pattern matching
- Real diagnosis requires probabilistic reasoning, uncertainty handling, integration of evidence
- Models have knowledge but lack **application skills**

#### Study 2: Clinical Decision Support Systems

**Previous findings**:
- Rule-based systems: 70-80% accuracy
- ML models (tabular): 75-85% accuracy
- Hybrid (ML + rules): 80-90% accuracy

**Our findings**:
- LLMs: 48-50% accuracy
- **Worse than traditional approaches**

**Interpretation**:
- LLMs **not superior** to domain-specific models
- General-purpose models lack specialized medical reasoning
- Traditional ML + domain knowledge > LLMs alone

#### Study 3: Inter-Rater Reliability in Medicine

**Previous findings**:
- Physician agreement: κ = 0.60-0.80
- Moderate variability reflects genuine uncertainty
- Calibrated disagreement on borderline cases

**Our findings**:
- LLM inter-model agreement: κ = 0.94
- Almost perfect agreement
- **Higher than human agreement**

**Interpretation**:
- **Overconfidence problem**
- Humans appropriately uncertain on difficult cases
- LLMs deterministic even when should be uncertain
- High agreement doesn't mean high accuracy

---

## 4.10 Interpretasi Klinis: Consistency-Accuracy Gap

### 4.10.1 Apa yang Diceritakan oleh Gap ~50 pp?

**Perspektif Reliability vs Validity**:

Dalam psychometrics dan medical testing:
- **Reliability**: Test menghasilkan hasil sama ketika diulang (consistency)
- **Validity**: Test mengukur apa yang seharusnya diukur (accuracy)

**Gold standard**: High reliability AND high validity

**LLM results**:
- ✅ High reliability (99% consistency)
- ❌ Low validity (50% accuracy)

**Analogi**: Timbangan yang selalu menunjukkan angka sama (reliable) tapi salah 5 kg (not valid).

### 4.10.2 Implikasi untuk Clinical Deployment

#### Skenario 1: Primary Diagnostic Tool ❌

**Penggunaan**: LLM sebagai primary decision maker untuk diagnosis

**Risiko**:
- 50% error rate = flip coin
- 50 false positives per 100 patients → massive over-treatment
- Unnecessary tests, anxiety, costs

**Rekomendasi**: **TIDAK DISARANKAN** untuk primary diagnosis

#### Skenario 2: Screening Tool (High Sensitivity Required) ⚠️

**Penggunaan**: LLM untuk initial screening, follow-up jika positive

**Kelebihan**:
- ✅ Sensitivity 98-100% (almost no missed cases)
- ✅ Consistent screening (no operator variability)
- ✅ Scalable (can screen large populations)

**Kekurangan**:
- ❌ Specificity ~0% (almost all healthy flagged)
- ❌ Very high false positive rate (50/51 healthy patients)
- ❌ Costly follow-up (banyak unnecessary confirmatory tests)

**Rekomendasi**: **MUNGKIN cocok** untuk pre-screening jika:
- Follow-up testing murah dan non-invasive
- Cost of missing disease sangat tinggi
- Population dengan high disease prevalence

#### Skenario 3: Supplementary Decision Support ✅

**Penggunaan**: LLM sebagai second opinion, bukan final decision

**Workflow**:
1. Physician membuat primary assessment
2. LLM memberikan suggestion
3. Physician integrates keduanya
4. Final decision tetap pada physician

**Kelebihan**:
- ✅ Safety net (high sensitivity catch cases physician might miss)
- ✅ Consistency check (jika LLM disagree, physician re-evaluate)
- ✅ Physician maintains control

**Kekurangan**:
- ⚠️ Alert fatigue (banyak false positive alerts)
- ⚠️ Risk of automation bias (physician over-rely on AI)

**Rekomendasi**: **PALING AMAN** dengan proper training dan oversight

#### Skenario 4: Triage System ⚠️

**Penggunaan**: LLM untuk prioritize cases (urgent vs non-urgent)

**Kelebihan**:
- ✅ High sensitivity → almost no urgent cases missed
- ✅ Fast processing

**Kekurangan**:
- ❌ Low specificity → banyak non-urgent cases flagged urgent
- ❌ Inefficient resource allocation

**Rekomendasi**: **Perlu threshold optimization** untuk balance sensitivity-specificity trade-off

### 4.10.3 Rekomendasi Deployment Berbasis Evidence

Berdasarkan hasil penelitian, deployment framework yang disarankan:

#### Level 1: TIDAK DIREKOMENDASIKAN ❌

**Use cases yang TIDAK cocok**:
- ❌ Autonomous diagnostic systems (no human oversight)
- ❌ Final decision maker untuk treatment
- ❌ Replacing physician judgment
- ❌ High-stakes decisions (surgery, chemotherapy, dll)
- ❌ Legal/forensic medicine (butuh akurasi tinggi)

**Alasan**: Akurasi 50% = unacceptable risk

#### Level 2: HATI-HATI, PERLU SAFEGUARDS ⚠️

**Use cases yang MUNGKIN dengan kondisi**:
- ⚠️ Initial screening (jika follow-up murah)
- ⚠️ Triage system (dengan threshold tuning)
- ⚠️ Educational purposes (dengan disclaimer clear)
- ⚠️ Research assistant (hypothesis generation)

**Safeguards required**:
- Mandatory human review untuk semua positive predictions
- Clear communication of false positive rate ke patients
- Regular monitoring dan audit
- Continuous performance tracking

#### Level 3: DIREKOMENDASIKAN dengan SUPERVISION ✅

**Use cases yang COCOK**:
- ✅ Supplementary decision support (second opinion)
- ✅ Consistency check (flag disagreements untuk review)
- ✅ Data entry assistance (bukan diagnosis)
- ✅ Literature review dan knowledge synthesis
- ✅ Patient education (dengan supervision)

**Best practices**:
- Physician maintains final decision authority
- LLM output clearly labeled as "AI suggestion, not diagnosis"
- Transparency tentang accuracy limitations
- Training untuk physicians tentang AI limitations

---

## 4.11 Keterbatasan Penelitian

Penelitian ini memiliki beberapa keterbatasan yang perlu dipertimbangkan dalam interpretasi hasil.

### 4.11.1 Keterbatasan Dataset

**1. Single Dataset (UCI Heart Disease)**
- Hanya menggunakan 1 dataset (303 patients)
- Data dari tahun 1988 → mungkin tidak representative untuk praktek modern
- Tidak dapat generalize ke datasets lain tanpa validation

**Implikasi**: Hasil mungkin berbeda untuk datasets dengan karakteristik berbeda (age distribution, severity spectrum, dll)

**2. Binary Classification Only**
- Hanya evaluate yes/no diagnosis (binary)
- Tidak test multi-class (severity levels, subtypes)
- Real-world diagnosis sering lebih nuanced

**Implikasi**: Performance mungkin berbeda untuk tasks yang lebih complex

**3. Limited Clinical Features**
- Hanya 13 parameters
- Tidak include: genetic markers, biomarkers, imaging data, patient history detail
- Real diagnosis uses lebih banyak information

**Implikasi**: Model mungkin perform differently dengan more comprehensive data

**4. De-identified Data**
- Tidak ada temporal information
- Tidak ada treatment history
- Tidak ada follow-up outcomes

**Implikasi**: Tidak dapat evaluate longitudinal reasoning

### 4.11.2 Keterbatasan Metodologi

**1. Fixed Temperature (0.7)**
- Tidak explore temperature variations (0.0, 0.3, 1.0, dll)
- Temperature 0.7 adalah compromise, mungkin suboptimal

**Implikasi**: Results mungkin improve/worsen dengan different temperature settings

**2. Limited Prompt Variations**
- Hanya 2 prompt types (Expert vs Neutral)
- Tidak test: few-shot prompting, chain-of-thought, tool use
- Prompt space sangat luas, tidak fully explored

**Implikasi**: Better prompts mungkin exist (tapi hasil current study suggest minimal impact)

**3. Majority Voting for Final Prediction**
- Menggunakan simple majority dari 4 runs
- Tidak test: weighted voting, confidence thresholding, abstention

**Implikasi**: Alternative aggregation methods mungkin improve accuracy

**4. No Fine-Tuning**
- Menggunakan pre-trained models as-is
- Tidak fine-tune pada medical data atau heart disease specifically

**Implikasi**: Fine-tuned models mungkin perform significantly better

### 4.11.3 Keterbatasan Generalisasi

**1. Specific Disease Domain**
- Fokus pada heart disease (cardiovascular)
- Tidak test: cancer, neurological, infectious diseases

**Implikasi**: Results may not generalize ke domains lain dengan different diagnostic logic

**2. Specific Task (Binary Diagnosis)**
- Tidak evaluate: differential diagnosis, treatment recommendations, prognosis prediction
- Different tasks mungkin different performance profiles

**Implikasi**: LLMs mungkin better/worse di other medical tasks

**3. English Language Only**
- Prompts dan outputs dalam English
- Multilingual capabilities tidak tested

**Implikasi**: Performance mungkin berbeda untuk non-English languages

**4. Model Versions**
- GPT-4o, Gemini-2.0-Flash, Qwen-Plus (specific versions)
- Models constantly updated → results mungkin tidak applicable untuk future versions

**Implikasi**: Need continuous re-evaluation as models evolve

### 4.11.4 Keterbatasan Evaluasi

**1. Ground Truth Assumption**
- Assume UCI labels = gold standard
- Medical diagnosis tidak selalu binary truth (gray areas exist)
- Inter-physician disagreement possible

**Implikasi**: Some "errors" mungkin reasonable clinical disagreements

**2. No Clinical Context**
- Evaluate prediksi tanpa clinical context (urgency, patient preferences, risk tolerance)
- Real decisions consider more factors

**Implikasi**: Binary accuracy mungkin not fully capture clinical utility

**3. No Cost-Benefit Analysis**
- Tidak evaluate: cost of false positives vs false negatives
- Equal weighting untuk semua errors

**Implikasi**: Optimal decision threshold mungkin berbeda if costs considered

**4. Short-Term Evaluation**
- Tidak track long-term outcomes
- Tidak evaluate: impact on patient outcomes, physician satisfaction, workflow integration

**Implikasi**: Lab performance ≠ real-world utility

---

## 4.12 Rekomendasi untuk Penelitian Future

Berdasarkan temuan dan keterbatasan, beberapa arah penelitian future disarankan:

### 4.12.1 Immediate Next Steps

**1. Multi-Dataset Validation**
- Replicate study pada datasets berbeda
- Include: different diseases, populations, data sources
- Assess generalizability across domains

**2. Fine-Tuning Experiments**
- Fine-tune models pada medical datasets
- Compare pre-trained vs fine-tuned performance
- Assess whether fine-tuning can close the accuracy gap

**3. Advanced Prompting Techniques**
- Test: chain-of-thought, few-shot learning, retrieval-augmented generation
- Systematic prompt optimization
- Assess upper bound of prompt engineering impact

**4. Temperature and Sampling Exploration**
- Vary temperature (0.0 → 1.5)
- Test sampling methods: top-p, top-k, beam search
- Find optimal settings for medical reasoning

### 4.12.2 Methodological Improvements

**1. Uncertainty Quantification**
- Implement confidence scores
- Calibration analysis
- Abstention mechanisms (allow "uncertain" responses)

**2. Explainable AI**
- Extract reasoning paths
- Identify key features driving predictions
- Assess clinical validity of reasoning

**3. Hybrid Systems**
- Combine LLMs with rule-based systems
- LLM + traditional ML models
- Ensemble methods with diversity

**4. Human-AI Collaboration**
- Study physician-LLM interaction
- Optimal workflow designs
- Impact on clinical decision quality

### 4.12.3 Extended Clinical Evaluation

**1. Prospective Clinical Trials**
- Deploy in real clinical settings
- Monitor patient outcomes
- Assess real-world effectiveness

**2. Comparative Effectiveness**
- LLM vs physicians
- LLM-assisted vs unassisted physicians
- Cost-effectiveness analysis

**3. Longitudinal Studies**
- Track diagnostic accuracy over time
- Assess learning/adaptation
- Monitor for drift and degradation

**4. Multi-Disease Evaluation**
- Extend to multiple diseases
- Assess domain-specific vs general capabilities
- Identify where LLMs excel vs struggle

### 4.12.4 Theoretical Understanding

**1. Mechanistic Interpretability**
- Understand why high consistency but low accuracy
- Identify failure modes
- Develop targeted improvements

**2. Bias and Fairness Analysis**
- Assess demographic disparities
- Evaluate across age, sex, ethnicity subgroups
- Ensure equitable performance

**3. Calibration Studies**
- Recalibrate model outputs
- Adjust decision thresholds
- Optimize sensitivity-specificity trade-off

**4. Knowledge Provenance**
- Trace model knowledge sources
- Identify training data biases
- Improve data curation for medical LLMs

---

## 4.13 Implikasi untuk AI Development

### 4.13.1 Lessons for LLM Developers

**1. Consistency ≠ Accuracy**
- Prioritize validity over reliability
- Reproducibility tidak cukup - must be reproducibly correct
- Need better evaluation beyond consistency metrics

**2. Domain-Specific Training Critical**
- General-purpose LLMs insufficient for specialized domains
- Medical reasoning requires specialized training
- Consider fine-tuning or domain-adaptive pre-training

**3. Uncertainty Quantification Essential**
- Models must express uncertainty
- High confidence on wrong answers = dangerous
- Implement calibration and abstention mechanisms

**4. Evaluation Must Match Use Case**
- Exam performance ≠ clinical performance
- Need task-specific benchmarks
- Real-world validation essential

### 4.13.2 Recommendations for Clinical AI

**1. Transparent Limitations**
- Clearly communicate accuracy limitations
- Avoid marketing claims without evidence
- Report both sensitivity AND specificity

**2. Human Oversight Mandatory**
- No autonomous medical AI yet
- Physician-in-the-loop required
- Clear accountability frameworks

**3. Continuous Monitoring**
- Track performance post-deployment
- Monitor for drift and degradation
- Regular re-validation

**4. Ethical Deployment**
- Prioritize patient safety
- Informed consent about AI use
- Equitable access and performance

---

## 4.14 Kesimpulan BAB 4

Penelitian ini menghasilkan temuan penting tentang reliabilitas dan akurasi LLM untuk diagnosis medis:

### Temuan Kunci

1. **High Consistency (99-100%)**: LLM sangat reliable dalam reproducibility
2. **Low Accuracy (~50%)**: Performance tidak better than random guessing
3. **Massive Gap (~50 pp)**: Dissociation antara consistency dan accuracy
4. **Systematic Bias**: Over-diagnosis ekstrem (FP:FN ratio 50:1)
5. **No Prompt Impact**: Prompt engineering tidak efektif (<3% change)
6. **High Inter-Model Agreement**: Models sangat aligned (κ=0.94), shared errors (96%)

### Implikasi Utama

**Untuk Deployment**:
- ❌ Tidak untuk autonomous diagnosis
- ⚠️ Hati-hati untuk screening (high FP rate)
- ✅ Cocok untuk supplementary decision support dengan supervision

**Untuk Research**:
- Perlu fokus pada validity, bukan hanya reliability
- Fine-tuning dan advanced prompting directions future work
- Multi-dataset validation essential

**Untuk Practice**:
- LLM knowledge ≠ clinical reasoning capability
- Human oversight tetap critical
- Transparency dan ethical deployment paramount

### Kontribusi Penelitian

Penelitian ini memberikan:
1. **Empirical evidence** tentang LLM limitations untuk diagnosis medis
2. **Methodological framework** untuk evaluasi consistency vs accuracy
3. **Practical guidance** untuk responsible AI deployment
4. **Theoretical insight** tentang AI reliability vs validity

Hasil ini mendorong pengembangan AI medis yang lebih **evidence-based**, **safe**, dan **effective** untuk meningkatkan patient care.

---

**[Akhir BAB 4 - HASIL DAN PEMBAHASAN]**
