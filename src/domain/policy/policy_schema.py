from pydantic import BaseModel
from datetime import datetime
from typing import List

# �⺻ ��Ű�� (���̽�)
class PolicyBase(BaseModel):
    title: str
    content: str

# ������ ���� �� ����� ��Ű��
class PolicyCreate(PolicyBase):
    pass

# DB���� �о�� �� ����� ��Ű��
class Policy(PolicyBase):
    id: int

    class Config:
        orm_mode = True

# ���� ��å ����Ʈ ��ȯ �� ���
class PolicyList(BaseModel):
    policies: List[Policy]
    total: int
