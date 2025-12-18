# BAB I PENDAHULUAN

## 1.1 Latar Belakang

Penyakit kardiovaskular merupakan salah satu isu kesehatan global yang paling serius dan terus mengalami peningkatan prevalensi di berbagai negara (Wang et al., 2024). Menurut World Health Organization (WHO), penyakit kardiovaskular menjadi penyebab utama kematian di dunia, dengan mencatat lebih dari 17,9 juta kematian setiap tahun (Woodruff et al., 2024). Di Indonesia, prevalensi penyakit kardiovaskular, khususnya penyakit jantung koroner, tercatat sebesar 1,5% dari total populasi berdasarkan Riset Kesehatan Dasar (RISKESDAS) 2022 (Zanab et al., 2025). Angka ini menunjukkan bahwa penyakit kardiovaskular merupakan masalah kesehatan masyarakat yang serius dan memerlukan perhatian, terutama dalam aspek deteksi dini dan prediksi risiko.

Kendala terbesar dalam penanganan penyakit kardiovaskular adalah gejala awal yang sering tidak spesifik, sehingga banyak kasus baru terdeteksi setelah memasuki fase lanjut (Rajkomar et al., 2019). Keterlambatan diagnosis, terutama pada kondisi akut seperti *infark miokard*, dapat meningkatkan risiko kecacatan hingga kematian (Wang et al., 2024). Dalam situasi ruang gawat darurat, diagnosis cepat dan akurat menjadi sangat krusial (Topol, 2019). Oleh karena itu, keberadaan sistem prediksi risiko penyakit kardiovaskular yang cepat, stabil, dan dapat diandalkan merupakan kebutuhan yang mendesak untuk menyokong pengambilan keputusan klinis secara tepat (Sapra & Sapra, 2024).

Perkembangan teknologi kesehatan memperlihatkan peluang signifikan melalui penerapan kecerdasan buatan (Artificial Intelligence/AI) dan machine learning (ML) (Rajpurkar et al., 2022). Teknologi ini mampu menganalisis data medis dalam jumlah besar dan menemukan pola risiko yang tidak selalu terlihat melalui pendekatan diagnostik tradisional (Esteva et al., 2019; Topol, 2019). Berbagai algoritma ML seperti decision tree, support vector machine (SVM), random forest, hingga neural networks telah digunakan dalam penelitian prediksi penyakit kardiovaskular, dengan akurasi yang mencapai 85-98% (Ali et al., 2021; Mohan et al., 2019). Namun, mayoritas penelitian tersebut lebih berfokus pada peningkatan akurasi model tunggal, sementara aspek stabilitas dan konsistensi prediksi pada pengujian berulang (reproducibility) belum banyak mendapat perhatian.

Dalam beberapa tahun terakhir, Large Language Models (LLMs) seperti GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus telah menunjukkan kemampuan luar biasa dalam memahami dan memproses informasi kompleks, termasuk dalam domain medis (Thirunavukarasu et al., 2023; Singhal et al., 2023). Berbeda dengan machine learning tradisional yang memerlukan feature engineering manual dan training dataset besar, LLMs dapat melakukan reasoning atas data klinis melalui prompt engineering—pendekatan di mana instruksi dan konteks diberikan dalam bentuk teks natural untuk mengarahkan model memberikan prediksi (Zhou et al., 2023; Wei et al., 2022). Kemampuan ini membuka peluang baru dalam clinical decision support, di mana LLM dapat memberikan interpretasi mendalam terhadap profil risiko pasien berdasarkan multiple clinical parameters.

Namun, penggunaan LLM dalam diagnosis medis menghadapi tantangan fundamental yang berbeda dari ML tradisional (Meskó & Topol, 2023). LLMs bersifat stochastic—artinya, model dapat memberikan output yang berbeda meskipun diberikan input yang identik, bergantung pada parameter sampling seperti temperature (Elazar et al., 2024). Fenomena ini menimbulkan pertanyaan krusial: apakah LLM dapat diandalkan untuk aplikasi medis yang membutuhkan prediksi konsisten? (Lee et al., 2024). Sebagian besar penelitian LLM dalam konteks medis fokus pada medical question answering atau clinical reasoning dari teks naratif, namun sangat sedikit yang mengevaluasi reproducibility—kemampuan model menghasilkan prediksi yang sama pada kasus yang sama ketika dijalankan berulang kali.

Penelitian Zhang et al. (2022) dan Liang et al. (2022) menunjukkan bahwa meskipun model ML dapat mencapai akurasi tinggi, hasil prediksi sering kali tidak stabil ketika diuji pada kondisi data yang berbeda-beda. Variasi data pasien mulai dari usia, jenis kelamin, tekanan darah, kadar kolesterol, hingga riwayat komorbiditas menjadi faktor penting yang dapat memengaruhi performa model (Chen et al., 2021; Ghassemi et al., 2020). Ketidakstabilan prediksi ini dapat mengurangi keandalan sistem ketika diterapkan di dunia nyata, sehingga menjadi tantangan yang harus diatasi sebelum AI dapat secara luas digunakan dalam layanan kesehatan.

Lebih kritis lagi, terdapat asumsi implisit dalam literatur AI medis bahwa konsistensi tinggi (reproducibility) secara otomatis mengimplikasikan akurasi tinggi (Zhang et al., 2023). Namun, apakah asumsi ini valid? Sebuah model dapat sangat konsisten—selalu memberikan jawaban yang sama—namun konsisten dalam kesalahan (Obermeyer et al., 2019; Vyas et al., 2020). Sebaliknya, model yang akurat namun tidak konsisten juga tidak dapat diandalkan dalam setting klinis di mana keputusan harus reproducible dan dapat diaudit (Ghassemi et al., 2020). Pemahaman tentang hubungan antara consistency dan accuracy ini menjadi sangat penting, namun belum ada penelitian yang secara sistematis mengevaluasi dissociation antara kedua dimensi kualitas model ini, khususnya pada LLM untuk diagnosis medis.

Teknik *clustering* seperti K-*Means Clustering* telah banyak diterapkan untuk mengelompokkan data medis berdasarkan karakteristik tertentu (Shang et al., 2025). Teknik ini terbukti dapat meningkatkan *representativitas* dan keberagaman dataset, sehingga hasil prediksi dapat lebih menggambarkan variasi kondisi pasien di lapangan (Tsoi et al., 2020). Namun, penggunaan *clustering* sebagai metode pemilihan data uji untuk meningkatkan stabilitas prediksi model masih sangat terbatas dalam literatur (Zhao et al., 2024). Padahal, dalam konteks penyakit kardiovaskular yang sangat heterogen, pemilihan data uji yang representatif sangat penting untuk menilai keandalan model AI secara komprehensif.

Untuk menjawab tantangan tersebut, penelitian ini mengimplementasikan multi-run protocol—pendekatan di mana setiap model dijalankan 4 kali secara independen untuk setiap kasus medis yang sama—untuk mengukur intra-model consistency (reproducibility). Penelitian ini menguji tiga model LLM state-of-the-art: GPT-4o (OpenAI), Gemini-2.0-Flash (Google), dan Qwen-Plus (Alibaba), yang masing-masing memiliki arsitektur, data pelatihan, dan karakteristik reasoning yang berbeda. Dataset yang digunakan adalah UCI Heart Disease dataset (Goldberger et al., 2000) yang berisi 303 pasien dengan 13 parameter klinis yang komprehensif, mencakup usia, jenis kelamin, tipe nyeri dada, tekanan darah, kolesterol, gula darah, hasil EKG, detak jantung maksimum, dan parameter diagnostik lainnya.

Untuk memastikan representativitas dan keberagaman kasus yang diuji, penelitian ini menggunakan stratified sampling berbasis K-Means Clustering. Seluruh dataset (303 pasien) terlebih dahulu di-cluster untuk mengidentifikasi subgrup pasien dengan profil klinis yang serupa, kemudian dari setiap cluster dipilih sampel secara proporsional sehingga diperoleh 100 test cases yang representatif. Setiap kasus diuji dengan 4 independent runs, 3 model LLM, dan 2 prompt variants (Expert Clinician tone vs Neutral tone), menghasilkan total 2,400 prediksi untuk analisis komprehensif.

Evaluasi model dilakukan menggunakan metrik komprehensif yang mencakup tiga dimensi utama: (1) **intra-model consistency**—mengukur agreement prediksi dalam multiple runs untuk kasus yang sama; (2) **diagnostic accuracy**—mengukur ketepatan prediksi dibandingkan dengan ground truth diagnosis menggunakan accuracy, precision, recall, dan F1-score; (3) **inter-model agreement**—mengukur konsensus prediksi antar model yang berbeda. Pendekatan evaluasi multidimensi ini memberikan gambaran komprehensif tentang reliability LLM, tidak hanya dari sisi "seberapa sering benar" (accuracy) tetapi juga "seberapa konsisten" (reproducibility) dan "seberapa sepakat" (consensus).

Penelitian ini juga mengevaluasi efek prompt engineering dengan membandingkan dua gaya prompt yang berbeda: Expert Clinician prompt (menggunakan terminologi medis formal dan tone direktif) versus Neutral prompt (menggunakan bahasa yang lebih umum dan tone objektif). Hipotesis yang akan diuji adalah apakah expert-framed prompts dapat meningkatkan akurasi dan consistency karena lebih aligned dengan medical reasoning, atau apakah LLM memiliki "internal representation" yang relatif stabil terhadap variasi superficial dalam prompt phrasing. Evaluasi ini penting untuk memahami limitations dari prompt engineering sebagai strategi untuk meningkatkan performa diagnostik.

Melalui pendekatan tersebut, penelitian ini bertujuan memberikan kontribusi signifikan terhadap pengembangan sistem prediksi penyakit kardiovaskular berbasis AI yang lebih akurat, stabil, dan dapat diandalkan dalam kondisi dunia nyata. Selain menutup celah penelitian sebelumnya, hasil penelitian ini diharapkan dapat menjadi dasar bagi pengembangan *Clinical Decision Support System* (CDSS) yang lebih efektif dan efisien. Dengan demikian, penelitian ini tidak hanya memberikan manfaat akademik, tetapi juga berpotensi meningkatkan kualitas layanan kesehatan melalui deteksi dini penyakit kardiovaskular yang lebih tepat dan konsisten.

### **Research Gaps yang Diidentifikasi**

Berdasarkan analisis komprehensif terhadap literatur existing, penelitian ini mengidentifikasi **enam research gaps krusial** yang menjadi motivasi utama:

**RG1. Reproducibility Evaluation Gap**: Tidak ada penelitian yang systematic mengevaluasi intra-model consistency LLM melalui multi-run protocol dalam medical diagnosis. Semua studi existing melakukan single prediction per case, mengasumsikan deterministic behavior padahal LLM bersifat stochastic.

**RG2. Consistency-Accuracy Relationship Gap**: Literature AI medis implicitly mengasumsikan korelasi positif antara consistency dan accuracy, namun asumsi ini belum divalidasi empirically. Tidak ada penelitian yang menganalisis kemungkinan dissociation—di mana model dapat highly consistent namun low accuracy (consistently wrong) atau sebaliknya.

**RG3. Multi-Model Comparative Gap**: Tidak ada comparative study yang mengevaluasi GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus secara head-to-head pada dataset medis yang sama dengan standardized protocol. Existing studies focus pada single model evaluation.

**RG4. Prompt Engineering Effectiveness Gap**: Meskipun prompt engineering widely acclaimed sebagai primary method untuk steering LLM behavior, efek actual terhadap consistency dan accuracy dalam medical diagnosis belum dievaluasi dengan controlled experiments. Unclear apakah prompt variations significantly impact diagnostic performance.

**RG5. Systematic Bias Identification Gap**: Research sebelumnya report aggregate metrics (accuracy, F1-score) tanpa menganalisis error patterns systematically. Distribution of false positives vs false negatives—yang memiliki clinical implications sangat berbeda—tidak investigated. Systematic biases yang dapat harm patients belum teridentifikasi.

**RG6. Stratified Evaluation Gap**: Tidak ada penelitian yang menggunakan clustering-based stratified sampling untuk ensure test set diversity dalam LLM evaluation. Random sampling atau convenience sampling dominan, potentially menghasilkan biased evaluation pada subset homogen.

### **Novelty dan Kontribusi Penelitian**

Penelitian ini **first-of-its-kind study** yang secara komprehensif addresses keenam research gaps tersebut dengan novel contributions berikut:

**Novelty 1: Multi-Run Reproducibility Protocol**  
First study yang systematically evaluates LLM reproducibility dalam medical diagnosis melalui 4 independent runs per case, generating 2,400 predictions (100 cases × 4 runs × 3 models × 2 prompts). Metodologi ini establishes new standard untuk LLM evaluation in high-stakes medical applications.

**Novelty 2: Systematic Consistency-Accuracy Dissociation Analysis**  
First study yang systematically investigates hubungan antara consistency dan accuracy dimensions dalam LLM medical diagnosis. Methodology ini challenges conventional assumption bahwa high consistency automatically implies high accuracy, providing framework untuk analyzing potential dissociation yang has profound implications untuk clinical deployment.

**Novelty 3: Head-to-Head Multi-Model Benchmark**  
First comprehensive comparison of three state-of-the-art LLMs (GPT-4o, Gemini-2.0-Flash, Qwen-Plus) pada identical cardiovascular dataset dengan standardized evaluation framework. Provides empirical evidence untuk model selection in medical AI.

**Novelty 4: Rigorous Controlled Prompt Engineering Experiment**  
First rigorous controlled experiment yang compares Expert Clinician vs Neutral prompt dengan large sample (1,200 predictions per prompt variant) untuk systematically evaluate prompt engineering effectiveness dalam numerical medical diagnosis. Methodology ini addresses gap dalam understanding whether prompt variations significantly impact diagnostic performance.

**Novelty 5: Comprehensive Systematic Bias Analysis**  
First study yang systematically analyzes error patterns beyond aggregate metrics, specifically investigating distribution of false positives vs false negatives across multiple models dan prompt variants. Methodology ini enables identification of systematic biases yang dapat harm patients dan must be addressed sebelum clinical deployment.

**Novelty 6: Clustering-Based Stratified Sampling Methodology**  
First application of K-Means clustering untuk stratified test set selection dalam LLM medical evaluation, ensuring diversity across clinical profiles. Methodology ini improves external validity dibanding random sampling yang dominan dalam existing studies, providing more robust evaluation framework.

**Theoretical Contribution**: Memperkenalkan framework conceptual baru untuk LLM evaluation dalam medical applications yang separates **reproducibility** (consistency dimension) dari **validity** (accuracy dimension), acknowledging bahwa kedua dimensi dapat dissociate dan harus evaluated independently.

**Methodological Contribution**: Establishes reproducible protocol untuk multi-run LLM evaluation yang dapat adopted widely dalam medical AI research, addressing current lack of standardization dalam LLM reproducibility testing.

**Empirical Contribution**: Provides large-scale systematic evaluation of LLM consistency-accuracy relationship dalam medical diagnosis through comprehensive multi-run protocol, generating benchmark data untuk future research.

**Practical Contribution**: Identifies critical limitations dan systematic biases yang must be addressed sebelum LLM dapat safely deployed dalam clinical decision support, providing evidence-based guidelines untuk responsible AI implementation.

Publikasi preprint dalam **JAMIA (Journal of the American Medical Informatics Association)** dengan DOI **10.64898/2025.12.08.25341823** (December 2025) validates international scientific significance dari research contributions ini.

## 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, maka rumusan masalah dalam penelitian ini adalah sebagai berikut:

1. Seberapa konsisten Large Language Models (GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus) dalam menghasilkan prediksi yang sama pada kasus medis yang identik ketika dijalankan berulang kali (intra-model consistency/reproducibility)?

2. Apakah consistency tinggi (reproducibility) menjamin akurasi diagnostik yang tinggi, ataukah terdapat dissociation antara kedua dimensi kualitas model ini dalam konteks diagnosis penyakit kardiovaskular?

3. Bagaimana efek prompt engineering (Expert Clinician vs Neutral tone) terhadap consistency dan accuracy prediksi diagnosis penyakit kardiovaskular oleh Large Language Models?

## 1.3 Batasan Masalah

Agar penelitian lebih terarah dan sesuai dengan tujuan yang ingin dicapai, maka batasan masalah dalam penelitian ini ditetapkan sebagai berikut:

1. Penelitian ini berfokus pada diagnosis biner penyakit kardiovaskular (presence/absence of heart disease) dan tidak mencakup severity staging, prognosis jangka panjang, atau jenis penyakit kardiovaskular spesifik lainnya.

2. Model Large Language Model yang diuji terbatas pada tiga model state-of-the-art: GPT-4o (OpenAI), Gemini-2.0-Flash (Google), dan Qwen-Plus (Alibaba); model LLM lain atau model machine learning tradisional tidak dibahas dalam penelitian ini.

3. Dataset yang digunakan adalah UCI Heart Disease Dataset yang berisi 303 pasien dengan 13 parameter klinis; penelitian tidak melakukan pengumpulan data primer atau menggunakan dataset lain.

4. Stratified sampling menggunakan K-Means Clustering (K=2) untuk pemilihan 100 test cases yang representatif; teknik clustering lain atau metode sampling lain tidak dibandingkan.

5. Multi-run protocol menggunakan 4 independent runs per kasus untuk setiap kombinasi model-prompt, menghasilkan total 2,400 prediksi (100 cases × 4 runs × 3 models × 2 prompts).

6. Prompt engineering terbatas pada dua variants: Expert Clinician tone dan Neutral tone; prompt variations lain tidak dieksplorasi secara sistematis.

7. Evaluasi performa menggunakan metrik standar: intra-model consistency, accuracy, precision, recall, F1-score, dan inter-model agreement; metrik advanced lain seperti calibration atau fairness tidak dibahas.

8. Penelitian ini merupakan evaluasi ex-post terhadap prediksi LLM dan tidak mencakup implementasi real-time dalam clinical decision support system atau pengujian pada pasien nyata.

## 1.4 Tujuan Penelitian

Berdasarkan rumusan masalah yang telah ditetapkan dan research gaps yang teridentifikasi, penelitian ini memiliki tujuan komprehensif sebagai berikut:

**Tujuan 1: Reproducibility Evaluation (Addressing RG1)**  
Mengukur dan membandingkan intra-model consistency (reproducibility) dari tiga Large Language Models (GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus) dalam diagnosis penyakit kardiovaskular melalui **novel multi-run protocol** (4 independent runs per case), establishing benchmark untuk LLM reproducibility dalam medical diagnosis.

**Tujuan 2: Consistency-Accuracy Dissociation Analysis (Addressing RG2)**  
Menganalisis hubungan antara consistency dan accuracy untuk mengevaluasi apakah reproducibility tinggi menjamin diagnostic accuracy tinggi, atau apakah terdapat **consistency-accuracy dissociation**—fenomena di mana model highly consistent namun low accuracy—yang challenging conventional assumptions dalam AI medis.

**Tujuan 3: Prompt Engineering Effects Evaluation (Addressing RG4)**  
Mengevaluasi efek prompt engineering (Expert Clinician tone vs Neutral tone) terhadap performa LLM dalam hal consistency, accuracy, dan systematic bias patterns melalui **controlled comparative experiment** dengan large sample size (1,200 predictions per variant).

**Tujuan 4: Systematic Bias Identification (Addressing RG5)**  
Mengidentifikasi error patterns dan systematic biases (khususnya false positive vs false negative distribution) yang mungkin terjadi pada LLM-based medical diagnosis untuk menginformasikan **safe and responsible deployment guidelines** dalam clinical settings.

## 1.5 Manfaat Penelitian

### 1.5.1 Manfaat Akademik

Penelitian ini diharapkan dapat memberikan kontribusi akademik sebagai berikut:

a. **Metodologis**: Memperkenalkan multi-run protocol sebagai framework evaluasi reproducibility untuk Large Language Models dalam medical diagnosis, yang dapat diadopsi dalam penelitian AI medis lainnya.

b. **Teoretis**: Mengungkap fenomena consistency-accuracy dissociation pada LLM, menantang asumsi konvensional bahwa high consistency secara otomatis mengimplikasikan high accuracy dalam aplikasi medis.

c. **Empiris**: Menyediakan data komparatif komprehensif tentang performa tiga LLM state-of-the-art (GPT-4o, Gemini-2.0-Flash, Qwen-Plus) dalam diagnosis medis, yang saat ini masih sangat terbatas dalam literatur.

d. **Memperluas literatur**: Menjadi referensi utama untuk penelitian reproducibility, prompt engineering effects, dan systematic bias patterns dalam LLM-based medical diagnosis.

### 1.5.2 Manfaat Praktis

Penelitian ini diharapkan memberikan manfaat praktis dalam implementasi AI di layanan kesehatan:

a. **Evidence-based deployment guidelines**: Memberikan bukti empiris tentang limitations LLM dalam medical diagnosis, menginformasikan pengambilan keputusan tentang kapan dan bagaimana LLM sebaiknya digunakan dalam clinical practice.

b. **Risk identification**: Mengidentifikasi systematic biases (khususnya false positive epidemic) yang dapat membahayakan pasien, membantu klinisi memahami limitations dan mengantisipasi potential errors.

c. **Responsible AI development**: Menginformasikan developer tentang pentingnya evaluasi reproducibility dan bias testing sebelum deployment dalam healthcare settings yang high-stakes.

d. **Clinical decision support system design**: Memberikan insights untuk desain CDSS yang lebih robust, misalnya dengan mengimplementasikan ensemble methods atau human-in-the-loop approaches untuk mitigasi systematic biases.

# BAB II TINJAUAN PUSTAKA

## 2.1 Kajian Pustaka

Prediksi penyakit kardiovaskular berbasis kecerdasan buatan telah berkembang pesat dalam lima tahun terakhir, dengan model prediksi yang sebelumnya didominasi oleh *machine learning* (ML) tradisional kini beralih ke pendekatan berbasis *deep learning* dan *Large Language Models* (LLMs). Penelitian oleh Mohan et al. (2019) menunjukkan bahwa model *hibrida Random Forest* dan model linier mampu mencapai akurasi 88,7% dalam memprediksi penyakit jantung, yang menandakan bahwa model ML klasik masih memiliki performa yang kompetitif dalam deteksi risiko kardiovaskular. Namun, pendekatan terbaru berbasis GPT-4o, model LLM *generatif* yang dikembangkan oleh *OpenAI*, menunjukkan kemajuan signifikan dalam hal akurasi prediksi, dan mampu mengidentifikasi pola yang lebih kompleks dalam data medis.\
Pendekatan *clustering* juga banyak digunakan dalam studi kardiovaskular untuk mengelompokkan data berdasarkan karakteristik medis yang serupa. Islam et al. (2020) menggunakan K-*Means* dan *Hierarchical Clustering* untuk mengidentifikasi pola yang berhubungan dengan *infark miokard,* sementara Tsoi et al. (2020) menerapkan K-*Means* dalam penelitian SPRINT untuk mengelompokkan variabilitas tekanan darah. Meskipun *clustering* dapat membantu memahami struktur data yang lebih kompleks, penelitian ini masih terbatas pada penggunaan teknik tersebut sebagai metode pemilihan data uji untuk mengevaluasi stabilitas prediksi model AI. Ini menunjukkan bahwa potensi *clustering* untuk meningkatkan evaluasi model, seperti *Gemini-*2.0-*flash* dan *Qwen*-*Plus,* masih belum optimal.\
*Deep learning* dan model berbasis *transformer* telah menunjukkan hasil yang luar biasa dalam prediksi penyakit jantung, terutama dalam menangani data sekuensial. (Islam et al., 2024) menunjukkan bahwa *Convolutional Neural Networks* (CNN) dan *Long Short-Term Memory* (LSTM) meningkatkan prediksi risiko jangka panjang, terutama dengan memanfaatkan data rekam medis elektronik (EHR). Sementara itu, model berbasis *transformer* yang dikembangkan oleh Chu et al. (2023) untuk klasifikasi sinyal EKG menunjukkan performa yang lebih baik, dengan akurasi mencapai 93,7%. Arsitektur transformer juga memiliki potensi besar dalam meningkatkan prediksi penyakit kardiovaskular karena kemampuannya untuk memahami konteks data medis secara lebih mendalam, yang menjadi kekuatan utama dari model GPT-4o.\
*Tren riset* dua tahun terakhir menunjukkan peralihan yang signifikan menuju penggunaan model AI *generatif* seperti GPT-4o, Gemini-2.0-*flash,* dan Qwen-*Plus.* Johnson et al. (2024) menunjukkan bahwa GPT-4o, yang diintegrasikan dengan data EHR, dapat meningkatkan ketepatan pengambilan keputusan klinis hingga 26%. Sementara itu, Zhao et al. (2024) menggunakan *Generative Adversarial Networks* (GANs) dan LLM untuk mengatasi ketidakseimbangan dataset penyakit kardiovaskular, dan hasilnya *augmentasi* data berbasis AI berhasil meningkatkan stabilitas prediksi sebesar 12%. Temuan ini menyoroti keunggulan model AI generatif yang tidak hanya mampu memberikan prediksi yang akurat, tetapi juga meningkatkan kualitas dataset yang digunakan, meningkatkan robustness model prediksi penyakit jantung.\
Seiring berkembangnya kemampuan LLM, muncul kebutuhan untuk mengevaluasi konsistensi prediksi pada data medis numerik, khususnya dalam prediksi penyakit kardiovaskular. Meskipun banyak penelitian yang menilai kekuatan model LLM dalam konteks *clinical reasoning* dan analisis teks medis, masih sangat sedikit yang secara langsung membandingkan kemampuan prediktif model-model seperti *Gemini-2.0-flash, Qwen-Plus*, dan GPT-4o terhadap dataset numerik, seperti tekanan darah, kolesterol, dan parameter kesehatan lainnya. Penelitian ini mencoba untuk mengisi kesenjangan tersebut.\
Kebutuhan untuk mengevaluasi konsistensi prediksi dalam konteks medis menjadi sangat penting. Sebagian besar penelitian terdahulu menitikberatkan pada akurasi tunggal tanpa memperhatikan *batch testing,* yaitu evaluasi prediktif berulang untuk mengukur stabilitas dan *reproducibility* model. Di dunia medis, kestabilan prediksi adalah faktor krusial, karena kesalahan kecil dalam input dapat mempengaruhi keputusan klinis yang sangat penting. Meskipun demikian, hingga saat ini belum ada penelitian yang menilai stabilitas prediksi LLM melalui pengujian berulang pada dataset penyakit jantung.

Sebagian besar penelitian sebelumnya hanya menguji satu model AI pada satu dataset, sehingga belum ada studi komparatif langsung yang membandingkan tiga model AI generatif modern Gemini-2.0-flash, Qwen-Plus, dan GPT-4o. Padahal, ketiga model ini memiliki arsitektur yang berbeda, teknik pelatihan yang berbeda, dan kapasitas analisis numerik yang berbeda. Penelitian ini bertujuan untuk mengisi celah penelitian tersebut, dengan fokus pada perbandingan akurasi dan konsistensi prediksi.

**Emerging Research on LLM Reproducibility and Medical Applications**

Perkembangan terkini dalam penelitian LLM menunjukkan bahwa reproducibility menjadi isu krusial yang belum terpecahkan. Studi oleh Elazar et al. (2021) menunjukkan bahwa model generative menunjukkan variasi output yang signifikan bahkan dengan temperature=0, mengindikasikan bahwa stochasticity inheren dalam architecture. Dalam konteks medis, Lee et al. (2024) mengevaluasi GPT-4 untuk clinical reasoning dan menemukan bahwa meskipun model menunjukkan impressive performance pada medical licensing exams, consistency dalam diagnostic recommendations untuk kasus yang sama masih menjadi concern. Namun, evaluasi systematic terhadap reproducibility melalui multi-run protocol belum dilakukan untuk medical diagnosis tasks.

**The Consistency-Accuracy Tradeoff**

Research gap yang paling kritis adalah pemahaman tentang hubungan antara consistency dan accuracy. Sebagian besar literatur AI medis mengasumsikan bahwa kedua metrik berkorelasi positif—model yang konsisten dianggap lebih reliable dan akurat. Namun, asumsi ini belum divalidasi secara empiris. Model yang always wrong but consistent akan memiliki perfect consistency namun zero accuracy. Sebaliknya, model yang occasionally correct but inconsistent juga tidak dapat diandalkan. Penelitian ini adalah yang pertama secara systematic mengukur dissociation antara consistency dan accuracy pada LLM-based medical diagnosis.

**Prompt Engineering and Its Limitations**

Prompt engineering telah menjadi paradigma utama untuk "steering" LLM behavior tanpa retraining. Dalam konteks medis, Zhou et al. (2023) menunjukkan bahwa expertly-crafted prompts dapat meningkatkan performance GPT-4 pada medical question answering tasks. Namun, belum jelas apakah prompt engineering efektif untuk meningkatkan consistency dan accuracy dalam diagnosis numerik-based. Lebih lanjut, belum ada penelitian yang systematic mengevaluasi robustness LLM terhadap prompt variations dalam medical diagnosis context.

Untuk memberikan gambaran yang lebih sistematis mengenai perkembangan penelitian dan posisi penelitian ini dalam landscape ilmiah, berikut disajikan tabel ringkasan komprehensif dari penelitian terdahulu yang menjadi acuan utama, diorganisasi secara thematic berdasarkan evolution dari traditional ML menuju LLM-based approaches.

**Tabel 2.1 Ringkasan Komprehensif Kajian Pustaka: Evolusi AI dalam Prediksi Kardiovaskular**

| **No** | **Peneliti & Tahun** | **Focus Area** | **Model/Method** | **Dataset & Sample** | **Evaluasi** | **Key Findings** | **Research Gaps** |
|--------|---------------------|----------------|------------------|---------------------|--------------|------------------|-------------------|
| **A. Traditional Machine Learning Era (2019-2021)** |||||||
| **1** | Mohan et al. (2019) | CVD Prediction | Hybrid RF + Linear Model | UCI Cleveland (303 patients, 13 features) | Single-run accuracy | Accuracy: **88.7%** <br> Sensitivity: 87.5% | No reproducibility testing; Single model evaluation |
| **2** | Banerjee et al. (2019) | ML Review for CVD | Systematic Review (40+ studies) | Meta-analysis of ML in CVD | Accuracy metrics only | ML effective for risk stratification (85-95% accuracy range) | Consistency not evaluated; Focus on aggregate metrics only |
| **3** | Islam et al. (2020) | Clustering for MI | K-Means + Hierarchical | Myocardial Infarction dataset (750 patients) | Clustering quality (Silhouette) | Clustering identifies 3 MI risk profiles; Silhouette=0.34 | Clustering not used for stratified sampling |
| **4** | Zhang et al. (2020) | MACE Prediction | Random Forest | ED patients (11,000 cases) | AUC-ROC | AUC: **0.915** for acute cardiac events | Single prediction per patient; No multi-model comparison |
| **5** | Fitriyani et al. (2020) | CDSS for HD | XGBoost + SMOTE-ENN + DBSCAN | Cleveland dataset (920 records) | Accuracy, Precision, Recall | Accuracy: **98.4%** (likely overfitted) | No external validation; Unrealistic performance |
| **B. Deep Learning & Advanced Methods (2020-2023)** |||||||
| **6** | Tsoi et al. (2020) | BP Variability | K-Means Clustering | SPRINT Trial (9,361 patients) | Cox regression for CVD risk | 4 BP patterns identified; HR=1.58 for high-variability group | Clustering for risk stratification only; No predictive model evaluation |
| **7** | Bilchick et al. (2020) | CRT Response | Hierarchical Clustering | Heart failure patients (1,200 cases) | Survival analysis | Cluster-based response prediction improves survival estimates | Domain-specific (CRT therapy); Not generalizable to diagnosis |
| **8** | Wang et al. (2021) | Explainable AI | XAI + Random Forest | Multi-center CVD cohort (4,500 patients) | Accuracy + Interpretability | Accuracy: **90.2%**; SHAP values for feature importance | No consistency evaluation; Focus on interpretability only |
| **9** | Lin et al. (2022) | Longitudinal Prediction | CNN + LSTM (RNN) | 5-year EHR data (longitudinal) | Time-series prediction accuracy | Accuracy: **94%** for 5-year CVD risk | Sequential data only; Not applicable to tabular/numeric data |
| **10** | Chu et al. (2023) | ECG Classification | Transformer Architecture | ECG signals (20,000 cases) | Multi-class accuracy | Accuracy: **93.7%** for arrhythmia classification | Signal processing focus; Different from tabular clinical data |
| **11** | Zhou et al. (2023) | Prompt Engineering | GPT-4 Medical QA | MedQA benchmark (1,273 questions) | QA accuracy | Expert prompts improve accuracy +8% over neutral prompts | Text-based QA only; No numerical diagnosis evaluation |
| **C. Large Language Models Era (2024-2025)** |||||||
| **12** | Elazar et al. (2024) | LLM Stochasticity | GPT-3, GPT-4 (general LLMs) | NLP benchmarks | Output variability | Significant variance even with temperature=0; Reproducibility concern | General NLP tasks; No medical diagnosis application |
| **13** | Lee et al. (2024) | Clinical Reasoning | GPT-4 Medical Licensing | USMLE practice exams | Exam pass rate | GPT-4 passes USMLE; Consistency concern noted but not measured | No systematic reproducibility evaluation; Single prediction per case |
| **14** | Johnson et al. (2024) | LLM-CDSS Integration | GPT-4 + EHR System | Cardiology patients (1,200 records) | Clinical decision accuracy | **+26%** improvement in decision quality with GPT-4 assistance | Single model only; No multi-run protocol; No consistency metrics |
| **15** | Zhao et al. (2024) | Generative Augmentation | GANs + LLMs | Imbalanced CVD dataset | Stability improvement | Data augmentation improves model stability **+12%** | Focus on data generation; No LLM diagnostic evaluation |
| **D. Penelitian Ini (2025)** |||||||
| **16** | **This Study (2025)** | **Multi-Run LLM Reproducibility** | **GPT-4o, Gemini-2.0-Flash, Qwen-Plus** | **UCI Cleveland (100 stratified cases via K-Means stratified sampling)** | **Multi-dimensional: Consistency + Accuracy + Bias Analysis** | **Protocol**: 4 independent runs × 3 models × 2 prompts = 2,400 predictions <br> **Framework**: Three-dimensional evaluation (reproducibility, validity, consensus) <br> **Innovation**: Stratified sampling + systematic bias analysis | **✓ Multi-run protocol (RG1)** <br> **✓ Consistency-accuracy dissociation analysis (RG2)** <br> **✓ Multi-model comparison (RG3)** <br> **✓ Prompt engineering evaluation (RG4)** <br> **✓ Systematic bias identification (RG5)** <br> **✓ Stratified sampling via clustering (RG6)** |

**Keterangan Kolom:**
- **Focus Area**: Domain atau aspek spesifik yang diteliti
- **Model/Method**: Algoritma atau pendekatan AI yang digunakan
- **Dataset & Sample**: Sumber data dan ukuran sampel
- **Evaluasi**: Metrik atau framework evaluasi yang digunakan
- **Key Findings**: Hasil utama dengan angka konkret
- **Research Gaps**: Keterbatasan yang menjadi motivasi penelitian ini

**Legend Kategori:**
- **A. Traditional ML (2019-2021)**: Era dominasi Random Forest, SVM, XGBoost dengan focus pada single-run accuracy
- **B. Deep Learning (2020-2023)**: Transisi ke CNN, LSTM, Transformer untuk data kompleks (time-series, images)
- **C. LLM Era (2024-2025)**: Emergence of GPT-4, Gemini untuk medical applications dengan reproducibility concerns
- **D. Penelitian Ini**: First systematic evaluation of LLM reproducibility, consistency-accuracy dissociation, dan multi-model comparison dalam cardiovascular diagnosis

**Analisis Tematik Berdasarkan Tabel 2.1:**

Berdasarkan analisis komprehensif terhadap 15 penelitian terdahulu yang tersistematisasi dalam Tabel 2.1, terlihat **tiga fase evolusi yang jelas** dalam penggunaan AI untuk prediksi kardiovaskular:

**Fase A: Traditional Machine Learning Era (2019-2021)**  
Periode ini didominasi oleh algoritma klasik (Random Forest, SVM, XGBoost) dengan fokus utama pada **aggregate accuracy metrics**. Mohan et al. (2019) dan Fitriyani et al. (2020) melaporkan accuracy 88.7% hingga 98.4% pada UCI Cleveland dataset yang sama yang digunakan dalam penelitian ini. Namun, **critical limitation** di fase ini adalah:
- **Single-run evaluation only**: Tidak ada penelitian yang menguji reproducibility melalui multiple predictions
- **No consistency metrics**: Semua fokus pada accuracy, precision, recall—mengabaikan stability concerns
- **Overfitting risks**: Beberapa studi (e.g., Fitriyani 98.4%) menunjukkan suspiciously high accuracy yang likely tidak generalizable

Clustering studies (Islam et al. 2020, Tsoi et al. 2020) menunjukkan potential K-Means untuk patient stratification, namun **tidak digunakan untuk test set selection**—gap yang diisi penelitian ini melalui stratified sampling.

**Fase B: Deep Learning Advancement (2020-2023)**  
Transisi ke arsitektur kompleks (CNN, LSTM, Transformer) untuk menangani **non-tabular data** (ECG signals, time-series EHR, medical images). Lin et al. (2022) dan Chu et al. (2023) mencapai accuracy 93-94%, namun **domain-specific** (sequential/signal data). Wang et al. (2021) fokus pada **explainable AI**, highlighting interpretability concerns namun masih dengan single-run evaluation.

**Critical insight**: Zhou et al. (2023) menunjukkan **prompt engineering effects** (+8% improvement) pada GPT-4 medical QA, namun **terbatas pada text-based tasks**. Penelitian ini extends evaluation ke numerical diagnosis domain.

**Fase C: Large Language Models Era (2024-2025)**  
Emergence of LLMs dalam medical applications dengan **mixed signals**:
- **Promising performance**: Johnson et al. (2024) menunjukkan GPT-4 improves clinical decisions +26%
- **Reproducibility concerns**: Elazar et al. (2024) dan Lee et al. (2024) note stochasticity issues namun **tidak mengukur systematically**
- **Single-model focus**: Semua studi mengevaluasi one LLM at a time—no comparative analysis across GPT-4o, Gemini, Qwen

**Fundamental Gap**: **Tidak ada satupun penelitian** yang:
1. Mengevaluasi **intra-model consistency** via multi-run protocol (semua single prediction)
2. Menganalisis **consistency-accuracy dissociation** (implicit assumption: korelasi positif)
3. Membandingkan **multiple LLMs head-to-head** dengan protocol yang sama
4. Mengidentifikasi **systematic bias patterns** (FP vs FN distribution)
5. Mengevaluasi **prompt engineering robustness** dalam numerical diagnosis context

**Posisi Penelitian Ini (Row 16)**: Mengisi **keenam research gaps** tersebut melalui rigorous experimental design yang combines:
- **Multi-run protocol** (4 independent runs) untuk systematic consistency evaluation
- **Multi-model comparison** (GPT-4o, Gemini-2.0-Flash, Qwen-Plus) dengan identical methodology
- **Stratified sampling** via K-Means clustering untuk ensure test set diversity across clinical profiles
- **Comprehensive systematic bias analysis** untuk identify error patterns beyond aggregate metrics
- **Rigorous controlled prompt engineering experiment** (Expert Clinician vs Neutral tone)
- **Novel framework**: Three-dimensional evaluation separating reproducibility, validity, dan consensus dimensions

**Identifikasi Research Gaps Krusial**

Dari keseluruhan temuan tersebut, terdapat beberapa research gaps mencolok yang menjadi motivasi penelitian ini:

1. **Reproducibility Evaluation**: Tidak ada penelitian yang systematic mengevaluasi intra-model consistency LLM dalam medical diagnosis melalui multiple independent runs. Padahal, dalam high-stakes medical applications, reproducibility adalah prerequisite fundamental untuk clinical deployment.

2. **Consistency-Accuracy Dissociation**: Tidak ada studi yang menganalisis hubungan antara consistency dan accuracy. Literature implicitly mengasumsikan korelasi positif, namun assumsi ini belum divalidasi empirically untuk LLM-based medical diagnosis.

3. **Multi-Model Comparison**: Belum ada comparative study yang mengevaluasi GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus secara head-to-head pada dataset medis yang sama dengan protocol yang standardized. Ini penting karena ketiga model memiliki architecture, training data, dan reasoning capabilities yang berbeda.

4. **Prompt Engineering Effects**: Meskipun prompt engineering sering diklaim sebagai solusi untuk meningkatkan LLM performance, efek actual terhadap consistency dan accuracy dalam medical diagnosis belum dievaluasi secara rigorous dengan controlled experiments.

5. **Systematic Bias Identification**: Research sebelumnya focus pada aggregate accuracy metrics, namun tidak menganalisis error patterns secara systematic. Identification of false positive vs false negative biases krusial untuk understanding clinical risks.

6. **Stratified Evaluation**: Tidak ada penelitian yang menggunakan clustering-based stratified sampling untuk memastikan test set diversity, padahal ini penting untuk external validity evaluation.

Penelitian ini dirancang specifically untuk mengisi keenam research gaps tersebut melalui rigorous experimental design, comprehensive evaluation metrics, dan systematic analysis of consistency-accuracy relationship dalam context of LLM-based cardiovascular disease diagnosis.

### 2.1.1 Systematic Biases in Medical AI: The False Positive Epidemic

Salah satu isu krusial yang jarang mendapat perhatian sufficient dalam medical AI literature adalah systematic bias dalam error patterns. Majority of studies report aggregate accuracy metrics (sensitivity, specificity, F1-score) tanpa menganalisis whether errors skew toward false positives (FP) atau false negatives (FN). Padahal, dalam clinical context, kedua tipe error memiliki implications yang sangat berbeda.

**False positive bias**—tendency model untuk over-diagnose disease—dapat menyebabkan unnecessary medical interventions, psychological distress, dan healthcare resource wastage. Sebaliknya, **false negative bias** dapat fatal karena pasien dengan penyakit actual tidak terdeteksi dan tidak menerima treatment yang diperlukan. Dalam cardiovascular disease diagnosis, FN bias arguably lebih dangerous karena dapat menyebabkan delayed treatment dan increased mortality risk.

Penelitian oleh Obermeyer et al. (2019) dalam *Science* menunjukkan bahwa commercial healthcare algorithms widely used di US healthcare system menunjukkan significant racial bias, systematically under-predicting illness severity untuk Black patients (false negative bias). Sementara itu, studi tentang cancer screening AI oleh McKinney et al. (2020) menemukan bahwa deep learning models cenderung produce more false positives dibanding human radiologists, leading to overdiagnosis concerns.

Dalam konteks LLM-based medical diagnosis, systematic bias identification menjadi semakin penting karena ketiga faktor berikut:

1. **Black-box Nature**: LLMs tidak memiliki explicit decision rules seperti traditional ML, making bias sources sulit di-trace.
2. **Training Data Imbalance**: Medical datasets typically imbalanced (more healthy cases than disease cases), yang dapat menyebabkan model bias toward majority class.
3. **Risk Aversion in Language Generation**: LLMs trained dengan RLHF (Reinforcement Learning from Human Feedback) may exhibit cautious behavior, potentially over-diagnosing untuk avoid litigation risks atau ethical concerns.

Penelitian ini specifically menganalisis error patterns dari GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus untuk mengidentifikasi whether they exhibit false positive or false negative bias dalam cardiovascular disease diagnosis. Understanding bias direction krusial untuk:
- **Clinical Risk Assessment**: Informing clinicians tentang model tendency (conservative vs liberal diagnosis)
- **Model Selection**: Choosing appropriate model based on clinical priorities (e.g., screening vs confirmatory diagnosis)
- **Threshold Calibration**: Adjusting decision thresholds untuk balance FP dan FN rates sesuai clinical utility

Penelitian ini specifically dirancang untuk menganalisis error patterns dari GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus untuk mengidentifikasi whether they exhibit false positive or false negative bias dalam cardiovascular disease diagnosis melalui comprehensive multi-run evaluation protocol.

## 2.2 Tinjauan Teoritis

### 2.2.1 Penyakit Kardiovaskular sebagai Masalah Kesehatan Global

Penyakit kardiovaskular merupakan kelompok gangguan pada jantung dan pembuluh darah, termasuk penyakit jantung koroner, infark miokard, gagal jantung, dan penyakit pembuluh darah perifer. Penyakit ini menjadi salah satu penyebab utama morbiditas dan mortalitas di dunia, dengan tren kejadian yang cenderung meningkat seiring perubahan gaya hidup, penuaan populasi, dan meningkatnya faktor risiko seperti hipertensi, dislipidemia, diabetes melitus, obesitas, dan kebiasaan merokok. Kompleksitas penyakit kardiovaskular terletak pada keterkaitan berbagai faktor risiko klinis, biokimia, dan perilaku, sehingga upaya deteksi dini dan prediksi risiko menjadi sangat penting untuk mencegah kejadian kardiovaskular fatal di kemudian hari. Dalam konteks ini, pengembangan model prediksi yang akurat dan konsisten menjadi salah satu strategi kunci untuk mendukung pengambilan keputusan klinis (Woodruff et al., 2024).

### 2.2.2 Kecerdasan Buatan dan Pembelajaran Mesin dalam Prediksi Medis

Kecerdasan buatan (*Artificial Intelligence*, AI) adalah cabang ilmu komputer yang berfokus pada pengembangan sistem yang mampu melakukan tugas-tugas yang biasanya membutuhkan kecerdasan manusia, seperti pengenalan pola, pengambilan keputusan, dan pemecahan masalah (Davenport & Kalakota, 2019). Salah satu cabang utama AI adalah *machine learning* (ML), yaitu pendekatan yang memungkinkan model belajar dari data untuk menghasilkan prediksi atau keputusan tanpa diprogram secara eksplisit untuk setiap kasus (Esteva et al., 2019). Dalam bidang medis, ML telah banyak dimanfaatkan untuk tugas-tugas seperti prediksi risiko penyakit kardiovaskular, klasifikasi citra medis, analisis sinyal EKG, hingga penentuan prognosis (Rajkomar et al., 2019; He et al., 2019).

Pada prediksi penyakit kardiovaskular, algoritma ML seperti Random Forest, Support Vector Machine, Logistic Regression, XGBoost, dan berbagai model *deep learning* terbukti mampu memanfaatkan variabel-variabel klinis (misalnya tekanan darah, kolesterol, usia, indeks massa tubuh, riwayat penyakit) untuk mengestimasi probabilitas kejadian penyakit (Ali et al., 2021; Mohan et al., 2019). Model-model ini bekerja dengan mempelajari pola hubungan kompleks antara fitur klinis dan label (misalnya "positif penyakit kardiovaskular" atau "negatif"), sehingga dapat digunakan untuk mendukung deteksi dini dan stratifikasi risiko (Banerjee et al., 2021).

### 2.2.3 *Large Language Models* (LLMs) dalam Konteks Medis: GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus

*Large Language Models* (LLMs) adalah model AI berskala besar yang dilatih menggunakan data teks dalam jumlah sangat besar untuk mempelajari pola bahasa, pengetahuan umum, dan kemampuan penalaran (Brown et al., 2020; Bommasani et al., 2021). Contoh LLMs modern adalah GPT (*Generative Pre-trained Transformer*), Gemini, dan Qwen yang kini dapat diakses melalui layanan API (*Application Programming Interface*) seperti GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus. Meskipun awalnya dikembangkan untuk tugas-tugas berbasis teks (seperti menjawab pertanyaan, merangkum, atau menerjemahkan), LLMs mulai dieksplorasi dalam konteks medis, termasuk untuk interpretasi data klinis, triase, rekomendasi berbasis guideline, hingga membantu prediksi risiko penyakit (Thirunavukarasu et al., 2023; Singhal et al., 2023; Islam et al., 2024).

Dalam konteks penelitian ini, LLMs dimanfaatkan sebagai "model prediksi" yang menerima input berupa fitur-fitur numerik penyakit kardiovaskular (misalnya usia, tekanan darah, kolesterol, riwayat diabetes) yang dikemas dalam bentuk prompt terstruktur, kemudian diminta memberikan output berupa klasifikasi binary (presence or absence of cardiovascular disease). GPT-4o, Gemini-2.0-Flash, dan Qwen-Plus merepresentasikan tiga keluarga LLM dengan arsitektur, data pelatihan, dan karakteristik perilaku yang berbeda, sehingga berpotensi menghasilkan perbedaan dalam hal akurasi, konsistensi, dan systematic bias patterns (Lee et al., 2024; Nori et al., 2023). Oleh karena itu, studi komparatif diperlukan untuk menilai seberapa baik masing-masing model bekerja pada data penyakit kardiovaskular dan whether they meet clinical reliability requirements untuk potential deployment (Gao et al., 2023).

### 2.2.4 Konsep Prediksi dan Evaluasi Performa Model

Prediksi dalam konteks penyakit kardiovaskular merujuk pada kemampuan model untuk mengestimasi apakah seorang individu termasuk kelompok berisiko tinggi atau rendah terhadap suatu kejadian kardiovaskular (misalnya infark miokard atau penyakit jantung koroner) berdasarkan data klinis yang tersedia (Rajkomar et al., 2019). Untuk menilai kualitas suatu model prediksi, digunakan berbagai metrik evaluasi, antara lain (Xie et al., 2022; Ali et al., 2021):

**a. Accuracy**: Proporsi prediksi yang benar dari seluruh sampel.

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

**b. Precision**: Proporsi kasus yang benar-benar positif dari seluruh kasus yang diprediksi positif.

$$\text{Precision} = \frac{TP}{TP + FP}$$

**c. Recall/Sensitivity**: Proporsi kasus positif yang berhasil dideteksi oleh model (Sapra & Sapra, 2024).

$$\text{Recall} = \frac{TP}{TP + FN}$$

**d. F1-score**: Harmonik mean antara *precision* dan *recall* (Ali et al., 2021).

$$F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

dimana TP = True Positive, TN = True Negative, FP = False Positive, FN = False Negative.

**Perbedaan Krusial: Accuracy vs Consistency**

Penting untuk memahami bahwa **accuracy** dan **consistency** adalah dua dimensi evaluasi yang **independent** (Ghassemi et al., 2020):

- **Accuracy** mengukur seberapa sering model benar dibandingkan dengan ground truth labels
- **Consistency** mengukur seberapa reproducible predictions across multiple runs

Model dapat memiliki kombinasi apapun dari kedua dimensi ini:
1. **High accuracy, high consistency**: Ideal state—model reliable dan correct
2. **High accuracy, low consistency**: Model kadang-kadang correct tetapi unpredictable
3. **Low accuracy, high consistency**: Model consistently wrong—reliable tetapi incorrect
4. **Low accuracy, low consistency**: Worst case—unreliable dan incorrect

Dalam clinical context, **consistency adalah prerequisite**. Model yang inconsistent (bahkan jika sometimes accurate) tidak dapat deployed karena clinicians tidak bisa trust outputs yang berubah-ubah untuk patient yang sama. Conversely, model yang highly consistent (bahkan jika accuracy moderate) provides predictable behavior yang dapat di-calibrate atau di-combine dengan clinical judgment.

Penelitian ini specifically investigates whether consistency dan accuracy berkorelasi positif (as commonly assumed) atau exhibits dissociation dalam context of LLM-based cardiovascular diagnosis.

### 2.2.5 *Clustering* dan K-Means sebagai Strategi Stratified Sampling

*Clustering* adalah teknik *unsupervised learning* yang digunakan untuk mengelompokkan data ke dalam beberapa cluster berdasarkan kemiripan karakteristik (Shang et al., 2025). Salah satu metode clustering yang paling populer adalah K-Means, yang bekerja dengan meminimalkan jarak antara titik data dan pusat cluster (*centroid*). Dalam penelitian penyakit kardiovaskular, clustering dapat digunakan untuk:

a. Menemukan subgrup pasien dengan profil risiko serupa
b. Mengidentifikasi pola klinis tersembunyi  
c. Membantu segmentasi data untuk keperluan analisis lanjutan

Dalam penelitian ini, K-Means digunakan sebagai **stratified sampling method** untuk memastikan test set diversity dan representativeness. Berbeda dari random sampling yang dapat menghasilkan test set yang homogen atau biased, clustering-based stratified sampling ensures bahwa test cases mencakup full spectrum of clinical profiles dalam dataset.

**Prosedur Stratified Sampling via Clustering**:

1. **Clustering Evaluation**: Evaluate K-Means dengan K=2 hingga K=10, pilih optimal K based on Silhouette Score
2. **Stratified Selection**: Sample equal number of cases dari setiap cluster untuk ensure balanced representation
3. **Diversity Verification**: Verify bahwa test set mencakup varied clinical characteristics (age, blood pressure, cholesterol, etc.)

Penelitian ini menggunakan evaluasi systematic dari K=2 hingga K=10 untuk menentukan optimal cluster number based on Silhouette Score sebagai metrik clustering quality. Setelah optimal K ditentukan, test cases diselect secara stratified dari setiap cluster untuk ensure balanced representation of diverse clinical profiles dalam evaluation set.

Pendekatan ini secara teoretis meningkatkan **external validity** karena model evaluation tidak terbatas pada specific subset of patients, melainkan covers diverse clinical scenarios yang likely encountered dalam real-world deployment.

### 2.2.6 Konsep Konsistensi, Reproducibility, dan Multi-Run Protocol dalam Evaluasi LLM

Selain akurasi, aspek penting lain dalam penerapan model AI di bidang medis adalah **reproducibility**—kemampuan model untuk menghasilkan hasil yang consistent ketika diuji berulang kali pada kondisi yang sama (Ghassemi et al., 2020; Zhang et al., 2022). Dalam konteks LLMs, reproducibility menjadi challenging karena sifat **stochastic** dari language generation process (Elazar et al., 2024). Bahkan dengan temperature=0 (setting paling deterministic), LLMs masih dapat menunjukkan variability dalam outputs karena faktor-faktor seperti:

1. **Sampling variability** dalam decoding algorithms (top-k, nucleus sampling)
2. **Model updates** yang dilakukan provider secara continuous
3. **Infrastructure variability** dalam distributed computing environments
4. **Prompt sensitivity** terhadap minor variations dalam input formatting (Zhou et al., 2023)

Untuk mengevaluasi reproducibility secara rigorous, penelitian ini menggunakan **multi-run protocol**—sebuah metodologi dimana setiap test case dievaluasi **multiple times** (dalam hal ini 4 independent runs) untuk mengukur **intra-model consistency** (Rajpurkar et al., 2022). Protocol ini berbeda dari traditional single-prediction approach yang assumes deterministic behavior.

**Intra-model consistency** didefinisikan sebagai percentage of test cases dimana model memberikan identical predictions across all runs. Formula matematisnya:

$$\text{Consistency} = \frac{\text{Jumlah kasus dengan prediksi identik di semua runs}}{\text{Total jumlah test cases}} \times 100\%$$

Contoh: Jika dari 100 test cases, 99 cases mendapat prediksi identical di 4 runs, maka consistency = 99%.

**Perbedaan Consistency vs Accuracy**: Ini adalah dimensi evaluasi yang **independent**. Model dapat:
- **High consistency, low accuracy**: Selalu salah dengan cara yang sama (consistent error)
- **Low consistency, high accuracy**: Kadang benar, kadang salah (unstable performance)
- **High consistency, high accuracy**: Ideal state (reliable dan accurate)
- **Low consistency, low accuracy**: Worst case (unreliable dan inaccurate)

Dalam konteks klinis, **high consistency** adalah **prerequisite** untuk deployment, bahkan jika accuracy moderate (Meskó & Topol, 2023). Model yang unpredictable (low consistency) tidak dapat digunakan dalam clinical decision support, regardless of average accuracy, karena clinicians tidak dapat trust outputs yang berubah-ubah untuk patient yang sama.

Multi-run protocol juga memungkinkan identifikasi **systematic vs random errors** (Chen et al., 2021):
- **Systematic errors**: Muncul consistently across all runs → indicates model bias atau knowledge gaps
- **Random errors**: Berbeda-beda across runs → indicates stochastic variability atau marginal cases

Penelitian ini menggunakan 4 runs sebagai balance antara:
- **Statistical power**: Cukup untuk detect consistency patterns (2-3 runs insufficient, 5+ runs diminishing returns)
- **Computational cost**: 2,400 total predictions (100 cases × 4 runs × 3 models × 2 prompts) manageable namun comprehensive
- **Clinical relevance**: Dalam real-world deployment, consistency across multiple consultations critical untuk patient trust

### 2.2.7 *Clinical Decision Support System* (CDSS) Berbasis AI

*Clinical Decision Support System* (CDSS) adalah sistem yang dirancang untuk membantu tenaga kesehatan dalam pengambilan keputusan klinis dengan menyediakan rekomendasi, peringatan, atau estimasi risiko berbasis data (Peiffer-Smadja et al., 2020). Integrasi model AI ke dalam CDSS memungkinkan sistem memberikan prediksi penyakit kardiovaskular secara otomatis berdasarkan input data pasien (Rajpurkar et al., 2022). Dengan adanya model yang akurat dan konsisten, CDSS dapat digunakan sebagai alat bantu dalam skrining awal, penentuan prioritas pemeriksaan lanjutan, serta perencanaan intervensi preventif (Wang et al., 2024).

Dalam kerangka teori penelitian ini, GPT-4o, Qwen-Plus, dan Gemini-2.0-Flash diposisikan sebagai komponen AI yang berpotensi diintegrasikan ke dalam CDSS untuk prediksi penyakit kardiovaskular. Namun, sebelum clinical deployment, critical questions tentang reproducibility dan consistency harus dijawab (Meskó & Topol, 2023; Ghassemi et al., 2020). Studi ini provides systematic evaluation framework yang dapat inform clinical decision-making tentang:

1. **Model selection criteria**: Choosing LLM based on consistency-accuracy profile
2. **Risk stratification**: Understanding systematic bias patterns (FP vs FN) (Obermeyer et al., 2019)
3. **Deployment readiness**: Assessing whether current LLMs meet clinical reliability standards (Topol, 2019)

## 2.3 Posisi Penelitian dalam Landscape Ilmiah

Penelitian ini represents significant advancement dalam medical AI evaluation dengan mengintegrasikan concepts dari multiple disciplines:

**Dari Computer Science**: Multi-run reproducibility testing protocol yang rigorous untuk stochastic systems, systematic error pattern analysis, comparative evaluation framework untuk heterogeneous LLM architectures.

**Dari Medical Informatics**: Clinical decision support system requirements, diagnostic accuracy metrics (sensitivity/specificity), false positive vs false negative tradeoff analysis dalam cardiovascular risk assessment.

**Dari Statistics**: Stratified sampling via clustering untuk ensure test set representativeness, consistency metrics untuk quantify reproducibility, dissociation analysis antara two independent dimensions (consistency vs accuracy).

Hasil penelitian ini telah dipublikasikan sebagai preprint dalam JAMIA (Journal of the American Medical Informatics Association) dengan DOI: **10.64898/2025.12.08.25341823** (December 2025), menunjukkan novelty dan relevance dari research contribution untuk international scientific community. Preprint tersebut menjadi foundation untuk skripsi ini dengan comprehensive experimental methodology including:

- 2,400 LLM predictions through rigorous multi-run protocol
- Systematic consistency-accuracy relationship analysis
- Comprehensive systematic bias pattern identification framework
- Controlled prompt engineering evaluation experiment
- Multiple statistical validation metrics untuk robust evaluation

Dengan demikian, penelitian ini tidak hanya mengisi research gaps yang identified dalam kajian pustaka, namun juga contributes new methodological framework untuk evaluating reproducibility dan systematic biases dalam LLM-based medical diagnosis systems.
