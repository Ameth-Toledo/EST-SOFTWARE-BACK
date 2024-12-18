from sqlalchemy import Column, Text, Integer, String
from app.config.db import Base

class ayudas(Base):
    __tablename__ = "ayudas"
    id_ayuda = Column(Integer, primary_key=True, index=True)
    name_user = Column(String(80), nullable=False)
    email = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)