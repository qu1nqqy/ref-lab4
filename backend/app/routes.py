from fastapi import APIRouter, HTTPException
from todo import TodoManager
from redis_client import redis
from typing import List
from schemas import TaskResponse, DeleteResponse

router = APIRouter()

todo = TodoManager(redis)


@router.post("/add")
def add_task(text: str) -> TaskResponse:
    return todo.add_task(text)


@router.get("/list")
def list_tasks() -> List[TaskResponse]:
    return todo.list_tasks()


@router.post("/done/{task_id}")
def mark_done(task_id: int) -> TaskResponse:
    task = todo.mark_done(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/delete/{task_id}")
def delete_task(task_id: int) -> DeleteResponse:
    return todo.delete_task(task_id)
