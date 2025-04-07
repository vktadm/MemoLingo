import secrets
from time import time
import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials


router = APIRouter(prefix="/demo-auth", tags=["Demo Auth"])

security = HTTPBasic()


@router.get("/basic-auth/")
def demo_basic_auth_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    return {
        "message": "Hi!",
        "username": credentials.username,
        "password": credentials.password,
    }


usernames_to_passwords = {
    "admin": "12345",
    "user": "qwerty",
    "jhon": "secret",
}


static_auth_token_to_username = {
    "f1b68523e5196fafbc07e91b6d5f727": "admin",
    "134e6a1cccc83a9f4fe5d8ad8e7f1d506": "user",
}


def get_auth_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> str:
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )

    if credentials.username not in usernames_to_passwords:
        raise exception

    password = usernames_to_passwords.get(credentials.username)

    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        password.encode("utf-8"),
    ):
        raise exception

    return credentials.username


def get_username_http(static_token: str = Header(alias="x-auth-token")) -> str:
    if static_token not in static_auth_token_to_username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return static_auth_token_to_username[static_token]


@router.get("/basic-auth-username/")
def demo_basic_auth_username(
    username: str = Depends(get_auth_user),
):
    return {
        "message": f"Hi!, {username}",
        "username": username,
    }


@router.get("/http-header-auth/")
def demo_auth_http(
    username: str = Depends(get_username_http),
):
    return {
        "message": f"Hi!, {username}",
        "username": username,
    }


COOKIES: dict[str, dict] = {}
COOKIE_SESSION_ID_KEY = "web-app-session-id"


def generate_session_id() -> str:
    return uuid.uuid4().hex


def get_session_data(session_id: str = Cookie(alias=COOKIE_SESSION_ID_KEY)) -> dict:
    if session_id not in COOKIES:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    return COOKIES[session_id]


@router.post("/login-cookie/")
def demo_login(
    response: Response,
    username: str = Depends(get_username_http),
):
    session_id = generate_session_id()
    COOKIES[session_id] = {"username": username, "login_at": int(time())}
    response.set_cookie(COOKIE_SESSION_ID_KEY, session_id)
    return {"result": "ok"}


@router.get("/check-cookie/")
def demo_check(user_session_data: dict = Depends(get_session_data)):
    username = user_session_data["username"]
    return {
        "message": f"Hello, {username}",
        **user_session_data,
    }


@router.get("/logout-cookie/")
def demo_logout(
    response: Response,
    session_id: str = Cookie(alias=COOKIE_SESSION_ID_KEY),
    user_session_data: dict = Depends(get_session_data),
):
    COOKIES.pop(session_id)
    response.delete_cookie(COOKIE_SESSION_ID_KEY)
    username = user_session_data["username"]
    return {"message": f"Goodbye, {username}"}
