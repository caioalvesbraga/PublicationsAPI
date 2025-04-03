from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import SessionLocal
from services import PublicationService
from repositories import PublicationRepository
from schemas import PublicationCreate, PublicationResponse, PublicationList
from typing import List
from config.database import get_db

router = APIRouter()

@router.post("/publications/", response_model=PublicationResponse)
def create_publication(publication: PublicationCreate, db: Session = Depends(get_db)):
    service = PublicationService(PublicationRepository(db))
    return service.create_publication(publication)

@router.post("/publications/multiple/", response_model=List[PublicationResponse])
def create_many_publications(publications: PublicationList, db: Session = Depends(get_db)):
    service = PublicationService(PublicationRepository(db))
    return service.create_many_publications(publications.publications)

@router.get("/publications/", response_model=List[PublicationResponse])
def read_publications(db: Session = Depends(get_db)):
    service = PublicationService(PublicationRepository(db))
    return service.list_publications()

@router.get("/publications/{publication_id}", response_model=PublicationResponse)
def read_publication(publication_id: int, db: Session = Depends(get_db)):
    service = PublicationService(PublicationRepository(db))
    return service.get_publication_by_id(publication_id)

@router.get("/publications/author/", response_model=List[PublicationResponse])
def read_publication_by_author(publication_author: str , db: Session = Depends(get_db)):
    service = PublicationService(PublicationRepository(db))
    return service.get_publication_by_author(publication_author)

@router.put("/publications/{publication_id}", response_model=PublicationResponse)
def update_publication(publication_id: int, publication: PublicationCreate, db: Session = Depends(get_db)):
    service = PublicationService(PublicationRepository(db))
    return service.update_publication(publication_id, publication)

@router.delete("/publications/{publication_id}")
def delete_publication(publication_id: int, db: Session = Depends(get_db)):
    service = PublicationService(PublicationRepository(db))
    return service.delete_publication(publication_id)
