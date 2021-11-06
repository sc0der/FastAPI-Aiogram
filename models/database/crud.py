from sqlalchemy.orm import Session

from . import models, schemas


# user crud
class CityCrud:
    def __init__(self, db: Session):
        self.db = db

    def get_by_ID(self, city_uid):
        return self.db.query(models.City).filter(models.City.uid == city_uid).first()

    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.City).offset(skip).limit(limit).all()

    def create(self, city):
        if self.get_by_ID(city['uid']):
            return "City is alredy added"
        db_city = models.City(
            name=city['name'], slug=city['slug'], uid=city['uid'])
        self.db.add(db_city)
        self.db.commit()
        self.db.refresh(db_city)
        return db_city


class RubricaCrud:
    def __init__(self, db: Session):
        self.db = db

    def get_by_Id(self, rubrica_id: int):
        return self.db.query(models.Rubric).filter(models.Rubric.uid == rubrica_id).first()

    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Rubric).offset(skip).limit(limit).all()

    def create(self, rubrica):
        if self.get_by_Id(rubrica['uid']):
            return "Rubric is alredy added"
        db_rubrica = models.Rubric(
            name=rubrica['name'], slug=rubrica['slug'], uid=rubrica['uid'])
        self.db.add(db_rubrica)
        self.db.commit()
        self.db.refresh(db_rubrica)
        return db_rubrica


class UserCrud:
    def __init__(self, db: Session):
        self.db = db

    def get_by_Id(self, user_id: int):
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def get_by_phone(self, phone: str):
        return self.db.query(models.User).filter(models.User.phone == phone).first()

    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.User).offset(skip).limit(limit).all()

    def create(self, user):
        db_user = models.User(
            full_name=user['full_name'], uid=user['uid'], phone=user['phone'])
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user


class ItemCrud:
    def __init__(self, db: Session):
        self.db = db

    def get_by_Id(self, item_id: int):
        return self.db.query(models.Item).filter(models.Item.uid == item_id).first()

    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Item).offset(skip).limit(limit).all()

    def getImages(self, item_id):
        return self.db.query(models.ItemImage).filter(models.ItemImage.item_id == item_id)

    def create(self, item):
        if self.get_by_Id(item['uid']):
            return "item is alredy added"
        db_item = models.Item(
            name=item['name'], slug=item['slug'], uid=item['uid'])
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item