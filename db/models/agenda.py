from datetime import date
from pydantic import Field

from . import AdaptedModel


class AgendaBase(AdaptedModel):
    # campos obligatorios
    dia: str = Field(max_length=8)
    hora: int
    minuto: int
    consulta: int
    paciente: str = Field(max_length=12)
    mod_visita: str = Field(max_length=2)
    nuevo_pac: bool
    pendiente_llegar: bool

class Agenda(AgendaBase):
    id: int
    # duracion: int
    # medico: str = Field(max_length=12)
    # tipo_visita: int 
    # notas: str = Field(max_length=900)
    # contador: str = Field(max_length=12)
    # descuento: str = Field(max_length=2)
    # FAC: date = Field(default = date.today())
    # UAC: str = Field(max_length=12)
    # urgencia: str = Field(max_length=10)
    # sede: int
    # Insurance_lid: int
    # Insurance_name: str = Field(max_length=100)
    # activity_lid: str = Field(max_length=100)
    # FEC: date = Field(default = date.today())
