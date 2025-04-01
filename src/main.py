from fastapi import FastAPI
from src.domain.recommendation import recommendation_router
from src.domain.policy import policy_router

app = FastAPI(
    title="AGI_Hackathon API",
    description="API for AGI_Hackathon",
    version="0.1.0",
)

@app.get("/hello")
def hello():
    return{"message": "This is AGI_Hackathon API"}

app.include_router(recommendation_router.router)
app.include_router(policy_router.router)