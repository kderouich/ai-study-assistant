from sentence_transformers import SentenceTransformer
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="study_materials"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def store_chunks(chunks):

    embeddings = model.encode(chunks).tolist()

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

def search_chunks(query, n_results=3):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]