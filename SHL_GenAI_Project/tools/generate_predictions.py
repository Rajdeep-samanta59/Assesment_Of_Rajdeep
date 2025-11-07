#!/usr/bin/env python3
"""
Generate predictions CSV (`rajdeep_samanta.csv`) from `products.json` using a simple heuristic scorer.

This script does not require the backend to be running. It reads `products.json`, runs a set
of queries (customize inside the script) and writes `rajdeep_samanta.csv` in the project root.

Weights used (simple and deterministic):
- title exact match: +5
- title term match: +2 per term
- description exact match: +3
- description term match: +1 per term
- skill match: +2 per match
- tag match: +0.5 per match

Usage:
  python tools/generate_predictions.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_PATH = ROOT / 'products.json'
OUT_CSV = ROOT / 'rajdeep_samanta.csv'

DEFAULT_QUERIES = [
    "logical reasoning",
    "verbal ability",
    "numerical reasoning",
    "abstract reasoning",
    "situational judgement",
    "problem solving",
    "comprehension",
    "pattern recognition",
    "decision making",
    "vocabulary",
]

def tokenize(text):
    if not text:
        return []
    return [t.lower() for t in re.findall(r"\w+", text)]

def score_product(prod, query_terms, query_raw):
    title = (prod.get('title') or '').lower()
    desc = (prod.get('description') or '').lower()
    skills = [s.lower() for s in prod.get('skills') or []]
    tags = [t.lower() for t in prod.get('tags') or []]

    score = 0.0
    q = query_raw.lower()
    if q and q in title:
        score += 5
    if q and q in desc:
        score += 3

    # term matches
    for term in query_terms:
        if term in title:
            score += 2
        if term in desc:
            score += 1
        for s in skills:
            if term == s or term in s:
                score += 2
        for t in tags:
            if term == t or term in t:
                score += 0.5

    return score

def main():
    if not PRODUCTS_PATH.exists():
        print("products.json not found. Run the converter or place products.json in the project root.")
        return

    data = json.loads(PRODUCTS_PATH.read_text(encoding='utf-8')).get('products', [])

    queries = DEFAULT_QUERIES
    rows = ["query,recommended_ids"]

    for q in queries:
        terms = tokenize(q)
        scored = []
        for p in data:
            s = score_product(p, terms, q)
            scored.append((s, p))
        scored.sort(key=lambda x: x[0], reverse=True)
        # take top 5 with positive score
        top = [p.get('id') for (sc, p) in scored if sc > 0][:5]
        rows.append(f"{q},{';'.join(top)}")

    OUT_CSV.write_text('\n'.join(rows), encoding='utf-8')
    print(f"✅ Wrote predictions to {OUT_CSV} with {len(rows)-1} queries")

if __name__ == '__main__':
    main()
