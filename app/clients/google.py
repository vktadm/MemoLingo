import httpx
import time
from dataclasses import dataclass

from app.schemas.auth import GoogleUserDataSchema
from app.config import GoogleSettings


@dataclass
class GoogleClient:
    settings: GoogleSettings

    async def get_user_info(self, code: str) -> GoogleUserDataSchema:
        """Получает data из Google."""
        access_token = await self._get_user_access_token(code)
        async with httpx.AsyncClient(verify=False) as client:
            user_info = await client.get(
                "https://www.googleapis.com/oauth2/v1/userinfo",
                headers={
                    "Authorization": f"Bearer {access_token}",
                },
            )
        return GoogleUserDataSchema(
            **user_info.json(),
            google_access_token=access_token,
            username=self._generate_random_username(),
        )

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
            )
        return response.json()["access_token"]

    @staticmethod
    def _generate_random_username() -> str:
        return f"user_{str(int(time.time()))[-10:]}"
