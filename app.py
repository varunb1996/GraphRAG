import streamlit as st
import requests

st.title("GraphRAG Knowledge Assistant")

query = st.text_input("Ask a question")

if st.button("Search"):

    response = requests.get(
        "http://127.0.0.1:8000/query",
        params={"q": query}
    )

    data = response.json()

    results = data["results"]

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    st.subheader("Search Results")

    for i in range(len(documents)):

        st.markdown(f"### Result {i+1}")

        st.write(f"**Source:** {metadatas[i]['source']}")
        st.write(f"**Type:** {metadatas[i]['type']}")
        st.write(f"**Similarity Score:** {round(distances[i], 4)}")

        st.text_area(
            "Retrieved Content",
            documents[i][:1000],
            height=250
        )

        st.divider()