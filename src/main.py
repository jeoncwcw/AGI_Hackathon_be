from fastapi import FastAPI
from src.domain.recommendation import recommendation_router

app = FastAPI(
    title="AGI_Hackathon API",
    description="API for AGI_Hackathon",
    version="0.1.0",
)

@app.get("/hello")
def hello():
    return{"message": "안녕하세요 AGI_Hackathon에 오신 것을 환영합니다!"}

app.include_router(recommendation_router.router)