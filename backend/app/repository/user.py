from .base import BaseRepository
from app.models.user import User

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    
    #TODO: añadir métodos para buscar usuarios por email o username, actualizar contraseña