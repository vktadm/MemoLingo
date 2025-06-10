import aiosmtplib
from jinja2 import Environment, FileSystemLoader
from email.message import EmailMessage
from dataclasses import dataclass

from backend.src.app.settings import YandexSMTPSettings


@dataclass
class SMTPYandexClient:
    settings: YandexSMTPSettings

    async def send_email(self, email_to: str, confirmation_url: str) -> bool:
        env = Environment(loader=FileSystemLoader("templates/"))
        html_template = env.get_template("email_confirmation.jinja2")

        html_content = html_template.render(
            format="html",
            company_name="MemoLingo",
            confirmation_url=confirmation_url,
            expiration_hours=24,
        )
        text_content = html_template.render(
            format="text",
            company_name="MemoLingo",
            confirmation_url=confirmation_url,
            expiration_hours=24,
        )

        msg = EmailMessage()

        msg["Subject"] = "MemoLingo [Email confirmation]"
        msg["From"] = self.settings.USERNAME
        msg["To"] = email_to
        msg.set_content(text_content)
        msg.add_alternative(html_content, subtype="html")

        try:
            await aiosmtplib.send(
                msg,
                hostname=self.settings.HOSTNAME,
                port=self.settings.PORT,
                username=self.settings.USERNAME,
                password=self.settings.PASSWORD,
                use_tls=self.settings.TLS,
                start_tls=self.settings.START_TLS,
                validate_certs=self.settings.VALIDATE_CERTS,
            )
            return True
        except Exception as e:
            print(e)
            return False
