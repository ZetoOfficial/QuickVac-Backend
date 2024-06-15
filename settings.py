from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_endpoint: str
    app_environment: str
    app_origins: str
    database_dsn: str
    async_database_dsn: str

    class Config:
        case_sensitive = False


settings = Settings()
