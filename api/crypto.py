import bcrypt


class Crypto:
    @staticmethod
    def hash_password(password: str) -> str:
        salt = bcrypt.gensalt()
        pwd_bytes: bytes = password.encode()
        return bcrypt.hashpw(pwd_bytes, salt).decode("utf-8")

    @staticmethod
    def validate_password(
        password: str,
        hashed_password: str,
    ) -> bool:
        return bcrypt.checkpw(
            password=password.encode(),
            hashed_password=hashed_password.encode("utf-8"),
        )
