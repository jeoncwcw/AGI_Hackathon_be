from pydantic import BaseModel
from typing import List
from datetime import datetime

class UserInfo(BaseModel):
    age: int
    income: int
    region: str
    industry: str
    user_type: str  # 예: 청년, 신혼부부, 소상공인 등

class PolicyRecommendation(BaseModel):
    policy_id: int
    title: str
    brief: str

class RecommendationResponse(BaseModel):
    recommendations: List[PolicyRecommendation]
    generated_at: datetime
