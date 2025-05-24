from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from datetime import datetime
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    due_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)
