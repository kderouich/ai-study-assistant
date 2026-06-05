from pydantic import BaseModel
from typing import Dict, Literal

class StudyRequest(BaseModel):
    topic: str
    difficulty: str
    explanation_type: str
    language: str

class QuizRequest(BaseModel):
    topic: str
    difficulty: Literal["beginner", "intermediate",  "advanced"]
    num_questions: int
    language: str

class QuizEvaluationRequest(BaseModel):
    topic: str
    quiz: list
    user_answers: Dict[str, str]
    language: str