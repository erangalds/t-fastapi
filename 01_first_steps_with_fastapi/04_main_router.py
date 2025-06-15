import define_the_router as router 
from fastapi import FastAPI

app = FastAPI()
app.include_router(router.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
# This code creates a FastAPI application and includes a router defined in another module.
# The router contains additional endpoints, such as the one for reading an item by its ID. 
# You can run this uvicorn 01_first_steps_with_fastapi.04-main-router:app --reload command to start the application.