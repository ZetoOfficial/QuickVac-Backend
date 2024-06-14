from uuid import UUID

from app.repositories import CRUDVacancy
from app.schemas import InputVacancyDTO, UpdateVacancyDTO, VacancyDTO


class VacancyService:
    @staticmethod
    async def create_vacancy(dto: InputVacancyDTO) -> VacancyDTO:
        return await CRUDVacancy.create_vacancy(dto)

    @staticmethod
    async def get_all_vacancies(limit: int = None, offset: int = None) -> list[VacancyDTO]:
        return await CRUDVacancy.get_all_vacancies(limit, offset)

    @staticmethod
    async def get_vacancy_by_id(vacancy_id: UUID) -> VacancyDTO:
        return await CRUDVacancy.get_vacancy_by_id(vacancy_id)

    @staticmethod
    async def update_vacancy(vacancy_id: UUID, dto: UpdateVacancyDTO) -> VacancyDTO:
        return await CRUDVacancy.update_vacancy(vacancy_id, dto)

    @staticmethod
    async def delete_vacancy(vacancy_id: UUID) -> None:
        return await CRUDVacancy.delete_vacancy(vacancy_id)
