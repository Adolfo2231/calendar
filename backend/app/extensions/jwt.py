from datetime import datetime, timedelta
from jose import jwt
from app.config import settings

def create_access_token(data: dict):
    """
    Crea un token de acceso con expiración corta.
    
    Args:
        data: Datos a incluir en el token (debe incluir "sub" con el user_id)
        
    Returns:
        str: Token JWT de acceso
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "type": "access"})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def create_refresh_token(data: dict):
    """
    Crea un token de refresco con expiración larga.
    
    Args:
        data: Datos a incluir en el token (debe incluir "sub" con el user_id)
        
    Returns:
        str: Token JWT de refresco
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "type": "refresh"})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def verify_token(token: str):
    """
    Verifica un token de acceso.
    """
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])

def verify_refresh_token(token: str):
    """
    Verifica un token de refresco.
    """
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])

def decode_token(token: str):
    """
    Decodifica un token.
    """
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])