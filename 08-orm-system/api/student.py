from fastapi import APIRouter
from models import *
from fastapi.templating import Jinja2Templates
from fastapi import Request

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



@student_api.post('/')
def addStudent():
    return {
        "操作": "添加一个学生"
    }


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
