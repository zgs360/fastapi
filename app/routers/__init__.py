from .heartbeat import router as heartbeat_router
from .posts import router as posts_router
from .laws import router as laws_router
from .xinfa import *

__all__ = ["heartbeat_router","posts_router","xinfa_router", "laws_router"]

   
routers = [posts_router, xinfa_router, laws_router]
__all__ += routers