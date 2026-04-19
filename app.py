import streamlit as st

from services.pdf_service import extract_text_by_page
from services.chunk_service import chunk_text
from services.groq_service import generate_answer
from dotenv import load_dotenv

load_dotenv()

st.title("📘 AI Learning Assistant (RAG - Gemini)")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
page_number = st.number_input("Enter Page Number", min_value=1, step=1)
question = st.text_input("Ask your question")

if st.button("Get Answer"):

    if not uploaded_file or not question:
        st.warning("Please upload PDF and enter question")
    else:
        with st.spinner("Processing..."):

            # Step 1: Extract text
            pages = extract_text_by_page(uploaded_file)

            # Step 2: Filter selected page
            selected_page = [p for p in pages if p["page"] == page_number]

            if not selected_page:
                st.error("No content found for this page")
            else:
                context = selected_page[0]["text"]

                # Step 3: Generate answer using Gemini
                answer = generate_answer(context, question)

                st.subheader("📖 Answer")
                st.write(answer)