from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse

from app.dependencies import (
    get_auth_service,
    get_google_auth_service,
    get_access_token_for_request_user,
)
from app.exceptions import (
    UserNotFound,
    UserIncorrectPassword,
    TokenExpired,
    TokenException,
)
from app.schemas import UserLoginSchema
from app.services import AuthService
from app.services.google_auth import GoogleAuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


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


@router.post("/token/revoke")
async def revoke(
    auth_service: AuthService = Depends(get_auth_service),
    access_token: str = Depends(get_access_token_for_request_user),
):
    try:
        username = await auth_service.revoke_token(access_token)
        return {
            "message": f"{username} successfully logged out",
        }
    except TokenExpired as e:
        raise HTTPException(**e.to_dict)
    except TokenException as e:
        raise HTTPException(**e.to_dict)


@router.get(
    "/login/google",
    response_class=RedirectResponse,
)
async def login_google(
    service: Annotated[GoogleAuthService, Depends(get_google_auth_service)],
):
    redirect_url = await service.get_google_redirect_url()
    print(redirect_url)
    return RedirectResponse(redirect_url)


@router.get("/google")
async def auth_google(
    service: Annotated[GoogleAuthService, Depends(get_google_auth_service)],
    code: str,
):
    return await service.auth_google(code=code)
