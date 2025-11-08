# 🚀 Complete Deployment Guide - SHL GenAI Project

## 📋 Table of Contents
- [Step A: Local Testing](#step-a-local-testing)
- [Step B: Deploy to Render](#step-b-deploy-to-render)
- [Step C: Generate Submission Files](#step-c-generate-submission-files)

---

## STEP A: Local Testing

### Prerequisites Check

First, let's check what you have installed on your computer:

#### 1. Check Node.js Installation
Open PowerShell or Command Prompt and type:
```powershell
node --version
```

**Expected:** Should show something like `v18.x.x` or `v20.x.x`

**If NOT installed:**
- Download from: https://nodejs.org/
- Install the LTS (Long Term Support) version
- Restart your computer after installation
- Run `node --version` again to verify

#### 2. Check npm (Node Package Manager)
```powershell
npm --version
```

**Expected:** Should show something like `9.x.x` or `10.x.x`

**Note:** npm comes with Node.js, so if Node.js is installed, npm should work too.

#### 3. Check Python Installation
```powershell
python --version
```
**OR**
```powershell
python3 --version
```

**Expected:** Should show something like `Python 3.8.x` or higher

**If NOT installed:**
- Download from: https://www.python.org/downloads/
- **IMPORTANT:** During installation, check the box "Add Python to PATH"
- Restart your computer after installation
- Run `python --version` again to verify

---

### Step-by-Step Local Testing

#### Step 1: Navigate to Project Directory

Open PowerShell or Command Prompt and navigate to your project:

```powershell
cd C:\Users\saman\Desktop\Assesment\SHL_GenAI_Project
```

#### Step 2: Verify products.json Exists

```powershell
dir products.json
```

**If it doesn't exist or you need to regenerate it:**

1. Make sure `Gen_AI Dataset.xlsx` is in the parent folder (`C:\Users\saman\Desktop\Assesment\`)
2. Install Python dependencies:
   ```powershell
   pip install pandas openpyxl
   ```
3. Run the converter:
   ```powershell
   python convert_to_json.py "..\Gen_AI Dataset.xlsx"
   ```
   (The `..\` means go up one folder to find the Excel file)

4. Verify it worked:
   ```powershell
   dir products.json
   ```
   You should see the file listed.

#### Step 3: Install Node.js Dependencies

Navigate to the backend folder and install dependencies:

```powershell
cd backend
npm install
```

**What this does:** Downloads all required packages (express, cors, natural) into the `node_modules` folder.

**Expected output:** You should see a lot of text scrolling, ending with something like:
```
added 50 packages in 30s
```

#### Step 4: Start the Server

While still in the `backend` folder, run:

```powershell
npm start
```

**Expected output:**
```
Static files served from: C:\Users\saman\Desktop\Assesment\SHL_GenAI_Project
Products loaded: 5
Server running on port 8080
```

**⚠️ If you see an error:**
- **Port 8080 already in use:** Change the port in `backend/index.js` line 11 to `8081` or `3000`
- **products.json not found:** Go back to Step 2
- **Module not found:** Run `npm install` again

#### Step 5: Test in Browser

1. **Open your web browser** (Chrome, Firefox, Edge, etc.)
2. **Navigate to:** `http://localhost:8080`
3. **You should see:** A simple form with a search box

#### Step 6: Test the Search Functionality

1. In the search box, type: `logical reasoning`
2. Click the **Search** button
3. **Expected:** You should see product cards showing:
   - Title: "Logical Reasoning Test"
   - Description
   - Skills and Tags
   - Score

#### Step 7: Test the API Endpoint Directly

Open a new browser tab and go to:
```
http://localhost:8080/api/recommend?query=logical+reasoning
```

**Expected:** You should see JSON data like:
```json
{
  "query": "logical reasoning",
  "recommendations": [
    {
      "id": "P1",
      "title": "Logical Reasoning Test",
      "description": "A test to assess logical thinking...",
      "skills": ["logical reasoning", "problem solving"],
      "tags": ["reasoning", "inductive"],
      "durationMinutes": 30,
      "score": 8.5
    }
  ]
}
```

#### Step 8: Test Health Endpoint

Navigate to:
```
http://localhost:8080/health
```

**Expected:**
```json
{
  "status": "ok",
  "port": 8080,
  "productsLoaded": 5
}
```

#### Step 9: Test Other Queries

Try these queries in your browser:
- `http://localhost:8080/api/recommend?query=verbal`
- `http://localhost:8080/api/recommend?query=numerical`
- `http://localhost:8080/api/recommend?query=problem+solving`

#### Step 10: Run Tests (Optional)

In a **new PowerShell window**, navigate to the backend folder:

```powershell
cd C:\Users\saman\Desktop\Assesment\SHL_GenAI_Project\backend
npm test
```

**Expected:** You should see test results showing recommendations for different queries.

#### Step 11: Stop the Server

When you're done testing:
- Go back to the PowerShell window where the server is running
- Press `Ctrl + C` to stop the server

---

## STEP B: Deploy to Render

### Prerequisites for Render Deployment

1. **GitHub Account:** You need a free GitHub account
   - Sign up at: https://github.com/signup
   - Verify your email address

2. **Render Account:** You need a free Render account
   - Sign up at: https://render.com/
   - You can sign up with your GitHub account (easiest option)

3. **Git Installation (Optional but Recommended):**
   - Check if Git is installed: `git --version`
   - If not installed: Download from https://git-scm.com/download/win
   - Restart computer after installation

---

### Step-by-Step Render Deployment

#### Phase 1: Prepare Your Code for GitHub

##### Step 1: Initialize Git Repository (if not already done)

Open PowerShell in your project root:
```powershell
cd C:\Users\saman\Desktop\Assesment
git init
```

##### Step 2: Check .gitignore File

Make sure `.gitignore` exists in the root folder and contains:
```
node_modules/
**/node_modules/
npm-debug.log*
.env
.DS_Store
__pycache__/
*.pyc
```

**Note:** We want to commit `products.json` but NOT `node_modules/`

##### Step 3: Add All Files to Git

```powershell
git add .
```

##### Step 4: Commit Your Code

```powershell
git commit -m "Initial commit: SHL GenAI Recommender"
```

**If you see an error about user name/email:**
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
Then run the commit command again.

---

#### Phase 2: Create GitHub Repository

##### Step 1: Go to GitHub

1. Open your browser and go to: https://github.com
2. **Log in** to your account

##### Step 2: Create New Repository

1. Click the **"+"** icon in the top right corner
2. Click **"New repository"**

##### Step 3: Fill Repository Details

- **Repository name:** `shl-genai-recommender` (or any name you like)
- **Description:** `SHL GenAI Assessment - RAG Recommender System`
- **Visibility:** Choose **Public** (Render free tier works with public repos)
- **DO NOT** check "Initialize with README" (we already have files)
- **DO NOT** add .gitignore or license (we already have them)

##### Step 4: Create Repository

Click the green **"Create repository"** button

##### Step 5: Push Your Code to GitHub

GitHub will show you commands. Use these (replace `YOUR_USERNAME` with your actual GitHub username):

```powershell
git remote add origin https://github.com/YOUR_USERNAME/shl-genai-recommender.git
git branch -M main
git push -u origin main
```

**If it asks for credentials:**
- **Username:** Your GitHub username
- **Password:** You need a **Personal Access Token** (NOT your GitHub password)

**To create a Personal Access Token:**
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a name: "Render Deployment"
4. Select scopes: Check `repo` (this gives full repository access)
5. Click "Generate token"
6. **COPY THE TOKEN** (you won't see it again!)
7. Use this token as your password when pushing

**After pushing:** Refresh your GitHub page. You should see all your files!

---

#### Phase 3: Deploy to Render

##### Step 1: Go to Render Dashboard

1. Open: https://render.com/
2. **Log in** (use "Log in with GitHub" for easiest setup)

##### Step 2: Create New Web Service

1. Click the **"New +"** button in the top right
2. Select **"Web Service"**

##### Step 3: Connect Your GitHub Repository

1. Render will show your GitHub repositories
2. **Find and click** on `shl-genai-recommender` (or whatever you named it)
3. Click **"Connect"**

##### Step 4: Configure Service Settings

Render will show a form. Fill it like this:

**Basic Settings:**
- **Name:** `shl-genai-recommender` (or any name)
- **Region:** Choose closest to you (e.g., `Oregon (US West)` or `Frankfurt (EU Central)`)
- **Branch:** `main` (should be selected by default)
- **Root Directory:** Leave **EMPTY** (Render will use the root)

**Build & Deploy:**
- **Runtime:** `Node`
- **Build Command:** 
  ```
  npm --prefix SHL_GenAI_Project/backend install
  ```
  (Copy this EXACTLY, including the path)
  
- **Start Command:**
  ```
  node SHL_GenAI_Project/backend/index.js
  ```
  (Copy this EXACTLY)

**Advanced Settings (Click to expand):**
- **Environment:** `Node`
- **Node Version:** `18` or `20` (Render will auto-detect)
- **Auto-Deploy:** `Yes` (this automatically redeploys when you push to GitHub)

**Environment Variables:**
- You don't need to add any for now. Render will automatically set `PORT`.

##### Step 5: Create Web Service

Click the green **"Create Web Service"** button at the bottom.

##### Step 6: Wait for Deployment

Render will now:
1. **Clone** your repository
2. **Install** dependencies (`npm install`)
3. **Build** your application
4. **Start** your server

**This takes 2-5 minutes.** You'll see logs in real-time.

**Watch for:**
- ✅ Green checkmarks = Success
- ❌ Red X = Error (read the error message)

##### Step 7: Check Deployment Status

When deployment finishes, you'll see:
- **Status:** "Live" (green)
- **URL:** Something like `https://shl-genai-recommender.onrender.com`

**⚠️ Important:** Free tier on Render spins down after 15 minutes of inactivity. First request after spin-down takes 30-60 seconds. This is normal!

##### Step 8: Test Your Deployed Application

1. **Copy the URL** from Render (e.g., `https://shl-genai-recommender.onrender.com`)
2. **Open it in your browser**
3. You should see the same interface as locally!

##### Step 9: Test API Endpoint

Open in browser:
```
https://shl-genai-recommender.onrender.com/api/recommend?query=logical+reasoning
```

**Expected:** Same JSON response as locally!

##### Step 10: Test Health Endpoint

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

---

### Troubleshooting Render Deployment

#### Problem: Build Fails

**Error:** "Cannot find module" or "Module not found"

**Solution:**
1. Check that `package.json` is in `SHL_GenAI_Project/backend/`
2. Check that build command is: `npm --prefix SHL_GenAI_Project/backend install`
3. Check Render logs for specific error

#### Problem: Application Crashes on Start

**Error:** "Application failed to respond"

**Solution:**
1. Check that start command is: `node SHL_GenAI_Project/backend/index.js`
2. Check that `products.json` is committed to GitHub (in `SHL_GenAI_Project/` folder)
3. Check Render logs - look for error messages

#### Problem: 404 Not Found

**Solution:**
1. Make sure `index.html` is in `SHL_GenAI_Project/` folder
2. Check that static file serving path is correct in `index.js`
3. Try accessing `/health` endpoint first

#### Problem: Port Error

**Error:** "Port already in use" or "EADDRINUSE"

**Solution:**
- This shouldn't happen on Render (they set PORT automatically)
- If it does, make sure you're using `process.env.PORT || 8080` in your code (you already are!)

#### Problem: Slow First Load

**Solution:**
- This is normal on Render free tier!
- The app "spins down" after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds to wake up
- Subsequent requests are fast

---

## STEP C: Generate Submission Files

### File 1: Update Report with URLs

1. Open `SHL_GenAI_Project/report_SHL_GenAI.md`
2. Replace placeholders with your actual URLs:
   - API: `https://your-app.onrender.com/api/recommend?query=logical+reasoning`
   - Web UI: `https://your-app.onrender.com`
   - GitHub: `https://github.com/YOUR_USERNAME/shl-genai-recommender`

### File 2: Generate PDF Report

#### Option A: Using Python Script (If you have reportlab)

```powershell
cd C:\Users\saman\Desktop\Assesment\SHL_GenAI_Project
pip install reportlab
python tools/export_report_pdf.py
```

#### Option B: Manual Conversion (Easier)

1. Open `report_SHL_GenAI.md` in VS Code or any markdown editor
2. Install "Markdown PDF" extension in VS Code (if using VS Code)
3. Right-click on the file → "Markdown PDF: Export (pdf)"
4. OR use online converter: https://www.markdowntopdf.com/
5. Upload the markdown file and download PDF

#### Option C: Copy to Google Docs

1. Open the markdown file
2. Copy all content
3. Paste into Google Docs
4. Format as needed (it should mostly work)
5. File → Download → PDF

### File 3: Generate Predictions CSV

#### Step 1: Update CSV with Your Name

The CSV should be named: `firstname_lastname.csv`

If your name is different from "rajdeep_samanta", you need to:

1. Rename the file OR
2. Regenerate it with your name:

```powershell
cd C:\Users\saman\Desktop\Assesment\SHL_GenAI_Project
python tools/generate_predictions.py
```

Then rename the output file:
```powershell
ren rajdeep_samanta.csv your_firstname_your_lastname.csv
```

#### Step 2: Verify CSV Format

Open the CSV file. It should look like:
```csv
query,recommended_ids
logical reasoning,P1;P4
verbal ability,P2
numerical reasoning,P3
...
```

**Format:** `query,recommended_ids` where `recommended_ids` are semicolon-separated (e.g., `P1;P2;P3`)

---

## 📝 Submission Checklist

Before submitting, verify:

- [ ] **Web App URL:** Working and accessible (test it!)
- [ ] **API Endpoint:** Returns JSON correctly (test it!)
- [ ] **GitHub Repo:** Public and contains all code
- [ ] **PDF Report:** 2 pages, includes your approach
- [ ] **CSV File:** Named `firstname_lastname.csv`, contains predictions

---

## 🎉 You're Done!

Your submission should include:
1. ✅ Web App URL: `https://your-app.onrender.com`
2. ✅ API Endpoint: `https://your-app.onrender.com/api/recommend?query=logical+reasoning`
3. ✅ GitHub Repo: `https://github.com/YOUR_USERNAME/shl-genai-recommender`
4. ✅ PDF Report: `report_SHL_GenAI.pdf`
5. ✅ CSV File: `your_firstname_your_lastname.csv`

---

## 💡 Pro Tips

1. **Test everything** before submitting - use the URLs you'll provide
2. **Keep Render app running** - free tier allows unlimited deployments
3. **Monitor Render logs** - if something breaks, check the logs
4. **GitHub commits** - make sure your latest code is pushed
5. **Backup your files** - keep local copies of PDF and CSV

---

## 🆘 Need Help?

If you encounter issues:
1. Check the error messages carefully
2. Review Render deployment logs
3. Test locally first to isolate problems
4. Verify all files are committed to GitHub
5. Make sure `products.json` is in the repository

Good luck with your submission! 🚀

