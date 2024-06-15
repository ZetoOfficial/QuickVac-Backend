import uuid

from sqlalchemy import UUID, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Candidate(Base):
    __tablename__ = 'candidates'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(20))
    location = Column(String(255))
    experience = Column(Integer)
    resume = Column(Text)
    expected_salary = Column(String(100))
    status = Column(String(50), nullable=False)

    skills = relationship('CandidateSkill', back_populates='candidate')
    applications = relationship('Application', back_populates='candidate')


class CandidateSkill(Base):
    __tablename__ = 'candidate_skills'
    candidate_id = Column(UUID(as_uuid=True), ForeignKey('candidates.id'), primary_key=True)
    skill_id = Column(UUID(as_uuid=True), ForeignKey('skills.id'), primary_key=True)

    candidate = relationship('Candidate', back_populates='skills')
    skill = relationship('Skill', back_populates='candidates')
