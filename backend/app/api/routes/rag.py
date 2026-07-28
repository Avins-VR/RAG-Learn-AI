import hashlib
import io

from fastapi import APIRouter, File, UploadFile, HTTPException

from app.models.rag_models import AskRequest, AskResponse, UploadResponse
from app.services.pdf_service import extract_text_by_page
from app.services.chunk_service import chunk_text
from app.services.embedding_service import create_embeddings
from app.services.retriever_service import build_faiss_index, retrieve
from app.services.groq_service import generate_answer
from app.utils.cache import get_cached, set_cached

router = APIRouter()

# Mirrors Streamlit's session state: stores the last processed chunks+index
# keyed by file_hash so repeated uploads of the same file are free.
_session: dict = {}


def _process_pdf(file_hash: str, file_bytes: bytes):
    cached = get_cached(file_hash)
    if cached:
        return cached

    file = io.BytesIO(file_bytes)
    pages = extract_text_by_page(file)
    pages = pages[:10]
    chunks = chunk_text(pages)
    chunks = create_embeddings(chunks)
    index = build_faiss_index(chunks)

    set_cached(file_hash, chunks, index)
    return chunks, index


@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")

    file_bytes = await file.read()
    file_hash = hashlib.md5(file_bytes).hexdigest()

    chunks, index = _process_pdf(file_hash, file_bytes)

    # Keep the latest processed document available for /ask
    _session["file_hash"] = file_hash
    _session["chunks"]    = chunks
    _session["index"]     = index

    return UploadResponse(
        success=True,
        message="PDF processed successfully.",
        file_hash=file_hash,
    )


@router.post("/ask", response_model=AskResponse)
async def ask_question(body: AskRequest):
    if "chunks" not in _session or "index" not in _session:
        raise HTTPException(
            status_code=400,
            detail="No document loaded. Please upload a PDF first.",
        )

    question = body.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Question must not be empty.")

    chunks = _session["chunks"]
    index  = _session["index"]

    results = retrieve(query=question, chunks=chunks, index=index, top_k=5)

    if not results:
        raise HTTPException(
            status_code=404,
            detail="No relevant content found in the uploaded document.",
        )

    context = "\n".join(results)[:4000]
    answer  = generate_answer(context, question)

    return AskResponse(success=True, answer=answer)

from fastapi import UploadFile, File

@router.post("/test-upload")
async def test_upload(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
    }