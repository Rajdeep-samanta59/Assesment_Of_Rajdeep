# ⚡ Quick Start Guide - SHL GenAI Project

## 🏃 Local Testing (5 Minutes)

### 1. Check Prerequisites
```powershell
node --version    # Should show v18+ or v20+
npm --version     # Should show version number
python --version  # Should show Python 3.8+
```

### 2. Install Dependencies
```powershell
cd C:\Users\saman\Desktop\Assesment\SHL_GenAI_Project\backend
npm install
```

### 3. Start Server
```powershell
npm start
```

### 4. Test in Browser
- Open: http://localhost:8080
- Test API: http://localhost:8080/api/recommend?query=logical+reasoning
- Test Health: http://localhost:8080/health

---

## 🚀 Deploy to Render (15 Minutes)

### 1. Push to GitHub
```powershell
cd C:\Users\saman\Desktop\Assesment
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

### 2. Deploy on Render
1. Go to: https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repo
4. Settings:
   - **Build Command:** `npm --prefix SHL_GenAI_Project/backend install`
   - **Start Command:** `node SHL_GenAI_Project/backend/index.js`
5. Click "Create Web Service"
6. Wait 2-5 minutes
7. Copy your URL!

### 3. Test Deployment
- Open your Render URL in browser
- Test API: `https://your-app.onrender.com/api/recommend?query=logical+reasoning`

---

## 📦 Generate Submission Files

### PDF Report
```powershell
# Option 1: Use Python script
python tools/export_report_pdf.py

# Option 2: Use online converter
# Go to: https://www.markdowntopdf.com/
# Upload: report_SHL_GenAI.md
```

### CSV Predictions
```powershell
python tools/generate_predictions.py
# Rename to: your_firstname_your_lastname.csv
```

---

## ✅ Submission Checklist

- [ ] Web App URL (Render)
- [ ] API Endpoint URL
- [ ] GitHub Repo URL (Public)
- [ ] PDF Report (2 pages)
- [ ] CSV File (firstname_lastname.csv)

---

## 🔗 Your URLs (Fill These In)

- **Web App:** `https://your-app.onrender.com`
- **API Endpoint:** `https://your-app.onrender.com/api/recommend?query=logical+reasoning`
- **GitHub Repo:** `https://github.com/YOUR_USERNAME/REPO_NAME`

---

For detailed instructions, see: `DEPLOYMENT_GUIDE.md`

