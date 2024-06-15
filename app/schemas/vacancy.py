from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from .enums import (
    Direction,
    EducationLevel,
    EmploymentType,
    ExperienceLevel,
    VacancyStatus,
    WorkType,
)


class InputVacancyDTO(BaseModel):
    title: str = Field(..., max_length=255, description="Название вакансии")
    salary_amount: Optional[float] = Field(None, description="Размер зарплаты")
    salary_currency: Optional[str] = Field(None, max_length=10, description="Валюта зарплаты")
    description: str = Field(..., max_length=2000, description="Описание вакансии")
    location: str = Field(..., max_length=255, description="Местоположение")
    status: VacancyStatus = Field(..., description="Статус вакансии")
    direction: Direction = Field(..., description="Направление")
    work_type: WorkType = Field(..., description="Тип работы")
    experience_level: ExperienceLevel = Field(..., description="Уровень опыта")
    employment_type: EmploymentType = Field(..., description="Тип занятости")
    education_level: EducationLevel = Field(..., description="Уровень образования")
    company_id: UUID = Field(..., description="Идентификатор компании")
    closing_date: Optional[date] = Field(None, description="Дата закрытия вакансии")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Software Developer",
                "salary_amount": 5000.00,
                "salary_currency": "USD",
                "description": "Develop and maintain software applications.",
                "location": "Remote",
                "status": "open",
                "direction": "development",
                "work_type": "full_time",
                "experience_level": "junior",
                "employment_type": "permanent",
                "education_level": "bachelor",
                "company_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "closing_date": "2024-12-31",
            }
        }


class UpdateVacancyDTO(BaseModel):
    title: Optional[str] = Field(None, max_length=255, description="Название вакансии")
    salary_amount: Optional[float] = Field(None, description="Размер зарплаты")
    salary_currency: Optional[str] = Field(None, max_length=10, description="Валюта зарплаты")
    description: Optional[str] = Field(None, max_length=2000, description="Описание вакансии")
    location: Optional[str] = Field(None, max_length=255, description="Местоположение")
    status: Optional[VacancyStatus] = Field(None, description="Статус вакансии")
    direction: Optional[Direction] = Field(None, description="Направление")
    work_type: Optional[WorkType] = Field(None, description="Тип работы")
    experience_level: Optional[ExperienceLevel] = Field(None, description="Уровень опыта")
    employment_type: Optional[EmploymentType] = Field(None, description="Тип занятости")
    education_level: Optional[EducationLevel] = Field(None, description="Уровень образования")
    company_id: Optional[UUID] = Field(None, description="Идентификатор компании")
    closing_date: Optional[date] = Field(None, description="Дата закрытия вакансии")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Software Developer",
                "salary_amount": 6000.00,
                "salary_currency": "USD",
                "description": "Develop, maintain, and enhance software applications.",
                "location": "Onsite",
                "status": "closed",
                "direction": "development",
                "work_type": "part_time",
                "experience_level": "senior",
                "employment_type": "temporary",
                "education_level": "master",
                "company_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "closing_date": "2024-11-30",
            }
        }


class ShortVacancyDTO(BaseModel):
    id: UUID
    title: str = Field(..., max_length=255, description="Название вакансии")
    salary_amount: Optional[float] = Field(None, description="Размер зарплаты")
    salary_currency: Optional[str] = Field(None, max_length=10, description="Валюта зарплаты")
    location: str = Field(..., max_length=255, description="Местоположение")
    status: VacancyStatus
    direction: Direction
    work_type: WorkType
    experience_level: ExperienceLevel
    employment_type: EmploymentType
    education_level: EducationLevel
    company_id: UUID
    posted_date: date
    closing_date: Optional[date] = Field(None, description="Дата закрытия вакансии")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "title": "Software Developer",
                "salary_amount": 5000.00,
                "salary_currency": "USD",
                "location": "Remote",
                "status": "open",
                "direction": "Разработка",
                "work_type": "Полный рабочий день",
                "experience_level": "Junior",
                "employment_type": "Постоянная",
                "education_level": "Бакалавр",
                "company_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "posted_date": "2024-06-14",
                "closing_date": "2024-12-31",
            }
        }


class VacancyDTO(BaseModel):
    id: UUID
    title: str = Field(..., max_length=255, description="Название вакансии")
    salary_amount: Optional[float] = Field(None, description="Размер зарплаты")
    salary_currency: Optional[str] = Field(None, max_length=10, description="Валюта зарплаты")
    description: str = Field(..., max_length=10000, description="Описание вакансии")
    location: str = Field(..., max_length=255, description="Местоположение")
    status: VacancyStatus
    direction: Direction
    work_type: WorkType
    experience_level: ExperienceLevel
    employment_type: EmploymentType
    education_level: EducationLevel
    company_id: UUID
    posted_date: date
    closing_date: Optional[date] = Field(None, description="Дата закрытия вакансии")

    class Config:
        json_schema_extra = {
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "title": "Software Developer",
                "salary_amount": 5000.00,
                "salary_currency": "USD",
                "description": "Develop and maintain software applications.",
                "location": "Remote",
                "status": "open",
                "direction": "Разработка",
                "work_type": "Полный рабочий день",
                "experience_level": "Junior",
                "employment_type": "Постоянная",
                "education_level": "Бакалавр",
                "company_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "posted_date": "2024-06-14",
                "closing_date": "2024-12-31",
            }
        }
