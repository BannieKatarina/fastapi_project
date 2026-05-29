from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.posts import PostRepository

from src.schemas.classes import Post as PostSchema


class GetPostsUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self) -> list[PostSchema]:
        with self._database.session() as session:
            posts = self._repo.get_all(session=session)

        return posts
