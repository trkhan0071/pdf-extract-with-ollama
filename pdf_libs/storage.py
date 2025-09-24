import sqlite3
from pathlib import Path

DB_PATH = Path("db/chunks.db")

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        chunk TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_chunks(filename: str, chunks: list[str]):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.executemany(
        "INSERT INTO chunks (filename, chunk) VALUES (?, ?)",
        [(filename, ch) for ch in chunks]
    )
    conn.commit()
    conn.close()

def search_chunks(query: str, limit: int = 5):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT chunk FROM chunks WHERE chunk LIKE ? LIMIT ?",
        (f"%{query}%", limit)
    )
    results = [row[0] for row in c.fetchall()]
    conn.close()
    return results