from pydantic import BaseModel
from typing import List
from app.schemas.task import TaskResponse

class ListBase(BaseModel):
    name: str
    project_id: int

class ListCreate(ListBase):
    pass

class ListUpdate(ListBase):
    pass

class ListResponse(ListBase):
    id: int
    project_id: int
    tasks: List[TaskResponse] = []

    class Config:
        orm_mode = True