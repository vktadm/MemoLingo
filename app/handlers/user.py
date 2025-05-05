from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, Form, HTTPException

from app.dependencies import get_user_service, get_auth_service, get_request_user_id
from app.exceptions import UserAlreadyExists, UserNoCreate
from app.exceptions.base import NoContent
from app.schemas import UserLoginSchema, UserSchema
from app.services import UserService, AuthService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=Optional[List[UserSchema]])
async def get_users(
    service: Annotated[UserService, Depends(get_user_service)],
):
    # TODO: Добавить роль admin
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


@router.get("/about", response_model=UserSchema)
async def auth_user_check_self_info(
    user_service: Annotated[UserService, Depends(get_user_service)],
    user_id: int = Depends(get_request_user_id),
):
    user = await user_service.get_user_by_id(user_id=user_id)
    return user
