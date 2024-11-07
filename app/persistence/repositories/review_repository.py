from app.models.review import Review
from app.persistence.repository import SQLAlchemyRepository

class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)

    def get_review_by_place(self, place):
        return super().get_by_attribute("_place", place)
