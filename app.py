import streamlit as st
from dotenv import load_dotenv
import io

from services.pdf_service import extract_text_by_page
from services.chunk_service import chunk_text
from services.embedding_service import create_embeddings
from services.retriever_service import store_embeddings, retrieve
from services.groq_service import generate_answer

load_dotenv()

st.title("📘 AI Learning Assistant (RAG - Groq)")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
page_number = st.number_input("Enter Page Number", min_value=1, step=1)
question = st.text_input("Ask your question")


@st.cache_data
def process_pdf(file_bytes):
    file = io.BytesIO(file_bytes)

    pages = extract_text_by_page(file)

    # 🚀 SPEED BOOST
    pages = pages[:20]

    chunks = chunk_text(pages)
    chunks = create_embeddings(chunks)
    index, chunks = store_embeddings(chunks)

    return chunks, index


if st.button("Get Answer"):

    if not uploaded_file or not question:
        st.warning("Please upload PDF and enter question")
    else:
        with st.spinner("Processing..."):

            file_bytes = uploaded_file.read()

            chunks, index = process_pdf(file_bytes)

            results = retrieve(
                question,
                chunks,
                index,
                page_number,
                top_k=3
            )

            if not results:
                st.error("No relevant content found")
            else:
                context = "\n".join(results)[:4000]

                answer = generate_answer(context, question)

                st.subheader("📖 Answer")
                st.write(answer)