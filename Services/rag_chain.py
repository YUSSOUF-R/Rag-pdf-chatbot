from services.embedding import EmbeddingModel
from services.retriever import Retriever
from services.prompt_template import PromptTemplate
from services.ollama_client import OllamaClient
from services.chat_memory_manager import ChatMemoryManager


class RAGChain:

    def __init__(self, vector_store):

        self.embedding_model = EmbeddingModel()

        self.retriever = Retriever(vector_store)

        self.prompt_template = PromptTemplate()

        self.ollama_client = OllamaClient()

        self.memory_manager = ChatMemoryManager()

    def run(self, user_question):
        """
        Execute complete conversational RAG pipeline.
        """

        # ===================================
        # Step 1 → Create Query Embedding
        # ===================================

        query_embedding = (
            self.embedding_model
            .create_query_embedding(user_question)
        )

        # ===================================
        # Step 2 → Retrieve Relevant Chunks
        # ===================================

        retrieved_chunks = (
            self.retriever
            .retrieve_relevant_chunks(
                query_embedding=query_embedding,
                top_k=3
            )
        )

        # ===================================
        # Step 3 → Build Chat Context
        # ===================================

        chat_history = (
            self.memory_manager
            .build_chat_context(limit=5)
        )

        # ===================================
        # Step 4 → Build Final Prompt
        # ===================================

        final_prompt = (
            self.prompt_template
            .build_prompt(
                user_question=user_question,
                retrieved_chunks=retrieved_chunks,
                chat_history=chat_history
            )
        )

        # ===================================
        # Step 5 → Generate AI Response
        # ===================================

        response = (
            self.ollama_client
            .generate_response(final_prompt)
        )

        # ===================================
        # Step 6 → Save Conversation
        # ===================================

        self.memory_manager.save_conversation(
            user_question,
            response
        )

        return response
