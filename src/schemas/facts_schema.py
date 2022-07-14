from pydantic import BaseModel
from typing import Optional

class CatResponse(BaseModel):
    status: dict
    _id: str
    source: Optional[str] = None
    type: str
    deleted: bool
    user: str
    text: str
    createdAt: str
    updatedAt: str
    __v: int
    used: Optional[bool] = None
