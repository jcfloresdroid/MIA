#import sys
#import os
#sys.path.append(os.path.abspath(r"C:\Users\joelf\Documents\MIA\Intro IA\repo\MIA\Intro IA\RAG\Proyecto final\rag-app"))
from pathlib import Path
from app.chunk import process_document

# Reemplaza 'data/mi_documento.pdf' por la ruta de un archivo real tuyo
ruta_archivo = Path("test/mind_lix_236_433.pdf") 

chunks = process_document(ruta_archivo, chunk_size=300, overlap=50)

print(f"Se generaron {len(chunks)} chunks para el archivo {ruta_archivo.name}\n")

# Mostrar el contenido del primer chunk
print("--- Chunk 0 ---")
print("ID:", chunks[0]["chunk_id"])
print("Fuente:", chunks[0]["source"])
print("Número de palabras:", len(chunks[0]["text"].split()))
print("Texto (primeras 100 palabras):", chunks[0]["text"][:200] + "...")