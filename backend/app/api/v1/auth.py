from fastapi import APIRouter, Depends
from app.schemas import User, ResponseUser, ResponseLogin, UserLogin
from app.api.v1.dependencies import get_auth_facade

router = APIRouter(tags=["auth"])

@router.post("/register", response_model=ResponseUser)
async def register(
    user_data: User,
    auth_facade = Depends(get_auth_facade)
):
    """Registra un nuevo usuario"""
    return await auth_facade.register_user(user_data)

@router.post("/login", response_model=ResponseLogin)
async def login(
    user_data: UserLogin,
    auth_facade = Depends(get_auth_facade)
):
    """Inicia sesión de un usuario"""
    return await auth_facade.login_user(user_data)