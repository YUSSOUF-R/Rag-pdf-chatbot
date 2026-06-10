from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingModel:

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    def create_embeddings(
        self,
        text_chunks
    ):

        embeddings = self.model.encode(
            text_chunks,
            convert_to_numpy=True
        )

        return embeddings.astype(np.float32)

    def create_query_embedding(
        self,
        query
    ):

        embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        return embedding.astype(np.float32)
