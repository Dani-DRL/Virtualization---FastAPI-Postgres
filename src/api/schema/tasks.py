from pydantic import BaseModel
from datetime import date
from pydantic import ConfigDict
    
class TaskBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    content: str
    deadline: date

class TaskCreate(TaskBaseModel):
    pass

class Task(TaskBaseModel):
    id: int
    is_completed: bool
