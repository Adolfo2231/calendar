from sqlalchemy.ext.asyncio import AsyncSession
from app.repository import UserRepository

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_repository = UserRepository(session)

    async def register_user(self, user_data: dict):
        """Registra un nuevo usuario"""
        user = await self.user_repository.create(user_data)
        await self.session.commit()  # Commit a nivel de servicio
        return user  # Devolvemos el objeto SQLAlchemy directamente ya que el Pydantic lo convierte automáticamente en el ResponseUser del endpoint

    #TODO: añadir métodos para login, logout, forgot password, reset password