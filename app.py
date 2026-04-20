import streamlit as st
from dotenv import load_dotenv
import hashlib
import io

from services.pdf_service import extract_text_by_page
from services.chunk_service import chunk_text
from services.embedding_service import create_embeddings
from services.retriever_service import build_faiss_index, retrieve
from services.groq_service import generate_answer

load_dotenv()

st.title("📘 AI Learning Assistant (100% RAG - Groq)")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
question = st.text_input("Ask your question")


# ✅ CACHE (based on file hash)
@st.cache_data
def process_pdf(file_hash, file_bytes):
    file = io.BytesIO(file_bytes)

    # 1. Extract
    pages = extract_text_by_page(file)

    # 🔥 SPEED CONTROL (IMPORTANT)
    pages = pages[:10]

    # 2. Chunk
    chunks = chunk_text(pages)

    # 3. Embeddings
    chunks = create_embeddings(chunks)

    # 4. FAISS Index
    index = build_faiss_index(chunks)

    return chunks, index


if st.button("Get Answer"):

    if not uploaded_file or not question:
        st.warning("Please upload PDF and enter question")
    else:
        with st.spinner("Processing..."):

            file_bytes = uploaded_file.read()
            file_hash = hashlib.md5(file_bytes).hexdigest()

            chunks, index = process_pdf(file_hash, file_bytes)

            # 5. Retrieval
            results = retrieve(
                query=question,
                chunks=chunks,
                index=index,
                top_k=5
            )

            if not results:
                st.error("No relevant content found")
            else:
                context = "\n".join(results)[:4000]

                # 6. LLM
                answer = generate_answer(context, question)

                st.subheader("📖 Answer")
                st.markdown(answer.replace("\n", "\n"))