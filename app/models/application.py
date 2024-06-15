import uuid

from sqlalchemy import UUID, Column, Date, ForeignKey, String, Text, func
from sqlalchemy.orm import relationship

from app.database import Base


class Application(Base):
    __tablename__ = 'applications'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    candidate_id = Column(UUID(as_uuid=True), ForeignKey('candidates.id'))
    vacancy_id = Column(UUID(as_uuid=True), ForeignKey('vacancies.id'))
    date_applied = Column(Date, nullable=False, default=func.now())
    status = Column(String(50), nullable=False)
    notes = Column(Text)

    candidate = relationship('Candidate', back_populates='applications')
    vacancy = relationship('Vacancy', back_populates='applications')
    interviews = relationship('Interview', back_populates='application')
    notes = relationship('Note', back_populates='application')
