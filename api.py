from fastapi import FastAPI
from retrieval import search

app = FastAPI()


@app.get("/query")
def query_rag(q: str):

    results = search(q)

    return {
        "query": q,
        "results": results
    }