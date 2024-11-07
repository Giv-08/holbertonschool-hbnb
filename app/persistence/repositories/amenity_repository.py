from app.models.amenity import Amenity
from app.persistence.repository import SQLAlchemyRepository

class AmenityRepository(SQLAlchemyRepository):
    """Amenity repository class"""
    def __init__(self):
        super().__init__(Amenity)
    
    def get_amenity_by_name(self, name):
        return super().get_by_attribute("_name", name)
