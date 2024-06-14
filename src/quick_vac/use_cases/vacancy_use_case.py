from typing import List, Optional
from uuid import UUID

from dependency_injector.wiring import Provide, inject

from core.containers import Container
from quick_vac.models.vacancy import Vacancy
from quick_vac.repositories.skill_repository import SkillRepository
from quick_vac.repositories.vacancy_repository import VacancyRepository
from quick_vac.repositories.vacancy_skill_repository import VacancySkillRepository

from .dtos.vacancy_dto import VacancyDto, create_vacancy_dto
from .errors import VacancyNotFound


class VacancyUseCase:
    @inject
    def __init__(
        self,
        vacancy_repository: VacancyRepository = Provide[Container.vacancy_repository],
        skill_repository: SkillRepository = Provide[Container.skill_repository],
        vacancy_skill_repository: VacancySkillRepository = Provide[Container.vacancy_skill_repository],
    ):
        self.vacancy_repository = vacancy_repository
        self.skill_repository = skill_repository
        self.vacancy_skill_repository = vacancy_skill_repository

    def _validate_vacancy(self, vacancy_id: UUID) -> Vacancy:
        vacancy = self.vacancy_repository.get_vacancy_by_id(vacancy_id)

        if vacancy is None:
            raise VacancyNotFound

        return vacancy


class GetVacancies(VacancyUseCase):
    async def execute(
        self,
        direction: Optional[str],
        location: Optional[str],
        query: Optional[str],
        offset: int,
        limit: int,
    ) -> List[VacancyDto]:
        vacancies = self.vacancy_repository.get_vacancies(direction, location, query, offset, limit)
        return [create_vacancy_dto(vacancy) for vacancy in vacancies]


class GetVacancy(VacancyUseCase):
    async def execute(self, vacancy_id: UUID) -> VacancyDto:
        vacancy = self._validate_vacancy(vacancy_id)
        return create_vacancy_dto(vacancy)


class AddVacancy(VacancyUseCase):
    async def execute(self, vacancy_data: dict) -> VacancyDto:
        vacancy = Vacancy(**vacancy_data)
        with self.vacancy_repository.session_factory() as session:
            self.vacancy_repository.add_vacancy(vacancy, session)
        return create_vacancy_dto(vacancy)


class UpdateVacancy(VacancyUseCase):
    async def execute(self, vacancy_id: UUID, vacancy_data: dict) -> VacancyDto:
        vacancy = self._validate_vacancy(vacancy_id)
        for key, value in vacancy_data.items():
            setattr(vacancy, key, value)
        self.vacancy_repository.update_vacancy(vacancy)
        return create_vacancy_dto(vacancy)


class DeleteVacancy(VacancyUseCase):
    async def execute(self, vacancy_id: UUID):
        self.vacancy_repository.delete_vacancy(vacancy_id)
