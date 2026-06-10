# 📄 RAG-Based AI PDF Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions based on their content.

The application extracts text from uploaded PDFs, generates vector embeddings, stores them in a FAISS vector database, retrieves relevant document chunks, and uses a local Ollama LLM to generate context-aware answers.

---

## 🚀 Features

* Upload PDF documents
* Extract and process PDF text
* Intelligent text chunking
* Sentence Transformer embeddings
* FAISS vector similarity search
* Retrieval-Augmented Generation (RAG)
* Conversational memory using MySQL
* Local LLM inference using Ollama
* Streamlit-based user interface
* Source citation for retrieved answers

---

## 🏗️ Project Architecture

```text
User Question
      │
      ▼
Sentence Embedding
      │
      ▼
FAISS Vector Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
Prompt Construction
      │
      ▼
Ollama LLM
      │
      ▼
Generated Answer
```

---

## 📂 Project Structure

```text
rag-pdf-chatbot/
│
├── app.py
├── requirements.txt
├── .env
│
├── routes/
│   ├── __init__.py
│   └── chat_routes.py
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── models.py
│
├── services/
│   ├── __init__.py
│   ├── embedding.py
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompt_template.py
│   ├── ollama_client.py
│   ├── rag_chain.py
│   └── chat_memory_manager.py
│
├── frontend/
│   └── streamlit_app.py
│
├── uploads/
├── vectorstore/
└── logs/
```

---

## 🛠️ Technologies Used

### Backend

* Flask
* Python

### Frontend

* Streamlit

### AI & RAG

* Ollama
* Llama 3
* Sentence Transformers
* FAISS

### Database

* MySQL

### PDF Processing

* PyMuPDF (fitz)

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git

cd rag-pdf-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Configure Environment Variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=rag_chatbot

OLLAMA_MODEL=llama3
```

---

## 🗄️ MySQL Setup

Create database:

```sql
CREATE DATABASE rag_chatbot;
```

The application automatically creates the required tables during execution.

---

## 🤖 Install Ollama

Download:

https://ollama.com

Pull the model:

```bash
ollama pull llama3
```

Run Ollama:

```bash
ollama serve
```

---

## ▶️ Run Backend

```bash
python app.py
```

Backend runs on:

```text
http://localhost:5000
```

---

## 🎨 Run Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

## 📖 How It Works

### PDF Upload

1. Upload a PDF document.
2. Text is extracted using PyMuPDF.
3. Text is split into chunks.
4. Embeddings are generated.
5. Embeddings are stored in FAISS.

### Question Answering

1. User submits a question.
2. Query embedding is generated.
3. Relevant chunks are retrieved from FAISS.
4. Previous chat history is loaded from MySQL.
5. Context-aware prompt is constructed.
6. Ollama generates an answer.
7. Conversation is stored in the database.

---

## 📸 Screenshots

Add screenshots of:

* PDF Upload Interface
* Question Answering Interface
* Source Retrieval Results

---

## 🔮 Future Improvements

* Multi-PDF Support
* User Authentication
* Chat Sessions
* Source Page References
* Hybrid Search (BM25 + Vector Search)
* Re-ranking Models
* Streaming Responses
* Cloud Deployment

---

## 👨‍💻 Author

YUSSOUF R

---

## 📜 License

This project is developed for educational and learning purposes.
