from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .containers import configure
from .settings import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f'{settings.BASE_URL}/openapi.json',
        docs_url=f'{settings.BASE_URL}/docs',
        redoc_url=f'{settings.BASE_URL}/redoc',
    )

    app.container = configure(settings)
    app.container.wire(packages=['quick_vac'])

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    return app
