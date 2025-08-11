from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Union, List

app07 = APIRouter()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartends", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app07.post("/user02", response_model=UserOut)
def create_user(user: UserIn):
    # 不直接返回 按照UserOut模型去做序列化
    # 存到数据库(暂时没做)
    return user


@app07.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# response_model_exclude_unset=True 只保留设置字段的值   unset 没有设置  default 默认字段 none 不是none字段
# response_model_include={} 集合里面是个字段 要留什么在里面写
# response_model_exclude={} 想要排除什么就在里面写
async def read_item(item_id: str):
    return items[item_id]
