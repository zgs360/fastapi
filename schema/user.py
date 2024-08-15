from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class User(BaseModel):
    user_id: int
    email: EmailStr
    created: datetime = Field(default_factory=datetime.now)