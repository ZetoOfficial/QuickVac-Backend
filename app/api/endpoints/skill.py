from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.schemas import InputSkillDTO, SkillDTO
from app.services import SkillService

skill_router = APIRouter()


@skill_router.post("/skills", response_model=SkillDTO)
async def create_skill(dto: InputSkillDTO):
    """Create a new skill in the database"""
    try:
        return await SkillService.create_skill(dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@skill_router.get("/skills", response_model=list[SkillDTO])
async def get_all_skills(limit: int = 100, offset: int = 0):
    """Get all skills from the database"""
    try:
        return await SkillService.get_all_skills(limit, offset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@skill_router.get("/skills/{skill_id}", response_model=SkillDTO)
async def get_skill_by_id(skill_id: UUID):
    """Get a specific skill by its ID"""
    try:
        return await SkillService.get_skill_by_id(skill_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@skill_router.put("/skills/{skill_id}", response_model=SkillDTO)
async def update_skill(skill_id: UUID, dto: InputSkillDTO):
    """Update a specific skill"""
    try:
        return await SkillService.update_skill(skill_id, dto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@skill_router.delete("/skills/{skill_id}", response_model=None)
async def delete_skill(skill_id: UUID):
    """Delete a specific skill"""
    try:
        await SkillService.delete_skill(skill_id)
        return {"message": "Skill deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
