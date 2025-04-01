from fastapi import FastAPI
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, AutoTokenizer
import torch

app = FastAPI()

checkpoint = "Salesforce/codet5p-220m"
device = "cpu"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = T5ForConditionalGeneration.from_pretrained(checkpoint).to(device)


class CodeSnippet(BaseModel):
    code: str


@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/generate/")
def generate_embeddings(snippet: CodeSnippet):
    inputs = tokenizer(snippet.code, return_tensors="pt", padding=True, truncation=True).to(device)

    with torch.no_grad():
        outputs = model.encoder(**inputs)
        embeddings = outputs.last_hidden_state

    code_embedding = embeddings.mean(dim=1).cpu().numpy()

    return {
        "embedding": code_embedding.tolist()
    }
