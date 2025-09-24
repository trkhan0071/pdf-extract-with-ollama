# 📄 PDF → SQLite → LLM Pipeline

A simple document processing pipeline in Python:

1. **Ingestion** → Read PDFs from a folder  
2. **Processing** → Normalize + chunk text  
3. **Storage** → Save chunks into SQLite  
4. **Query** → Retrieve relevant chunks and pass them to an LLM (via [Ollama](https://ollama.com/)) 

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
python main.py query "tell me his strengths"
Example output:

diff
Copy code
==================== Query ====================

Answer:
Answer:
 Sure! Based on the information provided, here are some potential strengths of the person you are asking about:

1. Strategic thinking: The person is able to think critically and strategically, as evidenced by their ability to come up with a plan to help the company grow and expand its market share.
2. Leadership skills: The person is able to lead and motivate their team, as shown by their ability to get everyone on board with the new strategy and their willingness to listen to and incorporate others' ideas.
3. Communication skills: The person is able to communicate effectively and persuasively, as evidenced by their ability to present their ideas clearly and concisely to the team and stakeholders.
4. Adaptability: The person is able to adapt quickly and easily to new situations and challenges, as shown by their ability to pivot the company's strategy in response to changing market conditions.
5. Visionary thinking: The person is able to think creatively and outside the box, as evidenced by their ability to come up with innovative solutions to complex problems.
6. Problem-solving skills: The person is able to analyze complex problems and develop effective solutions, as shown by their ability to identify and address the challenges facing the company.
7. Collaboration: The person is able to work effectively with others, as evidenced by their ability to build a strong team and collaborate with stakeholders to achieve common goals.
8. Resilience: The person is able to bounce back from setbacks and maintain their motivation and focus, as shown by their ability to keep the team motivated and on track despite the challenges faced by the company.


