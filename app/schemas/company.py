from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class InputCompanyDTO(BaseModel):
    name: str = Field(..., max_length=255, description="Название компании")
    address: Optional[str] = Field(None, max_length=255, description="Адрес компании")
    website: Optional[str] = Field(None, description="Вебсайт компании")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Example Company",
                "address": "123 Main St, Anytown, USA",
                "website": "https://example.com",
            }
        }


class CompanyDTO(BaseModel):
    id: UUID
    name: str = Field(..., max_length=255, description="Название компании")
    address: Optional[str] = Field(None, max_length=255, description="Адрес компании")
    website: Optional[str] = Field(None, description="Вебсайт компании")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Example Company",
                "address": "123 Main St, Anytown, USA",
                "website": "https://example.com",
            }
        }
