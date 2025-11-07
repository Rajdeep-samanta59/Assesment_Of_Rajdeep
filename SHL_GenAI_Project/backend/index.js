import express from "express";
import fs from "fs";
import cors from "cors";
import path from "path";
import { fileURLToPath } from 'url';
import pkg from 'natural';
const { TfIdf } = pkg;

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(cors());
app.use(express.json());

// Serve static frontend from project root (one level up)
app.use(express.static(path.join(__dirname, '..')));

let data = [];
let tfidf = null;
let docs = [];

function buildIndex() {
  tfidf = new TfIdf();
  docs = [];
  data.forEach((p) => {
    const text = [p.title || '', p.description || '', (p.skills || []).join(' '), (p.tags || []).join(' ')].join(' ');
    docs.push(text);
    tfidf.addDocument(text);
  });
}

try {
  const raw = fs.readFileSync(path.join(__dirname, '..', 'products.json'), 'utf8');
  data = JSON.parse(raw).products || [];
  buildIndex();
} catch (e) {
  console.warn('products.json not found or invalid. Start server after creating products.json for full functionality.');
}

function recommend(query) {
  query = (query || '').toLowerCase();
  if (!query) return [];

  // Simple weighted scoring: TF-IDF score sum + heuristics
  const terms = query.split(/\W+/).filter(Boolean);

  const scored = data.map((p, i) => {
    let score = 0;

    // heuristic matches
    if ((p.title || '').toLowerCase().includes(query)) score += 3;
    if ((p.description || '').toLowerCase().includes(query)) score += 2;
    (p.skills || []).forEach((s) => {
      if (query.includes(s)) score += 1;
    });
    (p.tags || []).forEach((t) => {
      if (query.includes(t)) score += 0.5;
    });

    // TF-IDF: sum of tfidf weights for each query term in that document
    if (tfidf && terms.length > 0) {
      let tfidfScore = 0;
      terms.forEach((term) => {
        try {
          tfidfScore += tfidf.tfidf(term, i) || 0;
        } catch (e) {
          // ignore
        }
      });
      score += tfidfScore; // combine
    }

    return { ...p, score };
  });

  scored.sort((a, b) => b.score - a.score);
  return scored.filter(s => s.score > 0).slice(0, 10);
}

app.get('/api/products', (req, res) => {
  res.json({ products: data });
});

app.get('/api/recommend', (req, res) => {
  const q = req.query.query || '';
  const result = recommend(q);
  res.json({ query: q, recommendations: result });
});

// fallback to index.html for SPA
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'index.html'));
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
