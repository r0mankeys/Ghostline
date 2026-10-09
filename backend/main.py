import uvicorn
import os
from fastapi import FastAPI, File, UploadFile, status, Response
from fastapi.middleware.cors import CORSMiddleware

API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = os.getenv("API_PORT", "8000")
WEB_URL = os.getenv("WEB_URL")

# Fail at startup, not with a confusing CORS error later.
if not WEB_URL:
    raise RuntimeError(
        "WEB_URL is not set. Add it to the root .env "
        "(e.g. WEB_URL=http://localhost:3001) and restart the server."
    )

app = FastAPI()

origins = [WEB_URL]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

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
    uvicorn.run("main:app", host=API_HOST, port=int(API_PORT), reload=True)
