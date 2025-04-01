from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.policy import schema, crud
from database import get_db

router = APIRouter(
    prefix="/policies",
    tags=["Policies"]
)

# 전체 지원금 조회 API
@router.get("/", response_model=schema.PolicyList)
def read_policies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    policies, total = crud.get_policies(db, skip=skip, limit=limit)
    return schema.PolicyList(policies=policies, total=total)

# 특정 지원금 조회 API
@router.get("/{policy_id}", response_model=schema.Policy)
def read_policy(policy_id: int, db: Session = Depends(get_db)):
    policy = crud.get_policy(db, policy_id)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    return policy

# 지원금 생성 API (관리자용)
@router.post("/", response_model=schema.Policy)
def create_policy(policy: schema.PolicyCreate, db: Session = Depends(get_db)):
    return crud.create_policy(db, policy)
