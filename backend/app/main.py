from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from redis import Redis
from todo import TodoManager

app = FastAPI(title="Cython TODO App")

redis = Redis(host="redis", port=6379, decode_responses=True)
todo = TodoManager(redis)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/add")
def add_task(text: str):
    return todo.add_task(text)

@app.get("/list")
def list_tasks():
    return todo.list_tasks()

@app.post("/done/{task_id}")
def mark_done(task_id: int):
    task = todo.mark_done(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/delete/{task_id}")
def delete_task(task_id: int):
    return todo.delete_task(task_id)
