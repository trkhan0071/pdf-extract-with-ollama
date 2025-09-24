# 📄 PDF → SQLite → LLM Pipeline

A simple document processing pipeline in Python:

1. **Ingestion** → Read PDFs from a folder  
2. **Processing** → Normalize + chunk text  
3. **Storage** → Save chunks into SQLite  
4. **Query** → Retrieve relevant chunks and pass them to an LLM (via [Ollama](https://ollama.com/))  

---

## 📂 Project Structure

pdf_pipeline/
├── data/ # 📥 put your PDFs here
│ ├── sample1.pdf
│ └── sample2.pdf
├── db/ # 📦 SQLite database (auto-created)
├── pdf_pipeline/ # 🔧 source code
│ ├── ingestion.py # PDF ingestion
│ ├── processing.py # text cleaning + chunking
│ ├── storage.py # SQLite storage
│ ├── query.py # query interface + LLM call
│ └── utils.py # helper functions
├── main.py # CLI entry point
├── requirements.txt # Python dependencies
└── README.md # this file

yaml
Copy code

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd pdf_pipeline
2. Create a virtual environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
3. Install Python dependencies
bash
Copy code
pip install -r requirements.txt
4. Install Ollama (system-wide, not in venv)
Windows → Download installer

macOS →

bash
Copy code
brew install ollama/tap/ollama
Linux →

bash
Copy code
curl -fsSL https://ollama.com/install.sh | sh
Verify installation:

bash
Copy code
ollama --version
5. Pull a model
bash
Copy code
ollama pull llama2
🚀 Usage
1. Add PDFs
Place your PDFs in the data/ folder. Example:

bash
Copy code
data/report1.pdf
data/report2.pdf
2. Ingest PDFs
bash
Copy code
python main.py ingest data/
This will:

Extract text from each PDF

Normalize + chunk the text

Store chunks in db/chunks.db

Example output:

diff
Copy code
==================== Ingestion ====================

Ingested report1.pdf (12 chunks)
Ingested report2.pdf (20 chunks)
3. Query the database
bash
Copy code
python main.py query "What is the main conclusion of the report?"
Example output:

diff
Copy code
==================== Query ====================

Answer:
The report concludes that...
🛠️ Troubleshooting
'ollama' is not recognized → Install Ollama system-wide (see Setup step 4) and restart your terminal.

ImportError: attempted relative import → Use absolute imports in main.py or run as a module:

bash
Copy code
python -m main ingest data/
Database not found → Run ingestion first (python main.py ingest data/).

📌 Notes
Storage uses simple keyword search (LIKE) for chunk retrieval.

For better accuracy, you can extend this with embeddings + semantic search (e.g., sentence-transformers + FAISS).

This project is a starting point — extend as needed for production.
