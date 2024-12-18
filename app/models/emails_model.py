from sqlalchemy import Column, Text, Enum, Integer, String
from app.config.db import Base

class emails(Base):
    __tablename__ = "emails"
    id_email = Column(Integer, primary_key=True, index=True)
    name_email = Column(String(80), nullable=False)
    email = Column(String(255), nullable=False)
    status = Column(Enum('pendiente', 'revisado'), default='pendiente', nullable=False)
    description = Column(Text, nullable=False)
    phone_number = Column(String(10), nullable=False)
