import shutil
import os 
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi import HTTPException
# UploadFile is used to handle file uploads 
# UploadFile is an asynchronous file upload handler and spools large files to disk to avoid memory issues

# Create a FastAPI application instance
app = FastAPI()
# Define the endpoint to upload a file
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)) -> dict:
    """
    Endpoint to upload a file.
    The file is saved to the server and a success message is returned.
    """
    # Save the uploaded file to the server
    with open(f"uploads/{file.filename}", "wb") as f:
        shutil.copyfileobj(file.file, f)
    # Close the file after saving
    return {"filename": file.filename, "message": "File uploaded successfully"}

## File Download Endpoint
@app.get("/downloadfile/{filename}", response_class=FileResponse)
async def download_file(filename: str):
    """
    Endpoint to download a file.
    The file is read from the server and returned to the client.
    """
    file_path = f"uploads/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    # FileResponse is used to send files as a response
    return FileResponse(file_path)

