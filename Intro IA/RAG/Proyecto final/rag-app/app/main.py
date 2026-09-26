import shutil
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.chunk import process_document
from app.embed import get_embeddings, get_single_embedding
from app.generate import generate_answer
from app.store import VectorStore

app = FastAPI(title="Sistema RAG API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

store = VectorStore()


class QueryRequest(BaseModel):
    question: str
    top_k: int = 3
    source_filter: Optional[str] = None


class Citation(BaseModel):
    id: str
    source: str
    text: str
    score: float


class QueryResponse(BaseModel):
    answer: str
    citations: List[Citation]
    abstained: bool


@app.get("/health")
def health():
    return {
        "status": "ok",
        "chroma_status": "accessible",
        "indexed_chunks": store.collection.count(),
    }


@app.post("/ingest")
async def ingest(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(
            status_code=400, detail="No se enviaron archivos."
        )

    temp_dir = Path("temp_uploads")
    temp_dir.mkdir(exist_ok=True)
    total_chunks = 0
    processed = []

    try:
        for file in files:
            file_path = temp_dir / file.filename
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            chunks = process_document(file_path)
            if chunks:
                embeddings = get_embeddings([c["text"] for c in chunks])
                added = store.add_chunks(chunks, embeddings)
                total_chunks += added
                processed.append(file.filename)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    return {
        "status": "success",
        "processed_files": processed,
        "total_chunks_indexed": total_chunks,
    }


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):
    if not req.question.strip():
        raise HTTPException(
            status_code=400, detail="La pregunta no puede estar vacía."
        )

    query_vec = get_single_embedding(req.question)
    retrieved = store.search(
        query_vec, top_k=req.top_k, source_filter=req.source_filter
    )
    res = generate_answer(req.question, retrieved)

    return QueryResponse(
        answer=res["answer"],
        citations=[Citation(**c) for c in res["citations"]],
        abstained=res["abstained"],
    )