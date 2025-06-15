from fastapi import FastAPI
 # Import the routers from our separate files
from routers import items, users

app = FastAPI()

# Include the routers in the main application
# The paths defined in routers/items.py will be prefixed with /items
app.include_router(items.router)
# The paths defined in routers/users.py will be prefixed with /users
app.include_router(users.router)

@app.get("/")
async def read_root():
    """
    Root endpoint of the application.
    """
    return {"message": "Welcome to the multi-router FastAPI app!"}

# To run this application, use the command:
# uvicorn 01_first_steps_with_fastapi.05_main_multiple_routers:app --reload
#
# You can then access:
# - http://localhost:8000/
# - http://localhost:8000/items/
# - http://localhost:8000/items/0
# - http://localhost:8000/users/
# - http://localhost:8000/users/1
# - http://localhost:8000/docs (for interactive documentation)