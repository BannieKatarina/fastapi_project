from typing import Type

from sqlalchemy.orm import Session

from src.infrastructure.sqlite.models.category import Category
from src.schemas.classes import Category as CategorySchema


class CategoryRepository:
    def __init__(self):
        self._model: Type[Category] = Category

    def post(self, session: Session, category: CategorySchema) -> Category:
        db_category = Category(**category.dict())
        session.add(db_category)
        session.commit()
        session.refresh(db_category)
        return db_category
