from repositories import PublicationRepository
from schemas import PublicationCreate
from fastapi import HTTPException
from typing import List

class PublicationService:
    def __init__(self, repository: PublicationRepository):
        self.repository = repository

    def create_publication(self, publication_data: PublicationCreate):
        return self.repository.create(publication_data)

    def create_many_publications(self, publications_data: List[PublicationCreate]):
        return self.repository.create_many(publications_data)
    
    def get_publication_by_id(self, publication_id: int):
        publication = self.repository.get_by_id(publication_id)
        if not publication:
            raise HTTPException(status_code=404, detail="Publication not found")
        return publication
    
    def get_publication_by_author(self, publication_author: str):
        publication = self.repository.get_by_author(publication_author)
        if not publication:
            raise HTTPException(status_code=404, detail="Publication not found")
        return publication

    def list_publications(self):
        return self.repository.get_all()

    def update_publication(self, publication_id: int, publication_data: PublicationCreate):
        publication = self.repository.update(publication_id, publication_data)
        if not publication:
            raise HTTPException(status_code=404, detail="Publication not found")
        return publication

    def delete_publication(self, publication_id: int):
        publication = self.repository.delete(publication_id)
        if not publication:
            raise HTTPException(status_code=404, detail="Publication not found")
        return {"message": "Publication deleted successfully"}