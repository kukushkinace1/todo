from pydantic import BaseModel, Field, ConfigDict

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=20)
    description: str | None = Field(default=None, max_length=100)


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=20)
    description: str | None = Field(default=None, max_length=100)
    is_complete: bool | None = None


class TaskRead(BaseModel):
    id: int 
    title: str
    description: str | None = None
    is_complete: bool

    model_config = ConfigDict(from_attributes=True)
