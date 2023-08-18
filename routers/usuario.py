from fastapi import APIRouter
from typing import List

from db.services.usuario import UsuarioSrv
from db.models import Usuario, UsuarioNuevo

app_route = APIRouter(prefix="/usuario")


@app_route.get("/list", name="Listado de usuarios", tags=["Usuarios"])
async def get_users_list() -> List[Usuario]:
    """Obtiene todos los usuarios de la base de datos utilizando 'services'."""
    return UsuarioSrv().list()


@app_route.post("", name="Nuevo usuario", tags=["Usuarios"])  # response_model=List[Usuario]
def post_user(data: UsuarioNuevo):
    return UsuarioSrv().create(data)


@app_route.get("/{id}", name="Obtener usuario", tags=["Usuarios"])
def get_user(id: int):
    """Obtiene un usuario de la base de datos utilizando 'services'."""
    return UsuarioSrv().read(id)


@app_route.put("/{id}", name="Actualización de usuario", tags=['Usuarios'])
def put_user(data: Usuario, id: int = None):
    return UsuarioSrv().update(data, id)


@app_route.delete("/{id}", name="Eliminación de usuario", tags=['Usuarios'])
def delete_user(id: int = None):
    return UsuarioSrv().delete(id)





# # obtiene todos los usuarios de la base de datos sin utilzar 'services'
# @app_route.get("/usuarios")
# async def get_usuarios():
#     with MSSQL().cursor() as cursor:
#         cursor.execute("SELECT * FROM [dbo].[usuario]")
#         data = []
#         for row in cursor.fetchall():
#             data.append(list(row))
#         return data


# # obtiene un usuario específico 
# @app_route.get("/{id}")
# def read_usuario(id: int):
#     cursor = connection().execute("SELECT * FROM [dbo].[usuario] WHERE id = {id}")
#     return {"usuario_id": id}



# usuarios: List[Usuario] = []

# @app_route.post("/nuevo", response_model=List[Usuario], name="usuario:create")
# def create_usuario(usuario: Usuario) -> List[Usuario]:
#     for item_save in usuarios:
#         if item_save.documento == usuario.documento:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe un usuario con ese documento"
#             )
#     usuarios.append(usuario)
#     return usuarios
