from typing import List, Optional
from uuid import UUID

from sqlalchemy import or_
from sqlalchemy.orm import Session

from quick_vac.models.vacancy import Vacancy
from quick_vac.repositories.base_repository import BaseRepository


class VacancyRepository(BaseRepository):
    def add_vacancy(self, vacancy: Vacancy, session: Session):
        session.add(vacancy)
        session.commit()
        return vacancy

    def get_vacancies(
        self,
        direction: Optional[str] = None,
        location: Optional[str] = None,
        query: Optional[str] = None,
        offset: int = 0,
        limit: int = 10,
    ) -> List[Vacancy]:
        with self.session_factory() as session:
            query_ = session.query(Vacancy)
            if direction:
                query_ = query_.filter(Vacancy.direction == direction)
            if location:
                query_ = query_.filter(Vacancy.location == location)
            if query:
                query_ = query_.filter(or_(Vacancy.title.ilike(f'%{query}%'), Vacancy.description.ilike(f'%{query}%')))
            query_ = query_.offset(offset).limit(limit)
            return query_.all()

    def get_vacancy_by_id(self, vacancy_id: UUID) -> Optional[Vacancy]:
        with self.session_factory() as session:
            return session.query(Vacancy).filter(Vacancy.id == vacancy_id).one_or_none()

    def update_vacancy(self, vacancy: Vacancy):
        with self.session_factory() as session:
            session.merge(vacancy)
            session.commit()

    def delete_vacancy(self, vacancy_id: UUID):
        with self.session_factory() as session:
            vacancy = session.query(Vacancy).filter(Vacancy.id == vacancy_id).one_or_none()
            if vacancy:
                session.delete(vacancy)
                session.commit()
