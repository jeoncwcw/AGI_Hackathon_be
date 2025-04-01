from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    age = Column(Integer, nullable=False)
    income = Column(Integer, nullable=False)
    region = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    user_type = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)
    
class UserRecommendation(Base):
    __tablename__ = "user_recommendation"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    policy_id = Column(Integer, ForeignKey("support_policy.id"), nullable=False)
    recommended_at = Column(DateTime, nullable=False)

    user = relationship("User", backref="recommendations")
    policy = relationship("SupportPolicy")
    
class SupportPolicy(Base):
    __tablename__ = "support_policy"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    eligibility_criteria = Column(Text, nullable=False)
    application_process = Column(Text, nullable=False)
    benefits = Column(Text, nullable=False)
    policy_type = Column(String, nullable=False)  
    region = Column(String, nullable=False)  


    