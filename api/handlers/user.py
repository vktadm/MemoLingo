from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException

from api.dependencies import get_user_service
from api.exceptions import UserAlreadyExists
from api.schemas import UserLoginSchema, UserSchema
from api.services import UserService

router = APIRouter(prefix="/users", tags=["USERS"])


@router.get("/")
async def get_users(
    service: Annotated[UserService, Depends(get_user_service)],
) -> list[UserSchema]:
    """Получает всех существующих пользователей."""
    return await service.get_users()


@router.post("/register")
async def create_user(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    service: Annotated[UserService, Depends(get_user_service)],
) -> UserLoginSchema:
    """Регистрация пользователя с login, password."""
    try:
        user: UserLoginSchema = await service.create_user(
            username=username, password=password
        )
    except UserAlreadyExists as e:
        raise HTTPException(**e.to_dict)
    return user


# @router.get("/users/about/")
# def auth_user_check_self_info(
#     payload: dict = Depends(get_current_auth_token),
#     user: UserSchema = Depends(get_current_auth_user),
# ):
#     iat = payload.get("iat")
#     return {
#         "username": user.username,
#         "email": user.email,
#         "logged_in_at": iat,
#     }
