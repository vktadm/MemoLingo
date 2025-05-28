from pydantic import BaseModel
from pydantic_settings import BaseSettings
from environs import Env

env = Env()
env.read_env()


class FakePostgresSettings(BaseModel):
    DB_DRIVER: str = "postgresql+asyncpg"
    DB_USER: str = env("DB_USER_TEST")
    DB_PASSWORD: str = env("DB_PASSWORD_TEST")
    DB_HOST: int = env("DB_HOST_TEST")
    DB_PORT: int = env("DB_PORT_TEST")
    DB_NAME: str = env("DB_NAME_TEST")
    echo: bool = True

    @property
    def get_url(self) -> str:
        return (
            f"{self.DB_DRIVER}://"
            f"{self.DB_USER}:"
            f"{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:"
            f"{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )


class FakeSettings(BaseSettings):
    db: FakePostgresSettings = FakePostgresSettings()


fake_settings = FakeSettings()
