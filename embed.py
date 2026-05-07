import json
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="embeddings")
collection = client.get_or_create_collection("knowledge_base")

with open("data/processed/documents.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

for idx, doc in enumerate(docs):

    content = doc["content"][:3000]

    embedding = model.encode(content).tolist()

    collection.add(
        ids=[str(idx)],
        documents=[content],
        embeddings=[embedding],
        metadatas=[{
            "source": doc["source"],
            "type": doc["type"]
        }]
    )

print("Embeddings stored successfully")