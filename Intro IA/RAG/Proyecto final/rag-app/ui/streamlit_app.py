import httpx
import streamlit as st

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Sistema RAG", page_icon="📚", layout="wide")
st.title("📚 Sistema RAG - Joel Flores =)")

# Estado de la API
try:
    r = httpx.get(f"{API_URL}/health", timeout=3.0)
    if r.status_code == 200:
        st.sidebar.success(
            f"🟢 API Conectada ({r.json()['indexed_chunks']} chunks en índice)"
        )
    else:
        st.sidebar.error("🔴 Error en API")
except Exception:
    st.sidebar.error("🔴 API no detectada en localhost:8000")

# Ingesta
st.sidebar.header("📁 Ingestar Documentos")
uploaded_files = st.sidebar.file_uploader(
    "Sube archivos (.txt, .md, .pdf)",
    accept_multiple_files=True,
    type=["txt", "md", "pdf"],
)

if st.sidebar.button("Procesar e Ingestar"):
    if uploaded_files:
        payload = [
            ("files", (f.name, f.getvalue(), f.type or "text/plain"))
            for f in uploaded_files
        ]
        with st.spinner("Indexando vectores con Google AI y ChromaDB..."):
            res = httpx.post(f"{API_URL}/ingest", files=payload, timeout=300.0)
            if res.status_code == 200:
                st.sidebar.success(
                    f"¡Indexados {res.json()['total_chunks_indexed']} chunks!"
                )
            else:
                st.sidebar.error("Error en la ingesta.")

# Consulta
st.header("💬 Consulta al Corpus")
question = st.text_input("Pregunta:")
top_k = st.slider("Chunks a recuperar (top-k):", 1, 5, 3)

if st.button("Enviar Pregunta"):
    if question.strip():
        with st.spinner("Consultando evidencia y generando respuesta..."):
            res = httpx.post(
                f"{API_URL}/query",
                json={"question": question, "top_k": top_k},
                timeout=30.0,
            )
            if res.status_code == 200:
                data = res.json()
                if data["abstained"]:
                    st.warning(f"⚠️ {data['answer']}")
                else:
                    st.markdown("### Respuesta:")
                    st.write(data["answer"])

                    st.markdown("---")
                    st.markdown("### 🔍 Citas y Evidencia Usada:")
                    for idx, cit in enumerate(data["citations"], start=1):
                        with st.expander(
                            f"Cita [{idx}] — {cit['source']} (Score: {cit['score']})"
                        ):
                            st.write(f"**ID:** {cit['id']}")
                            st.write(f"**Texto:** {cit['text']}")