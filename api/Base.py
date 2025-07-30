# -*- coding:utf-8 -*-
"""
@Created on : 2025/7/28/15:48
@Author: 比奇堡海绵宝宝 原作者:binkuolo
@Des: 基本路由
"""
from fastapi import APIRouter, Request
router = APIRouter()


@router.get('/')
async def home(num: int):

    return num