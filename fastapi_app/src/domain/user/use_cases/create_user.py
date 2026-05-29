from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.users import UserRepository

from src.schemas.classes import User as UserSchema


class PostUserUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepository()

    async def execute(self, new_user: UserSchema) -> UserSchema:
        with self._database.session() as session:
            user = self._repo.post(session=session, user=new_user)

        return UserSchema.model_validate(obj=user)
