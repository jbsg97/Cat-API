from pydantic import BaseModel

class CatResponse(BaseModel):
    _id: str
    __v: int
    text: str
    updatedAt: str
    deleted: bool
    source: str
    sentCount: int
