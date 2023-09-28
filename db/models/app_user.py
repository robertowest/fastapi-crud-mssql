from datetime import date
from pydantic import SecretBytes, SecretStr, field_serializer

from core.config import Settings
from . import AdaptedModel


class AppUserBase(AdaptedModel):
    dni: str
    nombre: str
    apellido1: str
    apellido2: str
    fecha_nacimiento: date


class AppUser(AppUserBase):
    id: int
    telefono: str
    email: str
    id_pac: str


class AppUserNew(AppUser):
    pwd: str


class AppUserToken(AdaptedModel):
    """
    Forma de uso:
    from db.models.app_user import AppUserToken
    dato = AppUserToken(dni='12345678A', password='MiClave')
    dato.password
    dato.model_dump()
    dato.model_dump_json()
    """
    dni: str
    password: SecretStr
    password_bytes: SecretBytes = Settings.SECRET_KEY

    @field_serializer('password', 'password_bytes', when_used='json')
    def dump_secret(self, v):
        return v.get_secret_value()
