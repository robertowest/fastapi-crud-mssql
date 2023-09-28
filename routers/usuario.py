from fastapi import APIRouter
from typing import List

from db.services.usuario import UsuarioSrv
from db.models.usuario import Usuario, UsuarioNuevo

app_route = APIRouter(prefix="/usuario")


@app_route.get("/list", name="Listado de usuarios", tags=["Usuarios"])
async def get_users_list():
    """Obtiene todos los usuarios de la base de datos"""
    #  async def get_users_list() -> List[Usuario]:
    # al intentar devoler el objeto Usuario da error
    # faltaría convertir result_to_dict() a Usuario()
    return UsuarioSrv().list()


@app_route.post("", name="Nuevo usuario", tags=["Usuarios"])  # response_model=List[Usuario]
def post_user(data: UsuarioNuevo):
    return UsuarioSrv().create(data)


@app_route.get("/{id}", name="Obtener usuario", tags=["Usuarios"])
def get_user(id: int):
    """Obtiene un usuario de la base de datos"""
    return UsuarioSrv().read(id)


@app_route.put("/{id}", name="Actualización de usuario", tags=["Usuarios"])
def put_user(data: Usuario, id: int=None):
    return UsuarioSrv().update(data, id)


@app_route.delete("/{id}", name="Eliminación de usuario", tags=["Usuarios"])
def delete_user(id: int = None):
    return UsuarioSrv().delete(id)
