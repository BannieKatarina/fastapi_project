from pydantic import BaseModel
from pydantic import SecretStr, EmailStr
from datetime import datetime


class Category(BaseModel):
    title: str
    description: str
    is_published: bool
    created_at: datetime


class User(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: SecretStr


class Location(BaseModel):
    name: str
    is_published: bool
    created_at: datetime


class Post(BaseModel):
    id: int
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
    id: int
    text: str
    post: Post
    created_at: datetime
    author: User
