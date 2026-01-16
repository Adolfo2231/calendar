import hashlib
from sqlalchemy import Column, String, event
from sqlalchemy.orm import relationship
from .base import BaseModel


class User(BaseModel):
    """Modelo de usuario en la base de datos"""
    __tablename__ = "users"
    
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)  # Hash de la contraseña
    role = Column(String(50), nullable=False, default="user")
    
    events = relationship("Event", back_populates="user")
    
    @staticmethod
    def _hash_password(password: str) -> str:
        """
        Hashea una contraseña usando SHA-256.
        
        Args:
            password: Contraseña en texto plano
            
        Returns:
            str: Contraseña hasheada
        """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    def verify_password(self, plain_password: str) -> bool:
        """
        Verifica si una contraseña en texto plano coincide con el hash almacenado.
        
        Args:
            plain_password: Contraseña en texto plano
            
        Returns:
            bool: True si la contraseña coincide, False en caso contrario
        """
        hashed = self._hash_password(plain_password)
        return hashed == self.password


@event.listens_for(User, 'before_insert', propagate=True)
@event.listens_for(User, 'before_update', propagate=True)
def hash_password_before_save(mapper, connection, target):
    """
    Evento que hashea la contraseña antes de insertar o actualizar.
    Solo hashea si la contraseña ha cambiado (no está ya hasheada).
    """
    # Verificar si la contraseña parece estar ya hasheada (64 caracteres para SHA-256)
    # o si es una contraseña nueva en texto plano
    if target.password and len(target.password) != 64:
        target.password = User._hash_password(target.password)