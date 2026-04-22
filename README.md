# Own-AI-Clone
An intelligent AI Clone of Karthik Yadav built using Retrieval-Augmented Generation (RAG).
This application answers questions based on a custom knowledge base (PDF) using semantic search and LLM reasoning.

🚀 Live Demo

👉https://karthik-yadav-ai-clone.streamlit.app
🧠 Features
🔍 RAG Pipeline (Retrieval-Augmented Generation)
📄 Extracts knowledge from PDF
🧩 Smart text chunking & embeddings
🗂 Vector database (ChromaDB) for semantic search
💬 Context-aware AI responses
🧠 Uses LLM (Groq API) for generation
⚡ Fast and interactive UI with Streamlit
📊 Response relevance scoring (semantic similarity)
🏗️ Architecture
PDF → Text Extraction → Chunking → Embeddings → ChromaDB
User Query → Embedding → Similarity Search → Context Retrieval
→ LLM (Groq) → Final Answer
🛠️ Tech Stack
Frontend/UI: Streamlit
Backend: Python
LLM: Groq (LLaMA / Gemma models)
Embeddings: HuggingFace Sentence Transformers
Vector DB: ChromaDB
PDF Processing: PyPDF2
📂 Project Structure
.
├── main.py
├── requirements.txt
├── knowledge_base/
│   └── dc_kc.pdf
├── chroma_db/
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the repo
git clone https://github.com/yourusername/ai-clone.git
cd ai-clone
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Add environment variables

Create a .env file:

GROQ_API_KEY=your_api_key_here
MODEL_NAME=llama-3.1-8b-instant
5️⃣ Run the app
streamlit run main.py
📊 How It Works
📄 PDF is loaded and converted into text
✂️ Text is split into chunks
🧠 Each chunk is converted into embeddings
🗂 Stored in ChromaDB
❓ User asks a question
🔍 Relevant chunks are retrieved
🤖 LLM generates answer using context
🔥 Future Improvements
📁 Upload multiple PDFs
📌 Source citation (show exact document chunk)
💬 Streaming responses (ChatGPT-like typing)
🔐 Authentication system
🌐 Multi-user support
