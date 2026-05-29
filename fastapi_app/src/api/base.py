from fastapi import APIRouter, Depends, status
from typing import List

from src.infrastructure.sqlite.models import *

from src.schemas.classes import Post as PostSchema
from src.schemas.classes import User as UserSchema
from src.schemas.classes import Category as CategorySchema
from src.schemas.classes import Location as LocationSchema
from src.domain.user.use_cases.get_user_by_login import GetUserByLoginUseCase
from src.domain.user.use_cases.get_all_users import GetUsersUseCase
from src.domain.user.use_cases.create_user import PostUserUseCase
from src.domain.category.use_cases.create_category import PostCategoryUseCase
from src.domain.location.use_cases.create_location import PostLocationUseCase
from src.domain.post.use_cases.get_all_posts import GetPostsUseCase
from src.domain.post.use_cases.get_post import GetPostUseCase
from src.domain.post.use_cases.create_post import CreatePostUseCase
from src.domain.post.use_cases.change_post import ChangePostUseCase
from src.domain.post.use_cases.delete_post import DeletePostUseCase
from src.api.depends import *


router = APIRouter(prefix="/posts")
router_user = APIRouter(prefix="/users")
# создать пост
@router.post("/", response_model=PostSchema,
             status_code=status.HTTP_201_CREATED)
async def create_post(
    post: PostSchema,
    use_case: CreatePostUseCase = Depends(create_post_use_case)
) -> Post:
    new_post = use_case.execute(new_post=post)
    return new_post


# Получить все посты
@router.get("/", status_code=status.HTTP_200_OK,
            response_model=List[PostSchema])
async def get_all_posts(
    use_case: GetPostsUseCase = Depends(get_all_posts_use_case)
) -> list[PostSchema]:
    posts = await use_case.execute()
    return posts


# получить один пост по ID
@router.get("/{post_id}", response_model=PostSchema)
async def get_post(
    post_id: int,
    use_case: GetPostUseCase = Depends(get_one_post_use_case)
) -> Post:
    post = await use_case.execute(id=post_id)
    return post


# обновить пост
@router.put("/{post_id}", response_model=PostSchema)
async def update_post(
    post_id: int, new_post: PostSchema,
    use_case: ChangePostUseCase = Depends(change_post_use_case)
) -> Post:
    db_post = await use_case.execute(id=post_id, new_post=new_post)
    return db_post


# удалить поста
@router.delete("/{post_id}",  response_model=PostSchema)
async def delete_post(
    post_id: int,
    use_case: DeletePostUseCase = Depends(delete_post_use_case)
) -> dict:
    message = await use_case.execute(id=post_id)
    return message


# создать ползователя
@router_user.post("/", response_model=UserSchema,
                  status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserSchema,
    use_case: PostUserUseCase = Depends(post_user_use_case)
) -> User:
    new_user = await use_case.execute(new_user=user)
    return new_user


# получить пользователя по логину
@router_user.get("/{login}", status_code=status.HTTP_200_OK,
                 response_model=UserSchema)
async def get_user_by_login(
    login: str,
    use_case: GetUserByLoginUseCase = Depends(get_get_user_by_login_use_case)
) -> User:
    user = await use_case.execute(login=login)
    return user


# получить всех пользователей
@router_user.get("/", status_code=status.HTTP_200_OK,
                 response_model=list[UserSchema])
async def get_all_users(
    use_case: GetUsersUseCase = Depends(get_all_users_use_case)
) -> list[UserSchema]:
    users = await use_case.execute()
    return users


# создать категорию
@router.post("/categories", response_model=CategorySchema,
             status_code=status.HTTP_201_CREATED)
async def create_category(
    category: CategorySchema,
    use_case: PostCategoryUseCase = Depends(post_category_use_case)
) -> Category:
    new_category = await use_case.execute(new_category=category)
    return new_category


# создать локацию
@router.post("/locations", response_model=LocationSchema,
             status_code=status.HTTP_201_CREATED)
async def create_location(
    location: LocationSchema,
    use_case: PostLocationUseCase = Depends(post_location_use_case)
) -> Location:
    new_location = await use_case.execute(new_location=location)
    return new_location
