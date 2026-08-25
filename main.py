from fastapi import FastAPI
from src.utils.db import init_db
from src.tasks.router import tasks_router
init_db()

app = FastAPI(title="Task management API",
              description="API for managing tasks")

app.include_router(tasks_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
