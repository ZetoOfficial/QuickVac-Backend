from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session

from quick_vac.models.skill import Skill
from quick_vac.models.vacancy import Vacancy
from quick_vac.models.vacancy_skill import VacancySkill
from quick_vac.repositories.base_repository import BaseRepository


class VacancySkillRepository(BaseRepository):
    def add_vacancy_skill(self, vacancy_id: str, skill_id: str, session: Session):
        vacancy_skill = VacancySkill(vacancy_id=vacancy_id, skill_id=skill_id)
        session.add(vacancy_skill)
        session.commit()
        return vacancy_skill

    def get_skills_for_vacancy(self, vacancy_id: str) -> List[Skill]:
        with self.session_factory() as session:
            return (
                session.query(Skill)
                .join(VacancySkill, Skill.id == VacancySkill.skill_id)
                .filter(VacancySkill.vacancy_id == vacancy_id)
                .all()
            )

    def get_vacancies_for_skill(self, skill_id: str) -> List[Vacancy]:
        with self.session_factory() as session:
            return (
                session.query(Vacancy)
                .join(VacancySkill, Vacancy.id == VacancySkill.vacancy_id)
                .filter(VacancySkill.skill_id == skill_id)
                .all()
            )

    def delete_vacancy_skill(self, vacancy_id: str, skill_id: str):
        with self.session_factory() as session:
            vacancy_skill = (
                session.query(VacancySkill)
                .filter(and_(VacancySkill.vacancy_id == vacancy_id, VacancySkill.skill_id == skill_id))
                .one_or_none()
            )
            if vacancy_skill:
                session.delete(vacancy_skill)
                session.commit()
