# 🚀 DEPLOYMENT ONLY - Step by Step Guide

## ✅ What I Verified (Everything is Ready!)

- ✅ All code files are correct
- ✅ `products.json` exists with 5 products
- ✅ All dependencies are in `package.json`
- ✅ `render.yaml` is configured correctly
- ✅ Server code is ready for deployment
- ✅ Frontend HTML is ready
- ✅ All files are in correct locations

**You're 100% ready to deploy!** 🎉

---

## 📋 DEPLOYMENT STEPS (Follow These Exactly)

### STEP 1: Push Code to GitHub (5 minutes)

#### 1.1: Open PowerShell in Project Root
```powershell
cd C:\Users\saman\Desktop\Assesment
```

#### 1.2: Initialize Git (if not already done)
```powershell
git init
```

#### 1.3: Add All Files
```powershell
git add .
```

#### 1.4: Commit
```powershell
git commit -m "SHL GenAI Recommender - Ready for deployment"
```

**If you see an error about user name/email, run these first:**
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### 1.5: Create GitHub Repository
1. Go to: https://github.com
2. Click **"+"** → **"New repository"**
3. Repository name: `shl-genai-recommender` (or any name)
4. Make it **PUBLIC**
5. **DO NOT** check "Initialize with README"
6. Click **"Create repository"**

#### 1.6: Push to GitHub
**Replace `YOUR_USERNAME` with your actual GitHub username:**

```powershell
git remote add origin https://github.com/YOUR_USERNAME/shl-genai-recommender.git
git branch -M main
git push -u origin main
```

**When it asks for password:**
- **Username:** Your GitHub username
- **Password:** You need a **Personal Access Token** (NOT your password)

**To create Personal Access Token:**
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Name: "Render Deployment"
4. Check `repo` scope
5. Click "Generate token"
6. **COPY THE TOKEN** (you won't see it again!)
7. Use this token as password

**After pushing:** Refresh GitHub page. You should see all your files!

---

### STEP 2: Deploy on Render (10 minutes)

#### 2.1: Create Render Account
1. Go to: https://render.com
2. Click **"Get Started for Free"**
3. Choose **"Log in with GitHub"** (easiest!)

#### 2.2: Create New Web Service
1. Click **"New +"** button (top right)
2. Select **"Web Service"**

#### 2.3: Connect GitHub Repository
1. Render will show your GitHub repositories
2. Find and click: **`shl-genai-recommender`** (or your repo name)
3. Click **"Connect"**

#### 2.4: Configure Service Settings

**Fill in these EXACT values:**

**Basic Settings:**
- **Name:** `shl-genai-recommender` (or any name you like)
- **Region:** Choose closest to you (e.g., `Oregon (US West)`)
- **Branch:** `main` (should be auto-selected)
- **Root Directory:** Leave **EMPTY** (don't change this!)

**Build & Deploy:**
- **Runtime:** `Node` (should be auto-selected)
- **Build Command:** 
  ```
  npm --prefix SHL_GenAI_Project/backend install
  ```
  (Copy this EXACTLY - including the path)
  
- **Start Command:**
  ```
  node SHL_GenAI_Project/backend/index.js
  ```
  (Copy this EXACTLY)

**Environment:**
- **Node Version:** `18` or `20` (Render will auto-detect, but you can set it)
- **Auto-Deploy:** `Yes` (recommended)

**Environment Variables:**
- **Don't add any!** Render will automatically set `PORT`.

#### 2.5: Create and Deploy
1. Scroll down
2. Click green **"Create Web Service"** button
3. Wait 2-5 minutes for deployment

**Watch the logs:**
- You'll see: "Cloning repository..."
- Then: "Installing dependencies..."
- Then: "Building..."
- Finally: "Your service is live!"

#### 2.6: Get Your URL
When deployment finishes:
- You'll see: **"Live"** status (green)
- Your URL will be: `https://shl-genai-recommender.onrender.com` (or similar)
- **Copy this URL!** 📋

---

### STEP 3: Test Your Deployment (2 minutes)

#### 3.1: Test Web App
1. Open your Render URL in browser
2. You should see the search interface
3. Type "logical reasoning" and click Search
4. You should see results!

#### 3.2: Test API Endpoint
Open in browser (replace with your URL):
```
https://shl-genai-recommender.onrender.com/api/recommend?query=logical+reasoning
```

**Expected:** JSON response with recommendations

#### 3.3: Test Health Endpoint
```
https://shl-genai-recommender.onrender.com/health
```

**Expected:**
```json
{
  "status": "ok",
  "port": 10000,
  "productsLoaded": 5
}
```

#### 3.4: Test Other Queries
Try these:
- `?query=verbal`
- `?query=numerical`
- `?query=problem+solving`

---

### STEP 4: Prepare Submission Files (5 minutes)

#### 4.1: Update Report with Your URLs
1. Open: `SHL_GenAI_Project/report_SHL_GenAI.md`
2. Find the "Links" section (near the end)
3. Replace placeholders:
   - API: `https://your-app.onrender.com/api/recommend?query=logical+reasoning`
   - Web UI: `https://your-app.onrender.com`
   - GitHub: `https://github.com/YOUR_USERNAME/shl-genai-recommender`

#### 4.2: Generate PDF Report
**Option A: Online (Easiest)**
1. Go to: https://www.markdowntopdf.com/
2. Upload: `report_SHL_GenAI.md`
3. Download PDF
4. Save as: `report_SHL_GenAI.pdf`

**Option B: Using Python**
```powershell
cd SHL_GenAI_Project
pip install reportlab
python tools/export_report_pdf.py
```

#### 4.3: Generate/Update CSV File
```powershell
cd SHL_GenAI_Project
python tools/generate_predictions.py
```

**Rename to your name:**
```powershell
ren rajdeep_samanta.csv your_firstname_your_lastname.csv
```

---

## ✅ FINAL CHECKLIST

Before submitting, verify:

- [ ] **Web App URL:** Working and accessible
  - URL: `_________________________________________`

- [ ] **API Endpoint:** Returns JSON correctly
  - URL: `_________________________________________`

- [ ] **GitHub Repo:** Public and contains all code
  - URL: `_________________________________________`

- [ ] **PDF Report:** 2 pages with correct URLs
  - File: `report_SHL_GenAI.pdf`

- [ ] **CSV File:** Named correctly
  - File: `your_firstname_your_lastname.csv`

---

## 🎯 SUBMISSION INFORMATION

Fill this out for the form:

```
Web App URL: 
https://your-app.onrender.com

API Endpoint: 
https://your-app.onrender.com/api/recommend?query=logical+reasoning

GitHub Repo: 
https://github.com/YOUR_USERNAME/shl-genai-recommender

PDF Report: 
[Attach: report_SHL_GenAI.pdf]

CSV File: 
[Attach: your_firstname_your_lastname.csv]
```

---

## 🆘 TROUBLESHOOTING

### Problem: Build Fails on Render
**Solution:**
- Check build command is: `npm --prefix SHL_GenAI_Project/backend install`
- Check start command is: `node SHL_GenAI_Project/backend/index.js`
- Check Render logs for specific error

### Problem: App Crashes on Start
**Solution:**
- Check that `products.json` is in GitHub repo
- Check Render logs for errors
- Verify file paths are correct

### Problem: 404 Not Found
**Solution:**
- Make sure `index.html` is in `SHL_GenAI_Project/` folder
- Check that static file serving is working
- Try `/health` endpoint first

### Problem: Slow First Load
**Solution:**
- This is NORMAL on Render free tier!
- App "spins down" after 15 minutes of inactivity
- First request takes 30-60 seconds to wake up
- Subsequent requests are fast

### Problem: Git Push Fails
**Solution:**
- Make sure you created Personal Access Token
- Use token as password, not GitHub password
- Check repository name is correct

---

## 🎉 YOU'RE DONE!

Once you complete these steps, you'll have:
- ✅ Working web app on Render
- ✅ Working API endpoint
- ✅ Public GitHub repository
- ✅ PDF report ready
- ✅ CSV predictions ready

**You're ready to submit!** 🚀

---

## 📞 Quick Reference

**Your URLs (fill these in after deployment):**
- Web App: `https://your-app.onrender.com`
- API: `https://your-app.onrender.com/api/recommend?query=logical+reasoning`
- GitHub: `https://github.com/YOUR_USERNAME/shl-genai-recommender`

**Important Commands:**
```powershell
# Push to GitHub
git add .
git commit -m "Initial commit"
git push -u origin main

# Generate CSV
python tools/generate_predictions.py
```

**Render Settings:**
- Build: `npm --prefix SHL_GenAI_Project/backend install`
- Start: `node SHL_GenAI_Project/backend/index.js`

Good luck! 🎯

