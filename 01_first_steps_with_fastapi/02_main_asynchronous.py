from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}
# The main difference is the use of 'async def' for the endpoint handler.
# This allows the function to be asynchronous, which can improve performance
# when handling multiple requests concurrently.