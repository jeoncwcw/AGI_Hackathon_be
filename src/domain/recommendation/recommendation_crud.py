from sqlalchemy.orm import Session
from domain.recommendation.schema import UserInfo, PolicyRecommendation
from models import SupportPolicy, User, UserRecommendation
from datetime import datetime

def get_or_create_user(db: Session, user_info: UserInfo) -> User:
    user = db.query(User).filter_by(
        age=user_info.age,
        income=user_info.income,
        region=user_info.region,
        industry=user_info.industry,
        user_type=user_info.user_type
    ).first()
    if not user:
        user = User(
            age=user_info.age,
            income=user_info.income,
            region=user_info.region,
            industry=user_info.industry,
            user_type=user_info.user_type,
            create_date=datetime.now()
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

def recommend_support_policies(user_info: UserInfo, db: Session):
    user = get_or_create_user(db, user_info)

    query = f"""
    추천 지원금 요청:
    - 나이: {user_info.age}
    - 소득: {user_info.income}
    - 지역: {user_info.region}
    - 업종: {user_info.industry}
    - 유형: {user_info.user_type}
    """
    recommended_titles = db.get(SupportPolicy, 1).title # 나중에 수정해야됨

    recommended_policies = db.query(SupportPolicy).filter(
        SupportPolicy.title.in_(recommended_titles)
    ).all()

    recommendations = []
    for policy in recommended_policies:
        # 추천 기록 저장
        user_recommendation = UserRecommendation(
            user_id=user.id,
            policy_id=policy.id,
            recommended_at=datetime.now()
        )
        db.add(user_recommendation)
        recommendations.append(
            PolicyRecommendation(
                policy_id=policy.id,
                title=policy.title,
                brief=policy.content[:100] + "..."
            )
        )
    db.commit()

    return recommendations
