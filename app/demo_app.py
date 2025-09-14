import streamlit as st
import sys
import os

# Make sure rag folder is in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAG_DIR = os.path.join(BASE_DIR, "../rag")
if RAG_DIR not in sys.path:
    sys.path.append(RAG_DIR)

from ask_question import ask_question  # Now the import should work

# Streamlit App
st.set_page_config(page_title="Biology QA", layout="centered")
st.title("🧬 Biology Question Answering")

question = st.text_input("Enter your biology question:")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question first!")
    else:
        with st.spinner("Fetching answer..."):
            answer = ask_question(question)
        st.success(answer)
