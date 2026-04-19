from services.embedding_service import model  # ✅ ADD THIS
import faiss
import numpy as np

def store_embeddings(chunks):
    embeddings = [c["embedding"] for c in chunks]
    dim = len(embeddings[0])

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    return index, chunks


def retrieve(query, chunks, index, page_number, top_k=5):
    # filter by page
    filtered_chunks = [c for c in chunks if c["page"] == page_number]

    if not filtered_chunks:
        return []

    embeddings = np.array(
        [c["embedding"] for c in filtered_chunks]
    ).astype("float32")

    temp_index = faiss.IndexFlatL2(len(embeddings[0]))
    temp_index.add(embeddings)

    # ✅ NOW WORKS
    query_embedding = model.encode([query]).astype("float32")

    D, I = temp_index.search(query_embedding, top_k)

    results = [filtered_chunks[i]["text"] for i in I[0]]

    return results