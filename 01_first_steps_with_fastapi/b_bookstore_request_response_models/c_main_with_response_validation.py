# Defining the Response Model for the Bookstore API
from pydantic import BaseModel
from typing import List, Any 

# Define a Pydantic model for the Book
class BookResponse(BaseModel):
    title: str
    author: str

from fastapi import FastAPI

app = FastAPI()

# Endpoint with GET method to retrieve a book details
@app.get("/all_books/")
def get_all_books() -> List[BookResponse]:
    """
    Get details of a book.
    This endpoint returns a BookResponse model.
    """
    # For demonstration purposes, we return a static book.
    # In a real application, this data would come from a database or other data source.
    return [
        {
            "isbn":"1",
            "title":"1984",
            "author":"George Orwell"
        },
        {
            "isbn":"2",
            "title":"To Kill a Mockingbird",
            "author":"Harper Lee"
        },
        {
            "isbn":"3",
            "title":"The Great Gatsby",
            "author":"F. Scott Fitzgerald"
        }
    ]

# Endpoint with GET method to retrieve a book details
@app.get("/all_books_v2/",response_model=List[BookResponse])
def get_all_books_v2() -> Any:
    """
    Get details of a book.
    This endpoint returns a BookResponse model.
    """
    # For demonstration purposes, we return a static book.
    # In a real application, this data would come from a database or other data source.
    return [
        {
            "isbn":"1_v2",
            "title":"1984_v2",
            "author":"George Orwell"
        },
        {
            "isbn":"2_v2",
            "title":"To Kill a Mockingbird_v2",
            "author":"Harper Lee"
        },
        {
            "isbn":"3_v2",
            "title":"The Great Gatsby_v2",
            "author":"F. Scott Fitzgerald"
        }
    ]