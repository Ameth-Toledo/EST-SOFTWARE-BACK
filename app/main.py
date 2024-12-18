from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.config.db import Base, engine
from app.routes.emails_route import api_router_email
from app.routes.coments_route import api_router_coment
from app.routes.ayudas_route import api_router_ayuda

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(api_router_email)
app.include_router(api_router_coment)
app.include_router(api_router_ayuda)

@app.get("/")
def root():
    return {"message": "Api de obtener emails, propiedad de ESTSOFWARE"}
