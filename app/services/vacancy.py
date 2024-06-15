from uuid import UUID

import markdown

from app.repositories import CRUDVacancy
from app.schemas import InputVacancyDTO, ShortVacancyDTO, UpdateVacancyDTO, VacancyDTO


def markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html


class VacancyService:
    @staticmethod
    async def create_vacancy(dto: InputVacancyDTO) -> VacancyDTO:
        return await CRUDVacancy.create_vacancy(dto)

    @staticmethod
    async def get_all_vacancies(limit: int = None, offset: int = None) -> list[ShortVacancyDTO]:
        return await CRUDVacancy.get_all_vacancies(limit, offset)

    @staticmethod
    async def get_vacancy_by_id(vacancy_id: UUID) -> VacancyDTO:
        vacancy = await CRUDVacancy.get_vacancy_by_id(vacancy_id)
        if not vacancy:
            raise ValueError(f"Vacancy with id {vacancy_id} not found")
        vacancy.description = markdown_to_html(vacancy.description)
        return vacancy

    @staticmethod
    async def update_vacancy(vacancy_id: UUID, dto: UpdateVacancyDTO) -> VacancyDTO:
        return await CRUDVacancy.update_vacancy(vacancy_id, dto)

    @staticmethod
    async def delete_vacancy(vacancy_id: UUID) -> None:
        return await CRUDVacancy.delete_vacancy(vacancy_id)
