from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from app.services.emails_service import list_emails, get_email, add_email, update_email_status
from app.config.db import get_db

router = APIRouter()

@router.get("/emails")
def read_emails(db: Session = Depends(get_db)):
    emails = list_emails(db)
    return {"emails": emails}

@router.get("/emails/{email_id}")
def read_email(email_id: int, db: Session = Depends(get_db)):
    email = get_email(db, email_id)
    if not email:
        raise HTTPException(status_code=404, detail="Email no encontrado")
    return email

@router.post("/emails")
def create_email(
    name_email: str = Form(...),
    email_user: str = Form(...),
    description: str = Form(...),
    phone_number : str = Form(...),
    db: Session = Depends(get_db)
):
    return add_email(db, name_email, email_user, description, phone_number)

@router.put("/emails/{email_id}/status")
def update_status(email_id: int, status: str, db: Session = Depends(get_db)):
    if status not in ['pendiente', 'revisado']:
        raise HTTPException(status_code=400, detail="Estado no válido")
    updated_email = update_email_status(db, email_id, status)
    if not updated_email:
        raise HTTPException(status_code=404, detail="Email no encontrado")
    return {"message": "Estado actualizado", "email": updated_email}
