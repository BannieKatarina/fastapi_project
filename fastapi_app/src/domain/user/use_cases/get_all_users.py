from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.users import UserRepository

from src.schemas.classes import User as UserSchema


class GetUsersUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepository()

    async def execute(self) -> list[UserSchema]:
        with self._database.session() as session:
            users = self._repo.get_all(session=session)

        return [UserSchema.model_validate(user) for user in users]
