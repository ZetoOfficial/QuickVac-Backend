from uuid import UUID

from pydantic import BaseModel, Field


class InputSkillDTO(BaseModel):
    name: str = Field(..., max_length=255, description="Название навыка")

    class Config:
        json_schema_extra = {"example": {"name": "Python"}}


class SkillDTO(BaseModel):
    id: UUID = Field(..., description="Идентификатор навыка")
    name: str = Field(..., max_length=255, description="Название навыка")

    class Config:
        json_schema_extra = {"example": {"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "name": "Python"}}
