import re

def normalize_text(text: str) -> str:
    """Basic cleaning of text"""
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_text(text: str, chunk_size: int = 500) -> list[str]:
    """Split text into chunks of ~chunk_size words"""
    words = text.split()
    return [
        " ".join(words[i:i+chunk_size])
        for i in range(0, len(words), chunk_size)
    ]