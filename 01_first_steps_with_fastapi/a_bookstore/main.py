from fastapi import FastAPI

app = FastAPI()
@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id, 
        "title": "Sample Book Title", 
        "author": "Sample Author"
    }

# {book_id} is a path parameter
# path parameters are used to capture values from the URL path 

# Adding another endpoint
@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    return {
        "author_id": author_id, 
        "name": "Sample Author"
    }

# Using Query Parameters
@app.get("/books/")
async def read_books(year: int = None):
    if year:
        return {
            "message": f"Books published in {year}",
            "books": [
                {"title": "Book 1", "year": year},
                {"title": "Book 2", "year": year}
            ]
        }
    return {
        "message": "All books",
        "books": [
            {"title": "Book 1"},
            {"title": "Book 2"},
            {"title": "Book 3"},
            {"title": "Book 4"},
            {"title": "Book 5"}
        ]
    }