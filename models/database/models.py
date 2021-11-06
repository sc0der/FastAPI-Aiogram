from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    uid: Column(Integer, unique=True)
    full_name: Column(String)
    phone: Column(String, unique=True, index=True)
    # items = relationship("Item", back_populates="owner")

class Rubric(Base):
    __tablename__ = "rubrics"
    id = Column(Integer, primary_key=True, index=True)
    uid= Column(Integer)
    name= Column(String)
    slug= Column(String, index=True)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    uid: Column(Integer, unique=True)
    title = Column(String, index=True)
    slug = Column(String, index=True)
    description = Column(String, index=True)
    rubric = Column(Integer, ForeignKey("rubrics.id"))
    # user = relationship("User", back_populates="items")

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