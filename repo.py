from sqlalchemy.ext.asyncio import AsyncSession
from todo_models import ToDo
from todo_schemas import TaskCreate, TaskUpdate

class TaskRepo:
    def __init__(self, session:AsyncSession) -> None:
        self.session = session
    
    async def get_by_id(self, task_id: int) -> ToDo | None:
        return await self.session.get(ToDo, task_id)
    
    async def create(self, data: TaskCreate) -> ToDo:
        task = ToDo(title = data.title,
            description = data.description,
            is_complete = False)
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def delete(self, task: ToDo) -> None:
        await self.session.delete(task)
        await self.session.commit()

    async def update(self, task: ToDo, data: TaskUpdate) -> ToDo:  
        if data.title is not None:
            task.title = data.title

        if data.description is not None:
            task.description = data.description

        if data.is_complete is not None:
            task.is_complete = data.is_complete

        await self.session.commit()
        await self.session.refresh(task)
        return task
