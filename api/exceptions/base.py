class MainException(Exception):
    detail: str = "Server error!"
    status_code: int = 500

    @property
    def to_dict(self):
        return {
            "detail": self.detail,
            "status_code": self.status_code,
        }
