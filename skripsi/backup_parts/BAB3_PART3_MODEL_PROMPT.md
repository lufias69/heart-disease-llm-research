# BAB 3 - METODOLOGI PENELITIAN
## BAGIAN 3: MODEL LLM DAN DESAIN PROMPT

---

## 3.5 Model Large Language Models (LLM)

Large Language Models (LLM) adalah model kecerdasan buatan berbasis arsitektur transformer yang telah dilatih pada korpus teks masif untuk memahami dan menghasilkan bahasa natural. Dalam penelitian ini, digunakan tiga model LLM state-of-the-art dari tiga perusahaan teknologi terkemuka untuk mengevaluasi kemampuan diagnosis medis.

### 3.5.1 Model yang Digunakan

#### A. GPT-4o (OpenAI)

**GPT-4o** adalah model generasi terbaru dari OpenAI, merupakan penerus dari GPT-4 dengan kemampuan multimodal yang ditingkatkan.

**Spesifikasi Teknis**:
- **Pengembang**: OpenAI (San Francisco, California, USA)
- **Versi Model**: gpt-4o (Omni model, released May 2024)
- **Arsitektur**: Transformer-based autoregressive language model
- **Ukuran Parameter**: Estimasi ~1.76 trillion parameters (tidak dipublikasikan resmi)
- **Data Pelatihan**: 
  - Korpus teks internet (web pages, books, articles)
  - Literatur medis dan jurnal ilmiah
  - Dataset terstruktur dari berbagai domain
  - Cutoff data: Oktober 2023
- **Kemampuan Khusus**:
  - Multimodal (teks, gambar, audio)
  - Reasoning capabilities yang kuat
  - Pemahaman konteks medis yang mendalam
  - Kemampuan mengikuti instruksi kompleks

**Keunggulan untuk Diagnosis Medis**:
- State-of-the-art natural language understanding
- Telah dilatih pada literatur medis ekstensif
- Kemampuan reasoning klinis yang baik
- Terbukti unggul dalam medical board exams (skor 90%+ pada USMLE)

**Akses API**:
- Platform: OpenAI API
- Endpoint: https://api.openai.com/v1/chat/completions
- Model name: "gpt-4o"
- Authentication: API key (environment variable OPENAI_API_KEY)

**Biaya Penggunaan** (saat penelitian):
- Input tokens: $5.00 per 1M tokens
- Output tokens: $15.00 per 1M tokens
- Estimasi biaya untuk 1,200 prediksi: ~$12-15

#### B. Gemini-2.0-Flash (Google)

**Gemini-2.0-Flash** adalah model generasi kedua dari Google AI, dirancang untuk inference cepat dengan tetap mempertahankan kualitas tinggi.

**Spesifikasi Teknis**:
- **Pengembang**: Google DeepMind (London, UK & Mountain View, California, USA)
- **Versi Model**: gemini-2.0-flash-exp (Experimental release, December 2024)
- **Arsitektur**: Multimodal transformer model dengan optimasi flash attention
- **Ukuran Parameter**: Large-scale (spesifikasi detail tidak dipublikasikan)
- **Data Pelatihan**:
  - Google's extensive web corpus
  - Scientific literature termasuk PubMed
  - Multimodal data (text, images, code)
  - Cutoff data: November 2024
- **Kemampuan Khusus**:
  - Inference sangat cepat (optimized for speed)
  - Multimodal native (teks, gambar, video, audio)
  - Long context window (1M tokens)
  - Reasoning dan analisis mendalam

**Keunggulan untuk Diagnosis Medis**:
- Fast inference untuk aplikasi real-time
- Akses ke literatur terbaru (cutoff lebih baru)
- Kemampuan multimodal jika diperlukan integrasi imaging
- Strong reasoning capabilities

**Akses API**:
- Platform: Google AI Studio API
- Endpoint: https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent
- Model name: "gemini-2.0-flash-exp"
- Authentication: API key (environment variable GOOGLE_API_KEY)

**Biaya Penggunaan**:
- Gratis untuk experimental version (dengan rate limits)
- Production version: $0.075 per 1M input tokens, $0.30 per 1M output tokens

#### C. Qwen-Plus (Alibaba)

**Qwen-Plus** adalah model LLM multilingual dari Alibaba DAMO Academy, dirancang khusus untuk pemahaman bahasa Inggris dan Mandarin.

**Spesifikasi Teknis**:
- **Pengembang**: Alibaba DAMO Academy (Hangzhou, China)
- **Versi Model**: qwen-plus (Latest stable version, 2024)
- **Arsitektur**: Transformer-based large language model
- **Ukuran Parameter**: Large-scale model (estimasi 70B+ parameters)
- **Data Pelatihan**:
  - Bilingual corpus (Chinese & English)
  - Scientific and medical literature
  - Technical documents
  - Cutoff data: Mid-2024
- **Kemampuan Khusus**:
  - Strong bilingual capabilities (EN/ZH)
  - Technical and scientific reasoning
  - Long context understanding
  - Instruction following accuracy

**Keunggulan untuk Diagnosis Medis**:
- Multilingual capability (meski input berbahasa Inggris)
- Trained on diverse scientific literature
- Competitive performance dengan model Barat
- Cost-effective untuk skala besar

**Akses API**:
- Platform: Alibaba Cloud DashScope API
- Endpoint: https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation
- Model name: "qwen-plus"
- Authentication: API key (environment variable DASHSCOPE_API_KEY)

**Biaya Penggunaan**:
- Input tokens: $0.40 per 1M tokens
- Output tokens: $1.20 per 1M tokens
- Lebih ekonomis dibanding GPT-4o dan Gemini

### 3.5.2 Perbandingan Tiga Model

| Aspek | GPT-4o | Gemini-2.0-Flash | Qwen-Plus |
|-------|--------|------------------|-----------|
| **Pengembang** | OpenAI (USA) | Google (USA/UK) | Alibaba (China) |
| **Parameters** | ~1.76T (est.) | Large (undisclosed) | 70B+ (est.) |
| **Training Cutoff** | Oct 2023 | Nov 2024 | Mid 2024 |
| **Multimodal** | ✅ Yes | ✅ Yes | ✅ Limited |
| **Context Window** | 128K tokens | 1M tokens | 32K tokens |
| **Inference Speed** | Medium | Very Fast | Fast |
| **Medical Knowledge** | Excellent | Excellent | Good |
| **Multilingual** | Good | Excellent | Excellent (EN/ZH) |
| **Cost** | High | Medium | Low |
| **Availability** | Commercial | Experimental/Commercial | Commercial |

**Justifikasi Pemilihan Tiga Model**:

1. **Diversitas Geografis**: Mewakili teknologi AI dari Amerika (GPT), Eropa-Amerika (Gemini), dan Asia (Qwen)
2. **Variasi Arsitektur**: Pendekatan berbeda dalam design dan optimization
3. **Ukuran Berbeda**: Dari sangat besar (GPT-4o) hingga lebih efisien (Qwen-Plus)
4. **Representasi Industri**: Leader dari tiga ekosistem AI terbesar dunia
5. **Komparabilitas**: Memungkinkan evaluasi apakah pola konsistensi-akurasi bersifat universal

### 3.5.3 Konfigurasi Parameter Model

Untuk memastikan konsistensi dan fairness dalam perbandingan, semua model dikonfigurasi dengan parameter yang identik atau setara.

#### Parameter Inference

| Parameter | Nilai | Justifikasi |
|-----------|-------|-------------|
| **temperature** | 0.7 | Balance antara determinism dan creativity |
| **max_tokens** | 300 | Cukup untuk diagnosis + justifikasi 2-3 kalimat |
| **top_p** | 1.0 | Default, menggunakan full probability distribution |
| **frequency_penalty** | 0.0 | Tidak ada penalti repetisi |
| **presence_penalty** | 0.0 | Tidak ada penalti kehadiran token |

#### Penjelasan Parameter Temperature

**Temperature** adalah parameter kunci yang mengontrol randomness dalam generasi teks LLM.

**Formula**: 
$$P(w_i) = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}$$

di mana:
- $P(w_i)$ = probabilitas memilih token $w_i$
- $z_i$ = logit (raw score) dari model untuk token $i$
- $T$ = temperature
- Semakin kecil $T$, semakin "peaked" distribusi probabilitas

**Range dan Interpretasi**:
- **T = 0.0**: Deterministik (selalu pilih token dengan probabilitas tertinggi)
- **T < 0.3**: Sangat deterministik, output predictable
- **T = 0.7**: **Pilihan penelitian ini** - balance optimal
- **T = 1.0**: Sampling sesuai probabilitas asli model
- **T > 1.0**: Sangat random, output creative tapi inconsistent

**Mengapa T = 0.7?**

Pilihan temperature 0.7 didasarkan pada pertimbangan berikut:

✅ **Mengukur Konsistensi**: T=0.0 akan menghasilkan output identik setiap run (100% consistency secara trivial). T=0.7 memungkinkan evaluasi "natural consistency" model.

✅ **Menghindari Over-Determinism**: Diagnosis medis tidak selalu hitam-putih. T=0.7 mencerminkan uncertainty yang wajar.

✅ **Best Practice**: Literatur OpenAI dan Google menyarankan T=0.7 untuk aplikasi yang memerlukan balance antara consistency dan diversity.

✅ **Testing Robustness**: Jika model robust, seharusnya tetap konsisten meskipun dengan sedikit randomness.

#### Max Tokens

**Max Tokens** = 300 dipilih berdasarkan analisis kebutuhan output:

**Struktur Output yang Diharapkan**:
```
PREDICTION: Yes/No                    → ~5 tokens
JUSTIFICATION: [2-3 kalimat]          → ~100-200 tokens
```

**Analisis**:
- Diagnosis sederhana: "Yes" atau "No" = 1 token
- Justifikasi 2-3 kalimat dengan medical reasoning = 100-200 tokens
- Buffer untuk variasi format = 50-100 tokens
- **Total**: ~150-250 tokens (300 memberikan margin safety)

**Validasi**: Dalam pilot testing, tidak ada response yang mencapai 300 tokens (rata-rata ~180 tokens).

---

## 3.6 Desain Prompt

Prompt engineering adalah aspek krusial dalam evaluasi LLM. Kualitas dan struktur prompt dapat secara signifikan mempengaruhi kualitas output. Penelitian ini menggunakan dua variasi prompt untuk menguji **prompt sensitivity** - seberapa besar perubahan prompt mempengaruhi prediksi model.

### 3.6.1 Variasi Prompt

Dua variasi prompt dirancang dengan karakteristik berbeda namun tujuan sama:

#### Prompt A: "Expert Cardiologist" (Dr. CardioExpert)

**Karakteristik**: Authoritative expert persona dengan pengalaman klinis ekstensif

**Full Text Prompt A**:
```
You are Dr. CardioExpert, a highly experienced cardiologist with over 20 years 
of specialized practice in diagnosing cardiovascular diseases. You have 
successfully diagnosed thousands of patients and are known for your exceptional 
accuracy and precision in identifying heart disease based on clinical parameters.

PATIENT CLINICAL DATA:
{patient_data}

CLINICAL PARAMETERS REFERENCE:
- age: Patient's age in years
- sex: 1 = male, 0 = female
- cp (Chest Pain Type): 0 = typical angina, 1 = atypical angina, 
  2 = non-anginal pain, 3 = asymptomatic
- trestbps: Resting blood pressure (mm Hg on admission)
- chol: Serum cholesterol level (mg/dl)
- fbs: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- restecg: Resting electrocardiographic results (0 = normal, 
  1 = ST-T abnormality, 2 = left ventricular hypertrophy)
- thalach: Maximum heart rate achieved during exercise test
- exang: Exercise-induced angina (1 = yes, 0 = no)
- oldpeak: ST depression induced by exercise relative to rest
- slope: Slope of peak exercise ST segment (0 = upsloping, 1 = flat, 
  2 = downsloping)
- ca: Number of major vessels (0-4) colored by fluoroscopy
- thal: Thalassemia test result (0 = normal, 1 = fixed defect, 
  2 = reversible defect, 3 = other)

YOUR DIAGNOSTIC TASK:
Based on your extensive clinical experience, analyze this patient's profile 
carefully and provide your expert diagnosis.

1. DIAGNOSIS: Determine whether this patient has coronary artery disease/heart 
   disease (answer "Yes" or "No")
2. CLINICAL REASONING: Provide your medical justification (2-3 sentences) citing 
   the specific clinical indicators that support your diagnosis

Format your response EXACTLY as follows:
PREDICTION: [Yes/No]
JUSTIFICATION: [Your clinical reasoning with specific medical indicators]
```

**Analisis Prompt A**:
- **Tone**: Professional, authoritative
- **Persona**: Expert dengan kredibilitas tinggi
- **Focus**: Akurasi dan presisi diagnosis
- **Risk**: Mungkin bias ke "over-diagnosis" (mencari penyakit karena expert mindset)

#### Prompt B: "Neutral AI Assistant"

**Karakteristik**: Objektif, balanced, tanpa persona spesifik

**Full Text Prompt B**:
```
You are a medical AI assistant trained to provide accurate and balanced 
diagnostic assessments for cardiovascular conditions. Your goal is to analyze 
clinical data objectively and provide precise diagnoses based solely on the 
presented evidence, avoiding both over-diagnosis and under-diagnosis.

PATIENT CLINICAL DATA:
{patient_data}

CLINICAL PARAMETERS REFERENCE:
- age: Patient's age in years
- sex: 1 = male, 0 = female
- cp (Chest Pain Type): 0 = typical angina, 1 = atypical angina, 
  2 = non-anginal pain, 3 = asymptomatic
- trestbps: Resting blood pressure (mm Hg on admission)
- chol: Serum cholesterol level (mg/dl)
- fbs: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- restecg: Resting electrocardiographic results (0 = normal, 
  1 = ST-T abnormality, 2 = left ventricular hypertrophy)
- thalach: Maximum heart rate achieved during exercise test
- exang: Exercise-induced angina (1 = yes, 0 = no)
- oldpeak: ST depression induced by exercise relative to rest
- slope: Slope of peak exercise ST segment (0 = upsloping, 1 = flat, 
  2 = downsloping)
- ca: Number of major vessels (0-4) colored by fluoroscopy
- thal: Thalassemia test result (0 = normal, 1 = fixed defect, 
  2 = reversible defect, 3 = other)

YOUR DIAGNOSTIC TASK:
Analyze this patient's clinical profile objectively and provide a precise 
diagnosis based on the evidence presented.

1. DIAGNOSIS: Determine whether this patient has coronary artery disease/heart 
   disease (answer "Yes" or "No")
2. CLINICAL REASONING: Provide your medical justification (2-3 sentences) citing 
   the specific clinical indicators that support your diagnosis, maintaining 
   balanced assessment without bias toward positive or negative outcomes

Format your response EXACTLY as follows:
PREDICTION: [Yes/No]
JUSTIFICATION: [Your clinical reasoning with specific medical indicators]
```

**Analisis Prompt B**:
- **Tone**: Neutral, objective
- **Persona**: AI assistant tanpa authority bias
- **Focus**: Balance antara mendeteksi penyakit DAN mengenali pasien sehat
- **Keunggulan**: Explicit instruction untuk menghindari over-diagnosis dan under-diagnosis

### 3.6.2 Perbandingan Prompt A vs Prompt B

| Aspek | Prompt A (Expert) | Prompt B (Neutral) |
|-------|-------------------|-------------------|
| **Persona** | Dr. CardioExpert, 20 tahun pengalaman | Medical AI assistant |
| **Authority** | Tinggi ("exceptional accuracy") | Sedang (netral) |
| **Framing** | "Based on extensive experience" | "Based on evidence presented" |
| **Bias Risk** | Over-diagnosis (expert seeking disease) | Balanced (explicit instruction) |
| **Instruction** | "analyze carefully" | "avoiding both over- and under-diagnosis" |
| **Tone** | Confident, authoritative | Objective, balanced |
| **Word Count** | ~320 words | ~310 words |

**Perbedaan Kunci**:

1. **Role Definition**:
   - Prompt A: "Dr. CardioExpert... 20 years... thousands of patients"
   - Prompt B: "medical AI assistant... trained... objective"

2. **Goal Statement**:
   - Prompt A: "known for exceptional accuracy and precision"
   - Prompt B: "avoiding both over-diagnosis and under-diagnosis"

3. **Task Instruction**:
   - Prompt A: "Based on your extensive clinical experience"
   - Prompt B: "based solely on the presented evidence"

4. **Balance Emphasis**:
   - Prompt A: Tidak menekankan balance
   - Prompt B: **Explicit**: "balanced assessment without bias"

### 3.6.3 Struktur Prompt

Kedua prompt memiliki struktur identik yang terdiri dari 5 komponen utama:

#### 1. Role Definition (Berbeda)
- Mendefinisikan identitas dan kapabilitas AI
- **Panjang**: 2-3 kalimat
- **Variasi**: Expert persona vs Neutral AI

#### 2. Patient Clinical Data (Identik)
- Placeholder untuk data pasien individual
- Format: `{patient_data}` akan diganti dengan 13 parameter klinis
- **Contoh**:
  ```
  age: 63, sex: 1 (male), cp: 3 (asymptomatic), trestbps: 145, 
  chol: 233, fbs: 1, restecg: 0, thalach: 150, exang: 0, 
  oldpeak: 2.3, slope: 0, ca: 0, thal: 1
  ```

#### 3. Clinical Parameters Reference (Identik)
- Definisi lengkap setiap parameter klinis
- **Tujuan**: Memastikan LLM memahami interpretasi setiap nilai
- **Panjang**: 13 bullets, ~200 words
- **Format**: parameter: definisi dan interpretasi

#### 4. Diagnostic Task (Sedikit berbeda)
- Instruksi eksplisit apa yang harus dilakukan
- Output format specification
- **Komponen**:
  a. Diagnosis binary (Yes/No)
  b. Clinical reasoning (2-3 kalimat)

#### 5. Output Format (Identik)
- Template ketat untuk parsing otomatis
- **Format**:
  ```
  PREDICTION: [Yes/No]
  JUSTIFICATION: [reasoning text]
  ```

### 3.6.4 Contoh Input-Output

**Contoh Kasus Pasien**:
```
age: 54, sex: 1, cp: 0, trestbps: 140, chol: 239, fbs: 0, 
restecg: 1, thalach: 160, exang: 1, oldpeak: 1.2, slope: 2, 
ca: 0, thal: 2
Ground Truth: Positive (Has heart disease)
```

**Contoh Response GPT-4o dengan Prompt A**:
```
PREDICTION: Yes
JUSTIFICATION: The patient presents with typical angina (cp=0), exercise-induced 
angina (exang=1), ST-T abnormality on resting ECG (restecg=1), and downsloping 
ST segment (slope=2), which are strong indicators of coronary artery disease. 
The reversible thalassemia defect (thal=2) further supports this diagnosis.
```

**Contoh Response GPT-4o dengan Prompt B**:
```
PREDICTION: Yes
JUSTIFICATION: Multiple clinical indicators suggest coronary artery disease: 
typical angina (cp=0), exercise-induced angina (exang=1), resting ECG abnormality 
(restecg=1), downsloping ST segment during exercise (slope=2), and reversible 
perfusion defect (thal=2). These findings collectively point to significant 
coronary stenosis.
```

**Analisis**:
- Kedua prompt menghasilkan prediksi sama (Yes)
- Justifikasi sedikit berbeda dalam framing tapi isi serupa
- Keduanya mengutip indikator klinis spesifik
- Konsisten dengan ground truth

### 3.6.5 Validasi Prompt Design

Sebelum eksperimen utama, dilakukan pilot testing dengan 10 kasus untuk memvalidasi:

✅ **Parsing Reliability**: Semua response mengikuti format yang diminta
✅ **Output Quality**: Justifikasi mengandung reasoning medis yang masuk akal
✅ **Response Length**: Rata-rata 150-200 tokens, dalam batas max_tokens
✅ **No Refusals**: Tidak ada model yang menolak membuat prediksi
✅ **Consistency**: Format output stabil across multiple runs

**Kesimpulan Design**: Prompt sudah siap untuk eksperimen skala penuh (100 kasus × 4 runs × 3 models × 2 prompts = 2,400 prediksi).

---

**[Lanjut ke BAGIAN 4: Protokol Eksperimen dan Evaluasi]**
