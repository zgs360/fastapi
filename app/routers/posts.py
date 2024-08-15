from http.client import HTTPException

from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
# 加载数据库
from app.database import database
from schema.post import Post, PostCreateInput, PostUpdateInput
from schema.user import User

# 设置唯一可以访问的路由
__all__ = ("router",)

router = APIRouter(
    prefix="/posts",
    tags=["posts"] # 添加标签
)


@router.get(
    "",
    description="Get all posts", # 设置描述
    response_model=list[Post], # 设置响应模型
    status_code=status.HTTP_200_OK, # 设置状态码
)
async def list_posts()->list[Post]:
    # 从数据库中获取数据
    return [
        Post(
            post_id=post["post_id"],
            title=post["title"],
            created=post["created"],
            user=User(
                user_id=post["user_id"],
                email=database.users[post["user_id"]]["email"],
                created=database.users[post["user_id"]]["created"],
            )
        )
        for post in database.posts.values()
    ]


@router.get(
    "/{post_id}",
    description="Get post", # 设置描述
    response_model=Post, # 设置响应模型
    status_code=status.HTTP_200_OK, # 设置状态码
)
async def list_posts(post_id: int)->Post:
    # 检查post_id是否存在
    if post_id not in database.posts:
        raise HTTPException(
            detail="Post not found",
            status_code=status.HTTP_404_NOT_FOUND
        )
    # 从数据库中获取数据
    post = database.posts[post_id]
    return Post(
        post_id=post["post_id"],
        title=post["title"],
        created=post["created"],
        user=User(
            user_id=post["user_id"],
            email=database.users[post["user_id"]]["email"],
            created=database.users[post["user_id"]]["created"],
        )
    )

@router.post(
    "",
    description="Create post", # 设置描述
    response_model=Post, # 设置响应模型
    status_code=status.HTTP_201_CREATED, # 设置状态码
)
async def create_post(input_post: PostCreateInput)->Post:
    if input_post.user_id not in database.users:
        raise HTTPException(
            detail="User not found",
            status_code=status.HTTP_422_NOT_FOUND

        )
    post = Post(
        post_id=len(database.posts) + 1,
        title=input_post.title,
        user=User(
            user_id=input_post.user_id,
            email=database.users[input_post.user_id]["email"],
            created=database.users[input_post.user_id]["created"],
        )
    )
    database.posts[post.post_id] = {
        "post_id": post.post_id,
        "title": post.title,
        "created": post.created,
        "user_id": post.user.user_id
    }

    return post

@router.patch(
    "/{post_id}",
    description="Update post", # 设置描述
    response_model=Post, # 设置响应模型
    status_code=status.HTTP_200_OK, # 设置状态码
)
async def update_post(post_id: int, input_post: PostUpdateInput)->Post:
    if post_id not in database.posts:
        raise HTTPException(
            detail="Post not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    post = database.posts[post_id]
    post["title"] = input_post.title
    return Post(
        post_id=post["post_id"],
        title=post["title"],
        created=post["created"],
        user=User(
            user_id=post["user_id"],
            email=database.users[post["user_id"]]["email"],
            created=database.users[post["user_id"]]["created"],
        )
)

@router.delete(
    "/{post_id}",
    description="Delete post", # 设置描述
    status_code=status.HTTP_204_NO_CONTENT, # 设置状态码
)
async def delete_post(post_id: int)->None:
    if post_id not in database.posts:
        return

    # 从数据库中删除数据
    database.posts.pop(post_id)
    return None