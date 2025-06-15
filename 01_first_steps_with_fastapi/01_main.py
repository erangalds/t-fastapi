from fastapi import FastAPI
# Importing FastAPI to create an application instance
app = FastAPI()

# Defining a route. 
# Route is a URL path that the application will respond to.
@app.get("/")  # This decorator defines the path for the route
def read_root():
    # This function will be called when the root URL is accessed
    return {"Hello": "World"}
# The function returns a JSON response with a greeting message
# The application will run on the default port 8000
# To run the application, use the command: uvicorn 01-main:app --reload
# The --reload option enables automatic reloading of the server when code changes are made
# To test the application, open a web browser and go to http://localhost:8000/
# You can also access the OpenAPI documentation at http://localhost:8000/docs

