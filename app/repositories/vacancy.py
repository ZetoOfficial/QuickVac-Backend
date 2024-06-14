from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.database import SessionLocal
from app.models.vacancy import Vacancy as ORMVacancy
from app.schemas import InputVacancyDTO, UpdateVacancyDTO, VacancyDTO

from .errors import NotFoundException


class CRUDVacancy:
    @staticmethod
    async def create_vacancy(dto: InputVacancyDTO) -> VacancyDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            orm_obj = ORMVacancy(**dto.model_dump())
            session.add(orm_obj)
            await session.commit()
            return await CRUDVacancy.get_vacancy_by_id(orm_obj.id)

    @staticmethod
    async def get_all_vacancies(limit: int, offset: int) -> list[VacancyDTO]:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMVacancy).options(joinedload(ORMVacancy.company), joinedload(ORMVacancy.skills))
            if limit:
                query = query.limit(limit)
            if offset:
                query = query.offset(offset)
            result = await session.execute(query)
            vacancies = result.unique().scalars().all()  # Используем unique() метод
            return vacancies

    @staticmethod
    async def get_vacancy_by_id(_id: UUID) -> VacancyDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = (
                select(ORMVacancy)
                .where(ORMVacancy.id == _id)
                .options(joinedload(ORMVacancy.company), joinedload(ORMVacancy.skills))
            )
            result = await session.execute(query)
            vacancy = result.unique().scalar_one_or_none()  # Используем unique() метод
            if vacancy is None:
                raise NotFoundException(f"Vacancy with id {_id} not found")
            return vacancy

    @staticmethod
    async def update_vacancy(_id: UUID, dto: UpdateVacancyDTO) -> VacancyDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            existing_vacancy = await CRUDVacancy.get_vacancy_by_id(_id)
            if not existing_vacancy:
                raise NotFoundException(f"Vacancy with id {_id} not found")

            update_data = dto.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(existing_vacancy, key, value)

            session.add(existing_vacancy)
            await session.commit()
            return await CRUDVacancy.get_vacancy_by_id(_id)

    @staticmethod
    async def delete_vacancy(_id: UUID) -> bool:
        async with SessionLocal() as session:
            session: AsyncSession
            query = delete(ORMVacancy).where(ORMVacancy.id == _id)
            await session.execute(query)
            await session.commit()
            return True
