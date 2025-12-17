# 📤 Panduan Upload ke GitHub Repository

## Step 1: Buat Repository di GitHub (5 menit)

### 1.1 Login ke GitHub
1. Buka https://github.com
2. Login dengan akun Anda
3. Klik tombol **"+"** di pojok kanan atas → **"New repository"**

### 1.2 Konfigurasi Repository
- **Repository name:** `heart-disease-llm-research`
- **Description:** `High Consistency, Limited Accuracy: Evaluating LLMs for Binary Medical Diagnosis`
- **Visibility:** ✅ **Public** (required untuk data availability statement)
- **Initialize:**
  - ❌ **Jangan** centang "Add a README file" (kita sudah punya)
  - ❌ **Jangan** centang ".gitignore" (kita sudah punya)
  - ❌ **Jangan** centang "Choose a license" (kita sudah punya)
- Klik **"Create repository"**

### 1.3 Copy Repository URL
Setelah repository dibuat, Anda akan melihat URL seperti:
```
https://github.com/YOUR_USERNAME/heart-disease-llm-research.git
```
**SIMPAN URL INI!** Akan digunakan di DATA_AVAILABILITY.md

---

## Step 2: Persiapan Lokal (10 menit)

### 2.1 Cek File yang Akan Diupload
Pastikan file-file ini ada dan siap:

```bash
cd e:\project\Riset\heart-disease

# Cek struktur
ls
```

Harus ada:
- ✅ `README.md` (baru dibuat, lengkap dengan badges)
- ✅ `.gitignore` (sudah diupdate)
- ✅ `LICENSE` (MIT License)
- ✅ `requirements.txt`
- ✅ Folder: `data/`, `clustering/`, `sampling/`, `llm_testing/`, `evaluation/`, `scripts/`, `results/`, `manuscript/`, `config/`

### 2.2 PENTING: Protect API Keys!
Sebelum upload, pastikan API keys TIDAK akan terupload:

```bash
# Cek apakah config.yaml ada (jangan sampai terupload!)
cat config/config.yaml
```

Jika ada API keys di `config.yaml`, HAPUS atau ganti dengan placeholder:

```yaml
api_keys:
  openai: "your-openai-api-key-here"
  google: "your-google-api-key-here"
  qwen: "your-qwen-api-key-here"
```

**Catatan:** `.gitignore` sudah dikonfigurasi untuk ignore file-file sensitif:
- `config/config.yaml`
- `load_env.ps1`
- `.env`
- `*.db` (database checkpoint)

---

## Step 3: Upload via Git (15 menit)

### 3.1 Initialize Git Repository
```bash
cd e:\project\Riset\heart-disease

# Initialize git (jika belum)
git init

# Add semua file (kecuali yang di .gitignore)
git add .

# Cek apa saja yang akan diupload
git status
```

**❗ PENTING:** Pastikan `config.yaml` dengan API keys TIDAK muncul di list!

### 3.2 First Commit
```bash
git commit -m "Initial commit: Complete LLM heart disease diagnosis research"
```

### 3.3 Connect ke GitHub Repository
Ganti `YOUR_USERNAME` dengan username GitHub Anda:

```bash
git remote add origin https://github.com/YOUR_USERNAME/heart-disease-llm-research.git

# Cek koneksi
git remote -v
```

### 3.4 Push ke GitHub
```bash
# Rename branch ke 'main' (GitHub default)
git branch -M main

# Push semua file
git push -u origin main
```

**Jika diminta login:**
- Username: `YOUR_GITHUB_USERNAME`
- Password: **Personal Access Token** (bukan password biasa!)

#### Cara Buat Personal Access Token:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. Note: "Heart disease research upload"
4. Expiration: 90 days (atau custom)
5. Scopes: Centang **repo** (full control)
6. Generate token → COPY & SIMPAN!

---

## Step 4: Alternatif - Upload via GitHub Web Interface (Lebih Mudah!)

Jika Git terasa rumit, gunakan web interface:

### 4.1 Upload Satu Per Satu (Folder Kecil)
1. Buka repository GitHub Anda
2. Klik **"Add file"** → **"Upload files"**
3. Drag & drop atau pilih file:
   - `README.md`
   - `.gitignore`
   - `LICENSE`
   - `requirements.txt`
4. Commit: "Add essential files"
5. Ulangi untuk folder lain (data, scripts, results, etc.)

### 4.2 Upload ZIP (Seluruh Project)

**BAHAYA! Jangan lakukan ini jika ada API keys!**

Lebih aman: Upload manual folder demi folder.

---

## Step 5: Verifikasi Upload (3 menit)

### 5.1 Cek Repository
1. Buka https://github.com/YOUR_USERNAME/heart-disease-llm-research
2. Pastikan ada:
   - ✅ README.md ter-render dengan badges
   - ✅ Folder structure lengkap
   - ✅ LICENSE terlihat (akan ada badge license di GitHub)
   - ✅ Data ada di `data/heart.csv`
   - ✅ Results ada di `results/`

### 5.2 Cek TIDAK Ada File Sensitif
Gunakan search GitHub:
```
config.yaml
load_env.ps1
.env
```
Pastikan **TIDAK ADA** hasil!

### 5.3 Test Clone
Coba clone dari lokasi berbeda:
```bash
cd C:\temp
git clone https://github.com/YOUR_USERNAME/heart-disease-llm-research.git
cd heart-disease-llm-research
ls
```

Jika semua file ada → **SUCCESS!** ✅

---

## Step 6: Update DATA_AVAILABILITY.md (2 menit)

Setelah repository berhasil dibuat, update DATA_AVAILABILITY.md:

```markdown
### Code Repository

All analysis code, configuration files, and documentation are available at:
https://github.com/YOUR_USERNAME/heart-disease-llm-research
```

Ganti `YOUR_USERNAME` dengan username GitHub Anda yang sebenarnya.

---

## Step 7: Tambahkan DOI Badge (Opsional, 5 menit)

### 7.1 Zenodo Integration
Untuk citable research repository:

1. Login https://zenodo.org dengan GitHub account
2. Enable integration untuk repository `heart-disease-llm-research`
3. Create new release di GitHub:
   - Tag: `v1.0.0`
   - Title: "Initial Release - medRxiv Preprint"
   - Description: Link ke preprint
4. Zenodo akan auto-generate DOI
5. Tambahkan badge ke README.md

---

## 🎯 Checklist Final

- [ ] Repository dibuat (public)
- [ ] README.md ter-render dengan baik
- [ ] LICENSE terlihat (MIT)
- [ ] .gitignore berfungsi (no API keys uploaded)
- [ ] Semua folder ter-upload (data, scripts, results, manuscript)
- [ ] Repository URL dicopy
- [ ] DATA_AVAILABILITY.md sudah diupdate dengan URL
- [ ] Repository accessible (coba buka di browser incognito)

---

## 🐛 Troubleshooting

### "Permission denied (publickey)"
**Solusi:** Gunakan Personal Access Token atau setup SSH key

### "Repository too large"
**Solusi:** 
```bash
# Cek ukuran
du -sh .

# Jika >1GB, pertimbangkan:
# 1. Hapus file besar dari results/
# 2. Gunakan Git LFS untuk file >100MB
# 3. Upload results/ secara terpisah (Zenodo/Figshare)
```

### "API key leaked!"
**BAHAYA! Harus segera:**
1. Revoke API key di provider (OpenAI/Google/Qwen)
2. Generate key baru
3. Hapus commit history:
```bash
# Nuclear option (rewrites history)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch config/config.yaml" \
  --prune-empty --tag-name-filter cat -- --all
git push origin --force --all
```

---

## 📞 Need Help?

**Corresponding Author:** Syaiful Bachri Mustamin  
**Email:** syaifulbachri@mail.ugm.ac.id

---

**Setelah repository dibuat, lanjut ke:**
- Document Conversion (Markdown → Word/PDF)
- Final manuscript review
- Submission to JAMIA
