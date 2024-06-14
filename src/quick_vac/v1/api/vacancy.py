from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from quick_vac.use_cases import errors, vacancy_use_case
from quick_vac.v1.schemas import Collection, EmptyModel, Pagination

from .dtos.vacancy_dto import (
    CreateVacancyInput,
    UpdateVacancyInput,
    Vacancy,
    VacancyFilters,
)

router = APIRouter()


@router.get('/vacancies/{vacancy_id}', response_model=Vacancy)
async def get_vacancy(vacancy_id: UUID):
    try:
        vacancy = await vacancy_use_case.GetVacancy().execute(vacancy_id)
        return Vacancy.model_validate(vacancy)
    except errors.VacancyNotFound:
        raise HTTPException(status_code=404, detail='Vacancy is not found')


@router.get('/vacancies', response_model=Collection[Vacancy])
async def get_vacancies(filters: VacancyFilters = Depends(), pagination: Pagination = Depends(Pagination)):
    vacancies = await vacancy_use_case.GetVacancies().execute(
        filters.direction,
        filters.location,
        filters.query,
        pagination.offset,
        pagination.limit,
    )
    return Collection[Vacancy].model_validate(vacancies)


@router.post('/vacancies', response_model=Vacancy)
async def create_vacancy(request: CreateVacancyInput):
    vacancy = await vacancy_use_case.AddVacancy().execute(request.model_dump())
    return Vacancy.model_validate(vacancy)


@router.patch('/vacancies/{vacancy_id}', response_model=Vacancy)
async def update_vacancy(vacancy_id: UUID, request: UpdateVacancyInput):
    pass


@router.delete('/vacancies/{vacancy_id}', response_model=EmptyModel)
async def delete_vacancy(vacancy_id: UUID):
    pass
