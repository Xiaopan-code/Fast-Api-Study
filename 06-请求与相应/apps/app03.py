from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List, Union, Optional

app03 = APIRouter()


class Addr(BaseModel):
    province: str
    city: str


class User(BaseModel):
    # name: str = Field(pattern="^a")         # pydantic v2 中用pattern 替换了 regex的正则表达
    name: str
    age: int = Field(default=0, gt=0, lt=100)  # 传入默认值为0,传入值大于0小于100
    birthday: Union[date, None] = None
    friends: List[int] = []  # 传入的为 [1,2,3]  不能是["hello"]
    description: Optional[str] = None
    addr: Addr  # 组合嵌套

    @field_validator("name")  # validator 被 field_validator 替换了
    def name_must_alpha(cls, value):  # cls 当前类本身, value 拿的是当前字段的value值-> 'name'
        assert value.isalpha(), "name must be alpha"  # "name must be alpha" 断言信息
        return value


class Date(BaseModel):
    date: List[User]


@app03.post("/user")
async def create_user(user: User):
    print(user, type(user))
    print(user.name, user.age, user.birthday, user.friends)
    print(user.model_dump())  # user.dict() 在后面版本换成了user.model_dump()
    return user


@app03.post("/data")  # 嵌套user使用 调用了 user 的模型方法
async def receive_data(data: Date):
    return data
