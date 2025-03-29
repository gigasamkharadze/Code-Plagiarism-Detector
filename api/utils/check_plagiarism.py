import os

from openai import OpenAI
from transformers.models import openai


# TODO: Need to take a look at this, looks bad
def check_plagiarism(similar_codes):
    api_key = os.environ.get("OPENAI_API_KEY")

    # TODO: not good
    with open("./prompts/prompt.txt", "r") as f:
        prompt = f.read()

    prompt = prompt.replace("{{similar_codes}}", str(similar_codes))

    openai.api_key = api_key
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    result = response.choices[0].message.content.strip().lower()
    return result == 'true'
