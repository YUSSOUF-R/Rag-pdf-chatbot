from flask import Blueprint, request, jsonify
import os

from services.pdf_loader import PDFLoader
from services.text_splitter import TextSplitter
from services.embedding import EmbeddingModel
from services.vector_store import VectorStore
from services.rag_chain import RAGChain

chat_bp = Blueprint("chat_bp", __name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

vector_store = VectorStore()


@chat_bp.route("/upload", methods=["POST"])
def upload_pdf():

    try:

        if "file" not in request.files:
            return jsonify({
                "error": "No file uploaded"
            }), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({
                "error": "Empty filename"
            }), 400

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        file.save(file_path)

        # Load PDF
        pdf_loader = PDFLoader()

        raw_text = pdf_loader.extract_text_from_pdf(
            file_path
        )

        # Split text
        text_splitter = TextSplitter()

        chunks = text_splitter.split_text(raw_text)

        # Create embeddings
        embedding_model = EmbeddingModel()

        embeddings = embedding_model.create_embeddings(
            chunks
        )

        # Store vectors
        vector_store.create_vector_store(
            embeddings,
            chunks
        )

        return jsonify({
            "message": "PDF processed successfully",
            "total_chunks": len(chunks)
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@chat_bp.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        user_question = data.get("question")

        if not user_question:

            return jsonify({
                "error": "Question is required"
            }), 400

        vector_store.load_index()

        rag_chain = RAGChain(vector_store)

        query_embedding = (
            rag_chain.embedding_model
            .create_query_embedding(user_question)
        )

        retrieved_chunks = (
            rag_chain.retriever
            .retrieve_relevant_chunks(
                query_embedding=query_embedding,
                top_k=3
            )
        )

        response = rag_chain.run(
            user_question
        )

        return jsonify({
            "question": user_question,
            "response": response,
            "sources": retrieved_chunks
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500