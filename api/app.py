import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from utils.check_plagiarism import check_plagiarism

from shared_utils.shared_utils.embeddings import Embedding
from shared_utils.shared_utils.db import DBManager

app = FastAPI()
load_dotenv()

api_url = os.environ.get("EMBEDDINGS_API")
key = os.environ.get("PINECONE_KEY")

embedding_service_manager = Embedding(api_url)
db_manager = DBManager(api_key=key)

class CodeInput(BaseModel):
    code: str


@app.get("/")
def read_root():
    return {"message": "Welcome to the Code Plagiarism Detector API"}


@app.post("/check")
def plagiarism(code: CodeInput):
    embedding = embedding_service_manager.get_embedding(code.code, wrap_for_db=False)
    similar_codes = db_manager.retrieve(embedding, top_k=5)

    if not similar_codes:
        return {
            "is_plagiarized": False,
        }

    is_plagiarized = check_plagiarism(similar_codes)

    return {
        "is_plagiarized": is_plagiarized,
    }

