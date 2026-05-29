from src.infrastructure.sqlite.database import database
from src.infrastructure.sqlite.repositories.locations import LocationRepository

from src.schemas.classes import Location as LocationSchema


class PostLocationUseCase:
    def __init__(self):
        self._database = database
        self._repo = LocationRepository()

    async def execute(self, new_location: LocationSchema) -> LocationSchema:
        with self._database.session() as session:
            location = self._repo.post(session=session, location=new_location)

        return LocationSchema.model_validate(obj=location)
