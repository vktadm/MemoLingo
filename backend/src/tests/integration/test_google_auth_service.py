import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from backend_old.app.services import GoogleAuthService

pytestmark = pytest.mark.asyncio


async def test_google_auth__success(
    google_auth_service: GoogleAuthService, session: AsyncSession
):
    code = "fake_code"
    user = await google_auth_service.auth_google(code)
    assert user is not None


if __name__ == "__main__":
    pytest.main()
