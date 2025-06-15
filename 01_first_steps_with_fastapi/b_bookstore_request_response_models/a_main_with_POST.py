from fastapi import FastAPI
from a_models import Book
from typing import List

app = FastAPI()

# Endpoint to add a new book to the bookstore
# This endpoint accepts a Book model and returns the same model.
# The data will come as JSON in the request body.
# FastAPI will automatically validate the data against the Book model.
# If invalid data is provided, FastAPI will return a 422 Unprocessable Entity error.
@app.post("/books/")
def add_book(book: Book) -> Book:
    """
    Add a new book to the bookstore.
    This endpoint accepts a Book model and returns the same model.
    """
    return book
