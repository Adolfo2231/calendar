from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.extensions import get_db
from app.services import AuthService


def get_auth_service(
    db: AsyncSession = Depends(get_db),
) -> AuthService:
    """Dependency para obtener AuthService con sesión de BD"""
    return AuthService(db)

