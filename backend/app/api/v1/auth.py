from fastapi import APIRouter, Depends
from app.schemas import User, ResponseUser
from app.api.v1.dependencies import get_auth_service

router = APIRouter(tags=["auth"])

@router.post("/register", response_model=ResponseUser)
async def register(
    user_data: User,
    auth_service = Depends(get_auth_service)
):
    """Registra un nuevo usuario"""
    db_user = await auth_service.register_user(user_data.model_dump())
    return ResponseUser.model_validate(db_user)