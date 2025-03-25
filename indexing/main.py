import os
import yaml
import logging

from dotenv import load_dotenv
from indexing.db import DBManager
from indexing.parser import Parser
from indexing.utils.get_embedding import get_embedding
from indexing.utils.get_chunks import get_chunks

logging.basicConfig(level=logging.INFO)

# TODO: logging
def main():
    load_dotenv()
    api_url = os.getenv("EMBEDDINGS_API")
    api_key = os.getenv("PINECONE_KEY")

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    parser = Parser(config)
    processed_content = parser.get_content()

    db_manager = DBManager(api_key)

    logging.info("Local processing complete. Starting to store embeddings in Pinecone.")

    # TODO: Thread this
    # TODO: move this to a separate function
    for processed_content in processed_content:
        chunks = get_chunks(processed_content)
        embeddings = []
        for chunks in chunks:
            embeddings.append(get_embedding(chunks, api_url))

        db_manager.store_embeddings(embeddings)

    logging.info("Local processing complete. Starting to store embeddings in Pinecone.")


if __name__ == "__main__":
    main()
