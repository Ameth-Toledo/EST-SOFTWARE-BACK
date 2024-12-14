from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.coments_model import coments
from app.repositories.coments_repository import (
    get_all_coments,
    get_coments_by_id,
    create_coments
)

def list_coments(db: Session):
    return get_all_coments(db)

def get_coment(db: Session, coment_id: int):
    return get_coments_by_id(db, coment_id)

def add_coment(db: Session, coment_text: str, name_user_coment: str):
    if not coment_text or coment_text.strip() == "": 
        raise HTTPException(status_code=400, detail="El comentario no puede estar vacía")

    new_coment = coments(
        coment_text=coment_text,
        name_user_coment=name_user_coment,
    )

    return create_coments(db, new_coment)
