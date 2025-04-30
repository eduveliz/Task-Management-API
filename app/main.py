from fastapi import FastAPI
from app.routers import projects, list, task

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}

app.include_router(projects.router)
app.include_router(list.router)
app.include_router(task.router)