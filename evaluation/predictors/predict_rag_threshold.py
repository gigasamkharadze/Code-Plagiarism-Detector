import os
from shared_utils.shared_utils.embeddings import Embedding
from shared_utils.shared_utils.db import DBManager

def predict(code: str) -> int:
    api_url = os.getenv("EMBEDDINGS_API")
    db_key = os.getenv("PINECONE_KEY")

    embedding_service_manager = Embedding(api_url)
    db_manager = DBManager(db_key)

    embedding = embedding_service_manager.get_embedding(code, wrap_for_db=False)
    similar_codes = db_manager.retrieve(embedding, top_k=5)

    threshold = 0.3
    filtered_results = [res for res in similar_codes["matches"] if res["score"] >= threshold]

    return int(bool(filtered_results))
