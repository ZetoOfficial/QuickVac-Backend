import uuid

from sqlalchemy import UUID, Column, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Interview(Base):
    __tablename__ = 'interviews'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    application_id = Column(UUID(as_uuid=True), ForeignKey('applications.id'))
    interview_date = Column(Date, nullable=False)
    interviewer_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    feedback = Column(Text)

    application = relationship('Application', back_populates='interviews')
    interviewer = relationship('User', back_populates='interviews')
