from sqlalchemy.ext.asyncio import AsyncSession
from app.repository import UserRepository
from app.exception.bussines import EmailExistError, UsernameExistError, ErrorAuthentication
from app.extensions.jwt import create_access_token, create_refresh_token


class AuthService:
    """
    Servicio de autenticación con lógica de negocio.
    
    Maneja toda la lógica de negocio relacionada con autenticación.
    Maneja las transacciones de BD (commit/rollback).
    """
    
    def __init__(self, user_repository: UserRepository, session: AsyncSession):
        self.user_repository = user_repository
        self.session = session
    
    async def register_user(self, user_data: dict):
        """
        Registra un nuevo usuario.
        
        Maneja toda la lógica de negocio:
        - Validaciones de existencia
        - Creación del usuario
        - Manejo de transacciones (commit/rollback)
        
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
            user = await self.user_repository.create(user_data)
            await self.session.commit()
            return user
        except Exception:
            await self.session.rollback()
            raise

    #TODO: añadir métodos para login, logout, forgot password, reset password
    async def login_user(self, user_data: dict):
        """
        Inicia sesión de un usuario.
        
        Maneja toda la lógica de negocio:
        - Validar que el usuario existe
        - Verificar contraseña
        - Generar tokens JWT
        
        Args:
            user_data: Datos del usuario (email y password)
            
        Returns:
            dict: Diccionario con access_token, refresh_token y user
            
        Raises:
            ErrorAuthentication: Si el email no existe o la contraseña es incorrecta
        """
        # Buscar usuario por email
        user = await self.user_repository.get_by_email(user_data["email"])
        
        # Validar que el usuario existe
        if not user:
            raise ErrorAuthentication()
        
        # Verificar contraseña
        if not user.verify_password(user_data["password"]):
            raise ErrorAuthentication()
        
        # Crear tokens con diccionario de datos
        access_token = create_access_token({"sub": user.id})
        refresh_token = create_refresh_token({"sub": user.id})
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": user
        }