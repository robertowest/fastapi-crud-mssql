from fastapi import FastAPI

from core.config import settings
from routers import usuario

app = FastAPI(
    title = settings.PROJECT_NAME,
    description = settings.PROJECT_DESCRIPTION,
    version = settings.PROJECT_VERSION,
    # servers=[{'url': 'localhost'}],
)

# incluímos las URL definidas en cada router
app.include_router(usuario.app_route)
