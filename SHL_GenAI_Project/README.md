# 🎯 SHL GenAI Recommender System

<div align="center">

![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**An intelligent recommendation system for SHL assessment products using TF-IDF and natural language processing**

[🌐 Live Demo](https://assesment-of-rajdeep.onrender.com) • [📖 API Documentation](#api-endpoints) • [🚀 Deployment](#deployment)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Algorithm](#algorithm)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **SHL GenAI Recommender System** is a Retrieval-Augmented Generation (RAG) style recommendation engine that intelligently matches user queries with relevant assessment products from the SHL catalog. Built with Node.js and Express, it leverages TF-IDF (Term Frequency-Inverse Document Frequency) and multi-factor scoring to provide accurate, ranked recommendations.

### Key Highlights

- 🔍 **Intelligent Search**: Uses TF-IDF algorithm for semantic text matching
- ⚡ **Fast Performance**: In-memory processing for instant recommendations
- 🎨 **User-Friendly UI**: Clean, responsive web interface
- 🔌 **RESTful API**: Well-documented API endpoints for integration
- 📊 **Multi-Factor Scoring**: Combines title, description, skills, and tags matching
- 🚀 **Production Ready**: Deployed on Render with health checks

---

## ✨ Features

- **Semantic Search**: Advanced TF-IDF algorithm for intelligent text matching
- **Multi-Factor Scoring**: Combines multiple signals (title, description, skills, tags) for accurate ranking
- **RESTful API**: Clean, well-documented API endpoints
- **Real-time Recommendations**: Instant results with in-memory processing
- **Web Interface**: Interactive UI for testing and demonstration
- **Health Monitoring**: Built-in health check endpoint for deployment monitoring
- **Data Conversion**: Python script to convert Excel data to JSON format
- **Scalable Architecture**: Designed to handle large product catalogs

---

## 🛠️ Tech Stack

### Backend
- **Node.js** - Runtime environment
- **Express.js** - Web framework
- **Natural** - NLP library for TF-IDF
- **CORS** - Cross-origin resource sharing

### Frontend
- **HTML5** - Structure
- **JavaScript (Vanilla)** - Interactivity
- **CSS3** - Styling

### Data Processing
- **Python 3** - Data conversion scripts
- **Pandas** - Data manipulation
- **OpenPyXL** - Excel file handling

### Deployment
- **Render** - Cloud hosting platform
- **Docker** - Containerization (optional)
- **Git** - Version control

---

## 🏗️ Architecture

```
┌─────────────┐
│   Client    │
│  (Browser)  │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  Express Server │
│  (Node.js)      │
└──────┬──────────┘
       │
       ├──► Static Files (HTML/CSS/JS)
       │
       ├──► API Routes
       │    ├── /api/recommend
       │    ├── /api/products
       │    └── /health
       │
       ▼
┌─────────────────┐
│  Recommender    │
│  Engine         │
└──────┬──────────┘
       │
       ├──► TF-IDF Algorithm
       ├──► Keyword Matching
       └──► Multi-Factor Scoring
       │
       ▼
┌─────────────────┐
│  Products Data  │
│  (JSON)         │
└─────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v18 or higher)
- **npm** (comes with Node.js)
- **Python** (3.8 or higher) - for data conversion
- **Git** - for version control

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rajdeep-samanta59/Assesment_Of_Rajdeep.git
   cd Assesment_Of_Rajdeep/SHL_GenAI_Project
   ```

2. **Install Node.js dependencies**
   ```bash
   cd backend
   npm install
   ```

3. **Convert Excel data to JSON** (if needed)
   ```bash
   pip install pandas openpyxl
   python convert_to_json.py "../Gen_AI Dataset.xlsx"
   ```

4. **Start the server**
   ```bash
   npm start
   ```

5. **Open in browser**
   ```
   http://localhost:8080
   ```

---

## 📡 API Endpoints

### 1. Get Recommendations

**Endpoint:** `GET /api/recommend`

**Query Parameters:**
- `query` (required): Search query string

**Example Request:**
```bash
curl "https://assesment-of-rajdeep.onrender.com/api/recommend?query=logical+reasoning"
```

**Example Response:**
```json
{
  "query": "logical reasoning",
  "recommendations": [
    {
      "id": "P1",
      "title": "Logical Reasoning Test",
      "description": "A test to assess logical thinking and problem solving using patterns and sequences.",
      "skills": ["logical reasoning", "problem solving"],
      "tags": ["reasoning", "inductive"],
      "durationMinutes": 30,
      "score": 8.5
    }
  ]
}
```

### 2. Get All Products

**Endpoint:** `GET /api/products`

**Example Request:**
```bash
curl "https://assesment-of-rajdeep.onrender.com/api/products"
```

**Example Response:**
```json
{
  "products": [
    {
      "id": "P1",
      "title": "Logical Reasoning Test",
      "description": "...",
      "skills": [...],
      "tags": [...],
      "durationMinutes": 30
    }
  ]
}
```

### 3. Health Check

**Endpoint:** `GET /health`

**Example Request:**
```bash
curl "https://assesment-of-rajdeep.onrender.com/health"
```

**Example Response:**
```json
{
  "status": "ok",
  "port": 10000,
  "productsLoaded": 5
}
```

---

## 📁 Project Structure

```
SHL_GenAI_Project/
├── backend/
│   ├── index.js              # Express server
│   ├── recommender.js        # Recommendation engine
│   ├── package.json          # Dependencies
│   └── node_modules/         # Installed packages
├── tools/
│   ├── convert_to_json.py    # Excel to JSON converter
│   ├── export_report_pdf.py  # PDF report generator
│   └── generate_predictions.py # CSV predictions generator
├── index.html                # Frontend UI
├── products.json             # Product catalog
├── convert_to_json.py        # Data converter
├── render.yaml               # Render configuration
├── Procfile                  # Process file
├── Dockerfile                # Docker configuration
└── README.md                 # This file
```

---

## 🧮 Algorithm

### Recommendation Scoring

The system uses a **multi-factor scoring algorithm** that combines:

1. **Title Match** (Weight: 3.0)
   - Exact match in product title

2. **Description Match** (Weight: 2.0)
   - Match in product description

3. **Skills Match** (Weight: 1.0)
   - Match in product skills list

4. **Tags Match** (Weight: 0.5)
   - Match in product tags

5. **TF-IDF Score** (Dynamic)
   - Term Frequency-Inverse Document Frequency
   - Semantic text matching
   - Handles synonyms and related terms

### Ranking

- Products are sorted by total score (descending)
- Top 10 recommendations are returned
- Only products with score > 0 are included

### Example Scoring

```
Query: "logical reasoning"

Product P1 (Logical Reasoning Test):
- Title match: +3.0
- Description match: +2.0
- Skills match: +1.0
- Tags match: +0.5
- TF-IDF score: +2.0
- Total Score: 8.5 ✅
```

---

## 🧪 Testing

### Manual Testing

1. **Web Interface**
   - Open: `https://assesment-of-rajdeep.onrender.com`
   - Enter query: "logical reasoning"
   - Verify results appear

2. **API Testing**
   ```bash
   # Health check
   curl https://assesment-of-rajdeep.onrender.com/health
   
   # Get recommendations
   curl "https://assesment-of-rajdeep.onrender.com/api/recommend?query=verbal"
   
   # Get all products
   curl https://assesment-of-rajdeep.onrender.com/api/products
   ```

### Test Queries

- `logical reasoning` → Should return "Logical Reasoning Test"
- `verbal ability` → Should return "Verbal Ability Test"
- `numerical` → Should return "Numerical Reasoning Test"
- `problem solving` → Should return relevant products

---

## 📊 Performance

- **Response Time:** < 100ms (in-memory processing)
- **Throughput:** Handles multiple concurrent requests
- **Scalability:** Can process large product catalogs
- **Memory Usage:** Efficient in-memory data structures

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is part of the SHL GenAI Assessment. All rights reserved...

---

## 👤 Author

**Rajdeep Samanta**

- GitHub: [@Rajdeep-samanta59](https://github.com/Rajdeep-samanta59)
- Project Link: [https://github.com/Rajdeep-samanta59/Assesment_Of_Rajdeep](https://github.com/Rajdeep-samanta59/Assesment_Of_Rajdeep)

---

## 🙏 Acknowledgments

- SHL for providing the assessment catalog
- Natural library for TF-IDF implementation
- Render for hosting platform
- Express.js community for excellent documentation

---

<div align="center">

**⭐ If you found this project helpful, please give it a star! ⭐**

[⬆ Back to Top](#-shl-genai-recommender-system)

</div>
