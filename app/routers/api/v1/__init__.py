from fastapi import APIRouter
from app.routers.api.v1.books.router import router as api_v1_books_router

router = APIRouter()

router.include_router(api_v1_books_router, prefix="/books", tags=["Books"])