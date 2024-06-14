from core.application import create_app
from core.settings import settings
from quick_vac.v1.api import _endpoints as rest_endpoints

app = create_app()
app.include_router(rest_endpoints.api_router, prefix=f'{settings.BASE_URL}/v1')
