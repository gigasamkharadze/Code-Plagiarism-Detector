import os

from dotenv import load_dotenv
from openai import OpenAI
from transformers.models import openai


def predict(code: str):
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")

    # TODO: not good - extract prompt
    prompt = f"""Is the following code plagiarized? {code}. Please answer with "1"
    for plagiarized and "0" for not plagiarized. Do not add any other text. """

    openai.api_key = api_key
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    result = response.choices[0].message.content.strip()
    return int(result)
