from fastapi import APIRouter
from app.models.schemas import StudyRequest
from app.services.ai_service import call_ai
router = APIRouter()

@router.post("/ask-ai")
def ask_ai(data: StudyRequest):
    messages = [
            {"role": "system", "content": "You are a helpful study assistant."},
            {"role": "user", "content": f"""
            explain topic: {data.topic}
            difficulty: {data.difficulty}
            explanation type: {data.explanation_type}
            language: {data.language}"
            Keep the explanation clear and adapted to the requested level
            """
            }
        ]
    result = call_ai("nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free", messages = messages)

    # safe access into response
    try:
        answer = result["choices"][0]["message"]["content"]
    except Exception:
        return {
            "error": result
        }

    return {"answer": answer}