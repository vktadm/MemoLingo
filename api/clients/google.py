import requests
from dataclasses import dataclass

from api.schemas.auth import GoogleUserDataSchema
from config import GoogleSettings


@dataclass
class GoogleClient:
    settings: GoogleSettings

    def get_user_info(self, code: str) -> GoogleUserDataSchema:
        """Получает data из Google."""
        access_token = self._get_user_access_token(code)
        user_info = requests.get(
            "https://www.googleapis.com/oauth2/v1/userinfo",
            headers={
                "Authorization": f"Bearer {access_token}",
            },
        )
        return GoogleUserDataSchema(**user_info.json(), access_token=access_token)

    def _get_user_access_token(self, code) -> str:
        """Получает токен доступа."""
        data = {
            "code": code,
            "client_id": self.settings.CLIENT_ID,
            "client_secret": self.settings.CLIENT_SECRET,
            "redirect_uri": self.settings.REDIRECT_URI,
            "grant_type": "authorization_code",
        }
        response = requests.post(
            self.settings.TOKEN_URI,
            data=data,
        )
        print(response)  # TODO: убрать
        return response.json()["access_token"]
