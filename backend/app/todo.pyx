import json

cdef class TodoManager:
    def __init__(self, redis_instance):
        self.redis = redis_instance

    cpdef add_task(self, str text):
        task_id = self.redis.incr("todo:id")
        task_key = f"todo:{task_id}"
        task_data = {"id": task_id, "text": text, "done": False}
        self.redis.set(task_key, json.dumps(task_data))
        self.redis.rpush("todos", task_id)
        return task_data

    cpdef list_tasks(self):
        task_ids = self.redis.lrange("todos", 0, -1)
        tasks = []
        for tid in task_ids:
            task = self.redis.get(f"todo:{int(tid)}")
            if task:
                tasks.append(json.loads(task))
        return tasks

    cpdef mark_done(self, int task_id):
        key = f"todo:{task_id}"
        data = self.redis.get(key)
        if data is None:
            return None
        task = json.loads(data)
        task["done"] = True
        self.redis.set(key, json.dumps(task))
        return task

    cpdef delete_task(self, int task_id):
        key = f"todo:{task_id}"
        self.redis.delete(key)
        self.redis.lrem("todos", 0, task_id)
        return {"deleted": True}
