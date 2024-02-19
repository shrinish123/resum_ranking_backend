import os
from engine.recommended_resumes import get_recommended_resumes
from engine.details import get_details
from engine.cosine_similarity import assign_similarity_scores

RESUME_DIR = os.path.join(os.getcwd(), './resumes')


def process_resumes_engine(job_role,job_description,file_paths):
    
    query = f'Job role is {job_role} and Job description is : {job_description}'
    
    # Get recommended resumes with a similarity threshold 
    recommended_resumes,non_recommended_resumes = get_recommended_resumes(file_paths,query)
    
    #Get all details of the recommended profiles and assign relevancy_scores for all of them 
    recommended_resumes_details = get_details(recommended_resumes)

    # Get and assign relevancy scores for projects and experiences
    recommended_resumes_details = assign_similarity_scores(recommended_resumes_details,query)
    
    results = dict()
    results['recommended_candidates'] = recommended_resumes_details
    results['non_recommended_candidates'] = non_recommended_resumes
    
    return results
    
    
    
    
    
    
    
    
    
    
    
    