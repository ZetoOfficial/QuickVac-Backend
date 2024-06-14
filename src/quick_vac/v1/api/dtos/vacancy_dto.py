from datetime import date
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class Company(BaseModel):
    id: UUID
    name: str
    address: Optional[str] = None
    website: Optional[str] = None


class Skill(BaseModel):
    id: UUID
    name: str


class Vacancy(BaseModel):
    id: UUID
    title: str
    salary_amount: Optional[float] = None
    salary_currency: Optional[str] = None
    description: str
    location: str
    status: str
    direction: str
    work_type: str
    experience_level: str
    employment_type: str
    education_level: str
    company: Company
    posted_date: date
    closing_date: Optional[date]
    skills: List[Skill]


class CreateVacancyInput(BaseModel):
    title: str
    salary_amount: Optional[float] = None
    salary_currency: Optional[str] = None
    description: str
    location: str
    status: str
    direction: str
    work_type: str
    experience_level: str
    employment_type: str
    education_level: str
    company_id: UUID


class UpdateVacancyInput(BaseModel):
    title: Optional[str] = None
    salary_amount: Optional[float] = None
    salary_currency: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    status: Optional[str] = None
    direction: Optional[str] = None
    work_type: Optional[str] = None
    experience_level: Optional[str] = None
    employment_type: Optional[str] = None
    education_level: Optional[str] = None


class VacancyFilters(BaseModel):
    direction: Optional[str] = None
    location: Optional[str] = None
    query: Optional[str] = None
