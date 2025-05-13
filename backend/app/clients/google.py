import httpx
import time
from dataclasses import dataclass

from backend.app.decorators import handle_client_errors
from backend.app.schemas.auth import GoogleUserDataSchema
from backend.app.settings import Settings


@dataclass
class GoogleClient:
    settings: Settings().auth_google

    @handle_client_errors
    async def get_user_info(self, code: str) -> GoogleUserDataSchema:
        """Получает data из Google."""
        access_token = await self._get_user_access_token(code)
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(
                "https://www.googleapis.com/oauth2/v1/userinfo",
                headers={
                    "Authorization": f"Bearer {access_token}",
                },
                timeout=10.0,
            )
        response.raise_for_status()
        return GoogleUserDataSchema(
            **response.json(),
            google_access_token=access_token,
            username=self._generate_random_username(),
        )

    @handle_client_errors
    async def _get_user_access_token(self, code) -> str:
        """Получает токен доступа."""
        data = {
            "code": code,
            "client_id": self.settings.CLIENT_ID,
            "client_secret": self.settings.CLIENT_SECRET,
            "redirect_uri": self.settings.REDIRECT_URI,
            "grant_type": "authorization_code",
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.post(
                self.settings.TOKEN_URI,
                data=data,
                headers=headers,
                timeout=10.0,
            )
        response.raise_for_status()
        return response.json()["access_token"]

    @staticmethod
    def _generate_random_username() -> str:
        return f"user_{str(int(time.time()))[-10:]}"
