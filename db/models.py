from datetime import date
from pydantic import BaseModel


class UsuarioBase(BaseModel):
    id: int

class Usuario(UsuarioBase):
    documento: str
    nombres: str
    telefono: str
    correo: str

class UsuarioNuevo(Usuario):
    ciudad: str
    fecha_registro: date
