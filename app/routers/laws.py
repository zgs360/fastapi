from http.client import HTTPException

from fastapi import APIRouter, status, Body

from .lawmodels import LawModel

# 设置唯一可以访问的路由
__all__ = ("router",)

router = APIRouter(
    prefix="/laws",
    tags=["laws"] # 添加标签
)


@router.get("/")
async def getxinfa():
    """
    获取法律信息
    """
    # 查询数据库
    law = await LawModel.all()
    if not law:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="法律不存在")
    return law