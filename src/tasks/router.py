from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db

tasks_router = APIRouter(prefix="/v1/tasks")


@tasks_router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return controller.get_tasks(db)


@tasks_router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    return controller.get_task(task_id, db)


@tasks_router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)


@tasks_router.put("/{task_id}")
def update_task(task_id: int, body: TaskSchema, db: Session = Depends(get_db)):
    return controller.update_task(task_id, body, db)


@tasks_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    controller.delete_task(task_id, db)
