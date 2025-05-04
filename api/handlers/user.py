from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, Form, HTTPException

from api.dependencies import get_user_service, get_auth_service
from api.exceptions import UserAlreadyExists, UserNoCreate
from api.exceptions.base import NoContent
from api.schemas import UserLoginSchema, UserSchema
from api.services import UserService, AuthService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=Optional[List[UserSchema]])
async def get_users(
    service: Annotated[UserService, Depends(get_user_service)],
):
    """Получает всех существующих пользователей."""
    try:
        return await service.get_users()
    except NoContent as e:
        raise HTTPException(**e.to_dict)


@router.post("/register", response_model=Optional[UserLoginSchema])
async def create_user(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    user_service: Annotated[UserService, Depends(get_user_service)],
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
):
    """Регистрация пользователя с login, password."""
    # Создаем пользователя.
    try:
        user = await user_service.create_user(
            username=username,
            password=password,
        )
    except UserAlreadyExists as e:
        raise HTTPException(**e.to_dict)
    except UserNoCreate as e:
        raise HTTPException(**e.to_dict)
    # Авторизируем его.
    login_user = await auth_service.login(
        username=username,
        password=password,
    )
    return login_user


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
