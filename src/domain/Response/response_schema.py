import datetime

from pydantic import BaseModel


class ResponseCreate(BaseModel):
    content: str