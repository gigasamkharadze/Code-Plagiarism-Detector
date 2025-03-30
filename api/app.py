import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from utils.check_plagiarism import check_plagiarism
from utils.get_embedding import get_embedding
from utils.get_similar_codes import get_similar_codes

app = FastAPI()
load_dotenv()


class CodeInput(BaseModel):
    code: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the Code Plagiarism Detector API"}


@app.post("/check")
def plagiarism(code: CodeInput):
    # TODO: Organize the code
    api_url = os.environ.get("EMBEDDINGS_API")
    embedding = get_embedding(code.code, api_url)
    similar_codes = get_similar_codes(embedding)
    is_plagiarized = check_plagiarism(similar_codes)

    return {
        "is_plagiarized": is_plagiarized,
    }

