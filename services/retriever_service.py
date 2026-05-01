import faiss
import numpy as np
from services.embedding_service import model


def build_faiss_index(chunks):
    embeddings = np.array([c["embedding"] for c in chunks]).astype("float32")

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return index


def retrieve(query, chunks, index, top_k=5):
    query_embedding = model.encode([query]).astype("float32")

    D, I = index.search(query_embedding, top_k)

    results = [chunks[i]["text"] for i in I[0]]

    return results