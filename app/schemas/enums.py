import enum


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
