from pydantic import BaseModel
from pydantic import SecretStr
from datetime import datetime


class Category(BaseModel):
    title: str
    description: str
    is_published: bool
    created_at: datetime


class User(BaseModel):
    id: int
    name: str
    password: SecretStr


class Location(BaseModel):
    name: str
    is_published: bool
    created_at: datetime


class Post(BaseModel):
    title: str
    text: str
    pub_date: datetime
    author: User
    location: Location
    category: Category
    is_published: bool
    created_at: datetime
    image: None


class Comment(BaseModel):
    text: str
    post: Post
    created_at: datetime
    author: datetime
