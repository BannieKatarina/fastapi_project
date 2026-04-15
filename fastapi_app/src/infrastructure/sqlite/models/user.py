from src.infrastructure.sqlite.database import Database

from sqlalchemy.orm import Mapped, mapped_column


class User(Database):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(primary_key=True, nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=False)
