**bioRAG: Biology RAG System**

A Retrieval-Augmented Generation (RAG) system built for answering biology-related questions using custom data (books, PDFs, and notes).  
This project demonstrates how to preprocess biology content, build embeddings, store them in a FAISS index, and query them with an LLM for accurate answers.

---

**🚀 Features**
- 📄 PDF to text conversion (preprocessing step)
- 📚 Build and store embeddings with FAISS
- 🔎 Query biology content via RAG pipeline
- 🖥️ Simple demo app to interact with the model
- ⚡ Uses LangChain + FAISS + Hugging Face

---

**📂 Project Structure**
```
bioRAG/
│── app/
│ └── demo_app.py # Streamlit or FastAPI demo app
│
│── data/
│ └── biology_book.pdf # Source biology PDF
│
│── preprocessing/
│ └── pdf_to_text.py # Convert PDFs into plain text
│
│── rag/
│ ├── ask_question.py # Query the RAG system
│ ├── build_index.py # Build FAISS index
│ └── pycache/ # Cached files
│
│── biology_text.txt # Extracted text from PDF
│── biology_index/
│ ├── index.faiss # Vector DB (FAISS index)
│ └── index.pkl # FAISS metadata
│
│── requirements.txt # Python dependencies
```

---

**🛠️ Installation & Setup**

1. **Clone this repository**
```bash
git clone https://github.com/baqirbalti/bioRAG.git
cd bioRAG

**🛠️ Installation & Setup**

1. **Clone this repository**
```bash
git clone https://github.com/baqirbalti/bioRAG.git
cd bioRAG

2. **Create a virtual environment (optional but recommended)**

python -m venv myenv
source myenv/bin/activate   # Mac/Linux
myenv\Scripts\activate      # Windows

3. **Install dependencies**
pip install -r requirements.txt

**▶️ Usage**

1. **Preprocess PDFs**  
```bash
python preprocessing/pdf_to_text.py

2. **Build the FAISS Index**
```bash
python rag/build_index.py

3. **Ask Questions**
```bash
python rag/ask_question.py

4. **Run Demo App**
```bash
python app/demo_app.py

**📌 Requirements**

- Python 3.9+
- LangChain
- FAISS
- Hugging Face Transformers
- PyPDF2 / pdfminer / fitz (for PDF processing)
- Streamlit / FastAPI (for demo app)

(Install via `requirements.txt`)

---

**📖 Future Improvements**

- Add support for multiple PDFs and datasets
- Enhance the frontend (UI for live Q&A)
- Fine-tune with biology-specific LLMs
- Deploy online (Hugging Face Spaces / Streamlit Cloud / Docker)

---

**👨‍💻 Author**  
Developed by **Baqir Ali**  
📧 Email: **baqirbalti777@gmail.com**  
🔗 GitHub: [baqirbalti](https://github.com/baqirbalti)
