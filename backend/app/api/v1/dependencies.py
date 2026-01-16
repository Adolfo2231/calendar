from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from app.extensions import get_db
from app.extensions.email import fastmail
from app.extensions.jwt import verify_token
from app.services import AuthService, EmailService
from app.facade import AuthFacade, EventFacade
from app.repository import UserRepository
from app.schemas import ResponseUser

security = HTTPBearer()


def get_auth_service(
    db: AsyncSession = Depends(get_db),
) -> AuthService:
    """Dependency para obtener AuthService con sesión de BD"""
    return AuthService(db)


def get_email_service() -> EmailService:
    """Dependency para obtener EmailService"""
    return EmailService()  # Ya no necesita fastmail como parámetro


def get_auth_facade(
    db: AsyncSession = Depends(get_db),
    email_service: EmailService = Depends(get_email_service),
) -> AuthFacade:
    """Dependency para obtener AuthFacade con sesión de BD y servicio de email"""
    return AuthFacade(db, email_service)

def get_event_facade(
    db: AsyncSession = Depends(get_db),
) -> EventFacade:
    """Dependency para obtener EventFacade con sesión de BD"""
    return EventFacade(db)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> ResponseUser:
    """
    Dependency que verifica el token JWT y retorna el usuario actual.
    
    Raises:
        HTTPException: Si el token es inválido, expirado o el usuario no existe
    """
    token = credentials.credentials
    
    try:
        # Verificar y decodificar el token
        payload = verify_token(token)
        user_id = payload.get("sub")
        token_type = payload.get("type")
        
        # Verificar que es un token de acceso
        if token_type != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type"
            )
        
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload"
            )
        
        # Obtener el usuario de la base de datos
        user_repository = UserRepository(db)
        user = await user_repository.get(user_id)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
        
        return ResponseUser.model_validate(user)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )