from sqlalchemy.ext.asyncio import AsyncSession
from app.services import EventService
from app.repository import EventRepository
from app.schemas import ResponseEvent
from typing import List

class EventFacade:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.event_repository = EventRepository(session)
        self.event_service = EventService(self.event_repository, session)

    async def create_event(self, event_data: dict) -> ResponseEvent:
        return await self.event_service.create_event(event_data)

    async def list_events(self, user_id: str) -> List[ResponseEvent]:
        return await self.event_service.list_events(user_id)

    async def get_event(self, event_id: str, user_id: str) -> ResponseEvent:
        return await self.event_service.get_event(event_id, user_id)

    async def update_event(self, event_id: str, event_data: dict, user_id: str) -> ResponseEvent:
        return await self.event_service.update_event(event_id, event_data, user_id)

    async def delete_event(self, event_id: str, user_id: str) -> ResponseEvent:
        return await self.event_service.delete_event(event_id, user_id)