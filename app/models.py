from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    done: bool = False

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None
