import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createRecommender } from '../recommender.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const DATA_PATH = path.join(__dirname, '..', '..', 'products.json');
function loadProducts() {
  const raw = fs.readFileSync(DATA_PATH, 'utf8');
  return JSON.parse(raw).products || [];
}

function runSmokeTests() {
  const products = loadProducts();
  if (!products || products.length === 0) {
    console.error('No products found in products.json — run converter first');
    process.exit(1);
  }

  const r = createRecommender(products);
  const queries = ['logical reasoning', 'verbal ability', 'numerical'];
  queries.forEach(q => {
    const recs = r.recommend(q);
    console.log('\nQuery:', q);
    console.log('Top results:', recs.slice(0,5).map(x => ({id:x.id, title:x.title, score: x.score}))); 
  });
  console.log('\nSmoke tests completed');
}

runSmokeTests();
