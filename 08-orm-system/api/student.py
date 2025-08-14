from fastapi import APIRouter

student_api = APIRouter()


@student_api.get('/')
def getAllStudent():
    return {
        "操作": "查看所有学生"
    }


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
