from starlette.status import HTTP_201_CREATED
from sqlalchemy.orm import Session
from fastapi import Depends
from ..controllers.task_manager import TaskManager
from fastapi import APIRouter
from typing import List
from ..schema.tasks import Task, TaskCreate
from config.postgres import get_db

router: APIRouter = APIRouter()

Manager = TaskManager()

@router.get("/")
async def greeting():
    return {"hello": "Welcome to Daniel FastAPI APP"}

@router.get("/overdue", response_model=List[Task])
async def get_overdue_rt(db : Session =Depends(get_db)):
    return await Manager.get_overdue(db=db)
    

@router.get("/{id}", response_model=Task)
async def get_task_rt(id: int, db : Session =Depends(get_db)):
    #Recovery from db
    return await Manager.get_task(db=db, task_id=id)

@router.post("/create/", response_model=Task, status_code=HTTP_201_CREATED)
async def create_task_rt(task: TaskCreate, db : Session =Depends(get_db)):
    return await Manager.create_task(db=db, task=task)


@router.put("/{id}/complete", response_model=Task)
async def complete_task_rt(id: int, db : Session =Depends(get_db)):
    return await Manager.complete_task(db=db, task_id=id)

@router.delete("/{id}/delete", response_model=Task)
async def delete_task_by_id_rt(id : int, db : Session = Depends(get_db)):
    return await Manager.delete_by_id(db=db, task_id=id)