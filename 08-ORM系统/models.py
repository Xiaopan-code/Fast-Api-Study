from tortoise.models import Model
from tortoise import fields


class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    sno = fields.IntField(description="学号")

    # 一对多的关系
    clas = fields.ForeignKeyField("models.Clas", related_name="student", on_delete=fields.CASCADE)

    # 多对多的关系
    courses = fields.ManyToManyField("models.Course", related_name="student", through="models.StudentField")


class Clas(Model):
    name = fields.CharField(max_length=32, description="班级名称")


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="课程名称")
    teacher = fields.ForeignKeyField("models.Teacher", related_name="course", on_delete=fields.CASCADE)


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    tno = fields.IntField(description="老师编号")
