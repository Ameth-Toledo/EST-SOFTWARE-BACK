from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.services.ayudas_service import list_ayudas, get_ayudas, add_ayudas
from app.config.db import get_db

router = APIRouter()

@router.get("/ayudas")
def read_ayudas(db: Session = Depends(get_db)):
    ayudas = list_ayudas(db)
    return {"ayudas": ayudas}

@router.get("/ayudas/{ayuda_id}")
def read_ayuda(ayuda_id: int, db: Session = Depends(get_db)):
    ayudas = get_ayudas(db, ayuda_id)

@router.post("/ayudas")
def create_ayuda(
    description: str = Form(...),
    name_user: str = Form(...),
    email_ayuda: str = Form(...),  
    db: Session = Depends(get_db)
):
    return add_ayudas(db, description, name_user, email_ayuda)

