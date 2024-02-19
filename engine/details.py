import os
from dotenv import load_dotenv
from llama_index.core import StorageContext,VectorStoreIndex,load_index_from_storage
from llama_index.core.readers import SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from engine.models import Candidate


INDEXES_DIR = os.path.join(os.getcwd(), './engine/indexes')
OPENAI_MODEL = 'gpt-3.5-turbo-0613'

load_dotenv()
llm = OpenAI(model=OPENAI_MODEL, temperature=0.1)
indexes_dir = INDEXES_DIR
query = 'Give me the name of the candidate, list all the project names of the candidate, list all the experiences of the candidate, also get the details of the college/university of the candidate.\
        If you arent able to get the field return it as Not Specified and return all the dates in MM-YYYY format and mark the relevancy fields with value of 0.0'


def get_index(data,index_name):
    index = None
    
    if not os.path.exists(index_name):
        index = VectorStoreIndex.from_documents(data,show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name))
    
    return index 

def get_details(resumes):
    
    os.makedirs(INDEXES_DIR, exist_ok=True)
    results = []
    
    for resume in resumes:
        resume_path = resume['source']
        reader =  SimpleDirectoryReader(
        input_files=[resume_path]
        )
        resume_data = reader.load_data()
        file_name = os.path.basename(resume_path)
        index_path = os.path.join(indexes_dir, file_name)
        resume_index = get_index(resume_data,os.path.join(indexes_dir, index_path))
        resume_engine = resume_index.as_query_engine(output_cls=Candidate, response_mode="compact", llm=llm)
        response = resume_engine.query(query)
        details = response.response.__dict__
        details['score'] = resume['score']
        results.append(details)

    return results
    
