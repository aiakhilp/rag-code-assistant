import os
from bs4 import BeautifulSoup
import openai
from openai import OpenAI
import faiss
import numpy as np
import pickle
from tqdm import tqdm

# Latest OpenAI client usage
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def chunk_html_doc(file_path, chunk_size=500):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    # Extract visible text (skip nav, footer)
    for nav in soup(['nav', 'footer', 'style', 'script']):
        nav.decompose()
    text = soup.get_text(separator="\n")
    # Simple chunking: split by lines, group into chunks
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    chunks, curr_chunk = [], []
    for line in lines:
        curr_chunk.append(line)
        if sum(len(l) for l in curr_chunk) > chunk_size:
            chunks.append('\n'.join(curr_chunk))
            curr_chunk = []
    if curr_chunk:
        chunks.append('\n'.join(curr_chunk))
    return chunks

def embed_texts(texts, batch_size=20, model="text-embedding-3-small"):
    embeddings = []
    for i in tqdm(range(0, len(texts), batch_size), desc="Embedding"):
        batch = texts[i:i+batch_size]
        response = client.embeddings.create(
            input=batch,
            model=model,
        )
        batch_embeddings = [np.array(e.embedding, dtype=np.float32) for e in response.data]
        embeddings.extend(batch_embeddings)
    return embeddings

def build_faiss_index(embeddings, out_path):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.stack(embeddings))
    faiss.write_index(index, out_path)

def save_metadata(chunks, embeddings, meta_path):
    with open(meta_path, "wb") as f:
        pickle.dump({"chunks": chunks}, f)

def load_retriever(index_path, meta_path):
    index = faiss.read_index(index_path)
    with open(meta_path, "rb") as f:
        meta = pickle.load(f)
    chunks = meta["chunks"]
    return index, chunks

def search_chunks(query, index, chunks, client, k=4, model="text-embedding-3-small"):
    query_emb = client.embeddings.create(
        input=[query],
        model=model,
    ).data[0].embedding
    query_emb = np.array(query_emb, dtype=np.float32).reshape(1, -1)
    D, I = index.search(query_emb, k)
    results = [chunks[i] for i in I[0]]
    
    # LOGGING: print or log what was retrieved!
    print("\n[INFO] Top RAG doc chunks retrieved for query:", query)
    for i, chunk in enumerate(results, 1):
        print(f"\n--- Chunk {i} ---\n{chunk[:500]}\n...")  # Show up to 500 chars
    print("[INFO] End of RAG chunks\n")
    
    return results


if __name__ == "__main__":
    # 1. Chunk the doc
    doc_path = "data/quickstart.html"
    chunks = chunk_html_doc(doc_path)
    print(f"Chunked {len(chunks)} chunks.")

    # 2. Embed the chunks
    embeddings = embed_texts(chunks)

    # 3. Build and save FAISS index
    os.makedirs("embeddings", exist_ok=True)
    build_faiss_index(embeddings, "embeddings/quickstart.index")

    # 4. Save metadata (chunk texts)
    save_metadata(chunks, embeddings, "embeddings/quickstart.pkl")
    print("Embedding and index complete!")

