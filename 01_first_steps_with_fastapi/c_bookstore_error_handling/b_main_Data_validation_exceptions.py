import json 
from fastapi import Request, status, FastAPI 
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field  

# Define a Pydantic model for the request body
class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    published_year: int = Field(..., ge=1450, le=2026)  # Assuming books were published after 1450 and before or in 2023

# Create a FastAPI application instance
app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(
        json.dumps(
            {
                "message": "Validation error occurred",
                "detail": exc.errors(), 
                "body": exc.body
            },
            indent=4,
        ),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )

@app.post("/books/")
async def create_book(book: Book):
    """
    Create a new book with validation.
    This endpoint requires a JSON body with the book's title, author, and published year.
    """
    return {"message": "Book created successfully", "book": book}
