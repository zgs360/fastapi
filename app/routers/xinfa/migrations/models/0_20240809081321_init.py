from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "clazz" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(32) NOT NULL
);
COMMENT ON COLUMN "clazz"."name" IS '班级名称';
CREATE TABLE IF NOT EXISTS "student" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "sno" INT NOT NULL,
    "pwd" VARCHAR(32) NOT NULL,
    "name" VARCHAR(32) NOT NULL,
    "clazzs_id" INT NOT NULL REFERENCES "clazz" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "student"."sno" IS '学生编号';
COMMENT ON COLUMN "student"."pwd" IS '学生密码';
COMMENT ON COLUMN "student"."name" IS '学生名称';
COMMENT ON COLUMN "student"."clazzs_id" IS '所属班级';
CREATE TABLE IF NOT EXISTS "teacher" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "tno" INT NOT NULL,
    "pwd" VARCHAR(32) NOT NULL,
    "name" VARCHAR(32) NOT NULL
);
COMMENT ON COLUMN "teacher"."tno" IS '教师编号';
COMMENT ON COLUMN "teacher"."pwd" IS '教师密码';
COMMENT ON COLUMN "teacher"."name" IS '教师名称';
CREATE TABLE IF NOT EXISTS "course" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(32) NOT NULL,
    "teacher_id" INT NOT NULL REFERENCES "teacher" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "course"."name" IS '课程名称';
CREATE TABLE IF NOT EXISTS "student_course" (
    "student_id" INT NOT NULL REFERENCES "student" ("id") ON DELETE CASCADE,
    "course_id" INT NOT NULL REFERENCES "course" ("id") ON DELETE CASCADE
);
CREATE UNIQUE INDEX IF NOT EXISTS "uidx_student_cou_student_0d222b" ON "student_course" ("student_id", "course_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
