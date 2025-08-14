from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8090,
        reload=True
    )