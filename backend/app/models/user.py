from sqlalchemy import Column, String
from .base import BaseModel

class User(BaseModel):
    """Modelo de usuario en la base de datos"""
    __tablename__ = "users"
    
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)  # Hash de la contraseña
    role = Column(String(50), nullable=False, default="user")

    #TODO: hashear la contraseña, verificar el hash de la contraseña