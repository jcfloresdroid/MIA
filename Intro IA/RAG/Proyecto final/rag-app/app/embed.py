import os
from typing import List
from dotenv import find_dotenv, load_dotenv
from google import genai

load_dotenv(find_dotenv())
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY no encontrada en el entorno .env")
print("Se encontró la clave de API de Gemini en el entorno .env");
client = genai.Client(api_key=GEMINI_API_KEY)

# Se crea un cliente HTTP personalizado que desactiva la verificación SSL
"""http_client = httpx.Client(verify=False)

client = genai.Client(
    api_key=GEMINI_API_KEY,
    http_options=types.HttpOptions(client=http_client),
)"""

def get_embeddings(
    texts: List[str], model: str = "gemini-embedding-001",batch_size: int = 10,
) -> List[List[float]]:
    if not texts:
        return []
    all_embeddings = []

    # Procesar en lotes pequeños para evitar timeouts
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        response = client.models.embed_content(model=model, contents=batch)
        all_embeddings.extend([e.values for e in response.embeddings])

    return all_embeddings


def get_single_embedding(
    text: str, model: str = "gemini-embedding-001"
) -> List[float]:
    return get_embeddings([text], model=model)[0]