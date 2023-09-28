from fastapi import APIRouter

from db.models.sede import SedeModel
from db.services.sede import SedeService

app_route = APIRouter(prefix="/sede")


@app_route.get("/list", name="Listado de sedes", tags=["Sedes"])
async def get_sede_list(page: int=1, per_page: int=20):
    """Obtiene todos los sedes de la base de datos"""
    return SedeService().list(page, per_page)


@app_route.get("/{id}", name="Obtener sede", tags=["Sedes"])
def get_sede(id: int):
    """Obtiene una sede de la base de datos"""
    return SedeService().read(id)
