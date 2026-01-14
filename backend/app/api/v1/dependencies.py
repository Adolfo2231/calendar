from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.extensions import get_db
from app.extensions.email import fastmail
from app.services import AuthService, EmailService
from app.facade import AuthFacade


def get_auth_service(
    db: AsyncSession = Depends(get_db),
) -> AuthService:
    """Dependency para obtener AuthService con sesión de BD"""
    return AuthService(db)


def get_email_service() -> EmailService:
    """Dependency para obtener EmailService"""
    return EmailService(fastmail)


def get_auth_facade(
    db: AsyncSession = Depends(get_db),
    email_service: EmailService = Depends(get_email_service),
) -> AuthFacade:
    """Dependency para obtener AuthFacade con sesión de BD y servicio de email"""
    return AuthFacade(db, email_service)

