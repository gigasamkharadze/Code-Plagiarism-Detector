import os
from pinecone import Pinecone


def get_similar_codes(embedding):
    # TODO: Do not like read env variables here
    key = os.environ.get("PINECONE_KEY")
    index_name = os.environ.get("PINECONE_INDEX_NAME")

    pc = Pinecone(api_key=key)
    index = pc.Index(index_name)

    results = index.query(vector=embedding, top_k=5, include_metadata=True)
    return results


