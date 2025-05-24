from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    due_date: Optional[datetime]

class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    due_date: Optional[datetime]
    completed: Optional[bool]

class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    created_at: datetime
    completed: bool

    class Config:
        from_attributes = True
