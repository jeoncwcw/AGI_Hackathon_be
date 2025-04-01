from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, get_db
from domain.Request import request_schema, request_crud

router = APIRouter(
    prefix="/api/request"
)

@router.get("/detail/{request_id}", response_model=request_schema.ReQuest)
def Request_detail(request_id: int, db: Session = Depends(get_db)):
    request = request_crud.get_request(db, request_id)
    return request