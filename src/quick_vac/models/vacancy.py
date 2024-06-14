import enum
import uuid

from sqlalchemy import DECIMAL, Column, Date, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from core.database import Base


class VacancyStatus(str, enum.Enum):
    open = 'open'
    closed = 'closed'
    pending = 'pending'


class Direction(str, enum.Enum):
    development = 'Разработка'
    sales = 'Продажи'
    customer_service = 'Клиентский сервис'
    marketing = 'Маркетинг'
    hr = 'HR'
    product_management = 'Управление продуктом'
    business_development = 'Развитие бизнеса'
    data_analytics = 'Аналитика данных'


class WorkType(str, enum.Enum):
    full_time = 'Полный рабочий день'
    part_time = 'Частичная занятость'
    contract = 'Контракт'
    freelance = 'Фриланс'
    internship = 'Стажировка'


class ExperienceLevel(str, enum.Enum):
    junior = 'Junior'
    middle = 'Middle'
    senior = 'Senior'
    lead = 'Lead'


class EmploymentType(str, enum.Enum):
    permanent = 'Постоянная'
    temporary = 'Временная'
    contract = 'Контракт'
    internship = 'Стажировка'


class EducationLevel(str, enum.Enum):
    high_school = 'Средняя школа'
    bachelor = 'Бакалавр'
    master = 'Магистр'
    phd = 'Доктор наук'
    no_degree = 'Без образования'


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
