from fastapi import APIRouter
from typing import List

from db.services.agenda import AgendaService

app_route = APIRouter(prefix="/agenda")


@app_route.get("/paciente/{paciente}", name="Visualiza agenda de un paciente", tags=["Agenda"])
async def list_agenda_paciente(paciente: str):
    """Obtiene la agenda de un paciente"""
    return AgendaService().list(paciente)


# @app_route.post("", name="Nuevo usuario", tags=["Agenda"])  # response_model=List[Usuario]
# def post_agenda(data: AgendaBase):
#     return AgendaService().create(data)


# @app_route.get("/{id}", name="Obtener usuario", tags=["Agenda"])
# def get_agenda(id: int):
#     """Obtiene un usuario de la base de datos utilizando 'services'."""
#     return AgendaService().read(id)


# @app_route.put("/{id}", name="Actualización de usuario", tags=["Agenda"])
# def put_agenda(data: Agenda, id: int=None):
#     return AgendaService().update(data, id)


# @app_route.delete("/{id}", name="Eliminación de usuario", tags=["Agenda"])
# def delete_agenda(id: int = None):
#     return AgendaService().delete(id)
