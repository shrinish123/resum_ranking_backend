# Resume Ranking Backend

Resume Ranking Backend is built with Django-Rest-Framework and with help of OpenAI Models along with LangChain and Llamma-Index.

# About 

The backend currently has a single api endpoint which accepts job_role,job_description and a list of files and with help of OpenAI models 
assigns a relevancy score to each resume and also responds with the details of the recommended resumes


# Setting up the Project

* Make sure you have python installed.
* Clone the repository to your local machine
```bash
 git clone https://github.com/<your-github-username>/resume_ranking_backend.git
```
* Change directory to resume_ranking_backend
 ```bash
 cd  resume_ranking_backend
 ```
* Create a virtual environment
 ```bash
 python -m venv venv
 ```
* Activate the virtual environment (For Windows)
 ```bash
 .\venv\scripts\activate  
 ``` 
* Install the dependencies : 
 ```bash
 pip install -r requirements.txt
 ```
* Configure the .env file by copy pasting the .env.example file and create a new .env file and add your API keys as required 

* To start running project locally:
```bash
 python manage.py runserver
 ```
* The server would be up and running on http://localhost:8000