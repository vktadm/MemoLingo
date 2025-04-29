from fastapi import Depends, security, Security, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.clients import GoogleClient
from api.exceptions import TokenExpired, TokenException
from api.repository import UsersRepository
from api.services import UserService
from api.services.auth import AuthService
from config import GoogleSettings
from database import db_helper


def get_user_repository(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> UsersRepository:
    return UsersRepository(session=session)


def get_google_client() -> GoogleClient:
    return GoogleClient(settings=GoogleSettings())


def get_auth_service(
    user_repository: UsersRepository = Depends(get_user_repository),
    google_client=Depends(get_google_client),
) -> AuthService:
    return AuthService(
        user_repository=user_repository,
        google_client=google_client,
    )


def get_user_service(
    user_repository: UsersRepository = Depends(get_user_repository),
    auth_service: AuthService = Depends(get_auth_service),
) -> UserService:
    return UserService(user_repository=user_repository, auth_service=auth_service)


reusable_oauth2 = security.HTTPBearer()


async def get_request_user_id(
    auth_service: AuthService = Depends(get_auth_service),
    token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth2),
) -> int:
    try:
        user_id: int = await auth_service.get_user_id_by_access_token(
            access_token=token.credentials
        )
    except TokenExpired as e:
        raise HTTPException(**e.to_dict)
    except TokenException as e:
        raise HTTPException(**e.to_dict)
    return user_id
