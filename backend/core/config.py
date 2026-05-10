from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:pass@localhost:5432/renewable"
    REDIS_URL: str = "redis://localhost:6379"

settings = Settings()
