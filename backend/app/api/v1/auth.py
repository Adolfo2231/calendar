from fastapi import APIRouter
from app.schemas import User, ResponseUser
from app.services import AuthService

router = APIRouter(tags=["auth"])

@router.post("/register", response_model=ResponseUser)
async def register(user: User):
    """Registra un nuevo usuario"""
    user = await AuthService().register_user(user.model_dump())
    #? Devolvemos el objeto SQLAlchemy directamente ya que el Pydantic lo convierte automáticamente en el ResponseUser del endpoint
    return user