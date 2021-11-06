from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: Optional[str] = None
    phone: str