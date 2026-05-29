from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.categories import CategoryRepository

from src.schemas.classes import Category as CategorySchema


class PostCategoryUseCase:
    def __init__(self):
        self._database = database
        self._repo = CategoryRepository()

    async def execute(self, new_category: CategorySchema) -> CategorySchema:
        with self._database.session() as session:
            category = self._repo.post(session=session, category=new_category)

        return CategorySchema.model_validate(obj=category)
