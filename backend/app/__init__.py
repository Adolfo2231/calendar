from fastapi import FastAPI
from app.api.v1 import api_router

def create_app() -> FastAPI:
    app = FastAPI(title="Calendar API", version="1.0.0")

    # Incluir el router principal de la API v1
    app.include_router(api_router, prefix="/api/v1")

    return app