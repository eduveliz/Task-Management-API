from pydantic import BaseModel
from typing import List, Optional
from app.schemas.list import ListResponse

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    lists: List[ListResponse] = []

    class Config:
        orm_mode = True
