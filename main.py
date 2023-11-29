from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from google.cloud.datastore import Entity
from pydantic import BaseModel
from settings import DS_CLIENT


app = FastAPI(title="Demo Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Task(BaseModel):
    """Task Model"""

    id: str
    title: str


def get_task(task_id: str) -> Entity | None:
    """Get Task from DataStore"""
    key = DS_CLIENT.key("Task", task_id)
    return DS_CLIENT.get(key)


@app.get("/api/tasks", response_model=List[Task])
async def get_tasks():
    """Getting a list of tasks"""
    q = DS_CLIENT.query(kind="Task")
    return [Task(**task) for task in q.fetch()]


@app.post("/api/tasks")
async def add_task(task: Task):
    key = DS_CLIENT.key("Task", task.id)
    entity = Entity(key=key)
    entity.update(task.model_dump())
    DS_CLIENT.put(entity)


@app.delete("/api/tasks/{task_id}")
async def delete_task(task_id: str):
    if not get_task(task_id):
        print("task not found")
        raise HTTPException(status_code=404, detail=f"task not found for id:{task_id}")
    key = DS_CLIENT.key("Task", task_id)
    DS_CLIENT.delete(key)
