from pydantic import BaseModel
from pydantic_settings import BaseSettings
from environs import Env
from urllib.parse import urlencode

env = Env()
env.read_env()


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


class JWTSettings(BaseModel):
    algorithm: str = "HS256"
    secret: str = env("SECRET_KEY")
    access_token_expire_minutes: int = 3


class GoogleSettings(BaseModel):
    CLIENT_ID: str = env("GOOGLE_CLIENT_ID")
    CLIENT_SECRET: str = env("GOOGLE_CLIENT_SECRET")
    REDIRECT_URI: str = env("GOOGLE_REDIRECT_URI")
    AUTH_URI: str = env("GOOGLE_AUTH_URI")
    TOKEN_URI: str = env("GOOGLE_TOKEN_URI")

    @property
    def get_url(self):
        base_url = "https://accounts.google.com/o/oauth2/auth"
        params = {
            "response_type": "code",
            "client_id": self.CLIENT_ID,
            "redirect_uri": self.REDIRECT_URI,
            "scope": "email profile",
            "access_type": "offline",
            "state": self.CLIENT_SECRET,
            "prompt": "consent",
        }
        return f"{base_url}?{urlencode(params)}"


class YandexSMTPSettings(BaseModel):
    HOSTNAME: str = env("YANDEX_SMTP_HOSTNAME")
    PORT: int = env("YANDEX_SMTP_PORT")
    USERNAME: str = env("YANDEX_SENDER_USERNAME")
    PASSWORD: str = env("YANDEX_APP_PASSWORD")
    REDIRECT_URL: str = "http://127.0.0.1:8000/api/v1/users/verify_email"
    TLS: bool = False
    START_TLS: bool = True
    VALIDATE_CERTS: bool = False  # TODO: Только для dev!!!


class ImageAPISettings(BaseModel):
    ACCESS_KEY: str = env("UNSPLASH_ACCESS_KEY")
    URL: str = "https://api.unsplash.com/photos/random"


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    db: PostgresSettings = PostgresSettings()
    cache: RedisSettings = RedisSettings()
    auth_jwt: JWTSettings = JWTSettings()
    auth_google: GoogleSettings = GoogleSettings()
    smtp_yandex: YandexSMTPSettings = YandexSMTPSettings()
    image: ImageAPISettings = ImageAPISettings()


settings = Settings()
