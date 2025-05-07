import httpx
from dataclasses import dataclass

from app.decorators import handle_client_errors
from app.settings import ImageAPISettings


@dataclass
class ImageAPIClient:
    settings: ImageAPISettings

    async def get_image(self, query: str) -> str:
        """Получает image из Unsplash API."""
        # TODO: Обработка ошибок
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url=self.settings.URL,
                params={
                    "query": query,
                },
                headers={
                    "Authorization": f"Client-ID {self.settings.ACCESS_KEY}",
                },
                timeout=10.0,
            )
            return response.json()["urls"]["regular"]
