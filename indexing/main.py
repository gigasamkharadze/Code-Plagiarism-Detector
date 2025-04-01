import os
import yaml
import logging

from dotenv import load_dotenv

from shared_utils.shared_utils.chunker import get_chunks
from shared_utils.shared_utils.embeddings import Embedding
from shared_utils.shared_utils.parser import Parser
from shared_utils.shared_utils.db import DBManager

logging.basicConfig(level=logging.INFO)

def main():
    load_dotenv()
    api_url = os.getenv("EMBEDDINGS_API")
    api_key = os.getenv("PINECONE_KEY")

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    parser = Parser(config)
    processed_content = parser.get_content()

    db_manager = DBManager(api_key)
    embedding_service_manager = Embedding(api_url)

    logging.info("Local processing complete. Starting to store embeddings in Pinecone.")

    for processed_content in processed_content:
        chunks = get_chunks(processed_content)
        embeddings = []
        for chunks in chunks:
            embeddings.append(embedding_service_manager.get_embedding(chunks, wrap_for_db=True))

        db_manager.store_embeddings(embeddings)

    logging.info("Completed storing embeddings in Pinecone.")


if __name__ == "__main__":
    main()
