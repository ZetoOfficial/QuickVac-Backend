from typing import List, Optional

from sqlalchemy.orm import Session

from quick_vac.models.skill import Skill
from quick_vac.repositories.base_repository import BaseRepository


class SkillRepository(BaseRepository):
    def add_skill(self, skill: Skill, session: Session):
        session.add(skill)
        session.commit()
        return skill

    def get_skills(self) -> List[Skill]:
        with self.session_factory() as session:
            return session.query(Skill).all()

    def get_skill_by_id(self, skill_id: str) -> Optional[Skill]:
        with self.session_factory() as session:
            return session.query(Skill).filter(Skill.id == skill_id).one_or_none()

    def update_skill(self, skill: Skill):
        with self.session_factory() as session:
            session.merge(skill)
            session.commit()

    def delete_skill(self, skill_id: str):
        with self.session_factory() as session:
            skill = session.query(Skill).filter(Skill.id == skill_id).one_or_none()
            if skill:
                session.delete(skill)
                session.commit()
