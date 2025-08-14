import uvicorn
from fastapi import FastAPI


app = FastAPI()

# tags 设置标签用的
# description 详情描述
# response_description 响应描述
# deprecated 标识是否废弃(状态)


@app.post("/items",tags=["这是一个items的测试接口"],
        summary="this is items测试 summary",
        description="this is items测试 description",
        response_description="this is items测试 response_description",
        deprecated=True
    )
def test():
    return {"items": "items数据"}


if __name__ == "__main__":
    uvicorn.run("04-路径操作装饰方法的参数:app", port=8080, reload=True)