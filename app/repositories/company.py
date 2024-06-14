from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import SessionLocal
from app.models.company import Company as ORMCompany
from app.schemas import CompanyDTO, InputCompanyDTO

from .errors import NotFoundException


class CRUDCompany:
    @staticmethod
    async def create_company(dto: InputCompanyDTO) -> CompanyDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            orm_obj = ORMCompany(**dto.model_dump())
            session.add(orm_obj)
            await session.commit()
            return await CRUDCompany.get_company_by_id(orm_obj.id)

    @staticmethod
    async def get_all_companies(limit: int, offset: int) -> list[CompanyDTO]:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMCompany)
            if limit:
                query = query.limit(limit)
            if offset:
                query = query.offset(offset)
            result = await session.execute(query)
            companies = result.scalars().all()
            return companies

    @staticmethod
    async def get_company_by_id(_id: UUID) -> CompanyDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMCompany).where(ORMCompany.id == _id)
            result = await session.execute(query)
            company = result.scalar_one_or_none()
            if company is None:
                raise NotFoundException(f"Company with id {_id} not found")
            return company

    @staticmethod
    async def update_company(_id: UUID, dto: InputCompanyDTO) -> CompanyDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = update(ORMCompany).where(ORMCompany.id == _id).values(**dto.model_dump()).returning(ORMCompany)
            await session.execute(query)
            await session.commit()
            return await CRUDCompany.get_company_by_id(_id)

    @staticmethod
    async def delete_company(_id: UUID) -> bool:
        async with SessionLocal() as session:
            session: AsyncSession
            query = delete(ORMCompany).where(ORMCompany.id == _id)
            await session.execute(query)
            await session.commit()
            return True
