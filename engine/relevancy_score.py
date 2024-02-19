from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()


def load_docs(file_path):
  loader = PyMuPDFLoader(file_path)
  documents = loader.load()
  return documents

def split_docs(documents, chunk_size=1000, chunk_overlap=0):
  text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

def get_relevancy_score(file_path:str,query:str):
    
    documents = load_docs(file_path) 
    splitted_docs = split_docs(documents)
    
    embeddings = OpenAIEmbeddings()
    
    db = FAISS.from_documents(splitted_docs, embeddings)
    docs_and_scores = db.similarity_search_with_score(query)
    
    faiss_score = 0

    for i in range(len(docs_and_scores)):
      doc, score = docs_and_scores[i]
      faiss_score += (1-score)
      print(f'{1-score}')
    
    faiss_score = faiss_score/len(docs_and_scores)  
    
    print(f',{faiss_score=}')
    
    return faiss_score

