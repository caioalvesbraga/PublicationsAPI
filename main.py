from fastapi import FastAPI
from routers import publication_router

app = FastAPI()
app.include_router(publication_router.router)
