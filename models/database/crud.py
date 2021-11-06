from sqlalchemy.orm import Session

from . import models, schemas


#user crud



#  crud city

# crud rubrics
def create_rubrica(db: Session, rubrica):
    if get_city_byID(db, city['uid']):
        return "Rubric is alredy added"
    db_rubrica = models.Rubric(name=rubrica['name'], slug=rubrica['slug'], uid=rubrica['uid'])
    db.add(db_rubrica)
    db.commit()
    db.refresh(db_rubrica)
    return db_rubrica

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


class CityCrud:
    def __init__(self, db:Session):
        self.db = db

    def get_city_byID(self, city_uid):
        return self.db.query(models.City).filter(models.City.uid == city_uid).first()
        
    def get_cities(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.City).offset(skip).limit(limit).all()

    def create_city(self, city):
        if self.get_city_byID(city['uid']):
            return "City is alredy added"
        db_city = models.City(name=city['name'], slug=city['slug'], uid=city['uid'])
        self.db.add(db_city)
        self.db.commit()
        self.db.refresh(db_city)
        return db_city

class RubricaCrud:
    def __init__(self, db:Session):
        self.db = db

    def get_rubrica_by_uid(self, rubrica_id: int):
        return self.db.query(models.Rubrica).filter(models.Rubrica.uid == rubrica_id).first()

    def get_rubrics(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Rubrica).offset(skip).limit(limit).all()

    def create_rubrica(self, rubrica):
        if self.get_rubrica_by_uid(self.db, rubrica['uid']):
            return "Rubric is alredy added"
        db_rubrica = models.Rubric(name=rubrica['name'], slug=rubrica['slug'], uid=rubrica['uid'])
        self.db.add(db_rubrica)
        self.db.commit()
        self.db.refresh(db_rubrica)
        return db_rubrica

class UserCrud:
    def __init__(self, db:Session):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def get_user_by_phone(self, phone: str):
        return self.db.query(models.User).filter(models.User.phone == phone).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.User).offset(skip).limit(limit).all()

    def create_user(self, user: schemas.UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    
    