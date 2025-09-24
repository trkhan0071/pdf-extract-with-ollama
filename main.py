import sys
import os
file_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from pdf_libs.ingestion import load_pdfs
from pdf_libs.processing import normalize_text, chunk_text
from pdf_libs.storage import init_db, insert_chunks
from pdf_libs.query import ask_question
from pdf_libs.utils import print_divider


def run_ingest(pdf_dir: str):
    print_divider("Ingestion")
    texts = load_pdfs(pdf_dir)
    init_db()
    for fname, raw_text in texts.items():
        norm = normalize_text(raw_text)
        chunks = chunk_text(norm)
        insert_chunks(fname, chunks)
        print(f"Ingested {fname} ({len(chunks)} chunks)")

def run_query(question: str):
    print_divider("Query")
    answer = ask_question(question)
    print("Answer:\n", answer)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:\n python main.py ingest <pdf_dir>\n python main.py query <question>")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "ingest":
        pdf_dir = sys.argv[2]
        run_ingest(pdf_dir)
    elif cmd == "query":
        question = " ".join(sys.argv[2:])
        run_query(question)
    else:
        print("Unknown command")