from app.repository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def register_user(self, user_data: dict):
        user = await self.user_repository.create(user_data)
        return user # Devolvemos el objeto SQLAlchemy directamente ya que el Pydantic lo convierte automáticamente en el ResponseUser del endpoint

    #TODO: añadir métodos para login, logout, forgot password, reset password