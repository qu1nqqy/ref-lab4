cdef class TodoManager:
    cdef object redis
    cpdef add_task(self, str text)
    cpdef list_tasks(self)
    cpdef mark_done(self, int task_id)
    cpdef delete_task(self, int task_id)
