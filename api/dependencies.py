from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.repository import UsersRepository
from api.services import UserService
from api.services.auth import AuthService
from database import db_helper


def get_user_repository(
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> UsersRepository:
    return UsersRepository(session=session)


def get_auth_service(
    user_repository: UsersRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(user_repository=user_repository)


def get_user_service(
    user_repository: UsersRepository = Depends(get_user_repository),
    auth_service: AuthService = Depends(get_auth_service),
) -> UserService:
    return UserService(user_repository=user_repository, auth_service=auth_service)
