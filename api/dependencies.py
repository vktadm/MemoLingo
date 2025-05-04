import httpx
from fastapi import Depends, security, Security, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis

from api.clients import GoogleClient
from api.exceptions import TokenExpired, TokenException
from api.repository import UsersRepository
from api.repository.black_list import TokenBlackListRepository
from api.services import UserService, CryptoService, AuthService, JWTService
from config import GoogleSettings, JWTSettings
from database import db_helper
from cache import db_helper as cache_db_helper


def get_user_repository(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> UsersRepository:
    return UsersRepository(session=session)


def get_google_client() -> GoogleClient:
    return GoogleClient(settings=GoogleSettings())


def get_jwt_service() -> JWTService:
    return JWTService(settings=JWTSettings())


def get_crypto_service() -> CryptoService:
    return CryptoService()


def get_block_list_repository(
    session: Redis = Depends(cache_db_helper.get_redis_connection),
) -> TokenBlackListRepository:
    return TokenBlackListRepository(session)


def get_auth_service(
    user_repository: UsersRepository = Depends(get_user_repository),
    google_client: GoogleClient = Depends(get_google_client),
    jwt: JWTService = Depends(get_jwt_service),
    crypto_service: CryptoService = Depends(get_crypto_service),
    block_list: TokenBlackListRepository = Depends(get_block_list_repository),
) -> AuthService:
    return AuthService(
        user_repository=user_repository,
        google_client=google_client,
        jwt_service=jwt,
        crypto_service=crypto_service,
        black_list=block_list,
    )


def get_user_service(
    user_repository: UsersRepository = Depends(get_user_repository),
    crypto_service: CryptoService = Depends(get_crypto_service),
) -> UserService:
    return UserService(
        user_repository=user_repository,
        crypto_service=crypto_service,
    )


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


async def revoke_token_for_current_user(
    auth_service: AuthService = Depends(get_auth_service),
    token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth2),
):
    try:
        username: str = await auth_service.revoke_token(
            access_token=token.credentials,
        )
    except TokenExpired as e:
        raise HTTPException(**e.to_dict)
    except TokenException as e:
        raise HTTPException(**e.to_dict)
    return username
