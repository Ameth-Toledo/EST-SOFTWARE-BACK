from fastapi import APIRouter
from app.controllers.coments_controller import router as coments_router

api_router_coment = APIRouter()
api_router_coment.include_router(coments_router, prefix="/api/v1", tags=["coments"])