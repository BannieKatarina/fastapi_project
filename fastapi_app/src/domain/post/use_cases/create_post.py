from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.posts import PostRepository
from src.schemas.classes import Post as PostSchema


class CreatePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self, new_post: PostSchema) -> PostSchema:
        with self._database.session() as session:
            post = self._repo.post(session=session, post=new_post)

        return PostSchema.model_validate(obj=post)
