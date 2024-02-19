import spacy
from scipy.spatial.distance import cosine

# Load spaCy model
nlp = spacy.load("en_core_web_md")

def cos_sim(object,query):
    """
    Evaluates the cosine similiarity between a object and query string
    """
    object_text = str(object)
    query_text = query

    # Tokenize and get word vectors for the object and query
    object_doc = nlp(object_text)
    query_doc = nlp(query_text)

    # Extract word vectors
    object_vec = object_doc.vector
    query_vec = query_doc.vector

    # Calculate cosine similarity
    similarity = 1 - cosine(object_vec, query_vec)
    return similarity

def get_time_dict(time_duration, time_dict):
    time_dict['start'] = time_duration.start
    time_dict['end'] = time_duration.end
    time_dict['duration_months'] = time_duration.duration_months


def assign_similarity_scores(recommended_resumes_details,query):
    
    results = []
    
    for candidate_details in recommended_resumes_details:
        
        candidate = dict()
        candidate['name'] = candidate_details['name']
        candidate['score'] = candidate_details['score']
        candidate['college'] = candidate_details['college'].dict()
        candidate['projects'] = []
        candidate['professional_experience'] =[]

        for i in range(len(candidate_details['projects'])):
            project = candidate_details['projects'][i]
            project.relevancy= cos_sim(project,query)
            
            time_dict = dict()
            get_time_dict(project.time_duration,time_dict)
            project_dict = project.dict()
            project_dict['time_duration'] = time_dict
            
            candidate['projects'].append(project_dict) 
            
        for i in range(len(candidate_details['professional_experience'])):
            experience = candidate_details['professional_experience'][i]
            experience.relevancy = cos_sim(experience,query)
            
            time_dict = dict()
            get_time_dict(experience.time_duration,time_dict)
            experience_dict = experience.dict()
            experience_dict['time_duration'] = time_dict
            
            candidate['professional_experience'].append(experience_dict)
        
        results.append(candidate)
            
    return results     
        