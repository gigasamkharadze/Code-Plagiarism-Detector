import os
import requests

def predict(code: str):
    check_endpoint = os.environ.get("CHECK_ENDPOINT")

    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        'code': code
    }

    response = requests.post(check_endpoint, headers=headers, json=data)
    response = response.json()

    return int(response.get('is_plagiarized'))

