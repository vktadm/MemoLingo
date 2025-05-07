import httpx
from dataclasses import dataclass

from app.decorators import handle_http_errors
from app.settings import ImageAPISettings


@dataclass
class ImageAPIClient:
    settings: ImageAPISettings

    @handle_http_errors
    async def get_image(self, query: str) -> str:
        """Получает image из Unsplash API."""
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
            response.raise_for_status()
            return response.json()["urls"]["regular"]
