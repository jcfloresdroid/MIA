from typing import Any, Dict, List, Optional
import chromadb


class VectorStore:

    def __init__(
        self,
        persist_directory: str = "chroma",
        collection_name: str = "rag_collection",
    ):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name=collection_name, metadata={"hnsw:space": "cosine"}
        )

    def add_chunks(
        self, chunks: List[Dict[str, Any]], embeddings: List[List[float]]
    ) -> int:
        if not chunks:
            return 0
        documents = [c["text"] for c in chunks]
        ids = [c["chunk_id"] for c in chunks]
        metadatas = [
            {"source": c["source"], "chunk_index": c["chunk_index"]}
            for c in chunks
        ]

        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )
        return len(chunks)

    def search(
        self,
        query_embedding: List[float],
        top_k: int = 3,
        source_filter: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        where_clause = {"source": source_filter} if source_filter else None
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where_clause,
        )

        formatted = []
        if results and results.get("documents") and len(results["documents"]) > 0:
            docs, ids, metas, dists = (
                results["documents"][0],
                results["ids"][0],
                results["metadatas"][0],
                results["distances"][0],
            )
            for doc, chunk_id, meta, dist in zip(docs, ids, metas, dists):
                score = max(0.0, 1.0 - dist)
                formatted.append(
                    {
                        "id": chunk_id,
                        "text": doc,
                        "source": meta.get("source", "desconocido"),
                        "score": round(score, 4),
                    }
                )
        return formatted 