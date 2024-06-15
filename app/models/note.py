import uuid

from sqlalchemy import UUID, Column, Date, ForeignKey, Text, func
from sqlalchemy.orm import relationship

from app.database import Base


class Note(Base):
    __tablename__ = 'notes'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    application_id = Column(UUID(as_uuid=True), ForeignKey('applications.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    note_text = Column(Text, nullable=False)
    date_created = Column(Date, nullable=False, default=func.now())

    application = relationship('Application', back_populates='notes')
    user = relationship('User', back_populates='notes')
