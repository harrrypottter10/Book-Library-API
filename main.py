from fastapi import FastAPI
from router.user import book
app = FastAPI()
app.include_router(book)