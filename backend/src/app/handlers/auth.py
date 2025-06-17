from typing import Annotated, Optional
from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse, JSONResponse


from backend.src.app.dependencies import get_auth_service, get_google_auth_service
from backend.src.app.access_verification import (
    only_for_admins,
    only_for_guests,
    only_for_users,
    get_access_token_for_request_user,
    get_current_user,
)

from backend.src.app.schemas import UserLoginSchema, UserLoginFormSchema
from backend.src.app.services import AuthService
from backend.src.app.services.google_auth import GoogleAuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=UserLoginSchema)
async def login(
    user: UserLoginFormSchema,
    service: Annotated[AuthService, Depends(get_auth_service)],
    _=Depends(only_for_guests),
) -> Optional[UserLoginSchema]:
    """Авторизация c login и password."""
    return await service.login(username=user.username, password=user.password)


@router.post("/logout", response_class=JSONResponse)
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
    _=Depends(only_for_guests),
):
    redirect_url = await service.get_google_redirect_url()
    return RedirectResponse(redirect_url)


@router.post("/google")
async def auth_google(
    service: Annotated[GoogleAuthService, Depends(get_google_auth_service)],
    code: str,
    _=Depends(only_for_guests),
):
    return await service.auth_google(code=code)
