from sqlalchemy.orm import Session

from . import models, schemas


#user crud

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_phone(db: Session, phone: str):
    return db.query(models.User).filter(models.User.phone == phone).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#  crud city
def get_city_byID(db:Session, city_uid):
    return db.query(models.City).filter(models.City.uid == city_uid).first()

def get_rubrica_byID(db:Session, rubric_uid):
    return db.query(models.Rubric).filter(models.Rubric.uid == rubric_uid).first()


def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.City).offset(skip).limit(limit).all()

def create_city(db: Session, city):
    if get_city_byID(db, city['uid']):
        return "User is alredy added"
    db_city = models.City(name=city['name'], slug=city['slug'], uid=city['uid'])
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

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