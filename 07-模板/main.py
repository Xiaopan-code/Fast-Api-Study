from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index")
def index(request: Request):
    name = "root"
    age = 16
    books = [{"title": "三国演义", "price": 100},
             {"title": "水浒传", "price": 120},
             {"title": "红楼梦", "price": 140},
             {"title": "西游记", "price": 160}]
    info = {"name": "rain", "age": 32, "gender": "male"}
    pai = 3.141592653589793

    movies = {"adult_movies": ["日韩", "欧美", "国产"], "young_movies": ["黑猫警长", "熊出没", "大头儿子和小头爸爸"]}

    return templates.TemplateResponse(
        "index.html",      # 模板文件
        {
            "request": request,
            "user": name,
            "age": age,
            "books": books,
            "info": info,
            "pai": pai,
            "movies": movies
         },     # context上下文对象,一个字典
    )


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8090,
        reload=True
    )