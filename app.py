# jonsrags by @joncoded
# app.py
# input PDF documents and get a variable-sized summary
# using vector store + retriever + LLM with streamlit UI

# api keys in environment variables
from dotenv import load_dotenv
import os
load_dotenv()
key_model = os.getenv("GROQ_API_KEY").strip()
key_vecdb = os.getenv("PINECONE_API_KEY").strip()

# connect to vector DB
from pinecone import Pinecone
pinecone = Pinecone(api_key=key_vecdb, environment="us-west1-gcp")
index_name = "jonsrags"
host = "https://jonsrags-su5cgy0.svc.aped-4627-b74a.pinecone.io"
index = pinecone.Index(index_name=index_name, host=host)

# connect to LLM
from openai import OpenAI
client = OpenAI(
  api_key=key_model,
  base_url="https://api.groq.com/openai/v1"
)

# set up streamlit UI
import streamlit as st
st.set_page_config(page_title="jonsrags (by @joncoded)", page_icon="📄")
st.title("jonsrags")