import uvicorn
import os
from typing import Annotated
from fastapi import FastAPI, File, UploadFile, status
from pydantic import BaseModel

app = FastAPI()

@app.get("/health", status_code=status.HTTP_200_OK)
async def health():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/submissions")
async def create_image(file: UploadFile): 
    return { "file": file.filename, "size": file.size }

if __name__ == "__main__":
    host = os.getenv("API_HOST", "127.0.0.1")
    port = int(os.getenv("API_PORT", "8000"))
    uvicorn.run("main:app", host=host, port=port, reload=True)
