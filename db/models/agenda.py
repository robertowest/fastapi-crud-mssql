from datetime import date
from pydantic import Field

from . import AdaptedModel


class AgendaModel(AdaptedModel):
    id : int
    dia : int = Field(max_length=8)
    hora : int
    minuto : int
    id_paciente : str
    paciente : str
    id_medico : str
    medico : str
    categoriaProf : int
    id_sede : int
    sede : str
    id_consulta : int
    consulta : str
    id_especialidad : str
    especialidad : str
    id_empresa_seguro : int
    empresa_seguro : str
    id_tipo_visita : int
    tipo_visita : str
    id_modo_visita : int
    modo_visita : str
    notas : str
    nuevo_pac : int
    pendiente_llegar : int
