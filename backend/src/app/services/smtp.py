import secrets
from dataclasses import dataclass


from backend.src.app.clients.yandex import SMTPYandexClient
from backend.src.app.exceptions import (
    UserAlreadyConfirmException,
    NotFoundException,
    SMTPCooldownException,
    SMTPTokenException,
)
from backend.src.app.repository import UsersRepository, SMTPRepository
from backend.src.app.services import CryptoService


@dataclass
class SMTPService:
    """Сервис для работы с email пользователя."""

    user_repository: UsersRepository
    smtp_repository: SMTPRepository
    crypto_service: CryptoService
    smtp_client: SMTPYandexClient

    async def send_confirmation_email(self, email_to: str):
        db_user = await self.user_repository.get_user_by_email(email_to)
        if not db_user:
            raise NotFoundException()

        if db_user.is_active:
            raise UserAlreadyConfirmException()

        if await self.smtp_repository.verify_cooldown(email=email_to):
            raise SMTPCooldownException()

        await self.smtp_repository.revoke_existing_tokens(email=email_to)

        token: str = secrets.token_urlsafe(10)
        await self.smtp_repository.add_token(email=email_to, token=token)
        await self.smtp_repository.set_email_cooldown(email=email_to)
        confirmation_url = f"{self.smtp_client.settings.REDIRECT_URL}?token={token}"
        await self.smtp_client.send_email(
            email_to=email_to,
            confirmation_url=confirmation_url,
        )

    async def verify_confirmation_email(self, token: str):
        email = await self.smtp_repository.verify_token(token=token)
        if not email:
            raise SMTPTokenException()

        await self.smtp_repository.revoke_existing_tokens(email=email)
        await self.user_repository.activate(email)
