# 🤖 Own-AI-Clone

An intelligent **AI Clone of Karthik Yadav** built using **Retrieval-Augmented Generation (RAG)**.
This application answers questions based on a custom knowledge base (PDF) using semantic search and LLM reasoning.

---

## 🚀 Live Demo

👉 https://karthik-yadav-ai-clone.streamlit.app

---

## 🧠 Features

* 🔍 **RAG Pipeline** (Retrieval-Augmented Generation)
* 📄 Extracts knowledge from PDF
* 🧩 Smart text chunking & embeddings
* 🗂 **Vector database (ChromaDB)** for semantic search
* 💬 Context-aware AI responses
* 🧠 Uses **LLM (Groq API)** for generation
* ⚡ Fast and interactive UI with Streamlit
* 📊 Response relevance scoring (semantic similarity)

---

## 🏗️ Architecture

```
PDF → Text Extraction → Chunking → Embeddings → ChromaDB  
User Query → Embedding → Similarity Search → Context Retrieval  
→ LLM (Groq) → Final Answer
```

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **LLM:** Groq (LLaMA / Gemma models)
* **Embeddings:** HuggingFace Sentence Transformers
* **Vector DB:** ChromaDB
* **PDF Processing:** PyPDF2

---

## 📂 Project Structure

```
.
├── main.py
├── requirements.txt
├── knowledge_base/
│   └── dc_kc.pdf
├── chroma_db/
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-clone.git
cd ai-clone
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
MODEL_NAME=llama-3.1-8b-instant
```

---

### 5️⃣ Run the app

```bash
streamlit run main.py
```

---

## 📊 How It Works

1. 📄 PDF is loaded and converted into text
2. ✂️ Text is split into chunks
3. 🧠 Each chunk is converted into embeddings
4. 🗂 Stored in ChromaDB
5. ❓ User asks a question
6. 🔍 Relevant chunks are retrieved
7. 🤖 LLM generates answer using context

---

## 🔥 Future Improvements

* 📁 Upload multiple PDFs
* 📌 Source citation (show exact document chunk)
* 💬 Streaming responses (ChatGPT-like typing)
* 🔐 Authentication system
* 🌐 Multi-user support

---

## 👤 Author

**Karthik Yadav**
🎓 B.E Information Science & Engineering
💻 Aspiring Full-Stack & AI Developer

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
