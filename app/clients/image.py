import httpx
from dataclasses import dataclass

from app.settings import ImageAPISettings


@dataclass
class ImageAPIClient:
    settings: ImageAPISettings

    async def get_image(self, query: str) -> str:
        """Получает image из Unsplash API."""
        async with httpx.AsyncClient() as client:
            image_data = await client.get(
                url=self.settings.URL,
                params={
                    "query": query,
                },
                headers={
                    "Authorization": f"Client-ID {self.settings.ACCESS_KEY}",
                },
            )
        return image_data.json()["urls"]["regular"]
