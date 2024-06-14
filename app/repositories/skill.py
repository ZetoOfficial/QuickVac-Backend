from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import SessionLocal
from app.models.skill import Skill as ORMSkill
from app.schemas import InputSkillDTO, SkillDTO

from .errors import NotFoundException


class CRUDSkill:
    @staticmethod
    async def create_skill(dto: InputSkillDTO) -> SkillDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            orm_obj = ORMSkill(**dto.model_dump())
            session.add(orm_obj)
            await session.commit()
            return await CRUDSkill.get_skill_by_id(orm_obj.id)

    @staticmethod
    async def get_all_skills(limit: int, offset: int) -> list[SkillDTO]:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMSkill)
            if limit:
                query = query.limit(limit)
            if offset:
                query = query.offset(offset)
            result = await session.execute(query)
            skills = result.scalars().all()
            return skills

    @staticmethod
    async def get_skill_by_id(_id: UUID) -> SkillDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = select(ORMSkill).where(ORMSkill.id == _id)
            result = await session.execute(query)
            skill = result.scalar_one_or_none()
            if skill is None:
                raise NotFoundException(f"Skill with id {_id} not found")
            return skill

    @staticmethod
    async def update_skill(_id: UUID, dto: InputSkillDTO) -> SkillDTO:
        async with SessionLocal() as session:
            session: AsyncSession
            query = update(ORMSkill).where(ORMSkill.id == _id).values(**dto.model_dump()).returning(ORMSkill)
            await session.execute(query)
            await session.commit()
            return await CRUDSkill.get_skill_by_id(_id)

    @staticmethod
    async def delete_skill(_id: UUID) -> bool:
        async with SessionLocal() as session:
            session: AsyncSession
            query = delete(ORMSkill).where(ORMSkill.id == _id)
            await session.execute(query)
            await session.commit()
            return True
