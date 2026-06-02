from fastapi import FastAPI
from app.routes.study import router as study_router
from app.routes.quiz import router as quiz_router

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"AI study assistant API is running"
    }

app.include_router(study_router)
app.include_router(quiz_router)
