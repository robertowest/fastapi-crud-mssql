from fastapi import APIRouter

from db.models.especialidad import EspecialidadModel
from db.services.especialidad import EspecialidadServices

app_route = APIRouter(prefix="/especialidad")


@app_route.get("/list", name="Listado de especialidades", tags=["Especialidades"])
async def get_especialidad_list():
    """Obtiene todos los especialidades de la base de datos"""
    return EspecialidadService().list()


@app_route.get("/{id}", name="Obtener especialidad", tags=["Especialidades"])
def get_especialidad(id: int):
    """Obtiene una especialidad de la base de datos"""
    return EspecialidadService().read(id)
