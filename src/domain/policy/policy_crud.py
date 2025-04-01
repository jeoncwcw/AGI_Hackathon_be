from sqlalchemy.orm import Session
from src.models import SupportPolicy
from src.domain.policy.policy_schema import PolicyCreate

# ��� ������ ��ȸ
def get_policies(db: Session, skip: int = 0, limit: int = 100):
    policies = db.query(SupportPolicy).offset(skip).limit(limit).all()
    total = db.query(SupportPolicy).count()
    return policies, total

# Ư�� ������ ��ȸ
def get_policy(db: Session, policy_id: int):
    return db.query(SupportPolicy).filter(SupportPolicy.id == policy_id).first()

# �� ������ ���� (�����ڿ�)
def create_policy(db: Session, policy: PolicyCreate):
    db_policy = SupportPolicy(
        title=policy.title,
        content=policy.content
    )
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy
