from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# When handling multiple endpoints that are defined in different modules, we can better organize our code by using routers.
# Routers allow us to group related endpoints together, making the code more modular and easier to maintain.
# In this example, we define a router with a single endpoint that reads an item by its ID.




