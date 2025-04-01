from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from domain.recommendation import schema, crud
from database import get_db

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)

@router.post("/", response_model=schema.RecommendationResponse)
def get_recommendations(user_info: schema.UserInfo, db: Session = Depends(get_db)):
    recommendations = crud.recommend_support_policies(user_info, db)
    return schema.RecommendationResponse(
        recommendations=recommendations,
        generated_at=datetime.now()
    )
