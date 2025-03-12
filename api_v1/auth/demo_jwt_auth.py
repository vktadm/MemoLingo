from fastapi import APIRouter, Depends, Form, HTTPException, status
from pydantic import BaseModel
from fastapi.security import (
    OAuth2PasswordBearer,
)
from jwt.exceptions import InvalidTokenError

from api_basic.user import UserSchema
from api_v1.auth import utils_jwt


class TokenInfo(BaseModel):
    access_token: str
    token_type: str


router = APIRouter(prefix="/jwt", tags=["JWT"])

admin = UserSchema(
    username="admin",
    password=utils_jwt.hash_password("qwerty"),
    email="example@gmail.com",
)

user = UserSchema(
    username="jhon",
    password=utils_jwt.hash_password("secret"),
    email="jhon@gmail.com",
)

users_db: dict[str, UserSchema] = {
    admin.username: admin,
    user.username: user,
}

# http_bearer = HTTPBearer()
oauth_bearer = OAuth2PasswordBearer(
    tokenUrl="/api/jwt/login",
)


def validate_auth_user(
    username: str = Form(),
    password: str = Form(),
):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )

    if not (user := users_db.get(username)):
        raise exception

    if utils_jwt.validate_password(password=password, hashed_password=user.password):
        return user

    raise exception


def get_current_auth_token(
    # credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
    token: str = Depends(oauth_bearer),
) -> dict:
    # token = credentials.credentials
    try:
        payload = utils_jwt.decode_jwt(token=token)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token error: {e}",
        )
    return payload


def get_current_auth_user(
    payload: dict = Depends(get_current_auth_token),
) -> UserSchema:
    username: str | None = payload.get("sub")

    if user := users_db.get(username):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token invalid (user not found)",
    )


@router.post("/login", response_model=TokenInfo)
def auth_user_issue_jwt(
    user: UserSchema = Depends(validate_auth_user),
):
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    access_token = utils_jwt.encode_jwt(payload=jwt_payload)
    return TokenInfo(
        access_token=access_token,
        token_type="Bearer",
    )


@router.get("/users/about/")
def auth_user_check_self_info(
    payload: dict = Depends(get_current_auth_token),
    user: UserSchema = Depends(get_current_auth_user),
):
    iat = payload.get("iat")
    return {
        "username": user.username,
        "email": user.email,
        "logged_in_at": iat,
    }
