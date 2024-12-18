from fastapi import APIRouter
from app.controllers.ayudas_controller import router as ayudas_router

api_router_ayuda = APIRouter()
api_router_ayuda.include_router(ayudas_router, prefix="/api/v1", tags=["ayudas"])