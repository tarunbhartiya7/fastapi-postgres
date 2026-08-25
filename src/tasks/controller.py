from sqlalchemy.orm import Session

from src.tasks.dtos import TaskSchema
from src.tasks.models import TaskModel


def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    return {"tasks": tasks}


def create_task(body: TaskSchema, db: Session):
    task = TaskModel(**body.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return {"task": task}
