from todo.database.base import Base, engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    text = Column(String(300))
    is_complete = Column(Boolean, default=False)
    data_created = Column(DateTime, default=datetime.utcnow)

