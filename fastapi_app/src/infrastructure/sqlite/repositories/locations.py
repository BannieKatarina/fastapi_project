from typing import Type

from sqlalchemy.orm import Session

from src.infrastructure.sqlite.models.location import Location
from src.schemas.classes import Location as LocationSchema


class LocationRepository:
    def __init__(self):
        self._model: Type[Location] = Location

    def post(self, session: Session, location: LocationSchema) -> Location:
        db_location = Location(**location.dict())
        session.add(db_location)
        session.commit()
        session.refresh(db_location)
        return db_location
