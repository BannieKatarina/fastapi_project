from src.domain.user.use_cases.get_user_by_login import GetUserByLoginUseCase
from src.domain.user.use_cases.get_all_users import GetUsersUseCase
from src.domain.user.use_cases.create_user import PostUserUseCase
from src.domain.post.use_cases.get_all_posts import GetPostsUseCase
from src.domain.post.use_cases.get_post import GetPostUseCase
from src.domain.post.use_cases.create_post import CreatePostUseCase
from src.domain.post.use_cases.change_post import ChangePostUseCase
from src.domain.post.use_cases.delete_post import DeletePostUseCase
from src.domain.category.use_cases.create_category import PostCategoryUseCase
from src.domain.location.use_cases.create_location import PostLocationUseCase


def get_get_user_by_login_use_case() -> GetUserByLoginUseCase:
    return GetUserByLoginUseCase()


def get_all_users_use_case() -> GetUsersUseCase:
    return GetUsersUseCase()


def post_user_use_case() -> PostUserUseCase:
    return PostUserUseCase()


def get_all_posts_use_case() -> GetPostsUseCase:
    return GetPostsUseCase()


def get_one_post_use_case() -> GetPostUseCase:
    return GetPostUseCase()


def change_post_use_case() -> ChangePostUseCase:
    return ChangePostUseCase()


def delete_post_use_case() -> DeletePostUseCase:
    return DeletePostUseCase()


def create_post_use_case() -> CreatePostUseCase:
    return CreatePostUseCase()


def post_category_use_case() -> PostCategoryUseCase:
    return PostCategoryUseCase()


def post_location_use_case() -> PostLocationUseCase:
    return PostLocationUseCase()
