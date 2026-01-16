from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy import select

class BaseRepository:
    def __init__(self, model: Any, session: AsyncSession):
        self.model = model
        self.session = session

    async def create(self, data: dict) -> Any:
        """Crea un nuevo registro en la BD desde un dict"""
        db_obj = self.model(**data)
        self.session.add(db_obj)
        await self.session.flush()  # NO commit - lo maneja el servicio
        await self.session.refresh(db_obj)  # Para obtener el ID generado
        return db_obj

    async def get(self, id: str) -> Any:
        return await self.session.get(self.model, id)
    
    async def get_all(self) -> List[Any]:
        return await self.session.execute(select(self.model))

    async def update(self, obj: Any) -> Any:
        merged_obj = await self.session.merge(obj)
        await self.session.flush()  # NO commit - lo maneja el servicio
        await self.session.refresh(merged_obj)
        return merged_obj

    async def delete(self, obj: Any) -> Any:
        merged_obj = await self.session.merge(obj)
        await self.session.delete(merged_obj)
        await self.session.flush()  # NO commit - lo maneja el servicio
        return merged_obj