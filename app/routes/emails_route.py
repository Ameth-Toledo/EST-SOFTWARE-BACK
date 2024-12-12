from fastapi import APIRouter
from app.controllers.emails_controller import router as emails_router

api_router = APIRouter()
api_router.include_router(emails_router, prefix="/api/v1", tags=["emails"])