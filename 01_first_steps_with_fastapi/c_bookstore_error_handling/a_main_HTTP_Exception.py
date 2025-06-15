from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    """
    Custom exception handler for HTTP exceptions.
    Returns a JSON response with the error details.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message":"Oops! Something went wrong.", 
            "detail": exc.detail
        }
    )
# Now whenever an HTTPException is raised, it will be handled by this custom handler.
@app.get("/error")
async def trigger_error():
    """
    Endpoint to trigger an HTTPException.
    This is just for demonstration purposes.
    """
    raise HTTPException(status_code=404,)