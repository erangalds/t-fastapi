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

# Endpoint to get a list of books
# Define a GET endpoint to retrieve a list of books.
@app.get("/books/")
def get_books() -> List[Book]:
    """
    Get a list of books in the bookstore.
    This endpoint returns a list of Book models.
    """
    # For demonstration purposes, we return a static list of books.
    # In a real application, this data would come from a database or other data source.
    return [
        Book(isbn="1", title="1984", author="George Orwell", published_year=1949),
        Book(isbn="2", title="To Kill a Mockingbird", author="Harper Lee", published_year=1960),
        Book(isbn="3", title="The Great Gatsby", author="F. Scott Fitzgerald", published_year=1925),
    ]
