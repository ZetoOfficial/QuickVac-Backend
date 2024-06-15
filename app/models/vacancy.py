import uuid

from sqlalchemy import DECIMAL, Column, Date, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base

from .enums import (
    Direction,
    EducationLevel,
    EmploymentType,
    ExperienceLevel,
    VacancyStatus,
    WorkType,
)


class Vacancy(Base):
    __tablename__ = 'vacancies'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    salary_amount = Column(DECIMAL(10, 2))
    salary_currency = Column(String(10))
    description = Column(Text, nullable=False)
    location = Column(String(255), nullable=False)
    status = Column(Enum(VacancyStatus), nullable=False, default=VacancyStatus.open)
    direction = Column(Enum(Direction), nullable=False, default=Direction.development)
    work_type = Column(Enum(WorkType), nullable=False, default=WorkType.full_time)
    experience_level = Column(Enum(ExperienceLevel), nullable=False, default=ExperienceLevel.junior)
    employment_type = Column(Enum(EmploymentType), nullable=False, default=EmploymentType.permanent)
    education_level = Column(Enum(EducationLevel), nullable=False, default=EducationLevel.bachelor)
    company_id = Column(UUID(as_uuid=True), ForeignKey('companies.id'))
    posted_date = Column(Date, nullable=False, default=func.now())
    closing_date = Column(Date)

    company = relationship('Company', back_populates='vacancies')
    skills = relationship('VacancySkill', back_populates='vacancy')
    applications = relationship('Application', back_populates='vacancy')


class VacancySkill(Base):
    __tablename__ = 'vacancy_skills'
    vacancy_id = Column(UUID(as_uuid=True), ForeignKey('vacancies.id'), primary_key=True)
    skill_id = Column(UUID(as_uuid=True), ForeignKey('skills.id'), primary_key=True)

    vacancy = relationship('Vacancy', back_populates='skills')
    skill = relationship('Skill', back_populates='vacancies')
