import pkg from 'natural';
const { TfIdf } = pkg;

function buildTfidf(data) {
  const tfidf = new TfIdf();
  const docs = [];
  data.forEach((p) => {
    const text = [p.title || '', p.description || '', (p.skills || []).join(' '), (p.tags || []).join(' ')].join(' ');
    docs.push(text);
    tfidf.addDocument(text);
  });
  return { tfidf, docs };
}

export function createRecommender(data) {
  const { tfidf } = buildTfidf(data || []);

  function recommend(query) {
    query = (query || '').toLowerCase();
    if (!query) return [];
    const terms = query.split(/\W+/).filter(Boolean);

    const scored = data.map((p, i) => {
      let score = 0;
      if ((p.title || '').toLowerCase().includes(query)) score += 3;
      if ((p.description || '').toLowerCase().includes(query)) score += 2;
      (p.skills || []).forEach((s) => {
        if (query.includes(s)) score += 1;
      });
      (p.tags || []).forEach((t) => {
        if (query.includes(t)) score += 0.5;
      });

      if (tfidf && terms.length > 0) {
        let tfidfScore = 0;
        terms.forEach((term) => {
          try {
            tfidfScore += tfidf.tfidf(term, i) || 0;
          } catch (e) {
            // ignore
          }
        });
        score += tfidfScore;
      }
      return { ...p, score };
    });

    scored.sort((a, b) => b.score - a.score);
    return scored.filter(s => s.score > 0).slice(0, 10);
  }

  return { recommend };
}
