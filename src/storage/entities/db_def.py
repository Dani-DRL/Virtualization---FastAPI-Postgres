from sqlalchemy import Boolean, Column, Integer, String, Date
from config.postgres import Base


class TaskEntity(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    content = Column(String, index=True)
    deadline = Column(Date, index=True)
    is_completed = Column(Boolean, index=True)