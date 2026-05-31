import faiss
import numpy as np
import pickle
import os


class VectorStore:

    def __init__(self):

        self.index = None

        self.text_chunks = []

        self.index_path = "vectorstore/faiss_index.index"

        self.chunks_path = "vectorstore/chunks.pkl"

        os.makedirs("vectorstore", exist_ok=True)

    def create_vector_store(
        self,
        embeddings,
        text_chunks
    ):
        """
        Create FAISS vector database.
        """

        embeddings = np.array(
            embeddings,
            dtype=np.float32
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        self.text_chunks = text_chunks

        faiss.write_index(
            self.index,
            self.index_path
        )

        with open(self.chunks_path, "wb") as f:

            pickle.dump(
                self.text_chunks,
                f
            )

    def load_index(self):
        """
        Load saved FAISS index.
        """

        self.index = faiss.read_index(
            self.index_path
        )

        with open(self.chunks_path, "rb") as f:

            self.text_chunks = pickle.load(f)

    def search(
        self,
        query_embedding,
        top_k=3
    ):
        """
        Retrieve relevant chunks.
        """

        query_embedding = np.array(
            query_embedding,
            dtype=np.float32
        )

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx < len(self.text_chunks):

                results.append(
                    self.text_chunks[idx]
                )

        return results