from app.persistence import db_session
from abc import ABC, abstractmethod
from repository import Repository

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db_session.add(obj)
        db_session.commit()

    def get(self, obj_id):
        return db_session.query(self.model).get(obj_id)

    def get_all(self):
        return db_session.query(self.model).all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db_session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db_session.delete(obj)
            db_session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        return db_session.query(self.model).where(getattr(self.model, attr_name) == attr_value).first()