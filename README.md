GraphRAG Knowledge Assistant-
A lightweight GraphRAG-based knowledge retrieval system designed to combine semantic search with graph-oriented relationships across technical documents and source code repositories.
This project ingests PDFs and code repositories, generates embeddings using open-source transformer models, stores semantic vectors in ChromaDB, and builds graph relationships between knowledge nodes for improved contextual retrieval. A FastAPI backend and Streamlit frontend enable interactive querying across engineering and non-engineering data sources.


Features-
PDF and code repository ingestion
Semantic search using Sentence Transformers
Vector storage with ChromaDB
Graph-based relationship mapping
FastAPI backend APIs
Streamlit interactive UI
Modular and extensible architecture
Foundation for Agentic Coding Tools and GraphRAG workflows


Tech Stack-
Python
FastAPI
Streamlit
ChromaDB
Sentence Transformers
NetworkX
PyPDF

graph_rag_system/
│
├── data/
│   ├── pdfs/
│   └── .gitkeep
│
├── embeddings/
│   └── .gitkeep
│
├── graph/
│   └── .gitkeep
│
├── ingest.py
├── embed.py
├── graph_builder.py
├── retrieval.py
├── api.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

Run the Project-

Install dependencies-
Bash-
pip install -r requirements.txt
2. Run ingestion
Bash
python ingest.py
3. Generate embeddings
Bash
python embed.py
4. Build graph relationships
Bash
python graph_builder.py
5. Start FastAPI backend
Bash
python -m uvicorn api:app --reload
6. Launch Streamlit UI
Bash
python -m streamlit run app.py

Future Improvements-
Semantic chunking
Incremental updates for evolving data
Dependency-aware GraphRAG relationships
Agentic coding endpoints
Neo4j integration
Notion / Azure document ingestion


Goal-
The project aims to provide a practical GraphRAG foundation for engineering and non-engineering collaboration systems, enabling semantic retrieval and connected knowledge exploration for future AI-assisted development workflows.


## Setup Data

Create the following folders:

```plaintext
data/pdfs/
data/repos/
data/processed/
```

Clone a repository inside:

```plaintext
data/repos/
```

Example:

```bash
git clone https://github.com/langchain-ai/langchain.git data/repos/langchain
```

Add your PDFs inside:

```plaintext
data/pdfs/
```

## Generated Artifacts

The following files/folders are generated automatically during execution and are not included in the repository:

```plaintext
data/processed/documents.json
embeddings/chroma_db/
graph/knowledge_graph.gml
```

## Notes

Large repositories, generated embeddings, vector databases, and processed artifacts are excluded using `.gitignore` to keep the repository lightweight and reproducible.
