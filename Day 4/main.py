from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#create fast api app
app = FastAPI()

#Data Model
class Book(BaseModel):
    id: int
    title: str
    author: str

# Fake DB
books: List[Book] = [
    Book(id=1, title='Mayurs new book on Fast Cars', author='Mayur'),
    Book(id=2, title='Mayurs 2nd new book on Fast Cars', author='Mayur')

]

# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Mayur's Library API"}

# Getting all books - Endpoint
@app.get("/books", response_model=List[Book])
def get_books():
    return books

# Get the book from ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id:int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error":"Book not found"}


