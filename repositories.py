from sqlalchemy.orm import Session
from models import Publication
from schemas import PublicationCreate
from config.exceptions import PublicationNotFoundError, DuplicatePublicationError
from typing import List

class PublicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, publication_data: PublicationCreate) -> Publication:
        existing = self.db.query(Publication).filter(Publication.isbn == publication_data.isbn).first()
        if existing:
            raise DuplicatePublicationError()
        publication = Publication(**publication_data.dict())
        self.db.add(publication)
        self.db.commit()
        self.db.refresh(publication)
        return publication

    def create_many(self, publications_data: List[PublicationCreate]) -> List[Publication]:
        publications = []
        for pub_data in publications_data:
            if self.db.query(Publication).filter(Publication.isbn == pub_data.isbn).first():
                raise DuplicatePublicationError()
            publications.append(Publication(**pub_data.dict()))
        self.db.add_all(publications)
        self.db.commit()
        return publications

    def get_by_id(self, publication_id: int) -> Publication:
        publication = self.db.query(Publication).filter(Publication.id == publication_id).first()
        if not publication:
            raise PublicationNotFoundError()
        return publication

    def get_by_author(self, publication_author: str) -> List[Publication]:
        publication = self.db.query(Publication).filter(Publication.autor.like(f"%{publication_author}%")).all()
        if not publication:
            raise PublicationNotFoundError()
        return publication

    def get_all(self) -> List[Publication]:
        return self.db.query(Publication).all()

    def update(self, publication_id: int, publication_data: PublicationCreate) -> Publication:
        publication = self.get_by_id(publication_id)
        for key, value in publication_data.dict().items():
            setattr(publication, key, value)
        self.db.commit()
        return publication

    def delete(self, publication_id: int):
        publication = self.get_by_id(publication_id)
        self.db.delete(publication)
        self.db.commit()
        return publication