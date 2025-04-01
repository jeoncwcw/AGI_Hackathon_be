from fastapi import APIRouter

from database import SessionLocal
from models import Request

router = APIRouter(
    prefix="/api/request"
)