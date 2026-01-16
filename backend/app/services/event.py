from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select
from app.repository import EventRepository
from app.models.events import Event as EventModel
from app.exception.event import EventNotFoundError, EventPermissionError
from typing import List
from app.schemas import ResponseEvent, ResponseUser

class EventService:
    def __init__(self, event_repository: EventRepository, session: AsyncSession):
        self.event_repository = event_repository
        self.session = session

    async def create_event(self, event_data: dict) -> ResponseEvent:
        try:
            # Crear el evento
            event = await self.event_repository.create(event_data)
            await self.session.commit()
            
            # Cargar el evento con la relación user usando eager loading
            result = await self.session.execute(
                select(EventModel)
                .options(selectinload(EventModel.user))
                .where(EventModel.id == event.id)
            )
            event_with_user = result.scalar_one()
            
            # Verificar que el usuario existe (la relación debería cargarlo automáticamente)
            if not event_with_user.user:
                raise ValueError(f"User with id {event.user_id} not found")
            
            # Construir ResponseEvent con el usuario completo usando la relación
            return ResponseEvent(
                id=event_with_user.id,
                title=event_with_user.title,
                description=event_with_user.description,
                start_date=event_with_user.start_date,
                end_date=event_with_user.end_date,
                user=ResponseUser.model_validate(event_with_user.user)
            )
        except Exception:
            await self.session.rollback()
            raise

    async def list_events(self, user_id: str) -> List[ResponseEvent]:
        try:
            events = await self.event_repository.get_events_by_user_id(user_id)
            # Cargar la relación user para cada evento
            result = await self.session.execute(
                select(EventModel)
                .options(selectinload(EventModel.user))
                .where(EventModel.user_id == user_id)
            )
            events_with_user = result.scalars().all()
            
            return [
                ResponseEvent(
                    id=event.id,
                    title=event.title,
                    description=event.description,
                    start_date=event.start_date,
                    end_date=event.end_date,
                    user=ResponseUser.model_validate(event.user)
                )
                for event in events_with_user
            ]
        except Exception:
            await self.session.rollback()
            raise

    async def get_event(self, event_id: str, user_id: str) -> ResponseEvent:
        try:
            # Cargar el evento con la relación user usando eager loading
            result = await self.session.execute(
                select(EventModel)
                .options(selectinload(EventModel.user))
                .where(EventModel.id == event_id)
            )
            event = result.scalar_one_or_none()
            
            if not event:
                raise EventNotFoundError(f"Event with id {event_id} not found")
            
            # Validar que el evento pertenezca al usuario
            if event.user_id != user_id:
                raise EventPermissionError("You don't have permission to access this event")
            
            if not event.user:
                raise ValueError(f"User not found for event {event_id}")
            
            return ResponseEvent(
                id=event.id,
                title=event.title,
                description=event.description,
                start_date=event.start_date,
                end_date=event.end_date,
                user=ResponseUser.model_validate(event.user)
            )
        except Exception:
            await self.session.rollback()
            raise

    async def update_event(self, event_id: str, event_data: dict, user_id: str) -> ResponseEvent:
        try:
            # Obtener el evento existente
            event = await self.event_repository.get(event_id)
            if not event:
                raise EventNotFoundError(f"Event with id {event_id} not found")
            
            # Validar que el evento pertenezca al usuario
            if event.user_id != user_id:
                raise EventPermissionError("You don't have permission to update this event")
            
            # Actualizar los campos
            for key, value in event_data.items():
                if key != "user_id":  # No permitir cambiar el user_id
                    setattr(event, key, value)
            
            # Actualizar en la BD
            updated_event = await self.event_repository.update(event)
            await self.session.commit()
            
            # Cargar el evento actualizado con la relación user
            result = await self.session.execute(
                select(EventModel)
                .options(selectinload(EventModel.user))
                .where(EventModel.id == updated_event.id)
            )
            event_with_user = result.scalar_one()
            
            return ResponseEvent(
                id=event_with_user.id,
                title=event_with_user.title,
                description=event_with_user.description,
                start_date=event_with_user.start_date,
                end_date=event_with_user.end_date,
                user=ResponseUser.model_validate(event_with_user.user)
            )
        except Exception:
            await self.session.rollback()
            raise

    async def delete_event(self, event_id: str, user_id: str) -> ResponseEvent:
        try:
            # Obtener el evento antes de eliminarlo
            result = await self.session.execute(
                select(EventModel)
                .options(selectinload(EventModel.user))
                .where(EventModel.id == event_id)
            )
            event = result.scalar_one_or_none()
            
            if not event:
                raise EventNotFoundError(f"Event with id {event_id} not found")
            
            # Validar que el evento pertenezca al usuario
            if event.user_id != user_id:
                raise EventPermissionError("You don't have permission to delete this event")
            
            # Guardar los datos antes de eliminar
            event_data = ResponseEvent(
                id=event.id,
                title=event.title,
                description=event.description,
                start_date=event.start_date,
                end_date=event.end_date,
                user=ResponseUser.model_validate(event.user)
            )
            
            # Eliminar el evento
            await self.event_repository.delete(event)
            await self.session.commit()
            
            return event_data
        except Exception:
            await self.session.rollback()
            raise