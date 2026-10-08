import uvicorn
import os
from fastapi import FastAPI, File, UploadFile, status, Response

app = FastAPI()

# A function that checks if the file type uploaded is an image, returns a Boolean value
def image_check(file: UploadFile):
    return bool(file.content_type and file.content_type.startswith("image/"))

@app.get("/health", status_code=status.HTTP_200_OK)
async def health():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/submissions")
async def create_image(file: UploadFile, response: Response): 
    if image_check(file):
        return {"file": file.filename, "size": file.size}
    else:
        response.status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        return {"error": "Must upload an image"}

if __name__ == "__main__":
    host = os.getenv("API_HOST", "127.0.0.1")
    port = int(os.getenv("API_PORT", "8000"))
    uvicorn.run("main:app", host=host, port=port, reload=True)
