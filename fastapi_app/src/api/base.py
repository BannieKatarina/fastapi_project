from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from src.schemas.classes import Post, User
from src.domain.user.use_cases.get_user_by_login import GetUserByLoginUseCase
from src.api.depends import get_get_user_by_login_use_case

router = APIRouter(prefix="/posts")
posts = []


@router.get("/", response_model=List[Post])
async def get_posts():
    return posts


@router.post("/", response_model=Post)
async def create_post(post: Post):
    posts.append(post)
    return post


@router.put("/{post_id}", response_model=Post)
async def update_post(post_id: int, updated_post: Post):
    for post in enumerate(posts):
        if post_id == post[0]:
            posts[post[0]] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found")


@router.delete("/{post_id}")
async def delete_post(post_id: int):
    for post in enumerate(posts):
        if post_id == post[0]:
            posts.pop(post[0])
            return {"message": "Post deleted"}
    raise HTTPException(status_code=404, detail="Post not found")


@router.get("/user/{login}", status_code=status.HTTP_200_OK,
            response_model=User)
async def get_user_by_login(
    login: str,
    use_case: GetUserByLoginUseCase = Depends(get_get_user_by_login_use_case)
) -> User:
    user = await use_case.execute(login=login)
    return user
