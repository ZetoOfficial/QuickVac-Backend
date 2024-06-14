from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'QuickVac'
    BASE_URL: str = '/api'
    DATABASE_DSN: str = 'postgresql://quick_vac:quick_vac@localhost:5432/quick_vac'


settings = Settings()
