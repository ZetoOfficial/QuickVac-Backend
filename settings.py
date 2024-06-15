from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_endpoint: str = "/api"
    app_environment: str = "development"
    app_origins: str = "*"
    database_dsn: str = "postgresql://quick_vac:quick_vac@localhost:5432/quick_vac"
    async_database_dsn: str = "postgresql+asyncpg://quick_vac:quick_vac@localhost:5432/quick_vac"

    class Config:
        case_sensitive = False
        env_file = ".env"


settings = Settings()
