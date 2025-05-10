from fastapi import Depends, security, Security
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis

from app.settings import settings
from app.clients import GoogleClient, ImageAPIClient, IconAPIClient
from app.repository import UsersRepository, TokenBlackListRepository, WordRepository
from app.services import (
    UserService,
    CryptoService,
    AuthService,
    JWTService,
    GoogleAuthService,
    WordService,
)

from app.database import db_helper
from app.cache import db_helper as cache_db_helper


# ---------- REPOSITORIES ---------- #
async def get_user_repository(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> UsersRepository:
    return UsersRepository(session=session)


async def get_word_repository(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> WordRepository:
    return WordRepository(session=session)


async def get_block_list_repository(
    session: Redis = Depends(cache_db_helper.get_redis_session),
) -> TokenBlackListRepository:
    return TokenBlackListRepository(session=session, settings=settings)


# ---------- CLIENTS ---------- #
async def get_google_client() -> GoogleClient:
    return GoogleClient(settings=settings.auth_google)


async def get_image_client() -> ImageAPIClient:
    return ImageAPIClient(settings=settings.image)


async def get_icon_client() -> IconAPIClient:
    return IconAPIClient()


# ---------- SERVICES ---------- #
async def get_jwt_service() -> JWTService:
    return JWTService(settings=settings.auth_jwt)


async def get_crypto_service() -> CryptoService:
    return CryptoService()


async def get_auth_service(
    user_repository: UsersRepository = Depends(get_user_repository),
    jwt_service: JWTService = Depends(get_jwt_service),
    crypto_service: CryptoService = Depends(get_crypto_service),
    block_list: TokenBlackListRepository = Depends(get_block_list_repository),
) -> AuthService:
    return AuthService(
        user_repository=user_repository,
        jwt_service=jwt_service,
        crypto_service=crypto_service,
        black_list=block_list,
    )


async def get_word_service(
    repository: WordRepository = Depends(get_word_repository),
    image_client: ImageAPIClient = Depends(get_image_client),
) -> WordService:
    return WordService(
        repository=repository,
        image_client=image_client,
    )


async def get_google_auth_service(
    user_repository: UsersRepository = Depends(get_user_repository),
    google_client: GoogleClient = Depends(get_google_client),
    jwt_service: JWTService = Depends(get_jwt_service),
    block_list: TokenBlackListRepository = Depends(get_block_list_repository),
) -> GoogleAuthService:
    return GoogleAuthService(
        user_repository=user_repository,
        google_client=google_client,
        jwt_service=jwt_service,
        black_list=block_list,
    )


async def get_user_service(
    user_repository: UsersRepository = Depends(get_user_repository),
    crypto_service: CryptoService = Depends(get_crypto_service),
) -> UserService:
    return UserService(
        user_repository=user_repository,
        crypto_service=crypto_service,
    )


# ---------- SECURITY ---------- #
reusable_oauth2 = security.HTTPBearer()


async def get_access_token_for_request_user(
    token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth2),
) -> str:
    return token.credentials


async def get_request_user_id(
    auth_service: AuthService = Depends(get_auth_service),
    token: str = Depends(get_access_token_for_request_user),
) -> int:
    user: dict = await auth_service.validate_access_token(access_token=token)
    return user["id"]
