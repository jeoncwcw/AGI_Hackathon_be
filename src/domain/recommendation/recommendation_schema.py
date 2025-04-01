from pydantic import BaseModel
from typing import List
from datetime import datetime

class UserInfo(BaseModel):
    age: int
    income: int
    region: str
    industry: str
    user_type: str  # ��: û��, ��ȥ�κ�, �һ���� ��

class PolicyRecommendation(BaseModel):
    policy_id: int
    title: str
    brief: str

class RecommendationResponse(BaseModel):
    recommendations: List[PolicyRecommendation]
    generated_at: datetime
