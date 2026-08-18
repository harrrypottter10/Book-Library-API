from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str
    author: str
    genre: str
    year: int = Field(gt=1000)
    in_stock: bool = True