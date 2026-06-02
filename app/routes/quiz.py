import json
from app.models.schemas import (QuizRequest, QuizEvaluationRequest)
from fastapi import APIRouter
from app.services.ai_service import call_ai

router = APIRouter()

@router.post("/generate-quiz")
def generate_quiz(data: QuizRequest):
           
    messages = [
            {
                "role": "system",
                "content": """
                You are a study assistant that creates quizzes.

                Return ONLY valid JSON.
                Do not add markdown.
                Do not add explanations.
                Return parseable JSON only.
                """
            },
            {
                "role": "user",
                "content": f"""
                Create a {data.difficulty} quiz about {data.topic}.

                Number of questions: {data.num_questions}

                Language: {data.language}

                Each question must have 4 options.                """
            }
        ]
    result = call_ai("nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free", messages = messages)
    try:
        ai_response = result["choices"][0]["message"]["content"]
    except Exception as e:
        return {"error": str(e)}
    try:
         return json.loads(ai_response)
    except Exception:
        return { "raw_response": ai_response }
    
@router.post("/evaluate-quiz")
def evaluate_quiz(data: QuizEvaluationRequest):

        messages = [
            {
                "role":"system",
                "content": """ 
                You are a study assistant.

                Evaluate the user's quiz answers.

                Return ONLY valid JSON.

                Format:
                {
                    "score": "2/3",
                    "feedback": "",
                    "corrections": [
                        {
                            "question": "",
                            "user_answer": "",
                            "correct_answer": "",
                            "explanation": ""
                        }
                    ]
                }

                Do not add markdown.
                Do not add explanations outside JSON.
                Return parseable JSON only.
                """
            },
            {
                "role":"user",
                "content": f"""
                Topic: {data.topic}
                quiz: {json.dumps(data.quiz, indent=2)}
                user answers: {json.dumps(data.user_answers, indent=2)}
                language: {data.language}
                Evaluate the quiz and explain mistakes biefly.
                """
            }
        ]
        result = call_ai("nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free", messages = messages)
        try:
            ai_response = result["choices"][0]["message"]["content"]
        except Exception as e:
            return {"error": str(e)}
        try:
            return json.loads(ai_response)
        except Exception:
            return { "raw_response": ai_response }