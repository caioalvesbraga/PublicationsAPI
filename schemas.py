from pydantic import BaseModel, validator
from typing import List

class PublicationBase(BaseModel):
    titulo: str
    autor: str
    isbn: int
    paginas: int
    ano: int

    @validator('isbn', pre=True)
    def parse_to_int(cls, value):
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Cannot convert {value} to an integer")

class PublicationCreate(PublicationBase):
    pass

class PublicationResponse(PublicationBase):
    
    class Config:
        from_attributes = True

class PublicationList(BaseModel):
    publications: List[PublicationCreate]