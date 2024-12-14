from sqlalchemy import Column, Text, Integer, String
from app.config.db import Base

class coments(Base):
    __tablename__ = "coments"
    id_coment = Column(Integer, primary_key=True, index=True)
    coment_text = Column(Text, nullable=False)
    name_user_coment = Column(String(80), nullable=False)