import random

from models import Student, Teacher, Clazz
# from tortoise import Tortoise, run_async
# async def init():
#     # 初始化
#     await Tortoise.init(
#         db_url='postgres://root:123456@localhost/testdb',
#         modules={'models':['models']}
#     )
#     # 异步生成模式
#     await Tortoise.generate_schemas()
#
# async def add_Teacher():
#     # 创建老师
#     # teacher = Teacher(tno=2009, pwd="123", name="张老师")
#     # return await teacher.save()
#     return await Teacher().create(tno=2009, pwd="123", name="张老师")
#
# async def add_Clazz():
#     # 创建班级
#     # clazz = Clazz(name="语文")
#     # return await clazz.save()
#     return await Clazz().create(name="语文")
#
#
#
async def add_Student():
    # 创建学生
    student = Student(name="张三", pwd="123", sno=2009, clazzs_id=1)
    await student.save()
    # 添加课程关系表
    await student.courses.add(1, 2)
    # return await student.save()
    return student



# run_async(init())
# run_async(add_Teacher())
# run_async(add_Clazz())
# run_async(add_Student())


# 删除数据
# from models import Student, Teacher, Clazz
# from tortoise import Tortoise, run_async
# async def init():
#     # 初始化
#     await Tortoise.init(
#         db_url='postgres://root:123456@localhost/testdb',
#         modules={'models':['models']}
#     )
#     # 异步生成模式
#     await Tortoise.generate_schemas()
#
# async def delete_Teacher(id):
#     # 删除老师
#     # await Teacher.filter(id=id).delete()
#     await Teacher.get(id=id).delete()
#
# run_async(init())
# run_async(delete_Teacher(2))

# 修改数据
# from models import Student, Teacher, Clazz
# from tortoise import Tortoise, run_async
# async def init():
#     # 初始化
#     await Tortoise.init(
#         db_url='postgres://root:123456@localhost/testdb',
#         modules={'models':['models']}
#     )
#     # 异步生成模式
#     await Tortoise.generate_schemas()
#
# async def update_Teacher(id, name):
#     # 修改老师
#     # await Teacher.filter(id=id).update(name=name)
#     await Teacher.get(id=id).update(name=name)
#
# run_async(init())
# run_async(update_Teacher(3, "大胜"))


# 批量增加数据
from models import Student, Teacher, Clazz, Course
from tortoise import Tortoise, run_async
async def init():
    # 初始化
    await Tortoise.init(
        db_url='postgres://root:123456@localhost/testdb',
        modules={'models':['models']}
    )
    # 异步生成模式
    await Tortoise.generate_schemas()
#
# # 批量新增
#
async def add_Teacher():
    await Teacher.bulk_create(
            [Teacher(name="老师"+str(i), pwd="123", tno=2009+i) for i in range(10)]
        )

async def add_Clazz():
    await Clazz.bulk_create(
            [Clazz(name="班级"+str(i)) for i in range(10)]
        )

async def add_course():
    await Course.bulk_create(
            [Course(name="课程"+str(i), teacher_id=i+1) for i in range(10)]
    )


async def add_Student():
    await Student.bulk_create(
            [Student(name="学生"+str(i), pwd="123", sno=2009+i, clazzs_id=i+1) for i in range(10)]
        )

# 添加学生数据的课程关系数据
async def add_Student_Course():
    courses = await Course.all().values("id")
    # 取出所有课程的id
    course_ids = [course["id"] for course in courses]
    # 给学生添加课程关系
    students = await Student.all()
    for student in students:
        # 随机取出两个课程
        chosen_course_ids = random.sample(course_ids, 2)
        print(chosen_course_ids)
        # 给学生添加课程关系
        choose_courses = await Course.filter(id__in=chosen_course_ids)
        await student.courses.add(*choose_courses)




run_async(init())
# run_async(add_Teacher())
# run_async(add_Clazz())
# run_async(add_course())
# run_async(add_Student())
# run_async(add_Student_Course())

#
# # 查询数据
from models import Student, Teacher, Clazz
from tortoise import Tortoise, run_async
async def init():
    # 初始化
    await Tortoise.init(
        db_url='postgres://root:123456@localhost/testdb',
        modules={'models':['models']}
    )
    # 异步生成模式
    await Tortoise.generate_schemas()

#
# 一对多查询
async def get_Students():
    # 查询学生
    # return await Student.filter(teacher__tno=tno).all()

    # students = await Student.all()
    # for student in students:
    #     print(student.name)
    #     print(await student.clazzs.values("name"))

    # students = await Student.all().values("name", "clazzs__name")
    # for student in students:
    #     print(student)

    # 　多对多查询
    # students = await Student.all()
    # for student in students:
    #     print(student.name)
    #     print(await student.courses.all().values("name"))


    #　综合查询
    students = await Student.all().values("name", "clazzs__name", "courses__name")
    for student in students:
        print(student)



#
run_async(init())
run_async(get_Students())