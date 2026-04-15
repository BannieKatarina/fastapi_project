from typing import Type

from sqlalchemy.orm import Session

from infrastructure.sqlite.models.post import Post


class PostRepository:
    def __init__(self):
        self._model: Type[Post] = Post

    def get(self, session: Session, id: int) -> Post:
        query = (
            session.query(self._model)
            .where(self._model.id == id)
        )

        return query.scalar()