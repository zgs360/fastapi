TORTOISE_ORM = {
    "connections": {"default": "postgres://root:123456@localhost/testdb"},
    "apps": {
        "models": {
            "models": ["aerich.models", "app.routers.xinfa.models"],
            "default_connection": "default",
        },
    },
}
#
# TORTOISE_ORM = {
#     'connections': {
#         'default': {
#             'engine': 'tortoise.backends.asyncpg',  #PostgreSQL
#             # 'engine': 'tortoise.backends.mysql',  # MySQL or Mariadb
#             'credentials': {
#                 'host': '127.0.0.1',
#                 'port': '5432',
#                 'user': 'root',
#                 'password': '123456',
#                 'database': 'testdb',
#             }
#         },
#     },
#     'apps': {
#         'models': {
#             'models': ['models', "aerich.models"],
#             'default_connection': 'default',
#             'use_tz': False,    # 时区设置
#             'timezone': 'Asia/Shanghai'  # 时区设置
#
#         }
#     },
#
# }

#
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
#
# run_async(init())