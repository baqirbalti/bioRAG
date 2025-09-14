import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

# -------------------------------
# Paths
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # rag/
TEXT_FILE = os.path.join(BASE_DIR, "../biology_text.txt")  # Main folder
INDEX_DIR = os.path.join(BASE_DIR, "../biology_index")  # FAISS DB folder
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def load_text(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[❌] Text file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def build_index():
    # Load text
    text = load_text(TEXT_FILE)
    print(f"[📖] Loaded text, length: {len(text)}")

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = splitter.split_text(text)
    print(f"[✂️] Split into {len(chunks)} chunks")

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    # Build FAISS index
    db = FAISS.from_texts(chunks, embeddings)

    # Save index
    if not os.path.exists(INDEX_DIR):
        os.makedirs(INDEX_DIR)
    db.save_local(INDEX_DIR)
    print(f"[✅] FAISS index saved at: {INDEX_DIR}")

if __name__ == "__main__":
    build_index()
