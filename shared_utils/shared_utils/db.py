from pinecone import Pinecone, ServerlessSpec


class DBManager:
    def __init__(self, api_key, index_name="code-parser", dimension=768):
        self.pc = Pinecone(api_key=api_key)
        self.index_name = index_name
        self.dimension = dimension

        self._create_index()

    def _create_index(self):
        if self.index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=self.index_name,
                dimension=self.dimension,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )

    def store_embeddings(self, embeddings: list[dict]) -> bool:
        """
        Store embeddings in the Pinecone index
        :param embeddings: the list of embeddings to store
        :return: if the embeddings were stored successfully
        """
        index = self.pc.Index(self.index_name)
        try:
            index.upsert(embeddings)
            return True
        except Exception as e:
            print(f"A problem occurred while storing embeddings: {e}")
        return False

    def retrieve(self, query_vector, top_k=5):
        """
        Retrieve the top k similar embeddings to the query_vector
        :param query_vector: the vector to query
        :param top_k: how many similar embeddings to retrieve
        :return: the top k similar embeddings
        """
        index = self.pc.Index(self.index_name)

        return index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True
        )
