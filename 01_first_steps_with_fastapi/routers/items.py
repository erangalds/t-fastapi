from fastapi import APIRouter, HTTPException
from typing import List, Dict

router = APIRouter(
    prefix="/items", # Optional: adds a prefix to all paths in this router
    tags=["items"],  # Optional: adds a tag for documentation
    responses={404: {"description": "Not found"}}, # Optional: common responses
)

# In-memory "database" for demonstration
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@router.get("/")
async def read_items():
    """
    Retrieve a list of items.
    """
    return fake_items_db

@router.get("/{item_id}")
async def read_item(item_id: int):
    """
    Retrieve a specific item by its ID.
    """
    if item_id < 0 or item_id >= len(fake_items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]

@router.post("/")
async def create_item(item: Dict[str, str]):
    """
    Create a new item.
    """
    fake_items_db.append(item)
    return item