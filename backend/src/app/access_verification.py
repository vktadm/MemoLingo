from typing import Optional

from fastapi import security, Security, Depends

from backend.src.app.database import UserRole
from backend.src.app.dependencies import get_auth_service
from backend.src.app.exceptions import UserForbiddenException
from backend.src.app.services import AuthService


# ---------- SECURITY ---------- #
reusable_oauth2 = security.HTTPBearer(auto_error=False)


async def get_access_token_for_request_user(
    token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth2),
):
    if not token:
        raise UserForbiddenException()

    return token.credentials


async def get_current_user(
    token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth2),
    auth_service: AuthService = Depends(get_auth_service),
) -> dict | None:
    if not token:
        return None

    user = await auth_service.validate_access_token(access_token=token.credentials)
    if not user:
        return None

    return user


async def only_for_users(
    user: dict = Depends(get_current_user),
) -> Optional[dict]:
    print(user.get("user_role"))
    if not user or user.get("user_role") == UserRole.ADMIN:
        raise UserForbiddenException()

    return user


async def only_for_guests(
    user: dict = Depends(get_current_user),
):
    if user:
        raise UserForbiddenException()


async def only_for_admins(
    user: dict = Depends(get_current_user),
):
    print(user)
    if not user or user.get("user_role") != UserRole.ADMIN:
        raise UserForbiddenException()
