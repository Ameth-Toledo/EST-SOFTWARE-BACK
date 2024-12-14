from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from app.services.coments_service import list_coments, get_coment, add_coment
from app.config.db import get_db

router = APIRouter()

@router.get("/coments")
def read_emails(db: Session = Depends(get_db)):
    coments = list_coments(db)
    return {"coments": coments}

@router.get("/coments/{coment_id}")
def read_email(coment_id: int, db: Session = Depends(get_db)):
    coments = get_coment(db, coment_id)
    if not coments:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return coments

@router.post("/coments")
def create_email(
    coment_text: str = Form(...),
    name_user_coment: str = Form(...),
    db: Session = Depends(get_db)
):
    return add_coment(db, coment_text, name_user_coment)
