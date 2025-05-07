import httpx
from typing import Optional
from dataclasses import dataclass

from app.settings import ImageAPISettings


@dataclass
class ImageAPIClient:
    settings: ImageAPISettings

    async def get_image(self, query: str) -> Optional[str]:
        """Получает image из Unsplash API."""
        async with httpx.AsyncClient() as client:
            try:
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

            except httpx.HTTPStatusError as e:
                print(e)  # TODO: заменить на loggin

            except httpx.TimeoutException as e:
                print(e)

            except httpx.RequestError as e:
                print(e)

            except Exception as e:
                print(e)

            finally:
                return None
