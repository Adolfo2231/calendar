from fastapi import APIRouter
from .auth import router as auth_router
from .event import router as event_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth")
api_router.include_router(event_router, prefix="/event")

__all__ = ["api_router"]