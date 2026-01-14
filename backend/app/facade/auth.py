from sqlalchemy.ext.asyncio import AsyncSession
from app.services import AuthService, EmailService
from app.repository import UserRepository
from app.schemas import User, ResponseUser, ResponseLogin, UserLogin


class AuthFacade:
    """
    Facade para operaciones de autenticación.
    
    Esta capa solo orquesta y coordina:
    - Crea los repositorios y servicios necesarios
    - Llama a los servicios que manejan la lógica de negocio y transacciones
    - Convierte objetos SQLAlchemy a schemas Pydantic
    """
    
    def __init__(self, session: AsyncSession, email_service: EmailService):
        self.session = session
        self.user_repository = UserRepository(session)
        self.auth_service = AuthService(self.user_repository, session)
        self.email_service = email_service  # Instancia de EmailService (objeto)
    
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
        
        # Enviar email de bienvenida (opcional, puede fallar sin afectar el registro)
        try:
            await self.email_service.send_registration_email(
                email=db_user.email,
                username=db_user.username
            )
        except Exception as e:
            # Log del error pero no fallar el registro
            print(f"⚠️ Error enviando email de bienvenida: {e}")
            # El registro continúa normalmente aunque el email falle
        
        return ResponseUser.model_validate(db_user)

    async def login_user(self, user_data: UserLogin) -> ResponseLogin:
        """ 
        Inicia sesión de un usuario.
        
        El facade solo orquesta:
        1. Llama al Service que maneja toda la lógica de negocio y transacciones
        2. Convierte a ResponseLogin
        
        Returns:
            ResponseLogin: Schema Pydantic con tokens y usuario
        """
        # Service maneja toda la lógica de negocio y devuelve dict con tokens y user
        login_data = await self.auth_service.login_user(user_data.model_dump())
        
        # Convertir el user SQLAlchemy a ResponseUser
        user_response = ResponseUser.model_validate(login_data["user"])
        
        # Retornar ResponseLogin con tokens y usuario
        return ResponseLogin(
            access_token=login_data["access_token"],
            refresh_token=login_data["refresh_token"],
            user=user_response
        )

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