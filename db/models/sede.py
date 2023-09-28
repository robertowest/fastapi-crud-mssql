from datetime import date

from . import AdaptedModel


class SedeModel(AdaptedModel):
    idSede: int
    nombre: str
    localidad: str
    provincia: str
    pais: str
    cp: str
    domicilio: str
    telefono: str
    email: str
    horario: str
    nombreCorto: str
