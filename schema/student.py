from typing import List

from pydantic import BaseModel, Field
from datetime import datetime

class S_Clazzs(BaseModel):
    name: str

class S_Teacher(BaseModel):
    tno: int
    pwd: str
    name: str

class S_course(BaseModel):
    cno: int
    name: str
    teacher_id: int
class S_Student(BaseModel):
    id: int
    sno: int
    pwd: str
    name: str
    # test_models.Clazz 与　配置文件中定义的　test_models.Clazz　一致
    clazzs: S_Clazzs
    course: S_course

class S_StudentInput(BaseModel):
    sno: int
    pwd: str
    name: str
    clazzs: int
    courses: List[int] = []