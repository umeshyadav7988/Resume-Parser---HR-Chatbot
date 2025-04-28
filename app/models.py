from pydantic import BaseModel
from typing import List

class CandidateInfo(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    education: List[str]
    work_experience: str
    skills: List[str]
    current_position: str
    years_of_experience: float
