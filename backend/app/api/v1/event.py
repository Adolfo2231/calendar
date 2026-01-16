from fastapi import APIRouter, Depends
from app.schemas import Event, EventUpdate, ResponseEvent, ResponseUser
from app.api.v1.dependencies import get_event_facade, get_current_user
from typing import List

router = APIRouter(tags=["event"])

@router.get("/list", response_model=List[ResponseEvent])
async def list_events(
    current_user: ResponseUser = Depends(get_current_user),
    event_facade = Depends(get_event_facade)
):
    """Obtiene la lista de eventos del usuario actual"""
    return await event_facade.list_events(current_user.id)

@router.get("/{event_id}", response_model=ResponseEvent)
async def get_event(
    event_id: str,
    current_user: ResponseUser = Depends(get_current_user),
    event_facade = Depends(get_event_facade)
):
    """Obtiene un evento específico (solo si pertenece al usuario)"""
    return await event_facade.get_event(event_id, current_user.id)

@router.post("/create", response_model=ResponseEvent)
async def create_event(
    event_data: Event,
    current_user: ResponseUser = Depends(get_current_user),
    event_facade = Depends(get_event_facade)
):
    """Crea un nuevo evento (requiere autenticación)"""
    # Agregar el user_id del token al evento
    event_dict = event_data.model_dump()
    event_dict["user_id"] = current_user.id
    return await event_facade.create_event(event_dict)

@router.patch("/{event_id}", response_model=ResponseEvent)
async def update_event(
    event_id: str,
    event_data: EventUpdate,
    current_user: ResponseUser = Depends(get_current_user),
    event_facade = Depends(get_event_facade)
):
    """Actualiza parcialmente un evento específico (PATCH) - solo si pertenece al usuario"""
    # Filtrar solo los campos que fueron enviados (no None)
    event_dict = event_data.model_dump(exclude_unset=True)
    # No permitir cambiar el user_id
    return await event_facade.update_event(event_id, event_dict, current_user.id)

@router.delete("/{event_id}", response_model=ResponseEvent)
async def delete_event(
    event_id: str,
    current_user: ResponseUser = Depends(get_current_user),
    event_facade = Depends(get_event_facade)
):
    """Elimina un evento específico (solo si pertenece al usuario)"""
    return await event_facade.delete_event(event_id, current_user.id)


