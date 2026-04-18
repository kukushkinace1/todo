from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import mapped_column, Mapped
from database import Base

class ToDo(Base):
    __tablename__ = 'todo' 
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    description:  Mapped[str | None] = mapped_column(String)
    is_complete:  Mapped[bool] = mapped_column(Boolean, default=False)