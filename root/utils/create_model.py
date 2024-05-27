import os
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def embed_store_and_model(chunks):
    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
    library = FAISS.from_documents(chunks, embeddings)
    # library.save_local('vectorstore')
    # library = FAISS.load_local('vectorstore', embeddings)
    qna_bot = RetrievalQA.from_chain_type(llm=OpenAI(api_key=OPENAI_API_KEY), chain_type='stuff', retriever=library.as_retriever())

    return qna_bot