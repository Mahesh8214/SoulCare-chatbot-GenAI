# chatbot/cores.py
import os
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from chatbot.prompts import DEFAULT_PROMPT
from src.config import GROQ_API_KEY, LLM_MODEL, EMBEDDING_MODEL, DATA_DIR, DB_DIR

def initialize_llm():
    return ChatGroq(
        temperature=0,
        groq_api_key=GROQ_API_KEY,
        model_name=LLM_MODEL
    )

def create_vector_db():
    loader = DirectoryLoader(DATA_DIR, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    embeddings = HuggingFaceBgeEmbeddings(model_name=EMBEDDING_MODEL)
    vector_db = Chroma.from_documents(texts, embeddings, persist_directory=DB_DIR)
    vector_db.persist()
    print("✅ Chroma vector store created and saved.")
    return vector_db

def load_or_create_vector_db():
    if not os.path.exists(DB_DIR):
        return create_vector_db()
    embeddings = HuggingFaceBgeEmbeddings(model_name=EMBEDDING_MODEL)
    return Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

def setup_qa_chain(vector_db, llm):
    retriever = vector_db.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": DEFAULT_PROMPT}
    )
    return qa_chain
