import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:5000"

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Document Q&A",
    page_icon="📄",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* Main App */
.stApp {
    background-color: #000000;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111111;
}

/* All Text */
h1, h2, h3, h4, h5, h6,
p, div, span, label {
    color: white !important;
}

/* Title */
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: white;
    margin-bottom: 10px;
}

.sub-title {
    color: #d1d5db;
    margin-bottom: 30px;
}

/* Answer Card */
.answer-card {
    background-color: #111111;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #333333;
    color: white;
    margin-bottom: 20px;
}

/* Source Card */
.source-card {
    background-color: #1a1a1a;
    padding: 15px;
    border-radius: 10px;
    color: white;
    border: 1px solid #333333;
}

/* Text Input */
.stTextInput input {
    background-color: #ffffff !important;
    color: black !important;
    border: 1px solid #444 !important;
}

/* Buttons */
.stButton > button {
    background-color: white;
    color: black;
    border-radius: 8px;
    font-weight: bold;
    border: none;
    width: 100%;
}

.stButton > button:hover {
    background-color: #dddddd;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background-color: #111111;
    border: 1px solid #333333;
    border-radius: 12px;
    padding: 15px;
}
            
/* Inner white upload box */
[data-testid="stFileUploaderDropzone"] {
    background-color: #ffffff !important;
    border: 2px dashed #cccccc !important;
    border-radius: 10px !important;
}

/* Upload text */
[data-testid="stFileUploaderDropzone"] * {
            
    color: black !important;
}
            
/* Expander */
.streamlit-expanderHeader {
    color: white !important;
}

.streamlit-expanderContent {
    color: white !important;
}

/* Success Box */
.stSuccess {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SESSION STATE
# ==================================================

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "sources" not in st.session_state:
    st.session_state.sources = []

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("## 📂 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file:

        st.success(
            f"Uploaded:\n\n{uploaded_file.name}"
        )

        if st.button(
            "Process PDF",
            use_container_width=True
        ):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }

            with st.spinner(
                "Processing PDF..."
            ):

                response = requests.post(
                    f"{BACKEND_URL}/upload",
                    files=files
                )

            if response.status_code == 200:

                data = response.json()

                st.success(
                    f"""
PDF Processed Successfully

Chunks Created:
{data['total_chunks']}
"""
                )

            else:

                st.error(
                    response.json()["error"]
                )

# ==================================================
# MAIN CONTENT
# ==================================================

st.markdown(
    """
<div class="main-title">
📄 Document Q&A with AI
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="sub-title">
Upload a PDF and ask questions about it.
</div>
""",
    unsafe_allow_html=True
)

st.markdown("## Ask a Question")

question = st.text_input(
    "",
    placeholder="What is BERT?"
)

if st.button("Ask"):

    if question.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        payload = {
            "question": question
        }

        with st.spinner(
            "Generating response..."
        ):

            response = requests.post(
                f"{BACKEND_URL}/chat",
                json=payload
            )

        if response.status_code == 200:

            data = response.json()

            st.session_state.answer = (
                data["response"]
            )

            st.session_state.sources = (
                data.get("sources", [])
            )

        else:

            st.error(
                response.json()["error"]
            )

# ==================================================
# ANSWER SECTION
# ==================================================

if st.session_state.answer:

    st.markdown("## Answer")

    st.markdown(
        f"""
<div class="answer-card">
{st.session_state.answer}
</div>
""",
        unsafe_allow_html=True
    )

# ==================================================
# SOURCES SECTION
# ==================================================

if st.session_state.sources:

    st.markdown("## Sources")

    for source in st.session_state.sources:

        with st.expander(
            f"Source {source['source_id']}"
        ):

            st.markdown(
                f"""
<div class="source-card">
{source['content']}
</div>
""",
                unsafe_allow_html=True
            )