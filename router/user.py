from fastapi import APIRouter, HTTPException
from models.books import Book
from models.db import conn
from schemas.user import serializeDict, serializelist
from bson import ObjectId
from bson.errors import InvalidId

book = APIRouter()


@book.post("/")
def create_book(book: Book):
    result = conn.local.books.insert_one(book.model_dump())
    return {
        "message": "Successfully Created",
        "id": str(result.inserted_id)
    }

@book.get("/{id}")
def get_book(id: str):
    try:
        book = conn.local.books.find_one({"_id": ObjectId(id)})

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        return serializeDict(book)

    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid ID"
        )



@book.get("/")
def get_books():
    books = conn.local.books.find()
    return serializelist(books)


@book.put("/{id}")
def update_book(id: str, book: Book):
    try:
        conn.local.books.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": book.model_dump()}
        )
        return "Successfully Updated"
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid ID"
        )


@book.delete("/{id}")
def delete_book(id: str):
    try:
        conn.local.books.find_one_and_delete(
            {"_id": ObjectId(id)}
        )
        return "Successfully Deleted"
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid ID"
        )