from engine.relevancy_score import get_relevancy_score
from dotenv import load_dotenv

SIMILARITY_THRESHOLD = 0.5

load_dotenv()


def get_recommended_resumes(resume_files,query):
    recommended_resumes = []
    non_recommended_resumes = []

    for filepath in resume_files:
        score = get_relevancy_score(filepath,query)
        
        if score >= SIMILARITY_THRESHOLD:
            recommended_resumes.append({
                "score":score,
                "source":filepath
            })
        else:
            non_recommended_resumes.append({
                "score":score,
                "source":filepath
            })
        
    recommended_resumes.sort(key=lambda resume: resume['score'], reverse=True)
    non_recommended_resumes.sort(key=lambda resume: resume['score'], reverse=True)

    return (recommended_resumes,non_recommended_resumes)



