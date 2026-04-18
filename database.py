from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase    
  
DATABASE_URL = "postgresql+asyncpg://todo_user:todo_pass@localhost:5433/todo_db"  

engine = create_async_engine(DATABASE_URL)  
  
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)  
  
class Base(DeclarativeBase):  
	pass

async def get_db():  
	async with AsyncSessionLocal() as session:  
		yield session