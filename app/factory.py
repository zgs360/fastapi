from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routers import routers
from app.config.config import config
# from app.config.config import TORTOISE_ORM
from .routers import TORTOISE_ORM


__all__ = ["create_app",]

def create_app() ->FastAPI:

    # 定义一个程序启动前的事件
    async def app_startup(application:FastAPI) -> None:
        print("Application started")
    

    # 定义一个程序关闭的事件
    async def app_shutdown(application:FastAPI) -> None:
        print("Application shutdown")
        
    # 注册事件，使用lifespan参数
    @asynccontextmanager
    async def lifespan(application:FastAPI) -> AsyncGenerator:
        await app_startup(application)
        yield
        await app_shutdown(application)

    app:FastAPI = FastAPI(
        title=config.app.title,
        description=config.app.description,
        version=config.app.version,
        lifespan=lifespan,
    )
    # 注册数据库
    register_tortoise(
        app=app,
        config=TORTOISE_ORM,
    )
    # 注册路由
    for router in  routers:
        app.include_router(router)


    return app