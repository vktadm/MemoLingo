from fastapi import APIRouter, Depends

from api.schemas.user import User
from api.auth import crud, utils_jwt

router = APIRouter(tags=["AUTH"])


@router.post("/login")
async def login(user: User = Depends(crud.validate_user)):
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    access_token = utils_jwt.encode_jwt(payload=jwt_payload)
    return {
        "message": "Авторизация прошла успешно",
        "username": user.username,
        "access_token": access_token,
    }


@router.post("/register")
async def register(user: User = Depends(crud.create_user)):
    return {
        "message": "Регистрация прошла успешно",
        "username": user.username,
    }


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
