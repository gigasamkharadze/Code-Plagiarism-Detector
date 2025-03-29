from typing import Any
import requests


def get_embedding(chunk: str, api_url: str) -> dict[str, Any]:
    payload = {"code": chunk}
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        embedding = response.json().get("embedding")
        return embedding
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return {}
