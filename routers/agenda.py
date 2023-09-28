from fastapi import APIRouter
from typing import List

from db.services.agenda import AgendaSrv
from db.models.agenda import AgendaBase, Agenda

app_route = APIRouter(prefix="/agenda")


@app_route.get("/list", name="Visualiza agenda de un paciente", tags=["Agenda"])
async def list_agenda(paciente: str):
    """Obtiene la agenda de un paciente"""
    return AgendaSrv().list(paciente)


# @app_route.post("", name="Nuevo usuario", tags=["Agenda"])  # response_model=List[Usuario]
# def post_agenda(data: AgendaBase):
#     return AgendaSrv().create(data)


# @app_route.get("/{id}", name="Obtener usuario", tags=["Agenda"])
# def get_agenda(id: int):
#     """Obtiene un usuario de la base de datos utilizando 'services'."""
#     return AgendaSrv().read(id)


# @app_route.put("/{id}", name="Actualización de usuario", tags=["Agenda"])
# def put_agenda(data: Agenda, id: int=None):
#     return AgendaSrv().update(data, id)


# @app_route.delete("/{id}", name="Eliminación de usuario", tags=["Agenda"])
# def delete_agenda(id: int = None):
#     return AgendaSrv().delete(id)
