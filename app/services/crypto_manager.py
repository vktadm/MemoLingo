import bcrypt


class CryptoService:
    """Сервис для криптографических операций, связанных с паролями."""

    @staticmethod
    def hash_password(password: str) -> str:
        """Хеширует пароль с использованием bcrypt."""
        salt = bcrypt.gensalt()
        pwd_bytes: bytes = password.encode()
        return bcrypt.hashpw(pwd_bytes, salt).decode("utf-8")

    @staticmethod
    def validate_password(
        password: str,
        hashed_password: str,
    ) -> bool:
        """Проверяет соответствие пароля его хешу."""
        return bcrypt.checkpw(
            password=password.encode(),
            hashed_password=hashed_password.encode("utf-8"),
        )
