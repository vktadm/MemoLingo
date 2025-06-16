from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from backend.src.app.dependencies import get_user_service, get_smtp_service
from backend.src.app.access_verification import (
    only_for_users,
    only_for_admins,
    only_for_guests,
)
from backend.src.app.schemas import UserSchema, UserCreateSchema, EmailRequestSchema
from backend.src.app.services import UserService
from backend.src.app.services.smtp import SMTPService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=Optional[List[UserSchema]])
async def get_users(
    service: Annotated[UserService, Depends(get_user_service)],
    _=Depends(only_for_admins),
):
    """Получает всех существующих пользователей."""
    return await service.get_users()


@router.post(
    "/register",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    user_create: UserCreateSchema,
    user_service: Annotated[UserService, Depends(get_user_service)],
    _=Depends(only_for_guests),
):
    """Регистрация пользователя с login, password."""
    user = await user_service.create_user(user_create)
    return user


@router.post("/send_confirmation_email", response_class=JSONResponse)
async def send_confirmation_email(
    user: EmailRequestSchema,
    service: Annotated[SMTPService, Depends(get_smtp_service)],
):
    # TODO: добавить user_id: int = Depends(get_request_user_id)
    await service.send_confirmation_email(email_to=user.email)

    # TODO: отображение сообщения на фронте
    return {
        "message": f"The message has been sent, check the mailbox {user.email}",
    }


@router.get("/verify_email", response_class=JSONResponse)
async def verify_email(
    token: str,
    service: Annotated[SMTPService, Depends(get_smtp_service)],
):
    await service.verify_confirmation_email(token=token)

    # TODO: отображение сообщения на фронте
    return {
        "message": f"Email successfully confirmed!",
    }


@router.get("/about", response_model=UserSchema)
async def check_self_info(
    user_service: Annotated[UserService, Depends(get_user_service)],
    user: dict = Depends(only_for_users),
):
    user = await user_service.get_user_by_id(user_id=user["id"])

    return user
