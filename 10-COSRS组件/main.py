import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 导入内置的CORS中间件

app = FastAPI()

# 允许的源列表
origins = [
    "http://localhost:63342",  # 你的前端地址
    "http://127.0.0.1:63342",
]

# 添加内置的CORS中间件（必须在路由前配置）
app.add_middleware(
    CORSMiddleware,  # 使用FastAPI内置的CORS中间件
    allow_origins=origins,  # 允许指定源
    allow_credentials=True,
    allow_methods=["*"],    # 允许所有HTTP方法
    allow_headers=["*"],    # 允许所有请求头
)


@app.get("/user")
def get_user():
    return {
        "user": "current user"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8030,
                reload=True, workers=1)
