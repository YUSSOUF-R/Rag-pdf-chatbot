class Retriever:

    def __init__(self, vector_store):

        self.vector_store = vector_store

    def retrieve_relevant_chunks(
        self,
        query_embedding,
        top_k=3
    ):
        """
        Retrieve relevant chunks with metadata.
        """

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        formatted_results = []

        for index, chunk in enumerate(results, start=1):

            formatted_results.append({
                "source_id": index,
                "content": chunk
            })

        return formatted_results
