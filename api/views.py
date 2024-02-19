import os 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from engine.main import process_resumes_engine

RESUME_DIR = os.path.join(os.getcwd(), './resumes')

@api_view(['POST'])
def process_resumes(request):
    job_role = request.data.get('jobRole', {})
    job_description = request.data.get('jobDescription', {})
    uploaded_files = request.FILES.getlist('files')
   
    print(f'{job_role=},{job_description=}, {uploaded_files=}')
    
    os.makedirs(RESUME_DIR, exist_ok=True)

    # Save each file to the Resume directory
    file_paths = []
    for uploaded_file in uploaded_files:
        file_path = os.path.join(RESUME_DIR, uploaded_file.name)
        with open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        file_paths.append(file_path)
        

    results = process_resumes_engine(job_role,job_description,file_paths)
    
    return Response(results, status=status.HTTP_201_CREATED)
