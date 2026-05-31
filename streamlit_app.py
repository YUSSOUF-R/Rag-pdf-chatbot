import streamlit as st
import requests


BACKEND_URL = "http://127.0.0.1:5000"


st.set_page_config(
    page_title="RAG PDF Chatbot",
    layout="wide"
)

st.title("📘 RAG-Based AI PDF Chatbot")


# ===================================
# Session State
# ===================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ===================================
# Upload PDF Section
# ===================================

st.header("📂 Upload PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    with st.spinner("Processing PDF..."):

        response = requests.post(
            f"{BACKEND_URL}/upload",
            files=files
        )

    if response.status_code == 200:

        data = response.json()

        st.success("PDF uploaded successfully!")

        st.write(
            f"Total Chunks Created: {data['total_chunks']}"
        )

    else:

        st.error(response.json()["error"])


# ===================================
# Chat Section
# ===================================

st.header("💬 Chat with AI")

user_question = st.text_input(
    "Ask a question from your PDF"
)

if st.button("Ask AI"):

    if user_question.strip() == "":

        st.warning("Please enter a question.")

    else:

        payload = {
            "question": user_question
        }

        with st.spinner("Generating AI response..."):

            response = requests.post(
                f"{BACKEND_URL}/chat",
                json=payload
            )

        if response.status_code == 200:

            data = response.json()

            ai_response = data["response"]

            retrieved_sources = data.get(
                "sources",
                []
            )

            # Save chat history
            st.session_state.chat_history.append({
                "question": user_question,
                "answer": ai_response,
                "sources": retrieved_sources
            })

        else:

            st.error(response.json()["error"])


# ===================================
# Display Chat History
# ===================================

st.header("🧠 Conversation History")

for chat in reversed(st.session_state.chat_history):

    # User Message
    with st.chat_message("user"):
        st.write(chat["question"])

    # AI Message
    with st.chat_message("assistant"):

        st.write(chat["answer"])

        # Display Sources
        if chat["sources"]:

            with st.expander("📚 View Sources"):

                for source in chat["sources"]:

                    st.markdown(
                        f"""
### Source {source['source_id']}

{source['content']}
"""
                    )