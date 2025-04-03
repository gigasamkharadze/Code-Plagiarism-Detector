from typing import Any

import requests
import uuid

class Embedding:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def get_embedding(self, chunk: str, wrap_for_db: bool=False) -> dict[str, Any]:
        """
        Get the embedding for a chunk of code
        :param chunk: piece of code to get the embedding for
        :param wrap_for_db: if True, wrap the embedding in a dict for DB storage
        :return: the embedding for the chunk of code
        """
        payload = {"code": chunk}
        response = requests.post(self.api_url, json=payload)

        if response.status_code == 200:
            embedding = response.json().get("embedding")
            if wrap_for_db:
                return {
                    "id": uuid.uuid4().hex,
                    "values": embedding[0]
                }
            return embedding
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return {}
