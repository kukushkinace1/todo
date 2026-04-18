from fastapi import FastAPI, Depends, HTTPException, status
from todo_schemas import TaskCreate, TaskRead, TaskUpdate
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from repo import TaskRepo
app = FastAPI()


@app.get("/health")
async def health():
    return {'status': "OK"}


@app.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(data: TaskCreate, db: AsyncSession  = Depends(get_db)):
    task = TaskRepo(db)
    return await task.create(data)


@app.get("/{task_id}", response_model=TaskRead)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task_repo = TaskRepo(db)
    task = await task_repo.get_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task_repo = TaskRepo(db)
    task = await task_repo.get_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    await task_repo.delete(task)
    

@app.patch("/{task_id}", response_model=TaskRead)
async def update_task(task_id: int, data: TaskUpdate, db: AsyncSession = Depends(get_db)):
    task_repo = TaskRepo(db)
    task = await task_repo.get_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return await task_repo.update(task, data)