#from fastapi_app.src.infrastructure.sqlite.database import Base
from src.infrastructure.sqlite.database import Base
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True)
    title: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=True)
    pub_date: Mapped[datetime] = mapped_column(default=func.now())
    author: Mapped[str] = mapped_column(ForeignKey("users.username"))
    category: Mapped[str] = mapped_column(ForeignKey("categories.title"))
    location: Mapped[str] = mapped_column(ForeignKey("locations.name"))
    is_published: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    image: Mapped[str] = mapped_column(nullable=True)
