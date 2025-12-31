from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any
from app.extensions.database import AsyncSessionLocal

class BaseRepository:
    def __init__(self, model: Any):
        self.model = model

    async def create(self, data: dict) -> Any:
        """Crea un nuevo registro en la BD desde un dict"""
        async with AsyncSessionLocal() as session:
            db_obj = self.model(**data)
            session.add(db_obj)
            await session.commit()
            await session.refresh(db_obj)  # Para obtener el ID generado
            return db_obj

    async def get(self, id: str) -> Any:
        async with AsyncSessionLocal() as session:
            return await session.get(self.model, id)

    async def update(self, obj: Any) -> Any:
        async with AsyncSessionLocal() as session:
            merged_obj = await session.merge(obj)
            await session.commit()
            await session.refresh(merged_obj)
            return merged_obj

    async def delete(self, obj: Any) -> Any:
        async with AsyncSessionLocal() as session:
            merged_obj = await session.merge(obj)
            await session.delete(merged_obj)
            await session.commit()
            return merged_obj