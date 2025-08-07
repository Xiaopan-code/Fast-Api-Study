from fastapi import APIRouter, Form
from pydantic import BaseModel, Field ,field_validator
from datetime import date
from typing import List, Union, Optional

app04 = APIRouter()


@app04.post("/regin")
async def reg(username: str = Form(), password: str = Form()):     # str 后面不带 Form() 就是个查询对象 带了就是说明他是Form下面的一个变量
    print(f"username: {username}, password: {password}")
    return {
        "username": username,
        "password": password
    }
