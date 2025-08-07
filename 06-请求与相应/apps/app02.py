from fastapi import APIRouter
from typing import Union, Optional

app02 = APIRouter()


@app02.get("/jobs")
async def get_jobs(kd, xl: Union[str,None], gj: Optional[str] = None):   #有默认参数的话代表着可以填可以不填
    # 在里面的是路径参数,不在里面的都算是查询参数
    # 基于kd, xl, gj数据库查询岗位信息
    return {
        "kd": kd,
        "xl": xl,
        "gj": gj
    }
