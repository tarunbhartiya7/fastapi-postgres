from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db

tasks_router = APIRouter(prefix="/v1/tasks")


@tasks_router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return controller.get_tasks(db)


@tasks_router.post("/")
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)
