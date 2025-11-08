# ✅ Submission Checklist - SHL GenAI Assessment

Use this checklist to ensure you have everything ready for submission.

---

## 📋 Required Submissions

### 1. Web App URL ✅
- [ ] Deployed on Render (or similar platform)
- [ ] URL is accessible and working
- [ ] Tested in browser - can see the search interface
- [ ] URL: `_________________________________________`

### 2. API Endpoint ✅
- [ ] API endpoint is working
- [ ] Returns JSON format
- [ ] Tested with query parameter
- [ ] Example URL: `_________________________________________`
- [ ] Test query: `?query=logical+reasoning` works correctly

### 3. GitHub Repository ✅
- [ ] Repository is **PUBLIC**
- [ ] Contains all code files
- [ ] Contains `products.json`
- [ ] Contains `README.md`
- [ ] Repository URL: `_________________________________________`

### 4. PDF Report (2 pages) ✅
- [ ] Generated from `report_SHL_GenAI.md`
- [ ] Updated with actual URLs (not placeholders)
- [ ] Contains your approach and solution
- [ ] Exactly 2 pages
- [ ] File name: `report_SHL_GenAI.pdf`

### 5. CSV Predictions ✅
- [ ] Generated using `tools/generate_predictions.py`
- [ ] Named: `firstname_lastname.csv` (replace with YOUR name)
- [ ] Contains query and recommended_ids columns
- [ ] Format: `query,recommended_ids` (ids semicolon-separated)

---

## 🧪 Pre-Submission Testing

### Local Testing
- [ ] Server starts without errors
- [ ] Web UI loads at `http://localhost:8080`
- [ ] API endpoint works: `/api/recommend?query=test`
- [ ] Health check works: `/health`
- [ ] Multiple queries tested and return results

### Deployment Testing
- [ ] Web app loads on Render URL
- [ ] API endpoint works on Render URL
- [ ] Health check works on Render URL
- [ ] Tested with different queries
- [ ] No errors in Render logs

### Code Verification
- [ ] All files committed to GitHub
- [ ] `products.json` is in repository
- [ ] No sensitive data (API keys, passwords) in code
- [ ] README is clear and helpful

---

## 📝 File Checklist

### Project Files (Should be in GitHub)
- [ ] `backend/index.js`
- [ ] `backend/recommender.js`
- [ ] `backend/package.json`
- [ ] `products.json`
- [ ] `index.html`
- [ ] `convert_to_json.py`
- [ ] `README.md`
- [ ] `report_SHL_GenAI.md`

### Deployment Files
- [ ] `render.yaml` (optional, but good to have)
- [ ] `Procfile` (optional, but good to have)
- [ ] `Dockerfile` (optional, but good to have)
- [ ] `.gitignore` (should exclude node_modules)

### Submission Files (Not in GitHub, but submit separately)
- [ ] `report_SHL_GenAI.pdf`
- [ ] `firstname_lastname.csv`

---

## 🔍 Final Verification

### Before Submitting, Verify:

1. **Web App Works:**
   - Open your Render URL
   - Type a query (e.g., "logical reasoning")
   - See results appear

2. **API Works:**
   - Open: `https://your-app.onrender.com/api/recommend?query=logical+reasoning`
   - See JSON response with recommendations

3. **GitHub Repo:**
   - Open your GitHub repo URL
   - Verify all files are there
   - Check that it's public

4. **PDF Report:**
   - Open the PDF
   - Verify URLs are correct (not placeholders)
   - Check it's 2 pages

5. **CSV File:**
   - Open the CSV file
   - Verify format is correct
   - Check it has your name in filename

---

## 📤 Submission Information

Fill this out and keep it handy:

```
Web App URL: 
_________________________________________

API Endpoint: 
_________________________________________

GitHub Repo: 
_________________________________________

PDF Report: 
[Attach: report_SHL_GenAI.pdf]

CSV File: 
[Attach: firstname_lastname.csv]
```

---

## 🎯 Quick Test Commands

### Test Locally
```powershell
cd backend
npm start
# Open: http://localhost:8080
```

### Test API
```
http://localhost:8080/api/recommend?query=logical+reasoning
http://localhost:8080/health
```

### Generate CSV
```powershell
python tools/generate_predictions.py
# Rename to: your_firstname_your_lastname.csv
```

---

## ✅ Ready to Submit?

- [ ] All checkboxes above are checked
- [ ] All URLs are working
- [ ] All files are ready
- [ ] PDF is 2 pages with correct URLs
- [ ] CSV has correct format and filename
- [ ] GitHub repo is public and complete

**You're ready to submit! 🚀**

---

## 🆘 Last Minute Issues?

### Web App Not Working?
1. Check Render logs
2. Verify build command is correct
3. Verify start command is correct
4. Check that products.json is in repo

### API Not Returning Results?
1. Check that products.json exists
2. Check Render logs for errors
3. Test locally first

### GitHub Repo Issues?
1. Make sure repo is public
2. Verify all files are committed
3. Check that products.json is included

---

Good luck with your submission! 🎉

