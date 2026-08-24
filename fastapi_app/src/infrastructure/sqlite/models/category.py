#from fastapi_app.src.infrastructure.sqlite.database import Base
from src.infrastructure.sqlite.database import Base
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Category(Base):
    __tablename__ = "categories"

    title: Mapped[str] = mapped_column(primary_key=True, nullable=False, unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    is_published: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
