from pathlib import Path
from typing import Any, Dict, List
from pypdf import PdfReader


def chunk_text(
    text: str, source_name: str, chunk_size: int = 300, overlap: int = 50
) -> List[Dict[str, Any]]:
    words = text.split()
    if not words:
        return []

    step = max(1, chunk_size - overlap)
    chunks = []
    start = 0
    chunk_index = 0

    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunk_text_str = " ".join(chunk_words)

        chunks.append(
            {
                "chunk_id": f"{source_name}_chunk_{chunk_index}",
                "text": chunk_text_str,
                "source": source_name,
                "chunk_index": chunk_index,
            }
        )
        if start + chunk_size >= len(words):
            break
        start += step
        chunk_index += 1

    return chunks


def extract_text_from_file(file_path: Path) -> str:
    suffix = file_path.suffix.lower()
    if suffix in [".txt", ".md"]:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    elif suffix == ".pdf":
        reader = PdfReader(file_path)
        return "\n".join(
            [page.extract_text() for page in reader.pages if page.extract_text()]
        )
    raise ValueError(f"Formato no soportado: {suffix}")


def process_document(
    file_path: Path, chunk_size: int = 300, overlap: int = 50
) -> List[Dict[str, Any]]:
    text = extract_text_from_file(file_path)
    return chunk_text(text, file_path.name, chunk_size, overlap)