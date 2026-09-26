import os
from typing import Any, Dict, List
from dotenv import find_dotenv, load_dotenv
from google import genai

load_dotenv(find_dotenv())
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_answer(
    query: str,
    retrieved_chunks: List[Dict[str, Any]],
    min_score: float = 0.35,
    model: str = "gemini-2.5-flash",
) -> Dict[str, Any]:
    # Regla de abstención por falta de chunks o score insuficiente
    if not retrieved_chunks or retrieved_chunks[0]["score"] < min_score:
        return {
            "answer": "No tengo evidencia suficiente en el corpus para responder esta pregunta.",
            "citations": [],
            "abstained": True,
        }

    context_lines = [
        f"[{i}] (Fuente: {c['source']})\n{c['text']}"
        for i, c in enumerate(retrieved_chunks, start=1)
    ]
    context = "\n\n".join(context_lines)

    prompt = f"""Usa ÚNICAMENTE el siguiente contexto para responder la pregunta en español.
Si el contexto no es suficiente para responder la pregunta, responde explícitamente: "No tengo evidencia suficiente en el corpus para responder esta pregunta."

Reglas:
1. Responde en español.
2. Incluye citas numéricas como [1], [2] para indicar de qué evidencia obtuviste la información.
3. No inventes datos que no estén presentes en el contexto.

Contexto:
{context}

Pregunta: {query}
Respuesta:"""

    response = client.models.generate_content(model=model, contents=prompt)
    answer_text = "".join(
        part.text
        for part in response.candidates[0].content.parts
        if getattr(part, "text", None)
    ).strip()

    if "no tengo evidencia suficiente" in answer_text.lower():
        return {
            "answer": answer_text,
            "citations": [],
            "abstained": True,
        }

    return {
        "answer": answer_text,
        "citations": retrieved_chunks,
        "abstained": False,
    }