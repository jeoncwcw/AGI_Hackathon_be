from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from src.domain.recommendation import recommendation_schema
from src.database import get_db
from src.domain.recommendation import recommendation_crud

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)

@router.post("/", response_model=recommendation_schema.RecommendationResponse)
def get_recommendations(user_info: recommendation_schema.UserInfo, db: Session = Depends(get_db)):
    recommendations = recommendation_crud.recommend_support_policies(user_info, db)
    return recommendation_schema.RecommendationResponse(
        recommendations=recommendations,
        generated_at=datetime.now()
    )
