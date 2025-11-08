# SHL GenAI Recommender — Project Scaffold

This scaffold provides a simple Retrieval-based recommender for SHL assessment catalog.

## 📚 Documentation

- **🚀 [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Complete step-by-step guide for local testing and Render deployment
- **⚡ [QUICK_START.md](QUICK_START.md)** - Quick reference for common tasks
- **✅ [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)** - Checklist for submission requirements

## 📁 Project Structure

- `convert_to_json.py` — Python script to convert `Gen_AI Dataset.xlsx` into `products.json`.
- `products.json` — sample catalog (replace by running converter on the real Excel file).
- `backend/` — Express backend (ES modules).
- `index.html` — Simple frontend UI calling `/api/recommend`.
- `rajdeep_samanta.csv` — sample prediction CSV for submission.
- `report_SHL_GenAI.md` — 2-page draft report (export to PDF for submission).

## 🚀 Quick Start (Local Testing)

### Prerequisites
- Node.js (v18 or higher)
- Python 3.8+ (for data conversion)
- npm (comes with Node.js)

### Step 1: Install Dependencies

```powershell
cd backend
npm install
```

### Step 2: Start Server

```powershell
npm start
```

### Step 3: Open in Browser

http://localhost:8080

### Step 4: Test API

- Web UI: http://localhost:8080
- API Endpoint: http://localhost:8080/api/recommend?query=logical+reasoning
- Health Check: http://localhost:8080/health

## 📦 Deployment to Render

**For detailed deployment instructions, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)**

### Quick Deployment Steps:

1. **Push to GitHub:**
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to https://render.com
   - Create new Web Service
   - Connect GitHub repo
   - Build Command: `npm --prefix SHL_GenAI_Project/backend install`
   - Start Command: `node SHL_GenAI_Project/backend/index.js`
   - Deploy!

## ✅ Submission Requirements

- [ ] Web app URL (Render or Railway)
- [ ] API endpoint: `<URL>/api/recommend?query=logical+reasoning`
- [ ] GitHub repo (public)
- [ ] PDF report (2 pages, exported from `report_SHL_GenAI.md`)
- [ ] CSV file: `firstname_lastname.csv`

**See [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md) for complete checklist.**

## 🧪 Verification

Run the verification script to check your setup:

```powershell
node verify_setup.js
```

## 📝 Generating Submission Files

### Generate PDF Report:
```powershell
# Option 1: Use Python script
pip install reportlab
python tools/export_report_pdf.py

# Option 2: Use online converter
# Go to https://www.markdowntopdf.com/ and upload report_SHL_GenAI.md
```

### Generate CSV Predictions:
```powershell
python tools/generate_predictions.py
# Rename to: your_firstname_your_lastname.csv
```

## 🆘 Need Help?

1. Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions
2. Check [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md) for requirements
3. Verify setup with: `node verify_setup.js`
