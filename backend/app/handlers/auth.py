from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Form
from fastapi.responses import RedirectResponse, JSONResponse


from backend.app.dependencies import (
    get_auth_service,
    get_google_auth_service,
    get_access_token_for_request_user,
)
from backend.app.schemas import UserLoginSchema
from backend.app.services import AuthService
from backend.app.services.google_auth import GoogleAuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=UserLoginSchema)
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    service: Annotated[AuthService, Depends(get_auth_service)],
) -> Optional[UserLoginSchema]:
    """Авторизация c login и password."""
    return await service.login(username=username, password=password)


@router.post("/token/revoke", response_class=JSONResponse)
async def revoke(
    auth_service: AuthService = Depends(get_auth_service),
    access_token: str = Depends(get_access_token_for_request_user),
):
    username = await auth_service.revoke_token(access_token)
    return {
        "message": f"{username} successfully logged out",
    }


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
