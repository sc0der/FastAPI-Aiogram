from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, unique=True)
    name = Column(String, index=True)
    phone = Column(String, unique=True, index=True)


class Rubric(Base):
    __tablename__ = "rubrics"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer)
    name = Column(String)
    slug = Column(String, index=True)


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, unique=True)
    title = Column(String, index=True)
    slug = Column(String, index=True)
    description = Column(String, index=True)
    price_description = Column(String)
    price = Column(String, index=True)
    created_dt = Column(String, index=True)
    raise_dt = Column(String, index=True)
    city_id = Column(String, index=True)
    status = Column(Boolean, index=True)
    record_dt = Column(DateTime, index=True)
    user_name = Column(String)
    user_phone = Column(String)
    templated_title = Column(String)
    rubric_id = Column(Integer)
    user_id = Column(Integer)

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, unique=True)
    name = Column(String)
    slug = Column(String)


class ItemImage(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, unique=True)
    item_id = Column(Integer)
    url = Column(String)
    orig = Column(String)
