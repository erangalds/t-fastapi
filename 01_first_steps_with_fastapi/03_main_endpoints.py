from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
# Endpoints are the paths in a web application that respond to HTTP requests.
# Endpoints can be defined using decorators like @app.get(), @app.post(), etc.
# This code defines a FastAPI application with a single endpoint.
# The endpoint responds to GET requests at the root URL ("/") and read_root() function is called.
# That returns a JSON response with a greeting message.
# The use of 'async def' allows the endpoint to handle requests asynchronously, which can improve performance.