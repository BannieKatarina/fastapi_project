#from fastapi_app.src.infrastructure.sqlite.database import Base
from src.infrastructure.sqlite.database import Base
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True)
    text: Mapped[str] = mapped_column(nullable=False)
    post: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    author: Mapped[str] = mapped_column(ForeignKey("users.username"))
