from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Event
from .base import BaseRepository

class EventRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(Event, session)

    async def get_events_by_user_id(self, user_id: str) -> list[Event]:
        result = await self.session.execute(select(Event).where(Event.user_id == user_id))
        return result.scalars().all()