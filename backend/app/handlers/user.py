from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, Form, status

from backend.app.dependencies import get_user_service, get_request_user_id
from backend.app.schemas import UserSchema
from backend.app.services import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=Optional[List[UserSchema]])
async def get_users(
    service: Annotated[UserService, Depends(get_user_service)],
):
    # TODO: Добавить роль admin
    """Получает всех существующих пользователей."""
    return await service.get_users()


@router.post(
    "/register",
    response_model=Optional[UserSchema],
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    """Регистрация пользователя с login, password."""
    user = await user_service.create_user(
        username=username,
        password=password,
    )
    return user


@router.get("/about", response_model=UserSchema)
async def auth_user_check_self_info(
    user_service: Annotated[UserService, Depends(get_user_service)],
    user_id: int = Depends(get_request_user_id),
):
    user = await user_service.get_user_by_id(user_id=user_id)
    return user
