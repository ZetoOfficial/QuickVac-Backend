from datetime import date
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from quick_vac.models.vacancy import Vacancy


class CompanyDto(BaseModel):
    id: UUID
    name: str
    address: Optional[str]
    website: Optional[str]


class SkillDto(BaseModel):
    id: UUID
    name: str


class VacancyDto(BaseModel):
    id: UUID
    title: str
    salary_amount: Optional[float]
    salary_currency: Optional[str]
    description: str
    location: str
    status: str
    direction: str
    work_type: str
    experience_level: str
    employment_type: str
    education_level: str
    company: CompanyDto
    posted_date: date
    closing_date: Optional[date]
    skills: List[SkillDto]


def create_vacancy_dto(vacancy: Vacancy) -> VacancyDto:
    company_dto = CompanyDto(
        id=vacancy.company.id,
        name=vacancy.company.name,
        address=vacancy.company.address,
        website=vacancy.company.website,
    )

    skills_dto = [SkillDto(id=skill.id, name=skill.name) for skill in vacancy.skills]

    return VacancyDto(
        id=vacancy.id,
        title=vacancy.title,
        salary_amount=vacancy.salary_amount,
        salary_currency=vacancy.salary_currency,
        description=vacancy.description,
        location=vacancy.location,
        status=vacancy.status.value,
        direction=vacancy.direction.value,
        work_type=vacancy.work_type.value,
        experience_level=vacancy.experience_level.value,
        employment_type=vacancy.employment_type.value,
        education_level=vacancy.education_level.value,
        company=company_dto,
        posted_date=vacancy.posted_date,
        closing_date=vacancy.closing_date,
        skills=skills_dto,
    )


class VacancyFilters(BaseModel):
    direction: Optional[str]
    location: Optional[str]
    query: Optional[str]
