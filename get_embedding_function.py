from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_ollama import OllamaEmbeddings

def get_embedding_function(): #assinging metadata tag to a chunk
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings