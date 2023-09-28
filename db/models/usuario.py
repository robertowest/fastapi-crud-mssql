from datetime import date

from . import AdaptedModel


class UsuarioBase(AdaptedModel):
    documento: str
    nombres: str
    telefono: str
    correo: str

class Usuario(UsuarioBase):
    id: int

class UsuarioNuevo(Usuario):
    ciudad: str
    fecha_registro: date
