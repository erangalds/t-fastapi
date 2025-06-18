from fastapi import FastAPI, HTTPException
import time 
import asyncio

# Create a FastAPI instance
app = FastAPI()

# Define an endpoint that simulates a synchronous operation
@app.get("/sync")
def sync_endpoint():
    # Simulate a synchronous operation
    time.sleep(5) # Simulating a blocking operation sleeping for 2 seconds
    
    return {"message": "This is a synchronous blocking endpoint."}

# Define an endpoint that simulates an asynchronous operation
@app.get("/async")
async def async_endpoint():
    # Simulate an asynchronous operation
    await asyncio.sleep(5)
    return {"message": "This is an asynchronous non-blocking endpoint."}