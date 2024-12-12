from sqlalchemy.orm import Session
from app.models.emails_model import emails

def get_all_emails(db: Session):
    return db.query(emails).all()

def get_email_by_id(db: Session, email_id: int):
    return db.query(emails).filter(emails.id_email == email_id).first()

def create_email(db: Session, email: emails):
    db.add(email)
    db.commit()
    db.refresh(email)
    return email