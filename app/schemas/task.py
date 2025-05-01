from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    list_id: int

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    list_id: int

    class Config:
        orm_mode = True
