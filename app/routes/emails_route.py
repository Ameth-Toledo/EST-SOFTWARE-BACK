from fastapi import APIRouter
from app.controllers.emails_controller import router as emails_router

api_router_email = APIRouter()
api_router_email.include_router(emails_router, prefix="/api/v1", tags=["emails"])