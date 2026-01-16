from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel
from datetime import datetime

class Event(BaseModel):
    __tablename__ = "events"
    
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    user_id = Column(String(255), ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="events")

    @staticmethod
    def validate_dates(start_date: datetime, end_date: datetime) -> bool:
        return start_date < end_date