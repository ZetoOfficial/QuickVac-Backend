from uuid import UUID

from app.repositories import CRUDSkill
from app.schemas import InputSkillDTO, SkillDTO


class SkillService:
    @staticmethod
    async def create_skill(dto: InputSkillDTO) -> SkillDTO:
        return await CRUDSkill.create_skill(dto)

    @staticmethod
    async def get_all_skills(limit: int = None, offset: int = None) -> list[SkillDTO]:
        return await CRUDSkill.get_all_skills(limit, offset)

    @staticmethod
    async def get_skill_by_id(skill_id: UUID) -> SkillDTO:
        return await CRUDSkill.get_skill_by_id(skill_id)

    @staticmethod
    async def update_skill(skill_id: UUID, dto: InputSkillDTO) -> SkillDTO:
        return await CRUDSkill.update_skill(skill_id, dto)

    @staticmethod
    async def delete_skill(skill_id: UUID) -> None:
        return await CRUDSkill.delete_skill(skill_id)
