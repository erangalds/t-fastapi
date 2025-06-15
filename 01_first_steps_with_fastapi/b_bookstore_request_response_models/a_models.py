# Request and Response Data Models for Bookstore API
# FastAPI integrates with Pydantic to create data models for request and response validation.
from pydantic import BaseModel

# Define a Pydantic model for the Book
# Any data conforming to this model will have these attributes with the specified types.
class Book(BaseModel):
    isbn: str
    title: str
    author: str
    published_year: int


    
