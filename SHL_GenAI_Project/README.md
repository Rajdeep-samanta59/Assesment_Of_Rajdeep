# SHL GenAI Recommender — Project Scaffold

This scaffold provides a simple Retrieval-based recommender for SHL assessment catalog.

Structure

- `convert_to_json.py` — Python script to convert `Gen_AI Dataset.xlsx` into `products.json`.
- `products.json` — sample catalog (replace by running converter on the real Excel file).
- `backend/` — Express backend (ES modules).
- `index.html` — Simple frontend UI calling `/api/recommend`.
- `rajdeep_samanta.csv` — sample prediction CSV for submission.
- `report_SHL_GenAI.md` — 2-page draft report (export to PDF for submission).

Quick start (Windows PowerShell)

1) Ensure Python and Node.js are installed.

2) Install Python deps and convert the real Excel (place `Gen_AI Dataset.xlsx` next to `convert_to_json.py`):

```powershell
pip install pandas openpyxl
python convert_to_json.py "Gen_AI Dataset.xlsx"
```

This will produce `products.json` in the same folder.

3) Start backend server

```powershell
cd backend
npm install
npm start
```

4) Open in browser:

http://localhost:8080

Notes for deployment (Render)

- Create a GitHub repo and push the project.
- On Render: Create a new Web Service, connect repo, set build command `npm install` and start command `node backend/index.js`.
- Ensure `products.json` is in the repo (or create a step to generate it during build using the Python script if you want to include Excel in the repo).

Submission checklist

- Web app URL (Render or Railway)
- API endpoint: `<URL>/api/recommend?query=logical+reasoning`
- GitHub repo (public)
- Upload `report_SHL_GenAI.pdf` (exported from `report_SHL_GenAI.md`)
- Upload `rajdeep_samanta.csv`

If you want, I can:
- Convert the Markdown report into a PDF for you (requires a local tool or allowing me to run commands),
- Help push to GitHub and create a Render deployment (if you give repo details),
- Improve the ranking algorithm (TF-IDF or embeddings).
