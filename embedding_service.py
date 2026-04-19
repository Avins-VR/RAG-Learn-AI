from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):
    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts)

    for i, chunk in enumerate(chunks):
        chunk["embedding"] = embeddings[i]

    return chunks