import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline

# -------------------------------
# Paths & settings
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # rag/
INDEX_DIR = os.path.join(BASE_DIR, "../biology_index")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "google/flan-t5-small"  # You can replace with another HF model

# -------------------------------
# Load FAISS retriever
# -------------------------------
def load_retriever():
    if not os.path.exists(INDEX_DIR):
        raise FileNotFoundError(f"[❌] FAISS index not found: {INDEX_DIR}")

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    db = FAISS.load_local(
        INDEX_DIR,
        embeddings,
        allow_dangerous_deserialization=True  # Needed for FAISS pickle
    )
    # top-5 relevant chunks
    retriever = db.as_retriever(search_kwargs={"k": 5})
    return retriever

# -------------------------------
# Build LLM QA chain
# -------------------------------
def ask_question(question: str):
    retriever = load_retriever()

    # HuggingFace pipeline for text-generation (PyTorch only)
    pipe = pipeline(
        "text2text-generation",
        model=LLM_MODEL,
        device=0 if os.name != "nt" else -1,  # CPU if Windows
        framework="pt",  # Force PyTorch to avoid TF DLL issues
        max_length=512,  # truncate long sequences
        clean_up_tokenization_spaces=True
    )
    llm = HuggingFacePipeline(pipeline=pipe)

    # Use map_reduce chain for cleaner summarization
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="map_reduce",  # combine retrieved chunks intelligently
        retriever=retriever
    )

    try:
        answer = qa.run(question)
    except Exception as e:
        answer = f"[❌ Error in generating answer]: {e}"
    return answer

# -------------------------------
# Main (for console testing)
# -------------------------------
if __name__ == "__main__":
    question = input("Enter your biology question: ")
    answer = ask_question(question)
    print("\n[💡 Answer]:", answer)
