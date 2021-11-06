from sqlalchemy.orm import Session

from . import models, schemas


#user crud
class CityCrud:
    def __init__(self, db:Session):
        self.db = db

    def get_by_ID(self, city_uid):
        return self.db.query(models.City).filter(models.City.uid == city_uid).first()
        
    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.City).offset(skip).limit(limit).all()

    def create(self, city):
        if self.get_by_ID(city['uid']):
            return "City is alredy added"
        db_city = models.City(name=city['name'], slug=city['slug'], uid=city['uid'])
        self.db.add(db_city)
        self.db.commit()
        self.db.refresh(db_city)
        return db_city

class RubricaCrud:
    def __init__(self, db:Session):
        self.db = db

    def get_by_uid(self, rubrica_id: int):
        return self.db.query(models.Rubrica).filter(models.Rubrica.uid == rubrica_id).first()

    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Rubrica).offset(skip).limit(limit).all()

    def create(self, rubrica):
        if self.get_by_uid(self.db, rubrica['uid']):
            return "Rubric is alredy added"
        db_rubrica = models.Rubric(name=rubrica['name'], slug=rubrica['slug'], uid=rubrica['uid'])
        self.db.add(db_rubrica)
        self.db.commit()
        self.db.refresh(db_rubrica)
        return db_rubrica

class UserCrud:
    def __init__(self, db:Session):
        self.db = db

    def get_by_ID(self, user_id: int):
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def get_by_phone(self, phone: str):
        return self.db.query(models.User).filter(models.User.phone == phone).first()

    def get_list(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.User).offset(skip).limit(limit).all()

    def create(self, user: schemas.UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    
    