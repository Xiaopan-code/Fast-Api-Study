import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM

app = FastAPI()

# fastapi一旦运行 register_tortoise就已经执行了 实现监控
register_tortoise(
    app=app,
    config=TORTOISE_ORM
)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8090,
        reload=True
    )
