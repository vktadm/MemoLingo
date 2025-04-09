from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from environs import Env

env = Env()
env.read_env()

BASE_DIR = Path(__file__).parent.parent

# Development database
DB_PATH = BASE_DIR / env("DB_SQLITE")


class PostgreSQLSettings(BaseModel):
    url: str = (
        f"postgresql+asyncpg://"
        f"{env('DB_USER')}:"
        f"{env("DB_PASSWORD")}@"
        f"{env("DB_HOST")}:"
        f"{env("DB_PORT")}/"
        f"{env("DB_NAME")}"
    )
    echo: bool = True  # TODO: remove if not debug


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
    api_prefix: str = "/api"
    # db: SQliteSettings = SQliteSettings()
    db: PostgreSQLSettings = PostgreSQLSettings()
    cache: RedisSettings = RedisSettings()
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
