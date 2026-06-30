import _frozen_importlib
from sqlalchemy.orm import Session
from storage.crud.db_crud import get_task_by_id, add_task, get_overdue_task, mark_as_completed, delete_task
from ..schema.tasks import TaskCreate
from api.exceptions.httpexception import NotFoundException, BadRequestException
from storage.entities import db_def as models
import datetime


class TaskManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True

    async def get_task(self, db: Session, task_id: int):
        task_retrieved = get_task_by_id(db, task_id=task_id)
        if task_retrieved:
            return task_retrieved
        else:
            raise NotFoundException(extra=f"there is no task with ID = {task_id}")
    
    async def create_task(self, db : Session, task: TaskCreate):
        if task.deadline < datetime.date.today():
            raise BadRequestException(extra="Deadline cannot be in the past")
        task_to_add = models.TaskEntity(
            name=task.name,
            content=task.content,
            deadline=task.deadline,
            is_completed = False
        )
        task_created = add_task(db, task2create=task_to_add)
        return task_created
    
    async def get_overdue(self, db : Session):
        return get_overdue_task(db)
    
    async def complete_task(self, db : Session, task_id: int):
        complete = mark_as_completed(db=db, task_id=task_id)
        if complete:
            return complete
        else:
            raise NotFoundException(extra=f"there is no task with ID = {task_id}")

    async def delete_by_id(self, db : Session, task_id : int):
        removed = delete_task(db, task_id)
        if removed is None:
            raise NotFoundException(extra=f"No task found with id = {task_id}, so no task is deleted")
        else:
            return removed