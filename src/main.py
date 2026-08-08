from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.database import (
    create_task,
    get_task,
    get_all_tasks,
    update_task,
    delete_task,
)

app = FastAPI()

@app.get("/")
def root():
    return{
        "message":"Smart Workspace Assistant API"
}

@app.get("/about")
def about():
    return{
        "project": "Smart Workspace Assistant API",
        "version": "2.0.0"
    }

@app.get("/tasks/{task_id}")
def get_task_endpoint(task_id: int):

    rows = get_task(task_id)

    if rows is None:
        raise HTTPException(
            status_code = 404,
            detail = "Task not found"
        )
    return rows 

@app.get("/search")
def search(keyword:str):
    return{
        "keyword": keyword
    }

class Task(BaseModel):
    title : str

@app.post("/tasks")
def create_task_endpoint(task:Task):
    create_task(task.title)
    return task

@app.get("/tasks")
def get_all_task_endpoint():
    return get_all_tasks()

@app.put("/tasks/{task_id}")
def update_task_endpoint(task_id: int, task:Task):
    update_task(task_id, task.title)
    return task

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int):
    delete_task(task_id)

    return{
        "message": "Task deleted successfully"
    }