from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.database import Base
from sqlalchemy.orm import relationship

class List(Base):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship("Project", back_populates="lists")
    tasks = relationship("Task", back_populates="list", cascade="all, delete-orphan")
