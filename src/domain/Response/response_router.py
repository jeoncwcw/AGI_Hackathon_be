from fastapi import APIRouter

from database import SessionLocal
from models import Response

router = APIRouter(
    prefix = "/api/response"
)