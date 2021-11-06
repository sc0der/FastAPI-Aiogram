from pydantic import BaseModel
from typing import Optional
from .Users import User
from .database.database import *

class ItemImage(BaseModel):
    id: int
    url: str
    orig: str


class Item(BaseModel):
    id: int
    title: str
    city: int
    images: list[ItemImage]
    description: str
    rubric: int
    user: User
