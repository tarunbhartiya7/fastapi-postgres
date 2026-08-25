from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.tasks.dtos import TaskSchema
from src.tasks.models import TaskModel


def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    return {"tasks": tasks}


def get_task(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task": task}


def create_task(body: TaskSchema, db: Session):
    task = TaskModel(**body.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return {"task": task}


def update_task(task_id: int, body: TaskSchema, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in body.model_dump().items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return {"task": task}


def delete_task(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
