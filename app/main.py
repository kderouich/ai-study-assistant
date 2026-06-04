from fastapi import FastAPI
from app.routes.study import router as study_router
from app.routes.quiz import router as quiz_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message":"AI study assistant API is running"
    }

app.include_router(study_router)
app.include_router(quiz_router)
