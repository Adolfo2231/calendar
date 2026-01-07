from sqlalchemy.ext.asyncio import AsyncSession
from app.services import AuthService
from app.repository import UserRepository
from app.schemas import User, ResponseUser


class AuthFacade:
    """
    Facade para operaciones de autenticación.
    
    Esta capa solo orquesta y coordina:
    - Crea los repositorios y servicios necesarios
    - Llama a los servicios que manejan la lógica de negocio y transacciones
    - Convierte objetos SQLAlchemy a schemas Pydantic
    """
    
    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_repository = UserRepository(session)
        self.auth_service = AuthService(self.user_repository, session)
    
    async def register_user(self, user_data: User) -> ResponseUser:
        """
        Registra un nuevo usuario.
        
        El facade solo orquesta:
        1. Llama al Service que maneja toda la lógica de negocio y transacciones
        2. Convierte a ResponseUser
        
        Returns:
            ResponseUser: Schema Pydantic listo para ser devuelto por el endpoint
        """
        # Service maneja toda la lógica de negocio y transacciones
        db_user = await self.auth_service.register_user(user_data.model_dump())
        return ResponseUser.model_validate(db_user)

    async def login_user(self, user_data: User) -> ResponseUser:
        """ 
        Inicia sesión de un usuario.
        
        El facade solo orquesta:
        1. Llama al Service que maneja toda la lógica de negocio y transacciones
        2. Convierte a ResponseUser
        
        Returns:
            ResponseUser: Schema Pydantic listo para ser devuelto por el endpoint
        """
        # Service maneja toda la lógica de negocio
        db_user = await self.auth_service.login_user(user_data.model_dump())
        return ResponseUser.model_validate(db_user)

    async def logout_user(self) -> ResponseUser:
        """
        Cierra sesión de un usuario.
        
        El facade solo orquesta:
        1. Llama al Service que maneja toda la lógica de negocio y transacciones
        2. Convierte a ResponseUser
        
        Returns:
            ResponseUser: Schema Pydantic listo para ser devuelto por el endpoint
        """
        pass

    async def forgot_password(self, user_data: User) -> ResponseUser:
        """
        Recupera la contraseña de un usuario.
        
        El facade solo orquesta:
        1. Llama al Service que maneja toda la lógica de negocio y transacciones
        2. Convierte a ResponseUser
        
        Returns:
            ResponseUser: Schema Pydantic listo para ser devuelto por el endpoint
        """
        pass

    async def reset_password(self, user_data: User) -> ResponseUser:
        """
        Resetea la contraseña de un usuario.
        
        El facade solo orquesta:
        1. Llama al Service que maneja toda la lógica de negocio y transacciones
        2. Convierte a ResponseUser
        
        Returns:
            ResponseUser: Schema Pydantic listo para ser devuelto por el endpoint
        """
        pass