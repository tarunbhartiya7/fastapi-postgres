from fastapi import FastAPI
from src.utils.db import init_db
from src.tasks.models import TaskModel
from src.utils.db import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

init_db()

app = FastAPI(title="Task management API",
              description="API for managing tasks")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).all()
    return {"tasks": tasks}
