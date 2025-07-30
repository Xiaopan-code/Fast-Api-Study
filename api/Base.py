# -*- coding:utf-8 -*-
"""
@Des: 基本路由
"""
from fastapi import APIRouter

from api.login import index, login

ApiRouter = APIRouter(prefix="/v1", tags=["api路由"])

@ApiRouter.get('/input')
async def home(num: int):
    return {"num": num, "data": [{"num": num, "data": []}, {"num": num, "data": []}]}

ApiRouter.get("/index",tags=["api路由"],summary="注册接口")(index)
ApiRouter.post("/login",tags=["api路由"],summary="登录接口")(login)