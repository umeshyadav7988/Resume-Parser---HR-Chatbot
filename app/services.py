from .models import CandidateInfo
from .utils import ask_llm
from typing import List

# In-memory storage
candidate_database: List[CandidateInfo] = []

def parse_resume(file_content: str) -> CandidateInfo:
    prompt = f"""
    Extract the following information from this resume text:
    First Name, Last Name, Email, Phone, Education (list), Work Experience (summary), Skills (list), Current Position, Years of Experience.
    
    Resume Text:
    {file_content}
    
    Respond ONLY in JSON format like this:
    {{
      "first_name": "",
      "last_name": "",
      "email": "",
      "phone": "",
      "education": [],
      "work_experience": "",
      "skills": [],
      "current_position": "",
      "years_of_experience": 0
    }}
    """
    json_response = ask_llm(prompt)
    import json
    data = json.loads(json_response)
    return CandidateInfo(**data)

def chatbot_query(question: str) -> str:
    # Build a context from all candidates
    context = ""
    for idx, candidate in enumerate(candidate_database):
        context += f"Candidate {idx+1}: {candidate.dict()}\n\n"

    prompt = f"""
    You are an HR Assistant AI.

    Using the following candidate data:
    {context}

    Answer the HR question:
    {question}
    """

    answer = ask_llm(prompt)
    return answer
