from pydantic import BaseModel
from typing import List

class PublicationBase(BaseModel):
    titulo: str
    autor: str
    isbn: str
    paginas: int
    ano: int

class PublicationCreate(PublicationBase):
    pass

class PublicationResponse(PublicationBase):
    
    class Config:
        from_attributes = True

class PublicationList(BaseModel):
    publications: List[PublicationCreate]
