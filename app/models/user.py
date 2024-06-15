import uuid

from sqlalchemy import UUID, Column, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    role = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)

    interviews = relationship('Interview', back_populates='interviewer')
    notes = relationship('Note', back_populates='user')
