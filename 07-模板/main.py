from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index")
def index(request: Request):
    name = "root"
    age = 32
    books = ["三国演义", "水浒传", "西游记", "红楼梦"]
    info = {"name": "rain", "age": 32, "gender": "male"}
    pai = 3.141592653589793

    return templates.TemplateResponse(
        "index.html",      # 模板文件
        {
            "request": request,
            "user": name,
            "age": age,
            "books": books,
            "info": info,
            "pai": pai
         },     # context上下文对象,一个字典
    )


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8090,
        reload=True
    )