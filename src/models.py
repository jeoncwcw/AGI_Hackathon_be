from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Request(Base):
    __tablename__ = "request"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    
class Response(Base):
    __tablename__ = "response"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    request_id = Column(Integer, nullable=False)
    request = relationship("Request", backref="response")
    
class SupportPolicy(Base):
    __tablename__ = "support_policy"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    