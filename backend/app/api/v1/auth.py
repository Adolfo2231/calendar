from fastapi import APIRouter, Depends
from app.schemas import User, ResponseUser
from app.api.v1.dependencies import get_auth_facade

router = APIRouter(tags=["auth"])

@router.post("/register", response_model=ResponseUser)
async def register(
    user_data: User,
    auth_facade = Depends(get_auth_facade)
):
    """Registra un nuevo usuario"""
    return await auth_facade.register_user(user_data)