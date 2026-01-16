from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .user import ResponseUser

class Event(BaseModel):
    title: str = Field(min_length=3, max_length=255)
    description: str = Field(min_length=3, max_length=255)
    start_date: datetime = Field(default_factory=datetime.now)
    end_date: datetime = Field(default_factory=datetime.now)
    # user_id se obtiene automáticamente del token JWT, no se envía en el body

    class Config:
        str_strip_whitespace = True #? Para eliminar los espacios en blanco de los strings

class EventUpdate(BaseModel):
    """Schema para actualización parcial de eventos (PATCH)"""
    title: Optional[str] = Field(None, min_length=3, max_length=255)
    description: Optional[str] = Field(None, min_length=3, max_length=255)
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    class Config:
        str_strip_whitespace = True

class ResponseEvent(BaseModel):
    id: str
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    user: ResponseUser  # Objeto usuario completo en lugar de solo user_id

    class Config:
        from_attributes = True #? Para convertir los objetos SQLAlchemy a Pydantic