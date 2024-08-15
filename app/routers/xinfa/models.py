
from tortoise.models import Model
from tortoise import fields



class Clazz(Model):
    name = fields.CharField(max_length=32, description="班级名称")

class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="课程名称")
    teacher = fields.ForeignKeyField("models.Teacher")


class Teacher(Model):
    id = fields.IntField(pk=True)
    tno = fields.IntField(description="教师编号")
    pwd = fields.CharField(max_length=32, description="教师密码")
    name = fields.CharField(max_length=32, description="教师名称")


class Student(Model):
    id = fields.IntField(pk=True)
    sno = fields.IntField(description="学生编号")
    pwd = fields.CharField(max_length=32, description="学生密码")
    name = fields.CharField(max_length=32, description="学生名称")
    # 一对多的关系
    clazzs = fields.ForeignKeyField('models.Clazz', related_name='students', description="所属班级")
    # 多对多的关系
    courses = fields.ManyToManyField("models.Course", related_name="students")