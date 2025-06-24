from fastapi import APIRouter, HTTPException
from typing import List, Dict

router = APIRouter(
    prefix="/users", # Optional: adds a prefix to all paths in this router
    tags=["users"],  # Optional: adds a tag for documentation
    responses={404: {"description": "User not found"}}, # Optional: common responses
)

# In-memory "database" for demonstration
fake_users_db = [{"username": "Alice"}, {"username": "Bob"}, {"username": "Charlie"}]

@router.get("/")
async def read_users():
    """
    Retrieve a list of users.
    """
    return fake_users_db

@router.get("/{user_id}") # /users/0
async def read_user(user_id: int):
    """
    Retrieve a specific user by their ID.
    """
    if user_id < 0 or user_id >= len(fake_users_db):
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users_db[user_id]

@router.post("/") # /users/
async def create_user(user: Dict[str, str]):
    """
    Create a new user.
    """
    fake_users_db.append(user)
    return user