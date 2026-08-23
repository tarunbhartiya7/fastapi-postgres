from fastapi import FastAPI

app = FastAPI(title="Task management API",
              description="API for managing tasks")


@app.get("/health")
def health_check():
    return {"status": "ok"}
