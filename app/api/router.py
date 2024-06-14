from fastapi import APIRouter

from app.api.endpoints import company, vacancy

api_router = APIRouter()
api_router.include_router(company.company_router, tags=["companies"])
# api_router.include_router(skill.skill_router, tags=["skills"])
api_router.include_router(vacancy.vacancy_router, tags=["vacancies"])
