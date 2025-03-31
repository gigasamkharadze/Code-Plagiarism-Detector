from api.utils.get_embedding import get_embedding
from api.utils.get_similar_codes import get_similar_codes

import os


def predict(code: str) -> int:
    api_url = os.getenv("EMBEDDINGS_API")

    embedding = get_embedding(code, api_url)
    similar_codes = get_similar_codes(embedding)

    threshold = 0.5
    filtered_results = [res for res in similar_codes["matches"] if res["score"] >= threshold]

    if filtered_results:
        return 1

    return 0
