from sqlalchemy import Column, Integer, String
from config.database import Base, engine

class Publication(Base):
    __tablename__ = "publications"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor = Column(String)
    isbn = Column(String)
    paginas = Column(Integer)
    ano = Column(Integer)

Base.metadata.create_all(bind=engine)