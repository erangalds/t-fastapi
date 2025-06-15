# Request and Response Data Models for Bookstore API
# FastAPI integrates with Pydantic to create data models for request and response validation.
from pydantic import BaseModel, Field

# Define a Pydantic model for the Book
# Any data conforming to this model will have these attributes with the specified types.
class Book(BaseModel):
    isbn: str = Field(..., description="Unique identifier for the book", min_length=1,max_length=100)
    title: str = Field(..., description="Title of the book", min_length=1, max_length=200)
    author: str = Field(..., description="Author of the book", min_length=1, max_length=100)
    published_year: int = Field(..., description="Year the book was published", ge=1450, le=2100)


    
