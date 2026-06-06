# 🚀 Production AI Assistant

An end-to-end Retrieval-Augmented Generation (RAG) system built from scratch using Haystack, Pinecone, and Sentence Transformers.

## 📈 Current Progress

- [x] Pinecone Setup
- [x] Haystack Pipeline Setup
- [x] PDF Ingestion
- [x] Chunking
- [x] Embedding Generation
- [x] Vector Storage
- [x] Retrieval Pipeline
- [x] Semantic Search
- [x] Gemini Integration
- [x] End-to-End RAG Pipeline

Upcoming:

- [ ] FastAPI API
- [ ] Chat Interface
- [ ] Conversation Memory
- [ ] Evaluation Metrics
- [ ] Production Deployment

# 🚀 AI RAG Assistant

A Retrieval-Augmented Generation (RAG) system built using Haystack, Pinecone, and Sentence Transformers.

This project demonstrates a production-style document ingestion pipeline that transforms PDFs into semantic embeddings and stores them in a vector database for efficient retrieval.

---

## 🏗 System Architecture

```text
PDF Documents
       │
       ▼
PyPDFToDocument
       │
       ▼
DocumentSplitter
       │
       ▼
SentenceTransformer Embeddings
       │
       ▼
Pinecone Vector Database
       │
       ▼
Question
       │
       ▼
Text Embedding
       │
       ▼
Pinecone Retrieval
       │
       ▼
Relevant Context
       │
       ▼
Gemini 2.5 Flash
       │
       ▼
Generated Answer
```

---

## 🔥 Features

- PDF Document Ingestion
- Semantic Chunking
- Dense Vector Embeddings
- Pinecone Vector Storage
- Modular Haystack Pipelines
- Environment-based Configuration

---

## 🛠 Tech Stack

| Component | Technology |
|------------|------------|
| Backend | Python |
| Orchestration | Haystack |
| Vector Database | Pinecone |
| Embeddings | Sentence Transformers |
| PDF Processing | PyPDF |
| LLM | Gemini 2.5 Flash |
| Configuration | Python Dotenv |

---

## 📂 Project Structure

```text
app/
├── pipelines/
├── services/
├── utils/
└── config.py

data/
main.py
requirements.txt
README.md
```

---

## ⚙️ Installation

Clone repository

```bash
git clone <your_repo_url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```env
PINECONE_API_KEY=your_api_key
PINECONE_INDEX=your_index_name
```

---

## 🚀 Running the Ingestion Pipeline

```bash
python main.py
```

Expected flow:

```text
PDF
 ↓
Chunking
 ↓
Embedding Generation
 ↓
Pinecone Indexing
```

---

## 📈 Current Progress

- [x] Pinecone Setup
- [x] Haystack Pipeline Setup
- [x] PDF Ingestion
- [x] Chunking
- [x] Embedding Generation
- [x] Vector Storage

Upcoming:

- [ ] Query Pipeline
- [ ] Retrieval
- [ ] Prompt Engineering
- [ ] LLM Integration
- [ ] FastAPI Interface
- [ ] Production Deployment

---

## 🧠 Key Concepts

- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector Databases
- Semantic Search
- Chunking Strategies
- Cosine Similarity
- AI Pipeline Orchestration

---

## 📜 License

MIT License