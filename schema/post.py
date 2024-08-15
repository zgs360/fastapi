from pydantic import BaseModel, Field
from datetime import datetime
from .user  import User

class Post(BaseModel):
    post_id: int
    title: str
    created: datetime = Field(default_factory=datetime.now)
    user: User


class PostCreateInput(BaseModel):
    title: str
    user_id: int


class PostUpdateInput(BaseModel):
    title: str
