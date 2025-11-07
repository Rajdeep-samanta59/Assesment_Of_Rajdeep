import express from "express";
import fs from "fs";
import cors from "cors";
import path from "path";
import { fileURLToPath } from 'url';
import { createRecommender } from './recommender.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(cors());
app.use(express.json());

// Serve static frontend from project root (one level up)
app.use(express.static(path.join(__dirname, '..')));

let data = [];
let recommender = null;

try {
  const raw = fs.readFileSync(path.join(__dirname, '..', 'products.json'), 'utf8');
  data = JSON.parse(raw).products || [];
  if (data.length > 0) recommender = createRecommender(data);
} catch (e) {
  console.warn('products.json not found or invalid. Start server after creating products.json for full functionality.');
}

app.get('/api/products', (req, res) => {
  res.json({ products: data });
});

app.get('/api/recommend', (req, res) => {
  const q = req.query.query || '';
  const result = recommender ? recommender.recommend(q) : [];
  res.json({ query: q, recommendations: result });
});

// fallback to index.html for SPA
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'index.html'));
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
