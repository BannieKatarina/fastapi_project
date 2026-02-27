from fastapi import APIRouter, HTTPException
from typing import List
from src.schemas.classes import Post

router = APIRouter()
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