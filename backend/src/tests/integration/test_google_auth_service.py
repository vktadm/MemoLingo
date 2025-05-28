import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from backend.src.app.services import GoogleAuthService


# async def test_google_auth__success(
#     google_auth_service: GoogleAuthService, session: AsyncSession
# ):
#     code = "fake_code"
#     user = await google_auth_service.auth_google(code)
#     assert user is not None
