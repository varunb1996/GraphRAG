import json
import networkx as nx

G = nx.Graph()

with open("data/processed/documents.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

for idx, doc in enumerate(docs):

    G.add_node(idx,
               source=doc["source"],
               type=doc["type"])

# Simple relationship logic
for i in range(len(docs)):
    for j in range(i + 1, len(docs)):

        if docs[i]["type"] == docs[j]["type"]:
            G.add_edge(i, j, relation="similar_type")

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

nx.write_gml(G, "graph/knowledge_graph.gml")