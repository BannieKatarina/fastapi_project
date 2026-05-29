from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.posts import PostRepository
from src.schemas.classes import Post as PostSchema


class GetPostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self, id: int) -> PostSchema:
        with self._database.session() as session:
            post = self._repo.get(session=session, id=id)

        return PostSchema.model_validate(obj=post)
