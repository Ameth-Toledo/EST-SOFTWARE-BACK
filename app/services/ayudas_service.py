from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.ayudas_model import ayudas
from app.repositories.ayudas_repository import (
    get_all_ayudas,
    get_ayudas_by_id,
    create_ayudas
)

def list_ayudas(db: Session):
    return get_all_ayudas(db)

def get_ayudas(db: Session, ayuda_id: int):
    return get_ayudas_by_id(db, ayuda_id)

def add_ayudas(db: Session, ayuda_text: str, name_user_ayuda: str, email_ayuda : str):
    if not ayuda_text or ayuda_text.strip() == "": 
        raise HTTPException(status_code=400, detail="La ayuda no puede estar vacía")

    new_ayuda = ayudas(
        name_user=name_user_ayuda,
        email = email_ayuda,
        description=ayuda_text,
    )

    return create_ayudas(db, new_ayuda)