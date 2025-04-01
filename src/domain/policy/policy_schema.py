from pydantic import BaseModel
from datetime import datetime
from typing import List

# 기본 스키마 (베이스)
class PolicyBase(BaseModel):
    title: str
    content: str

# 데이터 생성 시 사용할 스키마
class PolicyCreate(PolicyBase):
    pass

# DB에서 읽어올 때 사용할 스키마
class Policy(PolicyBase):
    id: int

    class Config:
        orm_mode = True

# 여러 정책 리스트 반환 시 사용
class PolicyList(BaseModel):
    policies: List[Policy]
    total: int
