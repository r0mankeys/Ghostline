import uvicorn
import os
from fastapi import FastAPI, status

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health", status_code=status.HTTP_200_OK)
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    host = os.getenv("API_HOST", "127.0.0.1")
    port = int(os.getenv("API_PORT", "8000"))
    uvicorn.run("main:app", host=host, port=port, reload=True)
