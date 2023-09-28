from fastapi import APIRouter
from typing import List

from db.services.paciente import PacienteSrv
from db.models.paciente import Paciente

app_route = APIRouter(prefix="/paciente")


@app_route.get("/list", name="Listado de pacientes", tags=["Pacientes"])
async def list_pacientes(page: int=1, per_page: int=20):    #  -> List[Paciente]
    """Obtiene un grupo de pacientes de la base de datos utilizando 'services'."""
    return PacienteSrv().list(page, per_page)


@app_route.get("/{id_pac}", name="Obtener paciente", tags=["Pacientes"])
def get_paciente(id_pac: str):  #  -> Paciente
    """Obtiene un paciente de la base de datos utilizando 'services'."""
    return PacienteSrv().read(id_pac)


@app_route.get("/dni/{dni}", name="Obtener paciente por dni", tags=["Pacientes"])
def get_paciente_dni(dni: str):
    """Obtiene un paciente de la base de datos utilizando 'services'."""
    return PacienteSrv().read_by_dni(dni)


@app_route.get("/tutor/{id_pac}", name="Obtener tutor y adherentes", tags=["Pacientes"])
def get_tutor(id_pac: str):
    """Obtiene un paciente (tutor) y sus adherentes (hijos)."""
    return PacienteSrv().read_tutor(id_pac)


@app_route.get("/tutor/dni/{dni}", name="Obtener tutor y adherentes por DNI", tags=["Pacientes"])
def get_tutor_dni(dni: str):
    """Obtiene un paciente (tutor) y sus adherentes (hijos) buscando por DNI"""
    return PacienteSrv().read_tutor_by_dni(dni)
