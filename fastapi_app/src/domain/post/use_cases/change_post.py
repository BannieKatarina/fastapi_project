from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.posts import PostRepository
from src.schemas.classes import Post as PostSchema


class ChangePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self, id: int, new_post: PostSchema) -> PostSchema:
        with self._database.session() as session:
            post = self._repo.put(session=session, id=id,
                                  updated_post_data=new_post)

        return PostSchema.model_validate(obj=post)
