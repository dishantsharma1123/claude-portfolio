import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag_engine import get_vector_store

def run_ingestion():
    file_path = os.path.join("data", "bio.md")
    if not os.path.exists(file_path):
        print("Error: Add target data markdown to data/bio.md first.")
        return
        
    loader = TextLoader(file_path)
    documents = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = splitter.split_documents(documents)
    
    store = get_vector_store()
    store.add_documents(docs)
    print(f"Successfully processed and embedded {len(docs)} data chunks into pgvector.")

if __name__ == "__main__":
    run_ingestion()