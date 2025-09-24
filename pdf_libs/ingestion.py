from pypdf import PdfReader
from pathlib import Path

def load_pdfs(pdf_dir: str) -> dict:
    """Load PDFs from a directory, return dict {filename: text}"""
    texts = {}
    for pdf_path in Path(pdf_dir).glob("*.pdf"):
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        texts[pdf_path.name] = text
    return texts