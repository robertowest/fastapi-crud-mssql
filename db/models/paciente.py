from datetime import date
from pydantic import Field

from . import AdaptedModel


class PacienteBase(AdaptedModel):
    # Field(..., title="Trino content", min_length=1, max_length=256)
    dni: str = Field(max_length=18)
    nombre: str = Field(max_length=50)
    apellido1: str = Field(max_length=50)
    apellido2: str = Field(max_length=50)
    fecha_nacimiento: date = Field(default = date.today())

class Paciente(PacienteBase):
    id_pac: str = Field(max_length=12)
    movil: str = Field(max_length=9)
    email: str = Field(max_length=50)
    sexo: str = Field(max_length=1)
