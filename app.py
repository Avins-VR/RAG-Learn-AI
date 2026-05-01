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

st.set_page_config(page_title="RAG Learn AI", layout="wide", page_icon="📘")

# ── Premium CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Root tokens ── */
:root {
    --bg:        #0a0c10;
    --surface:   #0f1117;
    --glass:     rgba(255,255,255,0.04);
    --border:    rgba(255,255,255,0.08);
    --border-hi: rgba(99,179,237,0.35);
    --accent:    #63b3ed;
    --accent2:   #76e4b0;
    --text:      #e2e8f0;
    --muted:     #718096;
    --danger:    #fc8181;
    --warn:      #f6ad55;
    --radius:    14px;
    --font:      'Sora', sans-serif;
    --mono:      'JetBrains Mono', monospace;
}

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: var(--font) !important;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

/* Subtle grid background */
.stApp {
    background-color: var(--bg) !important;
    background-image:
        linear-gradient(rgba(99,179,237,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(99,179,237,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding-top: 0rem;
}

/* Sidebar title */
[data-testid="stSidebar"] h1 {
    font-size: 1.4rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.04em !important;
    color: var(--accent) !important;
    text-transform: uppercase;
}

/* Sidebar subheaders */
[data-testid="stSidebar"] h3 {
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.12em !important;
    color: var(--muted) !important;
    text-transform: uppercase;
    margin-bottom: 0.5rem !important;
}

/* Caption text */
[data-testid="stSidebar"] .stCaption,
[data-testid="stSidebar"] small {
    color: var(--muted) !important;
    font-size: 0.75rem !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: var(--glass) !important;
    border: 1px dashed var(--border-hi) !important;
    border-radius: var(--radius) !important;
    transition: border-color 0.2s ease;
}
[data-testid="stFileUploader"]:hover {
    border-color: var(--accent) !important;
}
[data-testid="stFileUploader"] label { display: none !important; }

/* Text area */
[data-testid="stTextArea"] textarea {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    color: var(--text) !important;
    font-family: var(--font) !important;
    font-size: 0.9rem !important;
    resize: none !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
[data-testid="stTextArea"] textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(99,179,237,0.12) !important;
    outline: none !important;
}
[data-testid="stTextArea"] textarea::placeholder {
    color: var(--muted) !important;
}

/* Primary button */
[data-testid="stButton"] button[kind="primary"] {
    background: linear-gradient(135deg, #3a7bd5 0%, #63b3ed 100%) !important;
    border: none !important;
    border-radius: var(--radius) !important;
    color: #fff !important;
    font-family: var(--font) !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    letter-spacing: 0.05em !important;
    padding: 0.65rem 1.5rem !important;
    transition: opacity 0.2s ease, transform 0.15s ease, box-shadow 0.2s ease !important;
    box-shadow: 0 4px 20px rgba(99,179,237,0.25) !important;
}
[data-testid="stButton"] button[kind="primary"]:hover {
    opacity: 0.9 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 28px rgba(99,179,237,0.35) !important;
}
[data-testid="stButton"] button[kind="primary"]:active {
    transform: translateY(0) !important;
}

/* Divider */
hr {
    border-color: var(--border) !important;
    margin: 1rem 0 !important;
}

/* ── Main area ── */
.main .block-container {
    padding-top: 2.5rem !important;
    max-width: 860px !important;
}

/* Main title */
.main h1 {
    font-size: 1.75rem !important;
    font-weight: 700 !important;
    letter-spacing: -0.01em !important;
    background: linear-gradient(135deg, var(--text) 30%, var(--accent) 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}

/* Caption under title */
.main .stCaption {
    color: var(--muted) !important;
    font-size: 0.82rem !important;
}

/* ── Info / warning / error boxes ── */
.stAlert {
    border-radius: var(--radius) !important;
    border: none !important;
    font-size: 0.88rem !important;
}

/* Info */
[data-testid="stAlert"][data-baseweb="notification"][kind="info"],
div[data-baseweb="notification"] {
    background: rgba(99,179,237,0.08) !important;
    border: 1px solid rgba(99,179,237,0.2) !important;
    border-radius: var(--radius) !important;
    color: var(--text) !important;
}

/* Warning */
div[data-baseweb="notification"][kind="warning"] {
    background: rgba(246,173,85,0.08) !important;
    border: 1px solid rgba(246,173,85,0.25) !important;
    color: var(--warn) !important;
}

/* Error */
div[data-baseweb="notification"][kind="error"] {
    background: rgba(252,129,129,0.08) !important;
    border: 1px solid rgba(252,129,129,0.2) !important;
    color: var(--danger) !important;
}

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: var(--accent) !important;
}

/* ── Answer markdown ── */
.answer-card {
    background: var(--glass);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.75rem 2rem;
    margin-top: 0.75rem;
    line-height: 1.8;
    font-size: 0.95rem;
    animation: fadeUp 0.4s ease both;
}

.question-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(99,179,237,0.1);
    border: 1px solid rgba(99,179,237,0.2);
    border-radius: 999px;
    padding: 0.4rem 1rem;
    font-size: 0.82rem;
    color: var(--accent);
    font-weight: 500;
    margin-bottom: 1rem;
}

.idle-hint {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    padding: 4rem 2rem;
    color: var(--muted);
    font-size: 0.9rem;
    text-align: center;
}
.idle-hint .icon {
    font-size: 2.5rem;
    opacity: 0.35;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Scrollbar */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: var(--muted); }
</style>
""", unsafe_allow_html=True)


# ── Cache ──────────────────────────────────────────────────────────────────────
@st.cache_data
def process_pdf(file_hash, file_bytes):
    file = io.BytesIO(file_bytes)
    pages = extract_text_by_page(file)
    pages = pages[:10]
    chunks = chunk_text(pages)
    chunks = create_embeddings(chunks)
    index = build_faiss_index(chunks)
    return chunks, index


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("📘 RAG Learn AI")
    st.caption("100% RAG · Powered by Groq")
    st.divider()

    st.subheader("📂 Upload Document")
    uploaded_file = st.file_uploader(
        "Upload a PDF file", type="pdf", label_visibility="collapsed"
    )
    st.divider()

    st.subheader("💬 Ask a Question")
    question = st.text_area(
        "Type your question here…",
        height=120,
        placeholder="e.g. Summarise Chapter 3",
        label_visibility="collapsed",
    )
    submit = st.button("🔍 Get Answer", use_container_width=True, type="primary")
    st.divider()
    st.caption("Upload a PDF, enter your question, then click **Get Answer**.")


# ── Main ───────────────────────────────────────────────────────────────────────
st.title("📖 Answer")
st.caption("The generated answer will appear below once you submit a question.")
st.divider()

answer_container = st.container()

with answer_container:
    if submit:
        if not uploaded_file or not question:
            st.warning("⚠️ Please upload a PDF and enter a question before submitting.")
        else:
            with st.spinner("Processing your document and generating an answer…"):
                file_bytes = uploaded_file.read()
                file_hash = hashlib.md5(file_bytes).hexdigest()
                chunks, index = process_pdf(file_hash, file_bytes)

                results = retrieve(query=question, chunks=chunks, index=index, top_k=5)

                if not results:
                    st.error("❌ No relevant content found in the uploaded document.")
                else:
                    context = "\n".join(results)[:4000]
                    answer = generate_answer(context, question)

                    col_meta, col_spacer = st.columns([3, 1])
                    with col_meta:
                        st.markdown(
                            f'<div class="question-badge">💬 {question}</div>',
                            unsafe_allow_html=True,
                        )

                    st.markdown("---")

                    st.markdown(
                        f'<div class="answer-card">{answer.replace(chr(10), "<br>")}</div>',
                        unsafe_allow_html=True,
                    )
    else:
        st.markdown(
            """
            <div class="idle-hint">
                <div class="icon">📄</div>
                <span>Upload a PDF and ask a question using the sidebar<br>to get an AI-generated answer here.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )