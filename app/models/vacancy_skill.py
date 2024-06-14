from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class VacancySkill(Base):
    __tablename__ = 'vacancy_skills'
    vacancy_id = Column(UUID(as_uuid=True), ForeignKey('vacancies.id'), primary_key=True)
    skill_id = Column(UUID(as_uuid=True), ForeignKey('skills.id'), primary_key=True)

    vacancy = relationship('Vacancy', back_populates='skills')
    skill = relationship('Skill', back_populates='vacancies')
