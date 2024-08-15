from fastapi import APIRouter, status, HTTPException
from .models import Student, Clazz, Teacher, Course
from schema.student import S_StudentInput, S_Student, S_Clazzs, S_Teacher
# 设置唯一可以访问的路由
__all__ = ("xinfa_router",)

xinfa_router = APIRouter(
    prefix="/xinfa",
    tags=["刑法库"] # 添加标签
)



@xinfa_router.get(
    path='/{id}',
)
async def getBySno(id: int):
    # 查询学生
    # return await Student
    print(id)
    # response = await Student.filter(sno=sno).first()
    response = await Student.get(id=id)
    print(response)
    return response


@xinfa_router.get("/",
                  # response_model=S_Student,
                  status_code=status.HTTP_201_CREATED, # 设置状态码
                  )
async def getAll():
    # 查询所有学生
    response = await Student.all().values("name", "clazzs__name","courses__name")
    reslut = []
    for student in response:
        print('学生：',student)
    print("打印：",response)
    return response

@xinfa_router.put("/{id}")
async def update(id: int, studentIn: S_StudentInput):
    data = studentIn.dict()
    # 先将课程id除掉，再更新学生信息(因为课程是多对多的关系，需要单独更新)
    course_ids = data.pop("courses")
    # 更新学生信息
    selected_student = await Student.filter(id=id).update(**data)
    # 更新学生课程关系
    student = await Student.get(id=id)
    choose_courses = await Course.filter(id__in=course_ids)
    await student.courses.clear()
    await student.courses.add(*choose_courses)

    return await Student.get(id=id).values("name", "clazzs__name","courses__name")


@xinfa_router.post("/")
async def create(student: S_StudentInput):
    # 处理数据
    # 先将课程id除掉，再创建学生信息(因为课程是多对多的关系，需要单独创建)
    course_ids = student.courses
    # 创建学生信息
    new_student = await Student.create(sno=student.sno, name=student.name, pwd=student.pwd, clazzs_id=student.clazzs)
    print("创建学生：", new_student)
    # 创建学生课程关系
    choose_courses = await Course.filter(id__in=course_ids)
    await new_student.courses.add(*choose_courses)
    return await Student.filter(id=new_student.id).values("name", "clazzs__name", "courses__name")


# 删除学生
@xinfa_router.delete("/{id}")
async def delete(id: int):
    # student = await Student.get(id=id) # 查询一个学生
    # await student.delete() # 删除学生

    counts = await Student.filter(id=id).delete() # 查询符合条件的学生删除
    if counts == 0:
        raise HTTPException(status_code=404, detail="学生不存在")
    return {"message": "删除成功"}