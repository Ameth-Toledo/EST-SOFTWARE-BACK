from sqlalchemy.orm import Session
from app.models.coments_model import coments

def get_all_coments(db: Session):
    return db.query(coments).all()

def get_coments_by_id(db: Session, coment_id: int):
    return db.query(coments).filter(coments.id_coment == coment_id).first()

def create_coments(db: Session, coment: coments):
    db.add(coment)
    db.commit()
    db.refresh(coment)
    return coment