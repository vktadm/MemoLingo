import pytest

from app.services import GoogleAuthService
from app.settings import Settings

pytestmark = pytest.mark.asyncio


def test_google_redirect_url__success(
    google_auth_service: GoogleAuthService,
    settings: Settings,
):
    settings_google_redirect_url = google_auth_service.get_google_redirect_url

    auth_service_google_redirect_url = google_auth_service.get_google_redirect_url

    assert settings_google_redirect_url == auth_service_google_redirect_url


def test_google_redirect_url__fail(
    google_auth_service: GoogleAuthService,
):
    settings_google_redirect_url = "https://fake_google_redirect_url.com"

    auth_service_google_redirect_url = google_auth_service.get_google_redirect_url

    assert settings_google_redirect_url != auth_service_google_redirect_url
