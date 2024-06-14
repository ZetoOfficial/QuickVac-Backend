import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from core.database import Base


class Company(Base):
    __tablename__ = 'companies'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    address = Column(String(255))
    website = Column(String(255))
