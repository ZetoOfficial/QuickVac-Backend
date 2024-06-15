from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas import InputVacancyDTO, ShortVacancyDTO, UpdateVacancyDTO, VacancyDTO
from app.services import VacancyService

vacancy_router = APIRouter()


@vacancy_router.post("/vacancies", response_model=VacancyDTO)
async def create_vacancy(dto: InputVacancyDTO):
    """Create a new vacancy in the database"""
    try:
        return await VacancyService.create_vacancy(dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@vacancy_router.get("/vacancies", response_model=list[ShortVacancyDTO])
async def get_all_vacancies(limit: int = 100, offset: int = 0):
    """Get all vacancies from the database"""
    try:
        return await VacancyService.get_all_vacancies(limit, offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@vacancy_router.get("/vacancies/{vacancy_id}", response_model=VacancyDTO)
async def get_vacancy_by_id(vacancy_id: UUID):
    """Get a specific vacancy by its ID"""
    try:
        return await VacancyService.get_vacancy_by_id(vacancy_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@vacancy_router.patch("/vacancies/{vacancy_id}", response_model=VacancyDTO)
async def update_vacancy(vacancy_id: UUID, dto: UpdateVacancyDTO):
    """Update a specific vacancy"""
    try:
        return await VacancyService.update_vacancy(vacancy_id, dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@vacancy_router.delete("/vacancies/{vacancy_id}", response_model=None)
async def delete_vacancy(vacancy_id: UUID):
    """Delete a specific vacancy"""
    try:
        await VacancyService.delete_vacancy(vacancy_id)
        return {"message": "Vacancy deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
