import os
from dotenv import load_dotenv

class ConfigLoader:

    REQUIRED_KEYS = [
        "DB_HOST",
        "DB_USER",
        "DB_PASSWORD",
        "API_KEY"
    ]

    def __init__(self):
        load_dotenv()
        self.config = {}
        self._load_config()
        self._validate_config()

    def _load_config(self):
        for key in self.REQUIRED_KEYS:
            self.config[key] = os.getenv(key)

    def _validate_config(self):
        missing = [k for k, v in self.config.items() if not v]
        if missing:
            raise ValueError(f"Missing required config: {missing}")

    def get(self, key: str):
        return self.config.get(key)

    def get_safe_config(self):
        # hide secret
        safe_config = self.config.copy()
        if "DB_PASSWORD" in safe_config:
            safe_config["DB_PASSWORD"] = "***"
        if "API_KEY" in safe_config:
            safe_config["API_KEY"] = "***"
        return safe_config