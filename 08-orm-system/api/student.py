from fastapi import APIRouter
from models import *
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel, field_validator
from typing import List

student_api = APIRouter()


@student_api.get('/')
async def getAllStudent():
    # 查询所以 all方法
    studnets = await Student.all()  # Queryset: [Student(), Student(), Student()]
    # print("students", studnets)
    #
    # for stu in studnets:
    #     print(stu.name, stu.sno)
    #
    # print(studnets[0].name)
    #
    # # 过滤查询 filter
    # students = await Student.filter(name="rain")
    # students = await Student.filter(clas_id=14)
    # print("students", students)
    #
    # # get返回模型类对象
    # stu = await Student.get(id=6)
    # print(stu.name)
    #
    # # 模糊查询 --非完全查询
    # stus = await Student.filter(sno__gt=2001)            # 只查找2001
    # stus = await Student.filter(sno__range=[1, 10000])   # 在1和10000这两个数字里面取
    # stus = await Student.filter(sno__in=[2001, 2002])    # 在2001-2002这两个范围里面取
    # print(stus)

    # values查询
    stus = await Student.all().values("name","sno")         # 对字典进行序列化
    # stus = await Student.filter(sno__range=[1, 10000])    # 对对象进行序列化
    # print(stus)

    return {
        "查询所有学生": stus
    }


@student_api.get('/index.html')
async def getAllStudent(request: Request):
    templates = Jinja2Templates(directory='templates')
    students = await Student.all()

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "students": students
        }
    )


class StudentIn(BaseModel):
    name: str
    pwd: str
    sno: int
    clas_id: int
    courses: List[int] = []

    @field_validator('name')
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'name must be alpha'
        return value

    @field_validator('sno')
    def sno_validator(cls, value):
        assert 1000 < value < 10000, '学号要在1000-10000的范围内'
        return value


@student_api.post('/')
async def addStudent(student_in: StudentIn):

    # 插入到数据库
    # 方式1
    # student = Student(name=student_in.name, pwd=student_in.pwd, sno=student_in.sno, clas_id=student_in.clas_id)
    # await student.save()  # 插入到数据库student表

    # 方式2
    student = await Student.create(name=student_in.name, pwd=student_in.pwd,
                                   sno=student_in.sno, clas_id=student_in.clas_id)

    # 多对多的关系绑定
    choose_courses = await Course.filter(id__in=student_in.courses)
    await student.courses.add(*choose_courses)

    return student


@student_api.get('/{student_id}')
def getOneStudent(student_id: int):

    return {
        "操作": f"查看id={student_id}一个学生"
    }


@student_api.put('/{student_id}')
def updateStudent(student_id: int):
    return {
        "操作": f"更新id={student_id}一个学生"
    }


@student_api.delete('/{student_id}')
def deleteStudents(student_id: int):
    return {
        "操作": f"删除id={student_id}一个学生"
    }
