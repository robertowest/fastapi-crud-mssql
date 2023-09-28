from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from core.config import settings
from routers import agenda, especialidad, paciente, app_user as usuario, sede


app = FastAPI(
    title = settings.PROJECT_NAME,
    description = settings.PROJECT_DESCRIPTION,
    version = settings.PROJECT_VERSION,
    # servers=[{'url': 'localhost'}],
    swagger_ui_parameters = {"docExpansion": "none"},
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home(request: Request):
    # return {"message": "Hola mundo!"}
    return templates.TemplateResponse("langind.html", {"request": request})


# incluímos las URL definidas en cada router
app.include_router(agenda.app_route)
app.include_router(especialidad.app_route)
app.include_router(paciente.app_route)
app.include_router(sede.app_route)
app.include_router(usuario.app_route)
