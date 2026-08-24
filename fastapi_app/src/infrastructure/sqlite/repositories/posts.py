from typing import Type

from sqlalchemy.orm import Session

from src.infrastructure.sqlite.models.post import Post
from src.infrastructure.sqlite.models.category import Category
from src.infrastructure.sqlite.models.location import Location
from src.infrastructure.sqlite.models.user import User
from src.schemas.classes import PostCreate, Post as PostSchema


class PostRepository:
    def __init__(self):
        self._model: Type[Post] = Post

    def get_all(self, session: Session) -> list:
        query = session.query(self._model).all()
        return query

    def get_one(self, session: Session, post_id: int) -> Post:
        query = (
            session.query(self._model)
            .where(self._model.id == post_id)
        )
        return query.scalar()

    def put(self, session: Session, post_id: int,
            updated_post_data: PostSchema) -> Post:
        query = (
            session.query(self._model)
            .where(self._model.id == post_id)
        )
        for key, value in updated_post_data.dict(exclude_unset=True).items():
            setattr(query, key, value)
        session.add(query)
        session.commit()
        session.refresh(query)
        return query.scalar()

    def delete(self, session: Session, post_id: int) -> dict:
        query = (
            session.query(self._model)
            .where(self._model.id == post_id)
        )
        session.delete(query)
        session.commit()
        return {"message": "Post deleted successfully"}

    def post(self, post: PostCreate, session: Session) -> Post:
        author = (session.query(User)
                  .where(User.username == post.author).first())
        category = (session.query(Category)
                    .where(Category.title == post.category).first())
        location = (session.query(Location)
                    .where(Location.name == post.location).first())
        query = PostSchema(
            id=post.id,
            title=post.title,
            text=post.text,
            pub_date=post.pub_date,
            is_published=post.is_published,
            created_at=post.created_at,
            image=post.image,
            author=author,
            category=category,
            location=location
        )
        session.add(query)
        session.commit()
        session.refresh(query)
        return query
