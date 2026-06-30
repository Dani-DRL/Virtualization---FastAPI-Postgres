from sqlalchemy.orm import Session
from ..entities import db_def as models
import datetime

def get_task_by_id(db: Session, task_id:int):
    return db.query(models.TaskEntity).filter(models.TaskEntity.id == task_id).first()

def add_task(db: Session, task2create: models.TaskEntity):
    db.add(task2create)
    db.commit()
    db.refresh(task2create)
    return task2create

def get_overdue_task(db: Session):
    return db.query(models.TaskEntity).filter(models.TaskEntity.deadline < datetime.date.today()).all()

def mark_as_completed(db: Session, task_id: int):
    to_complete = get_task_by_id(db, task_id)
    if to_complete is None:
        return None
    to_complete.is_completed = True
    db.commit()
    db.refresh(to_complete)
    return to_complete

def delete_task(db: Session, task_id: int):
    to_delete = get_task_by_id(db, task_id)
    if to_delete is None:
        return None
    db.delete(to_delete)
    db.commit()
    return to_delete