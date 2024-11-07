from app.models.place import Place
from app.persistence.repository import SQLAlchemyRepository

class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)

    def get_place_by_owner(self, owner_id):
        return super().get_by_attribute("_owner_id", owner_id)