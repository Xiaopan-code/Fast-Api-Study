import uvicorn
import time
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import Response

app = FastAPI()


# 中间件谁在第一个谁就写在最下面
@app.middleware("http")
async def m2(request: Request, call_next):
    # 请求代码块
    print("m2 request")
    response = await call_next(request)
    # 响应代码块
    response.headers["author"] = "pan"
    print("m2 response")
    return response


@app.middleware("http")
async def m1(request: Request, call_next):
    # 请求代码块
    print("m1 request")
    # 黑名单
    # if request.client.host in ["localhost", "127.0.0.1"]:
    #     return Response(content="visit forbidden")

    # docs能进去 但是让你调试不了
    # if request.url.path in ["/user"]:
    #     return Response(content="visit forbidden")

    start = time.time()

    response = await call_next(request)
    # 响应代码块
    print("m1 response")

    end = time.time()

    response.headers["ProcessTimer"] = str(end - start)
    return response


@app.get("/user")
def get_user():
    time.sleep(3)
    print("get_user函数执行")
    return {
        "user": "current user"
    }


@app.get("/item/{item_id}")
def get_item(item_id: int):
    time.sleep(2)
    print("get_item函数执行")
    return {
        "item_id": item_id
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8030,
                reload=True, workers=1)
