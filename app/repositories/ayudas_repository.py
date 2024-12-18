from sqlalchemy.orm import Session
from app.models.ayudas_model import ayudas

def get_all_ayudas(db: Session):
    return db.query(ayudas).all()

def get_ayudas_by_id(db: Session, ayuda_id: int):
    return db.query(ayudas).filter(ayudas.id_ayuda == ayuda_id).first()

def create_ayudas(db: Session, ayuda: ayudas):
    db.add(ayuda)
    db.commit()
    db.refresh(ayuda)
    return ayuda