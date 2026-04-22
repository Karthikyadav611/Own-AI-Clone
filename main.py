import streamlit as st
import os
import chromadb
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from sentence_transformers import SentenceTransformer, util
from dotenv import load_dotenv

# Load env
load_dotenv()

# Config
PDF_FILE_PATH = "./knowledge_base/db_kc.pdf"
CHROMA_DB_PATH = "./chroma_db"
COLLECTION_NAME = "ai_knowledge_base"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.1-8b-instant")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ---------- PDF ----------
def load_pdf(file_path):
    reader = PdfReader(file_path)
    return "".join([page.extract_text() or "" for page in reader.pages])

# ---------- Chunk ----------
def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    return splitter.split_text(text)

# ---------- Embedding ----------
def get_embedding_model():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

# ---------- Chroma ----------
def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    return client.get_or_create_collection(name=COLLECTION_NAME)

# ---------- Store ----------
def store_embeddings(chunks, collection, embed_model):
    existing_docs = set(collection.get(include=["documents"])["documents"])

    new_chunks = [c for c in chunks if c not in existing_docs]

    if not new_chunks:
        return

    ids = [str(i) for i in range(len(existing_docs), len(existing_docs) + len(new_chunks))]
    embeddings = embed_model.embed_documents(new_chunks)

    collection.add(
        ids=ids,
        documents=new_chunks,
        embeddings=embeddings
    )

# ---------- Retrieve ----------
def retrieve(query, collection, embed_model, top_k=3):
    q_emb = embed_model.embed_query(query)
    results = collection.query(
        query_embeddings=[q_emb],
        n_results=top_k,
        include=["documents"]
    )
    return results["documents"][0] if results["documents"] else []

# ---------- LLM ----------
def get_llm():
    return ChatGroq(
        model_name=LLM_MODEL_NAME,
        temperature=0.5,
        groq_api_key=GROQ_API_KEY
    )

# ---------- Setup ----------
@st.cache_resource
def setup():
    text = load_pdf(PDF_FILE_PATH)
    chunks = chunk_text(text)

    embed_model = get_embedding_model()
    collection = get_collection()

    store_embeddings(chunks, collection, embed_model)

    semantic_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    llm = get_llm()

    return embed_model, collection, semantic_model, llm

# ---------- Evaluation ----------
def evaluate(response, context, model):
    if not context:
        return 0.0
    context_text = " ".join(context)

    r_emb = model.encode(response, convert_to_tensor=True)
    c_emb = model.encode(context_text, convert_to_tensor=True)

    return util.pytorch_cos_sim(r_emb, c_emb)[0][0].item()

# ---------- UI ----------
st.set_page_config(page_title="Karthik AI Clone")
st.title("🤖 Karthik Yadav AI Clone")

if "messages" not in st.session_state:
    st.session_state.messages = []

embed_model, collection, semantic_model, llm = setup()

# show history
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# ---------- Chat ----------
if prompt := st.chat_input("Ask something..."):

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # format history
    history_text = "\n".join(
        [f"{m['role']}: {m['content']}" for m in st.session_state.messages[-6:]]
    )

    # retrieve
    context = retrieve(prompt, collection, embed_model)

    context_text = "\n".join(context)

    # system prompt (fixed)
    system_prompt = """
You are an AI clone who is the personality mimic of Karthik Yadav, an Information Science and Engineering student and aspiring full-stack developer with strong interest in AI and web development.

Rules:
- Use the provided context to answer
- If answer is not in context, say "I don't know"
- Keep answers clear and concise
- Be natural and human-like
"""

    user_prompt = f"""
Context:
{context_text}

Chat History:
{history_text}

Question:
{prompt}
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]

    response = llm.invoke(messages)
    answer = response.content

    score = evaluate(answer, context, semantic_model)

    with st.chat_message("assistant"):
        st.markdown(answer)
        st.caption(f"Relevance Score: {score:.2f}")

    st.session_state.messages.append({"role": "assistant", "content": answer})