from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException

from api.dependencies import get_auth_service
from api.exceptions import UserNotFound, UserIncorrectPassword
from api.schemas import UserLoginSchema

from api.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["AUTH"])


@router.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    service: Annotated[AuthService, Depends(get_auth_service)],
) -> UserLoginSchema:
    """Авторизация с генерацией JWT токена."""
    try:
        user: UserLoginSchema = await service.login(
            username=username, password=password
        )
    except UserNotFound as e:
        raise HTTPException(**e.to_dict)
    except UserIncorrectPassword as e:
        raise HTTPException(**e.to_dict)
    # jwt_payload = {
    #     "sub": user.username,
    #     "username": user.username,
    #     "email": user.email,
    # }
    # access_token = utils_jwt.encode_jwt(payload=jwt_payload)
    return user


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
