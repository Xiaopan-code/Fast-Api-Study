from fastapi import APIRouter, Request

app06 = APIRouter()


@app06.post("/items")
async def items(request: Request):
    print("URL", request.url)
    print("客户端IP地址", request.client.host)
    print("客户端宿主", request.headers.get("User-Agent"))
    print("cookies", request.cookies)
    return {
        "URL": str(request.url),        # request.url 未显式转字符串让 OpenAPI 规范生成逻辑 “卡住” 把 request.url 转成 str，让返回值类型更明确
        "客户端IP地址": request.client.host,
        "客户端宿主": request.headers.get("User-Agent"),
        "cookies": request.cookies,
    }

