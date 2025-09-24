import requests
from .storage import search_chunks

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama2"  # Ensure you have this pulled: `ollama pull llama2`

def ask_question(question: str):
    """Retrieve relevant chunks and query Ollama"""
    relevant = search_chunks(question)
    context = "\n".join(relevant)

    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    resp = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt, "stream": False}
    )
    data = resp.json()
    return data.get("response", "No response from model.")