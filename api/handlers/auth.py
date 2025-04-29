from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse

from api.dependencies import get_auth_service
from api.exceptions import UserNotFound, UserIncorrectPassword
from api.schemas import UserLoginSchema
from api.services import AuthService

router = APIRouter(prefix="/auth", tags=["AUTH"])


@router.post("/login", response_model=UserLoginSchema)
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    service: Annotated[AuthService, Depends(get_auth_service)],
):
    """Авторизация c login и password."""
    try:
        user: UserLoginSchema = await service.login(
            username=username, password=password
        )
    except UserNotFound as e:
        raise HTTPException(**e.to_dict)
    except UserIncorrectPassword as e:
        raise HTTPException(**e.to_dict)
    return user


@router.get(
    "/login/google",
    response_class=RedirectResponse,
)
async def login_google(
    service: Annotated[AuthService, Depends(get_auth_service)],
):
    redirect_url = await service.get_google_redirect_url()
    print(redirect_url)
    return RedirectResponse(redirect_url)


@router.get("/google")
async def auth_google(
    service: Annotated[AuthService, Depends(get_auth_service)],
    code: str,
):
    return await service.auth_google(code=code)
