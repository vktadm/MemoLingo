from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from environs import Env

env = Env()
env.read_env()

BASE_DIR = Path(__file__).parent.parent

# Development database
DB_PATH = BASE_DIR / env("DB_SQLITE")


class PostgresSettings(BaseModel):
    DB_DRIVER: str = "postgresql+asyncpg"
    DB_USER: str = env("DB_USER")
    DB_PASSWORD: str = env("DB_PASSWORD")
    DB_HOST: int = env("DB_HOST")
    DB_PORT: int = env("DB_PORT")
    DB_NAME: str = env("DB_NAME")
    echo: bool = True  # TODO: remove if not debug

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


class RedisSettings(BaseModel):
    host: str = env("REDIS_HOST")
    port: int = env("REDIS_PORT")
    db: int = env("REDIS_DB")


class SQliteSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True  # TODO: remove if not debug


class AuthJWT(BaseModel):
    algorithm: str = "HS256"
    secret: str = env("SECRET_KEY")
    access_token_expire_minutes: int = 15


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    # db: SQliteSettings = SQliteSettings()
    db: PostgresSettings = PostgresSettings()
    cache: RedisSettings = RedisSettings()
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
