from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.emails_model import emails
from app.repositories.emails_repository import (
    get_all_emails,
    get_email_by_id,
    create_email
)

def list_emails(db: Session):
    return get_all_emails(db)

def get_email(db: Session, email_id: int):
    return get_email_by_id(db, email_id)

def add_email(db: Session, name_email: str, email_user: str, description: str, phone_number: str):
    if not description or description.strip() == "": 
        raise HTTPException(status_code=400, detail="La descripción no puede estar vacía")

    new_email = emails(
        name_email=name_email,
        email=email_user,
        description=description,
        phone_number=phone_number 
    )

    return create_email(db, new_email)

def update_email_status(db: Session, email_id: int, new_status: str):
    email = get_email_by_id(db, email_id)
    if email:
        email.status = new_status
        db.commit()
        db.refresh(email)
        return email
    return None
