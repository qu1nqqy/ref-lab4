from pydantic import BaseModel, Field

class TaskResponse(BaseModel):
    id: int = Field(...)
    text: str = Field(...)
    done: bool = Field(...)

class DeleteResponse(BaseModel):
    deleted: bool = Field(...)