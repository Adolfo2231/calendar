from fastapi import FastAPI
from app.api.v1 import api_router
from app.extensions import init_db

def create_app() -> FastAPI:
    app = FastAPI(title="Calendar API", version="1.0.0")

    # Incluir el router principal de la API v1
    app.include_router(api_router, prefix="/api/v1")

    # Evento de startup: crear tablas si no existen
    @app.on_event("startup")
    async def startup_event():
        await init_db()

    return app