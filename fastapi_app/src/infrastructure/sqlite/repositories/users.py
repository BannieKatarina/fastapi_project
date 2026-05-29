from typing import Type

from sqlalchemy.orm import Session

from src.infrastructure.sqlite.models.user import User
from src.schemas.classes import User as UserSchema


class UserRepository:
    def __init__(self):
        self._model: Type[User] = User

    def get(self, session: Session, login: str) -> User:
        query = (
            session.query(self._model)
            .where(self._model.username == login)
        )
        return query.scalar()

    def get_all(self, session: Session) -> list:
        query = session.query(self._model).all()
        return query

    def post(self, session: Session, user: UserSchema) -> User:
        db_user = User(**user.dict())
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
