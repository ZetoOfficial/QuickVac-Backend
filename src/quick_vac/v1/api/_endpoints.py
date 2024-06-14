from fastapi import APIRouter

from . import vacancy

api_router = APIRouter()
api_router.include_router(vacancy.router, tags=['vacancies'])
