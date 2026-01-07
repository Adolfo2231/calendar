from app.repository import UserRepository
from app.exception.bussines import EmailExistError, UsernameExistError


class AuthService:
    """
    Servicio de autenticación con lógica de negocio.
    
    Maneja toda la lógica de negocio relacionada con autenticación.
    Recibe el repository para acceder a datos cuando lo necesite.
    """
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    async def register_user(self, user_data: dict):
        """
        Registra un nuevo usuario.
        
        Maneja toda la lógica de negocio:
        - Validaciones de existencia
        - Creación del usuario
        
        Args:
            user_data: Datos del usuario a registrar
            
        Returns:
            Usuario creado (objeto SQLAlchemy)
            
        Raises:
            EmailExistError: Si el email ya existe
            UsernameExistError: Si el username ya existe
        """
        # Validar existencia
        if await self.user_repository.get_by_email(user_data["email"]):
            raise EmailExistError()
        
        if await self.user_repository.get_by_username(user_data["username"]):
            raise UsernameExistError()
        try:
            # Crear usuario
            return await self.user_repository.create(user_data)
        except Exception:
            await self.session.rollback()
            raise

    #TODO: añadir métodos para login, logout, forgot password, reset password