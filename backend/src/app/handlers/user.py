from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, Form, status
from starlette.responses import JSONResponse

from backend.src.app.dependencies import (
    get_user_service,
    get_request_user_id,
    get_smtp_service,
)
from backend.src.app.schemas import UserSchema, UserCreateSchema
from backend.src.app.services import UserService
from backend.src.app.services.smtp import SMTPService

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
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    user_create: UserCreateSchema,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    """Регистрация пользователя с login, password."""
    user = await user_service.create_user(user_create)
    return user


@router.post("/send_confirmation_email", response_class=JSONResponse)
async def send_confirmation_email(
    email: Annotated[str, Form()],
    service: Annotated[SMTPService, Depends(get_smtp_service)],
):
    await service.send_confirmation_email(email_to=email)
    return {
        "message": f"The message has been sent, check the mailbox {email}",
    }


@router.get("/verify_email", response_class=JSONResponse)
async def verify_email(
    token: str,
    service: Annotated[SMTPService, Depends(get_smtp_service)],
):
    await service.verify_confirmation_email(token=token)
    return {
        "message": f"Email successfully confirmed!",
    }


@router.get("/about", response_model=UserSchema)
async def auth_user_check_self_info(
    user_service: Annotated[UserService, Depends(get_user_service)],
    user_id: int = Depends(get_request_user_id),
):
    user = await user_service.get_user_by_id(user_id=user_id)
    return user
