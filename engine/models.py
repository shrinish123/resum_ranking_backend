from pydantic import BaseModel
from typing import List

class TimeDuration(BaseModel):
    """
    Data Model for Time Duration of the parent Data Model
    """
    start:str
    end:str
    duration_months:int
        

class Project(BaseModel):
    """
    Data Model for Project of the candidate 
    """
    project_title:str
    short_description:str
    tech_stack:str
    time_duration:TimeDuration
    relevancy:float

class Experience(BaseModel):
    """
    Data Model for Experience of the candidate  
    """
    role:str
    organisation:str
    short_description:str
    tech_stack:str
    time_duration:TimeDuration
    relevancy:float
    
class College(BaseModel):
    """
    Data Model for College of the candidate  
    """
    name:str
    branch:str
    degree:str
    CGPA:float
    start:str
    end:str


class Candidate(BaseModel):
    """
    Data Model for output of the particular candidate
    """
    name:str
    projects: List[Project]
    professional_experience:List[Experience]
    college:College
          
    